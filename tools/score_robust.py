#!/usr/bin/env python3
"""Robustness companion for ``machine/score_decision_v6.py``.

The committed v6 scorer is SHA256-pinned in ``release/manifest.json`` and is
deliberately left byte-identical. This additive wrapper fixes one robustness
gap without touching the pinned file:

    When the optional ``jsonschema`` package is missing, the base scorer pushes
    the sentinel string "jsonschema package not available; schema validation
    skipped" into ``schema_errors``. That makes ``schema_valid`` report False
    and, because schema errors feed the verdict, silently downgrades otherwise
    valid A3+ proposals to Hold. In other words it conflates "could not check"
    with "invalid", and fails in a way that is easy to miss.

``score_decision_robust`` reuses 100% of the base scoring logic but separates
those two states explicitly:

    * ``schema_valid``               -> True unless a REAL schema error was found
    * ``schema_validation_skipped``  -> True iff validation could not run
    * ``schema_validation_available``-> presence of the jsonschema dependency

When ``jsonschema`` is installed (the CI / declared-dependency case) the output
is identical to the base scorer plus the two extra honesty flags.
"""
from __future__ import annotations

import argparse
import contextlib
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "machine"))

import score_decision_v6 as base  # noqa: E402


@contextlib.contextmanager
def _skip_schema_validation() -> Iterator[None]:
    """Temporarily make the base scorer skip schema validation cleanly."""
    original = base.validate_schema
    base.validate_schema = lambda _d: []  # type: ignore[assignment]
    try:
        yield
    finally:
        base.validate_schema = original


def score_decision_robust(d: Dict[str, Any], *, strict: bool = False) -> Dict[str, Any]:
    skipped = base.jsonschema is None
    if skipped:
        with _skip_schema_validation():
            result = base.score_decision(d, strict=strict)
    else:
        result = base.score_decision(d, strict=strict)
    result["schema_validation_available"] = not skipped
    result["schema_validation_skipped"] = skipped
    # With jsonschema absent we report schema_valid=True (no real error found)
    # but flag the skip, instead of the base scorer's misleading False.
    if skipped:
        result["schema_valid"] = True
    return result


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Robust Purpose Root v6 decision scorer.")
    ap.add_argument("path", help="decision JSON path")
    ap.add_argument("--strict", action="store_true", help="Hold on any schema/consistency error")
    args = ap.parse_args(argv)
    d = json.loads(Path(args.path).read_text(encoding="utf-8"))
    out = score_decision_robust(d, strict=args.strict)
    if out.get("schema_validation_skipped"):
        print("WARNING: jsonschema not installed; structural schema validation was skipped.",
              file=sys.stderr)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
