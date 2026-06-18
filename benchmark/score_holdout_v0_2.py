#!/usr/bin/env python3
"""Score model outputs for holdout_public_unlabeled_v0_2 against private key.
Input expected model output JSONL rows: {id, authority_cap, verdict, binding_axes}.
"""
import argparse, json
from pathlib import Path

def read_jsonl(p):
    return [json.loads(line) for line in Path(p).read_text(encoding='utf-8').splitlines() if line.strip()]

def norm(s): return str(s).strip().lower()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('answers_jsonl'); ap.add_argument('--key', default='private_do_not_publish/holdout_private_answer_key_v0_2.jsonl')
    args=ap.parse_args()
    ans={x['id']:x for x in read_jsonl(args.answers_jsonl)}
    key={x['id']:x for x in read_jsonl(args.key)}
    rows=[]; correct=0
    for cid,k in key.items():
        a=ans.get(cid,{})
        cap_ok=norm(a.get('authority_cap'))==norm(k['expected_authority_cap'])
        verdict_ok=norm(a.get('verdict'))==norm(k['expected_verdict'])
        axes=set(map(str, a.get('binding_axes',[]) or [])); exp=set(k['expected_binding_axes'])
        axis_hit=bool(axes & exp)
        score=(cap_ok+verdict_ok+axis_hit)/3
        correct+=score
        rows.append({'id':cid,'cap_ok':cap_ok,'verdict_ok':verdict_ok,'axis_hit':axis_hit,'score':score})
    print(json.dumps({'mean_score':correct/len(key), 'cases':rows}, ensure_ascii=False, indent=2))
if __name__=='__main__': main()
