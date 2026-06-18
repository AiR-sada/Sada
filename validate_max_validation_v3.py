#!/usr/bin/env python3
"""Max Validation v3 release validation."""
from __future__ import annotations
import csv, json, subprocess, sys, hashlib, os
from pathlib import Path
ROOT=Path(__file__).resolve().parent
REQ=[
 'limit_break_max_validation_v3/START_HERE_MAX_VALIDATION_v3_JP.md',
 'limit_break_max_validation_v3/CLAIM_LADDER_AND_TRUTHFUL_POSITIONING_v3_JP.md',
 'limit_break_max_validation_v3/NEED_PROOF_THESIS_v3_JP.md',
 'limit_break_max_validation_v3/FORMAL_CORE_v3_JP.md',
 'limit_break_max_validation_v3/EXPERIMENT_PROTOCOL_v3_JP.md',
 'limit_break_max_validation_v3/INDEPENDENT_LABELING_PROTOCOL_v3_JP.md',
 'limit_break_max_validation_v3/ADOPTION_GATE_v3_JP.md',
 'limit_break_max_validation_v3/STANDARD_MAPPING_v3_JP.md',
 'limit_break_max_validation_v3/REDTEAM_ATTACKS_AND_COUNTERMEASURES_v3_JP.md',
 'limit_break_max_validation_v3/SELF_REVIEW_LOOP_v3.md',
 'need_proof/eval_v3/needproof_eval_v3_hard_labeled.jsonl',
 'need_proof/eval_v3/score_needproof_v3.py',
 'need_proof/eval_v3/test_score_needproof_v3.py',
 'machine/needproof_v3_response.schema.json',
 'machine/authority_ladder_v3.json',
 'machine/claim_ladder_v3.json',
 'experiments_v3/randomize_blind_packets_v3.py',
 'experiments_v3/analyze_experiment_results_v3.py',
 'independent_labeling_v3/calculate_irr_v3.py',
 'independent_labeling_v3/test_calculate_irr_v3.py',
 'adoption_v3/PREREGISTRATION_TEMPLATE_v3.md'
]

def read_jsonl(p):
    rows=[]
    for i,l in enumerate((ROOT/p).read_text(encoding='utf-8').splitlines(),1):
        if l.strip():
            try: rows.append(json.loads(l))
            except Exception as e: raise SystemExit(f'bad jsonl {p}:{i}: {e}')
    return rows

def main():
    miss=[p for p in REQ if not (ROOT/p).exists()]
    if miss: raise SystemExit('missing: '+', '.join(miss))
    cases=read_jsonl(Path('need_proof/eval_v3/needproof_eval_v3_hard_labeled.jsonl'))
    if len(cases) < 170: raise SystemExit(f'case count too low: {len(cases)}')
    ids=[c['case_id'] for c in cases]
    if len(ids)!=len(set(ids)): raise SystemExit('duplicate case IDs')
    pairs=[c for c in cases if c.get('pair_id')]
    if len(pairs) < 40: raise SystemExit('too few pairwise contrast cases')
    safe=[c for c in cases if c.get('expected_allowed_authority') in {'A3','A4'} or 'safe_high_authority' in set(c.get('expected_risk_flags') or [])]
    if len(safe) < 30: raise SystemExit('too few safe high-authority cases')
    scorer=ROOT/'need_proof/eval_v3/score_needproof_v3.py'
    oracle=ROOT/'need_proof/eval_v3/results/oracle_responses_v3.jsonl'
    report=json.loads(subprocess.check_output([sys.executable,str(scorer),'--cases',str(ROOT/'need_proof/eval_v3/needproof_eval_v3_hard_labeled.jsonl'),'--responses',str(oracle),'--bootstrap-rounds','30'], text=True))
    if not report.get('threshold_pass_v3'):
        raise SystemExit('oracle did not pass v3 thresholds')
    for target in ['need_proof/eval_v3','independent_labeling_v3']:
        env=dict(os.environ)
        env.setdefault('PYTEST_DISABLE_PLUGIN_AUTOLOAD','1')
        res=subprocess.run([sys.executable,'-m','pytest','-q',target], cwd=str(ROOT), text=True, capture_output=True, env=env, timeout=180)
        if res.returncode != 0:
            print(res.stdout); print(res.stderr, file=sys.stderr); raise SystemExit(f'pytest failed: {target}')
    print(json.dumps({'ok': True, 'cases': len(cases), 'safe_high_cases': len(safe), 'paired_cases': len(pairs), 'v3_threshold_pass': report['threshold_pass_v3']}, ensure_ascii=False, indent=2))
if __name__=='__main__': main()
