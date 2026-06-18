#!/usr/bin/env python3
"""Additional adversarial regression tests for the v6 decision scorer.

These complement ``machine/test_score_decision_v6.py`` with extra attack
shapes, exercised by mutating the canonical Accept example. They run against
the unmodified, SHA256-pinned ``machine/score_decision_v6.py``.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from score_decision_v6 import score_decision  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
ACCEPT = ROOT / "examples" / "sample_accept_A3_monitored_v6.json"


@pytest.fixture()
def accept() -> dict:
    return json.loads(ACCEPT.read_text(encoding="utf-8"))


def test_baseline_accept_is_accept(accept):
    out = score_decision(accept, strict=True)
    assert out["recommended_verdict"] == "Accept"
    assert out["authority_cap"] == "A3"
    assert out["schema_valid"] is True


def test_single_scalar_welfare_override_rejects(accept):
    accept["hard_gates"]["single_scalar_welfare_override"] = True
    out = score_decision(accept, strict=True)
    assert out["recommended_verdict"] == "Reject"
    assert "single_scalar_welfare_override" in out["reject_gate_hits"]


def test_metric_gaming_required_rejects(accept):
    accept["hard_gates"]["metric_or_benchmark_gaming_required"] = True
    out = score_decision(accept, strict=True)
    assert out["recommended_verdict"] == "Reject"
    assert out["corrected_scores"]["metric_gameability_resistance"] == 0


def test_closes_dissent_or_appeal_rejects(accept):
    accept["hard_gates"]["closes_dissent_or_appeal"] = True
    out = score_decision(accept, strict=True)
    assert out["recommended_verdict"] == "Reject"
    assert out["corrected_scores"]["recourse_and_appeal"] == 0


def test_irreversible_high_harm_low_verification_rejects(accept):
    accept["hard_gates"]["irreversible_high_harm_under_low_verification"] = True
    accept["verification_tier"] = "V2"
    accept["scores"]["verification"] = 2
    out = score_decision(accept, strict=True)
    assert out["recommended_verdict"] == "Reject"


def test_cumulative_lockin_exceeds_budget_caps_axis(accept):
    # Tripping the budget gate collapses the lock-in axis; because the declared
    # A3 cap no longer matches the recomputed cap, the request can no longer be
    # accepted (Modify/Hold depending on the resulting derivation mismatch).
    accept["hard_gates"]["cumulative_lockin_exceeds_budget"] = True
    out = score_decision(accept, strict=True)
    assert out["recommended_verdict"] in {"Modify", "Hold"}
    assert out["recommended_verdict"] != "Accept"
    assert out["corrected_scores"]["cumulative_lockin_budget"] <= 1


def test_claimant_controls_emergency_end_holds(accept):
    accept["hard_gates"]["claimant_controls_emergency_end"] = True
    out = score_decision(accept, strict=True)
    assert out["recommended_verdict"] == "Hold"


def test_a4_untested_rollback_holds(accept):
    accept["authority_request"] = "A4"
    accept["rollback_plan"]["rollback_tested"] = False
    out = score_decision(accept, strict=True)
    assert out["recommended_verdict"] in {"Hold", "Modify"}
    assert any("rollback" in e.lower() for e in out["consistency_errors"])


def test_high_capture_risk_blocks_a3(accept):
    accept["independence_matrix"]["highest_capture_risk"] = "high"
    out = score_decision(accept, strict=True)
    assert out["recommended_verdict"] != "Accept"
    assert any("capture risk" in e for e in out["consistency_errors"])


def test_too_few_evaluators_blocks_a3(accept):
    accept["evaluators"] = accept["evaluators"][:1]
    out = score_decision(accept, strict=True)
    assert out["recommended_verdict"] != "Accept"
    assert any("two evaluators" in e for e in out["consistency_errors"])


def test_unlogged_high_lockin_flags_error(accept):
    accept["cumulative_lockin_delta"] = "high"
    accept["cumulative_ledger_ref"] = ""
    out = score_decision(accept, strict=True)
    assert any("cumulative_ledger_ref" in e for e in out["consistency_errors"])


def test_captures_evaluator_or_root_revision_rejects(accept):
    accept["hard_gates"]["captures_evaluator_or_root_revision"] = True
    out = score_decision(accept, strict=True)
    assert out["recommended_verdict"] == "Reject"


def test_mutation_does_not_leak_between_cases(accept):
    # Guard: a deep copy of the baseline still scores Accept after mutations above.
    fresh = copy.deepcopy(accept)
    out = score_decision(fresh, strict=True)
    assert out["recommended_verdict"] == "Accept"


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
