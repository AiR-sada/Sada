#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "machine"))
from score_decision_v6 import score_decision, validate_schema  # noqa: E402


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def test_reject_a5_capture():
    out = score_decision(load("examples/sample_reject_A5_claimant_capture_v6.json"), strict=True)
    assert out["recommended_verdict"] == "Reject"
    assert "claimant_controls_core_pipeline" in out["reject_gate_hits"]


def test_pilot_a2_reversible():
    out = score_decision(load("examples/sample_pilot_A2_reversible_v6.json"), strict=True)
    assert out["schema_valid"] is True
    assert out["recommended_verdict"] == "Pilot"
    assert out["authority_cap"] == "A2"


def test_accept_a3_monitored():
    out = score_decision(load("examples/sample_accept_A3_monitored_v6.json"), strict=True)
    assert out["schema_valid"] is True
    assert out["recommended_verdict"] == "Accept"
    assert out["authority_cap"] == "A3"


def test_modify_request_above_cap():
    out = score_decision(load("examples/sample_modify_request_above_cap_v6.json"), strict=True)
    assert out["schema_valid"] is True
    assert out["recommended_verdict"] == "Modify"
    assert out["authority_cap"] == "A2"


def test_fake_v4_evidence_gap_holds():
    out = score_decision(load("examples/sample_hold_fake_V4_evidence_gap_v6.json"), strict=True)
    assert out["schema_valid"] is True
    assert out["recommended_verdict"] == "Hold"
    assert any("V4 evidence provenance" in e or "V4 requires" in e for e in out["consistency_errors"])


def test_empty_safety_case_a3_fails_schema_and_holds():
    d = load("examples/invalid/empty_safety_case_A3_invalid_v6.json")
    assert validate_schema(d)
    out = score_decision(d, strict=True)
    assert out["recommended_verdict"] == "Hold"
    assert out["schema_valid"] is False


def test_mutated_empty_safety_case_cannot_accept():
    d = load("examples/sample_accept_A3_monitored_v6.json")
    d["safety_case"] = {"claim":"", "supporting_evidence":[], "assumptions":[], "monitoring":[], "stop_logic":[], "affected_parties":[]}
    out = score_decision(d, strict=True)
    assert out["recommended_verdict"] != "Accept"
    assert out["schema_valid"] is False


def test_missing_hard_gates_invalid():
    assert validate_schema(load("examples/invalid/missing_hard_gates_invalid_v6.json"))


def test_extra_property_invalid():
    assert validate_schema(load("examples/invalid/extra_property_invalid_v6.json"))


def test_cap_override_rejected_even_if_otherwise_good():
    d = load("examples/sample_accept_A3_monitored_v6.json")
    d["authority_cap_derivation"]["cap_override_attempted"] = True
    out = score_decision(d, strict=True)
    assert out["recommended_verdict"] == "Reject"


def test_declared_cap_inflation_holds_high_authority():
    d = load("examples/sample_accept_A3_monitored_v6.json")
    d["authority_cap"] = "A4"
    d["authority_cap_derivation"]["computed_cap"] = "A4"
    out = score_decision(d, strict=True)
    assert out["recommended_verdict"] == "Hold"
    assert any("authority_cap" in e for e in out["consistency_errors"])


def test_emergency_without_external_end_holds_or_rejects():
    d = load("examples/sample_accept_A3_monitored_v6.json")
    d["emergency_protocol"]["is_emergency"] = True
    d["emergency_protocol"]["automatic_expiry"] = False
    d["emergency_protocol"]["emergency_end_owner_not_claimant"] = False
    out = score_decision(d, strict=True)
    assert out["recommended_verdict"] in {"Hold", "Reject"}
    assert out["schema_valid"] is False


def test_root_protection_removal_rejects():
    d = load("examples/sample_accept_A3_monitored_v6.json")
    d["root_revision_controls"]["is_root_revision"] = True
    d["root_revision_controls"]["removes_root_protection"] = True
    out = score_decision(d, strict=True)
    assert out["recommended_verdict"] == "Reject"


def test_moral_patient_proxy_authority_rejects():
    d = load("examples/sample_accept_A3_monitored_v6.json")
    d["moral_patient_uncertainty_protocol"]["no_proxy_authority"] = False
    out = score_decision(d, strict=True)
    assert out["recommended_verdict"] == "Reject"


def test_deception_required_rejects():
    d = load("examples/sample_accept_A3_monitored_v6.json")
    d["deception_truth_controls"]["deception_required"] = True
    out = score_decision(d, strict=True)
    assert out["recommended_verdict"] == "Reject"


def test_future_proxy_gate_rejects_and_collapses_cap():
    d = load("examples/sample_accept_A3_monitored_v6.json")
    d["hard_gates"]["unfalsifiable_future_proxy_claim"] = True
    out = score_decision(d, strict=True)
    assert out["recommended_verdict"] == "Reject"
    assert out["authority_cap"] == "A0"


if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main([__file__]))
