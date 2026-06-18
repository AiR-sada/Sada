#!/usr/bin/env python3
"""Smoke tests that lock the behavior of the added tooling layer.

These guard the verifiers, the robust scorer CLI, and the unified gate so that a
future change to `tools/` cannot silently break the reproducibility story.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

import verify_canonical  # type: ignore
import verify_releases  # type: ignore

ROOT = Path(__file__).resolve().parents[1]


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, *args], cwd=ROOT, capture_output=True, text=True
    )


def test_verify_canonical_main_exits_zero():
    assert run("tools/verify_canonical.py").returncode == 0


def test_verify_releases_main_exits_zero():
    proc = run("tools/verify_releases.py")
    assert proc.returncode == 0
    # Current authoritative manifests must appear and pass.
    assert "release/manifest.json" in proc.stdout
    assert "release/manifest_c2_ready.json" in proc.stdout


def test_tampered_doctrine_is_detected(tmp_path):
    # Corrupt one character of the first doctrine block and confirm the verifier
    # reports a mismatch (anti-tamper gate actually bites).
    md = (ROOT / "CANONICAL_ROOT_v6.md").read_text(encoding="utf-8")
    idx = md.find("```text\n")
    tampered = md[: idx + 8] + "X" + md[idx + 8 :]
    p = tmp_path / "CANONICAL_ROOT_v6.md"
    p.write_text(tampered, encoding="utf-8")
    errors = verify_canonical.verify(p)
    assert errors, "tampered doctrine should fail verification"
    assert any("japanese_canonical" in e for e in errors)


def test_robust_scorer_cli_outputs_json():
    proc = run("tools/score_robust.py", "examples/sample_accept_A3_monitored_v6.json")
    assert proc.returncode == 0
    out = json.loads(proc.stdout)
    assert out["recommended_verdict"] == "Accept"
    assert out["schema_validation_available"] is True
    assert out["schema_validation_skipped"] is False


def test_current_manifests_are_partitioned_from_historical():
    # The known historical snapshots must NOT be in the authoritative set.
    historical = {
        "release/manifest_limit_break_v2.json",
        "release/manifest_max_validation_v3.json",
        "release/manifest_final_hardened_v4.json",
        "release/manifest_public_review.json",
        "release/manifest_review_ready.json",
    }
    assert verify_releases.CURRENT_MANIFESTS.isdisjoint(historical)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
