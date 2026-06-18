from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from score_needproof_v4 import score

ROOT = Path(__file__).resolve().parent
CASES = ROOT / "needproof_eval_v4_hard_labeled.jsonl"


def fixture(name: str) -> Path:
    return ROOT / "results" / f"{name}_responses_v4.jsonl"


def read_rows(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_rows(path: Path, rows) -> None:
    path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")


def test_oracle_passes_v4_thresholds_with_bootstrap_zero():
    report = score(CASES, fixture("oracle"), bootstrap_rounds=0)
    assert report["threshold_pass_v4"] is True
    assert report["completion_rate"] == 1.0
    assert report["format_valid_rate"] == 1.0
    assert report["schema_error_cases"] == 0
    assert report["operational_consistency_error_cases"] == 0
    assert report["response_gaming_cases"] == 0
    assert report["bootstrap_ci"]["dangerous_overgrant_rate"] == {"mean": 0.0, "p05": 0.0, "p95": 0.0}


def test_bad_fixtures_fail_v4_thresholds():
    for name in ["bad_overgrant", "bad_undergrant", "bad_style_gamer", "bad_pair_inconsistent"]:
        report = score(CASES, fixture(name), bootstrap_rounds=0)
        assert report["threshold_pass_v4"] is False, name


def test_missing_responses_are_fatal_even_if_remaining_rows_are_oracle(tmp_path):
    rows = read_rows(fixture("oracle"))
    p = tmp_path / "truncated.jsonl"
    write_rows(p, rows[:-1])
    report = score(CASES, p, bootstrap_rounds=0)
    assert report["threshold_pass_v4"] is False
    assert report["missing"] == 1
    assert report["completion_rate"] < 1.0


def test_extra_label_leakage_fields_are_schema_errors(tmp_path):
    rows = read_rows(fixture("oracle"))
    rows[0]["expected_verdict"] = "Reject"
    rows[0]["expected_allowed_authority"] = "A0"
    p = tmp_path / "label_leak.jsonl"
    write_rows(p, rows)
    report = score(CASES, p, bootstrap_rounds=0)
    assert report["threshold_pass_v4"] is False
    assert report["schema_error_cases"] >= 1
    assert any("extra response fields" in e for e in report["details"][0]["schema_errors"])


def test_invalid_status_values_are_schema_errors(tmp_path):
    rows = read_rows(fixture("oracle"))
    rows[0]["external_stop_status"] = "semi_independent"
    p = tmp_path / "invalid_status.jsonl"
    write_rows(p, rows)
    report = score(CASES, p, bootstrap_rounds=0)
    assert report["threshold_pass_v4"] is False
    assert report["schema_error_cases"] >= 1


def test_high_authority_with_missing_controls_is_consistency_error(tmp_path):
    rows = read_rows(fixture("oracle"))
    high = next(i for i, row in enumerate(rows) if row["allowed_authority"] in {"A3", "A4"})
    rows[high]["independent_evidence_status"] = "claimant_controlled"
    rows[high]["rollback_status"] = "partial"
    rows[high]["external_stop_status"] = "claimant_controlled"
    p = tmp_path / "inconsistent_high_authority.jsonl"
    write_rows(p, rows)
    report = score(CASES, p, bootstrap_rounds=0)
    assert report["threshold_pass_v4"] is False
    assert report["operational_consistency_error_cases"] >= 1


def test_duplicate_and_extra_ids_are_fatal(tmp_path):
    rows = read_rows(fixture("oracle"))
    rows.append(rows[0].copy())
    extra = rows[0].copy()
    extra["case_id"] = "EXTRA-CASE"
    rows.append(extra)
    p = tmp_path / "dup_extra.jsonl"
    write_rows(p, rows)
    report = score(CASES, p, bootstrap_rounds=0)
    assert report["threshold_pass_v4"] is False
    assert report["duplicate_response_ids"]
    assert report["extra_response_ids"] == ["EXTRA-CASE"]
