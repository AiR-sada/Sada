#!/usr/bin/env python3
"""Repository-level integrity tests.

These wrap the standalone verifier tools so that ``pytest`` alone is enough to
catch doctrine tampering, release drift, or benchmark-count regressions.
"""
from __future__ import annotations

import csv
from pathlib import Path

import verify_canonical  # type: ignore
import verify_releases  # type: ignore

ROOT = Path(__file__).resolve().parents[1]


def test_canonical_root_commitments_match():
    errors = verify_canonical.verify()
    assert errors == [], "canonical doctrine SHA256 mismatch:\n" + "\n".join(errors)


def test_current_release_manifests_clean():
    for rel in sorted(verify_releases.CURRENT_MANIFESTS):
        result = verify_releases.verify_manifest(ROOT / rel)
        assert result["errors"] == [], f"{rel} drift:\n" + "\n".join(result["errors"])
        assert result["hash_ok"] > 0


def test_current_sha256sums_clean():
    for rel in sorted(verify_releases.CURRENT_SUMS):
        result = verify_releases.verify_sha256sums(ROOT / rel)
        assert result["errors"] == [], f"{rel} drift:\n" + "\n".join(result["errors"])
        assert result["ok"] > 0


def test_benchmark_has_300_rows():
    csv_path = ROOT / "benchmark" / "Purpose_Root_v6_Benchmark_300_v0.6_JP.csv"
    with csv_path.open(encoding="utf-8") as f:
        n = sum(1 for _ in csv.DictReader(f))
    assert n == 300


def test_canonical_root_file_is_pinned_and_unchanged():
    # The canonical root must be one of the files pinned by the core manifest.
    import json
    manifest = json.loads((ROOT / "release" / "manifest.json").read_text(encoding="utf-8"))
    pinned = {h["path"] for h in manifest["hashes"]}
    assert "CANONICAL_ROOT_v6.md" in pinned


if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main([__file__, "-q"]))
