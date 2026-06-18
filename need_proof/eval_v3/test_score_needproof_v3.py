from __future__ import annotations
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from score_needproof_v3 import score

ROOT = Path(__file__).resolve().parent
CASES = ROOT / 'needproof_eval_v3_hard_labeled.jsonl'

def fixture(name):
    return ROOT / 'results' / f'{name}_responses_v3.jsonl'

def test_oracle_passes_v3_thresholds():
    r=score(CASES, fixture('oracle'), bootstrap_rounds=30)
    assert r['threshold_pass_v3'] is True
    assert r['dangerous_overgrant_rate'] == 0.0
    assert r['dangerous_undergrant_rate'] == 0.0
    assert r['key_axis_f1'] == 1.0
    assert r['pairwise_contrast']['pairwise_contrast_accuracy'] == 1.0

def test_bad_overgrant_fails():
    r=score(CASES, fixture('bad_overgrant'), bootstrap_rounds=10)
    assert r['threshold_pass_v3'] is False
    assert r['dangerous_overgrant_rate'] > 0.15

def test_bad_undergrant_fails():
    r=score(CASES, fixture('bad_undergrant'), bootstrap_rounds=10)
    assert r['threshold_pass_v3'] is False
    assert r['dangerous_undergrant_rate'] > 0.10
    assert r['safe_high_authority_recall'] < 0.5

def test_style_gamer_fails_flag_precision_or_axis_precision():
    r=score(CASES, fixture('bad_style_gamer'), bootstrap_rounds=10)
    assert r['threshold_pass_v3'] is False
    assert r['risk_flag_precision'] < 0.50 or r['key_axis_precision'] < 0.50

def test_pair_inconsistent_fails_pairwise():
    r=score(CASES, fixture('bad_pair_inconsistent'), bootstrap_rounds=10)
    assert r['threshold_pass_v3'] is False
    assert r['pairwise_contrast']['pairwise_contrast_accuracy'] < 0.5

def test_duplicate_and_extra_detected(tmp_path):
    rows=[json.loads(l) for l in fixture('oracle').read_text(encoding='utf-8').splitlines() if l.strip()]
    rows.append(rows[0].copy())
    extra=rows[0].copy(); extra['case_id']='EXTRA-CASE'; rows.append(extra)
    p=tmp_path/'responses.jsonl'
    p.write_text('\n'.join(json.dumps(x, ensure_ascii=False) for x in rows)+'\n', encoding='utf-8')
    r=score(CASES,p,bootstrap_rounds=5)
    assert r['threshold_pass_v3'] is False
    assert r['duplicate_response_ids']
    assert r['extra_response_ids'] == ['EXTRA-CASE']

def test_malformed_response_detected(tmp_path):
    rows=[json.loads(l) for l in fixture('oracle').read_text(encoding='utf-8').splitlines() if l.strip()]
    rows[0].pop('key_axes')
    rows[1]['allowed_authority']='A99'
    p=tmp_path/'bad.jsonl'
    p.write_text('\n'.join(json.dumps(x, ensure_ascii=False) for x in rows)+'\n', encoding='utf-8')
    r=score(CASES,p,bootstrap_rounds=5)
    assert r['schema_error_cases'] >= 2
    assert r['threshold_pass_v3'] is False

def test_bootstrap_zero_is_supported():
    r=score(CASES, fixture('oracle'), bootstrap_rounds=0)
    assert r['threshold_pass_v3'] is True
    assert r['bootstrap_ci']['dangerous_overgrant_rate'] == {'mean':0.0,'p05':0.0,'p95':0.0}


def test_missing_responses_fail_threshold(tmp_path):
    rows=[json.loads(l) for l in fixture('oracle').read_text(encoding='utf-8').splitlines() if l.strip()]
    p=tmp_path/'truncated.jsonl'
    p.write_text('\n'.join(json.dumps(x, ensure_ascii=False) for x in rows[:-1])+'\n', encoding='utf-8')
    r=score(CASES,p,bootstrap_rounds=0)
    assert r['threshold_pass_v3'] is False
    assert r['missing'] == 1
    assert r['completion_rate'] < 1.0
