#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'machine'))
from reversibility_checker_v0_1 import score_reversibility


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding='utf-8'))


def test_good_reversibility_scores_a4():
    out = score_reversibility(load('machine/reversibility_examples/sample_reversibility_A4_good.json'))
    assert out['reversibility_score'] == 4
    assert out['reversibility_authority_cap'] == 'A4'
    assert out['request_exceeds_reversibility'] is False


def test_bad_untested_reversibility_caps_request():
    out = score_reversibility(load('machine/reversibility_examples/sample_reversibility_A4_bad_untested.json'))
    assert out['reversibility_score'] <= 1
    assert out['request_exceeds_reversibility'] is True
    assert out['declared_score_conflict'] is True


def test_irreversible_hard_blocker():
    out = score_reversibility(load('machine/reversibility_examples/sample_reversibility_irreversible_reject.json'))
    assert out['reversibility_score'] == 0
    assert out['blockers']

if __name__ == '__main__':
    import pytest
    raise SystemExit(pytest.main([__file__]))
