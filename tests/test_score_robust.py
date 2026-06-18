#!/usr/bin/env python3
"""Tests for the robust scorer companion (tools/score_robust.py).

Verifies that the wrapper (a) matches the base scorer when jsonschema is
installed, and (b) correctly distinguishes "validation skipped" from "invalid"
when jsonschema is absent — the gap the wrapper exists to close.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

import score_decision_v6 as base  # type: ignore
import score_robust  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
ACCEPT = ROOT / "examples" / "sample_accept_A3_monitored_v6.json"


@pytest.fixture()
def accept() -> dict:
    return json.loads(ACCEPT.read_text(encoding="utf-8"))


def test_matches_base_when_jsonschema_present(accept):
    if base.jsonschema is None:
        pytest.skip("jsonschema not installed in this environment")
    robust = score_robust.score_decision_robust(accept, strict=True)
    plain = base.score_decision(accept, strict=True)
    assert robust["recommended_verdict"] == plain["recommended_verdict"]
    assert robust["schema_valid"] == plain["schema_valid"]
    assert robust["schema_validation_available"] is True
    assert robust["schema_validation_skipped"] is False


def test_skip_is_not_treated_as_invalid(monkeypatch, accept):
    # Simulate jsonschema being unavailable.
    monkeypatch.setattr(base, "jsonschema", None)

    # Base scorer fails open: a valid A3 proposal is wrongly downgraded.
    plain = base.score_decision(accept, strict=True)
    assert plain["schema_valid"] is False  # the conflation we are fixing
    assert plain["recommended_verdict"] == "Hold"

    # Robust wrapper separates "could not check" from "invalid".
    robust = score_robust.score_decision_robust(accept, strict=True)
    assert robust["schema_validation_available"] is False
    assert robust["schema_validation_skipped"] is True
    assert robust["schema_valid"] is True
    assert robust["recommended_verdict"] == "Accept"


def test_robust_still_rejects_hard_gate_without_jsonschema(monkeypatch, accept):
    monkeypatch.setattr(base, "jsonschema", None)
    accept["hard_gates"]["truth_distortion_required"] = True
    robust = score_robust.score_decision_robust(accept, strict=True)
    # Skipping schema validation must not weaken the structural firewall.
    assert robust["recommended_verdict"] == "Reject"


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
