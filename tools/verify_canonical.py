#!/usr/bin/env python3
"""Verify the cryptographic commitments embedded in CANONICAL_ROOT_v6.md.

The canonical Root ships three doctrine text blocks (Japanese canonical,
English reference, strongest short form). Each is immediately followed by a
``SHA256:`` label and a fenced hash block. This tool recomputes the SHA256 of
each doctrine text block (raw UTF-8, no trailing newline) and asserts it equals
the embedded commitment.

This is the most important integrity gate in the repository: it proves the
doctrine text has not been silently altered. The Root forbids editing the
committed text without an audited, high-impact revision; this tool makes any
drift fail loudly in CI.

Exit code 0 on success, 1 on any mismatch or parse failure.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "CANONICAL_ROOT_v6.md"

# (human label, 0-based index of the doctrine text block among ```text fences)
DOCTRINE_BLOCKS = [
    ("japanese_canonical", 0),
    ("english_reference", 2),
    ("strongest_short_form", 4),
]


def _text_blocks(md: str) -> list[str]:
    return re.findall(r"```text\n(.*?)\n```", md, re.S)


def _sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def verify(canonical_path: Path = CANONICAL) -> list[str]:
    """Return a list of human-readable error strings (empty == OK)."""
    errors: list[str] = []
    if not canonical_path.exists():
        return [f"missing canonical root: {canonical_path}"]

    md = canonical_path.read_text(encoding="utf-8")
    blocks = _text_blocks(md)

    for label, idx in DOCTRINE_BLOCKS:
        # The commitment is the very next ```text block after the doctrine block.
        doctrine_idx, commit_idx = idx, idx + 1
        if commit_idx >= len(blocks):
            errors.append(f"{label}: could not locate doctrine/commitment block pair")
            continue
        doctrine = blocks[doctrine_idx]
        embedded = blocks[commit_idx].strip()
        computed = _sha256_text(doctrine)
        if not re.fullmatch(r"[0-9a-f]{64}", embedded):
            errors.append(f"{label}: block #{commit_idx} is not a 64-char sha256 hex: {embedded!r}")
            continue
        if computed != embedded:
            errors.append(
                f"{label}: SHA256 mismatch\n    embedded={embedded}\n    computed={computed}"
            )
    return errors


def main() -> int:
    errors = verify()
    if errors:
        print("CANONICAL VERIFICATION FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("OK: CANONICAL_ROOT_v6.md doctrine commitments verified "
          "(japanese_canonical, english_reference, strongest_short_form).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
