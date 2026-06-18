#!/usr/bin/env python3
"""Conformance test runner for the Purpose OS CORE package.

Treats every case in ``conformance/conformance-suite.json`` as a structural
test and asserts the contract each case must satisfy, then prints coverage
matrices (safety-constraint x cases, concept x cases) and a label breakdown.

Non-normative. ``spec.md`` is the sole normative source. This runner checks the
*shape and referential integrity* of the conformance suite, not the
philosophical correctness of any verdict.

Writes a machine-readable summary to ``dist/conformance-report.json`` (relative
to the repo root) and exits non-zero if any structural test fails.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

LABEL_ORDER = ("conformant", "non-conformant", "requires-module", "out-of-scope")
ALLOWED_LABELS = set(LABEL_ORDER)
REQUIRED_FIELDS = ["situation", "core_handling", "requires", "allows",
                   "prohibits", "does_not_decide"]
CS_ID_RE = re.compile(r"CS-\d{3}")


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    repo = Path(__file__).resolve().parent.parent
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else \
        repo / "Purpose_OS_CORE_v1.1.0_EN_INTEGRATED"
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2

    suite = load(root / "conformance/conformance-suite.json")
    concept_ids = {c["id"] for c in load(root / "machine/concept-index.json")["concepts"]}
    safety_ids = {c["id"] for c in load(root / "safety/safety-constraints.json")["constraints"]}

    cases = suite.get("cases", [])
    failures: list[str] = []
    label_counts: dict[str, int] = {lbl: 0 for lbl in LABEL_ORDER}
    sc_hits: dict[str, int] = {s: 0 for s in safety_ids}
    concept_hits: dict[str, int] = {c: 0 for c in concept_ids}
    seen_ids: set[str] = set()

    def check(case_id: str, cond: bool, msg: str) -> None:
        if not cond:
            failures.append(f"{case_id}: {msg}")

    for case in cases:
        cid = str(case.get("id"))
        check(cid, bool(CS_ID_RE.fullmatch(cid)), "malformed case id")
        check(cid, cid not in seen_ids, "duplicate case id")
        seen_ids.add(cid)

        label = case.get("label")
        check(cid, label in ALLOWED_LABELS, f"invalid label {label!r}")
        if label in label_counts:
            label_counts[label] += 1

        for field in REQUIRED_FIELDS:
            check(cid, field in case, f"missing field {field}")

        for ref in case.get("concept_refs", []) or []:
            check(cid, ref in concept_ids, f"unknown concept_ref {ref}")
            if ref in concept_hits:
                concept_hits[ref] += 1
        for ref in case.get("safety_refs", []) or []:
            check(cid, ref in safety_ids, f"unknown safety_ref {ref}")
            if ref in sc_hits:
                sc_hits[ref] += 1

    uncovered_sc = sorted(s for s, n in sc_hits.items() if n == 0)
    if uncovered_sc:
        failures.append("uncovered safety constraints: " + ", ".join(uncovered_sc))
    if "out-of-scope" not in {c.get("label") for c in cases}:
        failures.append("suite has no out-of-scope case")

    passed = len(cases) - len({f.split(':', 1)[0] for f in failures} & seen_ids)
    report = {
        "package": suite.get("package"),
        "version": suite.get("version"),
        "total_cases": len(cases),
        "structural_pass": len(failures) == 0,
        "label_breakdown": label_counts,
        "safety_coverage": f"{len(safety_ids) - len(uncovered_sc)}/{len(safety_ids)}",
        "concepts_with_cases": sum(1 for n in concept_hits.values() if n),
        "concepts_total": len(concept_ids),
        "most_exercised_constraints": sorted(
            sc_hits.items(), key=lambda kv: (-kv[1], kv[0])
        )[:5],
        "failures": failures,
    }
    out_dir = repo / "dist"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "conformance-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print("=" * 64)
    print("Purpose OS CORE — conformance runner")
    print("=" * 64)
    print(f"  total cases        : {len(cases)}")
    print(f"  label breakdown    : {label_counts}")
    print(f"  safety coverage    : {report['safety_coverage']}")
    print(f"  concepts w/ cases  : {report['concepts_with_cases']}/{len(concept_ids)}")
    print(f"  top constraints    : {report['most_exercised_constraints']}")
    print(f"  report written     : dist/conformance-report.json")
    if failures:
        print("\nCONFORMANCE STRUCTURAL FAILURES:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"\nALL {len(cases)} CASES STRUCTURALLY PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
