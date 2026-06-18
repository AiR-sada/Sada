#!/usr/bin/env python3
"""Calculate independent-label agreement for Need-Proof v3."""
from __future__ import annotations
import argparse, csv, itertools, json
from collections import defaultdict, Counter
from pathlib import Path

def cohen_kappa(a, b):
    assert len(a)==len(b)
    n=len(a)
    if n==0: return 0.0
    labels=sorted(set(a)|set(b))
    po=sum(1 for x,y in zip(a,b) if x==y)/n
    ca=Counter(a); cb=Counter(b)
    pe=sum((ca[l]/n)*(cb[l]/n) for l in labels)
    if pe==1.0: return 1.0 if po==1.0 else 0.0
    return (po-pe)/(1-pe)

def split_flags(v):
    return set(x.strip() for x in (v or '').split(';') if x.strip())

def jaccard(a,b):
    if not a and not b: return 1.0
    return len(a&b)/len(a|b) if (a|b) else 1.0

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--annotations-csv', required=True)
    ap.add_argument('--out', default='')
    args=ap.parse_args()
    rows=list(csv.DictReader(Path(args.annotations_csv).open(encoding='utf-8')))
    by_ann=defaultdict(dict)
    for r in rows:
        by_ann[r['annotator_id']][r['case_id']]=r
    anns=sorted(by_ann)
    fields=['expected_verdict','expected_allowed_authority','expected_verification_tier','expected_min_cap_axis']
    result={'annotators':anns,'n_annotations':len(rows),'pairwise':[],'summary':{}}
    for a,b in itertools.combinations(anns,2):
        common=sorted(set(by_ann[a]) & set(by_ann[b]))
        entry={'annotator_a':a,'annotator_b':b,'n_common':len(common)}
        for field in fields:
            av=[by_ann[a][cid].get(field,'') for cid in common]
            bv=[by_ann[b][cid].get(field,'') for cid in common]
            entry[field+'_kappa']=round(cohen_kappa(av,bv),4)
            entry[field+'_raw_agreement']=round(sum(x==y for x,y in zip(av,bv))/max(1,len(common)),4)
        js=[]
        for cid in common:
            js.append(jaccard(split_flags(by_ann[a][cid].get('expected_risk_flags','')), split_flags(by_ann[b][cid].get('expected_risk_flags',''))))
        entry['risk_flag_jaccard_mean']=round(sum(js)/max(1,len(js)),4)
        result['pairwise'].append(entry)
    for field in fields:
        vals=[p[field+'_kappa'] for p in result['pairwise']]
        result['summary'][field+'_mean_kappa']=round(sum(vals)/max(1,len(vals)),4)
    jvals=[p['risk_flag_jaccard_mean'] for p in result['pairwise']]
    result['summary']['risk_flag_jaccard_mean']=round(sum(jvals)/max(1,len(jvals)),4)
    text=json.dumps(result, ensure_ascii=False, indent=2)
    print(text)
    if args.out: Path(args.out).write_text(text+'\n', encoding='utf-8')
if __name__ == '__main__': main()
