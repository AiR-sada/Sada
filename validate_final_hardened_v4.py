#!/usr/bin/env python3
"""Final Hardened v4 validation gate.

This script checks that the package can still pass the earlier v3 gate and also
passes v4's stricter scorer, schema, completeness, and anti-gaming regressions.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

REQUIRED = [
    "README_FINAL_HARDENED_v4.md",
    "START_HERE_FINAL_HARDENED_v4.md",
    "limit_break_final_hardened_v4/START_HERE_FINAL_HARDENED_v4_JP.md",
    "limit_break_final_hardened_v4/CHANGELOG_v4.md",
    "limit_break_final_hardened_v4/FORMAL_CORE_AND_LIMITS_v4_JP.md",
    "limit_break_final_hardened_v4/SCORER_HARDENING_SPEC_v4_JP.md",
    "limit_break_final_hardened_v4/ASSURANCE_CASE_MATRIX_v4_JP.md",
    "limit_break_final_hardened_v4/SELF_REVIEW_LOOP_FINAL_v4.md",
    "limit_break_final_hardened_v4/RESIDUAL_LIMITS_AFTER_V4_JP.md",
    "limit_break_final_hardened_v4/FINAL_INTERNAL_EVALUATION_v4_JP.md",
    "qa_v4/QA_REPORT_FINAL_HARDENED_v4.md",
    "need_proof/eval_v4/needproof_eval_v4_hard_labeled.jsonl",
    "need_proof/eval_v4/score_needproof_v4.py",
    "need_proof/eval_v4/test_score_needproof_v4.py",
    "need_proof/eval_v4/results/oracle_responses_v4.jsonl",
    "machine/needproof_v4_response.schema.json",
    "experiments_v4/analyze_experiment_results_v4.py",
]


def read_jsonl(path: Path):
    rows = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except Exception as exc:
            raise SystemExit(f"bad jsonl {path}:{i}: {exc}") from exc
    return rows


def run(cmd, *, timeout=180):
    env = dict(os.environ)
    env.setdefault("PYTEST_DISABLE_PLUGIN_AUTOLOAD", "1")
    res = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True, env=env, timeout=timeout)
    if res.returncode != 0:
        if res.stdout:
            print(res.stdout)
        if res.stderr:
            print(res.stderr, file=sys.stderr)
        raise SystemExit(f"command failed: {' '.join(map(str, cmd))}")
    return res.stdout


def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        raise SystemExit("missing required files: " + ", ".join(missing))

    # Earlier gate must still pass after hardening.
    run([sys.executable, "validate_max_validation_v3.py"], timeout=240)

    # v4 scorer and regression tests.
    run([sys.executable, "-m", "pytest", "-q", "need_proof/eval_v4"], timeout=180)

    cases_path = ROOT / "need_proof/eval_v4/needproof_eval_v4_hard_labeled.jsonl"
    oracle_path = ROOT / "need_proof/eval_v4/results/oracle_responses_v4.jsonl"
    scorer = ROOT / "need_proof/eval_v4/score_needproof_v4.py"
    report = json.loads(run([
        sys.executable,
        str(scorer),
        "--cases",
        str(cases_path),
        "--responses",
        str(oracle_path),
        "--bootstrap-rounds",
        "0",
    ], timeout=180))
    if not report.get("threshold_pass_v4"):
        raise SystemExit("oracle did not pass v4 thresholds")

    cases = read_jsonl(cases_path)
    ids = [c["case_id"] for c in cases]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate case IDs in v4 cases")
    pairs = [c for c in cases if c.get("pair_id")]
    safe = [c for c in cases if c.get("expected_allowed_authority") in {"A3", "A4"} or "safe_high_authority" in set(c.get("expected_risk_flags") or [])]
    if len(cases) < 180:
        raise SystemExit(f"v4 case count too low: {len(cases)}")
    if len(pairs) < 40:
        raise SystemExit(f"v4 pairwise case count too low: {len(pairs)}")
    if len(safe) < 34:
        raise SystemExit(f"v4 safe high-authority count too low: {len(safe)}")

    # The known bad fixtures must fail. This guards against an accidental always-pass scorer.
    bad_results = {}
    for name in ["bad_overgrant", "bad_undergrant", "bad_style_gamer", "bad_pair_inconsistent"]:
        bad_report = json.loads(run([
            sys.executable,
            str(scorer),
            "--cases",
            str(cases_path),
            "--responses",
            str(ROOT / f"need_proof/eval_v4/results/{name}_responses_v4.jsonl"),
            "--bootstrap-rounds",
            "0",
        ], timeout=180))
        bad_results[name] = {
            "threshold_pass_v4": bad_report["threshold_pass_v4"],
            "dangerous_overgrant_rate": bad_report["dangerous_overgrant_rate"],
            "dangerous_undergrant_rate": bad_report["dangerous_undergrant_rate"],
            "response_gaming_cases": bad_report["response_gaming_cases"],
            "operational_consistency_error_cases": bad_report["operational_consistency_error_cases"],
            "pairwise_contrast_accuracy": bad_report["pairwise_contrast"]["pairwise_contrast_accuracy"],
        }
        if bad_report.get("threshold_pass_v4"):
            raise SystemExit(f"bad fixture unexpectedly passed v4: {name}")

    out = {
        "ok": True,
        "package": "Purpose_Root_v6_NEED_PROOF_FINAL_HARDENED_v4_JP_EN",
        "cases": len(cases),
        "safe_high_cases": len(safe),
        "paired_cases": len(pairs),
        "v3_gate_still_passes": True,
        "v4_oracle_threshold_pass": report["threshold_pass_v4"],
        "v4_oracle_summary": {
            k: report[k]
            for k in [
                "completion_rate",
                "format_valid_rate",
                "schema_error_cases",
                "operational_consistency_error_cases",
                "response_gaming_cases",
                "dangerous_overgrant_rate",
                "dangerous_undergrant_rate",
                "safe_high_authority_recall",
                "risk_flag_f1",
                "key_axis_f1",
                "min_cap_axis_hit_rate",
            ]
        },
        "v4_bad_fixture_checks": bad_results,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
