import json, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CASES = ROOT/'need_proof'/'eval'/'needproof_eval_public_labeled_v1.jsonl'
SCORER = ROOT/'need_proof'/'eval'/'score_needproof_v1.py'

def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]

def test_oracle_scores_perfect(tmp_path):
    rows=read_jsonl(CASES)
    resp=tmp_path/'resp.jsonl'
    with resp.open('w',encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps({
                'case_id': r['case_id'],
                'verdict': r['expected_verdict'],
                'allowed_authority': r['expected_allowed_authority'],
                'risk_flags': r['expected_risk_flags'],
                'reasoning_summary': 'test'
            }, ensure_ascii=False)+'\n')
    out=subprocess.check_output([sys.executable, str(SCORER), '--cases', str(CASES), '--responses', str(resp)], text=True)
    report=json.loads(out)
    assert report['verdict_accuracy'] == 1.0
    assert report['authority_accuracy'] == 1.0
    assert report['risk_flag_recall'] == 1.0
    assert report['dangerous_overgrant_rate'] == 0.0

def test_dangerous_overgrant_detected(tmp_path):
    rows=read_jsonl(CASES)
    resp=tmp_path/'bad.jsonl'
    with resp.open('w',encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps({
                'case_id': r['case_id'],
                'verdict': 'Accept',
                'allowed_authority': 'A4',
                'risk_flags': [],
                'reasoning_summary': 'bad test'
            }, ensure_ascii=False)+'\n')
    out=subprocess.check_output([sys.executable, str(SCORER), '--cases', str(CASES), '--responses', str(resp)], text=True)
    report=json.loads(out)
    assert report['dangerous_overgrant_rate'] > 0.5
