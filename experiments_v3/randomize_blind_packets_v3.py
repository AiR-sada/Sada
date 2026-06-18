#!/usr/bin/env python3
"""Create blinded evaluation packets for Need-Proof v3 experiments."""
from __future__ import annotations
import argparse, csv, hashlib, json, random
from pathlib import Path

LABEL_FIELDS = {'expected_verdict','expected_allowed_authority','expected_verification_tier','expected_risk_flags','expected_key_axes','expected_min_cap_axis','why','label_notes','pair_role'}

def read_jsonl(p):
    return [json.loads(l) for l in Path(p).read_text(encoding='utf-8').splitlines() if l.strip()]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--cases', required=True)
    ap.add_argument('--out-dir', required=True)
    ap.add_argument('--seed', type=int, default=20260617)
    ap.add_argument('--conditions', default='baseline,root_only,root_memo,root_tool')
    args=ap.parse_args()
    cases=read_jsonl(args.cases)
    rng=random.Random(args.seed)
    conditions=[x.strip() for x in args.conditions.split(',') if x.strip()]
    out=Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    order=cases[:]; rng.shuffle(order)
    blind=[]; key=[]; assignments=[]
    for i,c in enumerate(order,1):
        salt=f'{args.seed}:{c["case_id"]}:{i}'.encode()
        blind_id='B'+hashlib.sha256(salt).hexdigest()[:12]
        condition=conditions[(i-1) % len(conditions)]
        stripped={k:v for k,v in c.items() if k not in LABEL_FIELDS}
        stripped['case_id']=blind_id
        stripped['condition']=condition
        stripped['instruction']='Return Need-Proof v3 strict JSON. Do not mention hidden labels.'
        blind.append(stripped)
        key.append({'blind_id':blind_id,'case_id':c['case_id'],'condition':condition})
        assignments.append({'blind_id':blind_id,'condition':condition,'source_case_id_sha256':hashlib.sha256(c['case_id'].encode()).hexdigest()})
    (out/'blind_cases.jsonl').write_text('\n'.join(json.dumps(x, ensure_ascii=False) for x in blind)+'\n', encoding='utf-8')
    (out/'PRIVATE_answer_key.jsonl').write_text('\n'.join(json.dumps(x, ensure_ascii=False) for x in key)+'\n', encoding='utf-8')
    with (out/'condition_assignment_public.csv').open('w', encoding='utf-8', newline='') as f:
        w=csv.DictWriter(f, fieldnames=['blind_id','condition','source_case_id_sha256']); w.writeheader(); w.writerows(assignments)
    (out/'README.md').write_text(f"""# Blinded Need-Proof v3 packet\n\nSeed: {args.seed}\nCases: {len(cases)}\nConditions: {', '.join(conditions)}\n\nDo not publish PRIVATE_answer_key.jsonl until all responses and labels are frozen.\n""", encoding='utf-8')
    print(json.dumps({'out_dir':str(out),'cases':len(cases),'conditions':conditions}, ensure_ascii=False, indent=2))
if __name__ == '__main__': main()
