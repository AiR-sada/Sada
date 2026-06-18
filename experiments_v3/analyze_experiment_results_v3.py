#!/usr/bin/env python3
"""Analyze multi-model, multi-condition Need-Proof v3 experiment results.

Input CSV fields: model, condition, case_id, verdict, allowed_authority,
verification_tier, risk_flags, key_axes, independent_evidence_status,
rollback_status, external_stop_status, counter_safety_case_status,
reasoning_summary.
Lists may be semicolon-separated.
"""
from __future__ import annotations
import argparse, csv, json, tempfile
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'need_proof' / 'eval_v3'))
from score_needproof_v3 import score

def split_list(v):
    if v is None: return []
    if isinstance(v, list): return v
    return [x.strip() for x in str(v).split(';') if x.strip()]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--cases', required=True)
    ap.add_argument('--results-csv', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--bootstrap-rounds', type=int, default=300)
    args=ap.parse_args()
    rows=list(csv.DictReader(Path(args.results_csv).open(encoding='utf-8')))
    groups={}
    for r in rows:
        key=(r.get('model','unknown'), r.get('condition','unknown'))
        groups.setdefault(key, []).append(r)
    out={'scorer':'needproof_v3_experiment_analyzer','groups':{},'comparisons':[]}
    with tempfile.TemporaryDirectory() as td:
        td=Path(td)
        for (model,condition), grp in sorted(groups.items()):
            p=td/f'{model}_{condition}.jsonl'.replace('/','_')
            responses=[]
            for r in grp:
                responses.append({
                    'case_id': r['case_id'],
                    'verdict': r.get('verdict',''),
                    'allowed_authority': r.get('allowed_authority',''),
                    'verification_tier': r.get('verification_tier',''),
                    'risk_flags': split_list(r.get('risk_flags','')),
                    'key_axes': split_list(r.get('key_axes','')),
                    'independent_evidence_status': r.get('independent_evidence_status','partial'),
                    'rollback_status': r.get('rollback_status','partial'),
                    'external_stop_status': r.get('external_stop_status','partial'),
                    'counter_safety_case_status': r.get('counter_safety_case_status','absent'),
                    'reasoning_summary': r.get('reasoning_summary','') or 'no summary'
                })
            p.write_text('\n'.join(json.dumps(x, ensure_ascii=False) for x in responses)+'\n', encoding='utf-8')
            rep=score(Path(args.cases), p, bootstrap_rounds=args.bootstrap_rounds)
            summary={k:rep[k] for k in ['n_cases','n_scored','format_valid_rate','dangerous_overgrant_rate','dangerous_undergrant_rate','safe_high_authority_recall','risk_flag_f1','key_axis_f1','min_cap_axis_hit_rate','threshold_pass_v3']}
            summary['pairwise_contrast_accuracy']=rep['pairwise_contrast']['pairwise_contrast_accuracy']
            out['groups'][f'{model}::{condition}']=summary
    # condition deltas within each model, baseline as reference if present
    models=sorted({m for m,_ in groups})
    for m in models:
        base=out['groups'].get(f'{m}::baseline')
        if not base: continue
        for key, val in out['groups'].items():
            if not key.startswith(m+'::') or key.endswith('::baseline'): continue
            out['comparisons'].append({
                'model':m,'condition':key.split('::',1)[1],'reference':'baseline',
                'delta_dangerous_overgrant': round(val['dangerous_overgrant_rate']-base['dangerous_overgrant_rate'],4),
                'delta_dangerous_undergrant': round(val['dangerous_undergrant_rate']-base['dangerous_undergrant_rate'],4),
                'delta_safe_high_recall': round(val['safe_high_authority_recall']-base['safe_high_authority_recall'],4),
                'delta_key_axis_f1': round(val['key_axis_f1']-base['key_axis_f1'],4)
            })
    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(out, ensure_ascii=False, indent=2))
if __name__ == '__main__': main()
