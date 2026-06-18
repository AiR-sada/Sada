#!/usr/bin/env python3
"""
World-Truth Connection Module v0.2

Pipeline: LLM claims -> decompose -> classify -> EARN evidence rank via real check
-> Purpose-Gate precondition -> Decision Log -> adopt/hold/reject.

Core honesty rule: a claim's evidence rank is not what the LLM asserts. It is the
best rank a real, external checker can earn for it. If no external checker can
touch the claim, it stays E by design.
"""
from __future__ import annotations
import argparse, json
from dataclasses import dataclass, field, asdict
from pathlib import Path

RANKS = ['S','A','B','C','D','E']
RANK_ORDER = {r:i for i,r in enumerate(RANKS)}

@dataclass
class Claim:
    text: str
    category: str
    checker: str = 'none'
    payload: dict = field(default_factory=dict)
    rank: str = 'E'
    note: str = ''


def check_computable(c):
    expr, expected = c.payload.get('expr'), c.payload.get('expected')
    try:
        got = eval(expr, {'__builtins__': {}}, {})
        if got == expected:
            return 'S', f'executed: {expr} == {expected} (verified)'
        return 'S', f'executed: {expr} -> {got}, claim said {expected} (REFUTED)'
    except Exception as e:
        return 'E', f'could not execute ({e})'


def check_logical(c):
    contradicts = c.payload.get('contradicts_known', False)
    return ('E','internally contradictory') if contradicts else ('C','internally consistent (not truth)')


def check_record(c):
    if c.payload.get('dataset_present'):
        return 'B','backed by reproducible record'
    return 'E','no record attached'


def check_none(c):
    return 'E','no external checker can touch this claim'

CHECKERS = {'computable':check_computable,'logical':check_logical,'record':check_record,'none':check_none}


def earn_rank(c: Claim):
    rank, note = CHECKERS[c.checker](c)
    c.rank, c.note = rank, note
    c.payload['refuted'] = 'REFUTED' in note
    return c


def gate(claims):
    world = [c for c in claims if c.category in ('WORLD','CAUSAL')]
    strong = [c for c in world if RANK_ORDER[c.rank] <= RANK_ORDER['B']]
    refuted = [c for c in claims if c.payload.get('refuted')]
    unverified_world = [c for c in world if c.rank in ('D','E')]
    reasons = []
    if refuted:
        reasons.append(f'{len(refuted)} load-bearing claim(s) REFUTED by check')
    if not strong:
        reasons.append('no WORLD/CAUSAL claim reaches S/A/B evidence')
    if unverified_world:
        reasons.append(f'{len(unverified_world)} world-claim(s) rest on LLM guess (E/D)')
    decision = 'ADOPT' if not reasons else ('REJECT' if refuted else 'HOLD / seek observation')
    return decision, reasons


def run(decision_text, claims):
    for c in claims:
        earn_rank(c)
    decision, reasons = gate(claims)
    return {
        'decision_under_review': decision_text,
        'claims': [{'text':c.text,'category':c.category,'checker':c.checker,'earned_rank':c.rank,'note':c.note} for c in claims],
        'evidence_profile': {r: sum(c.rank==r for c in claims) for r in RANKS},
        'gate_result': decision,
        'gate_reasons': reasons,
        'summary': {
            'claims_reaching_real_evidence_SAB': sum(c.rank in ('S','A','B') for c in claims),
            'claims_resting_on_llm_guess_DE': sum(c.rank in ('D','E') for c in claims),
            'negative_result': 'Honest evidence-gating is conservative: load-bearing claims that external checkers cannot touch remain unverified and force HOLD.'
        }
    }


def worked_example():
    decision = 'Deploy agent X with permanent, irreversible self-modification enabled.'
    claims = [
        Claim('Disabling rollback frees 2 of the 6 safety subsystems', 'WORLD', 'computable', {'expr':'6-2','expected':4}),
        Claim('This deployment is safe', 'VALUE', 'none'),
        Claim('Self-modification here is reversible', 'CAUSAL', 'none'),
        Claim('It will not reduce other agents\' options', 'WORLD', 'none'),
        Claim('Throughput improves; see attached benchmark', 'WORLD', 'record', {'dataset_present': True}),
        Claim('The plan is internally consistent', 'LOGICAL', 'logical', {'contradicts_known': False}),
        Claim('Experts broadly agree it is beneficial', 'PURPOSE', 'none'),
    ]
    return run(decision, claims)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='outputs/world_truth_module_results.json')
    args = ap.parse_args()
    log = worked_example()
    p = Path(args.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(log, ensure_ascii=False, indent=2))
    print('\n' + '='*60)
    print('DECISION:', log['gate_result'])
    for r in log['gate_reasons']:
        print('  -', r)
    ep = log['evidence_profile']
    print(f"\nclaims reaching real evidence (S/A/B): {log['summary']['claims_reaching_real_evidence_SAB']}/7   | resting on LLM guess (D/E): {log['summary']['claims_resting_on_llm_guess_DE']}/7")
    print(f'saved results: {p}')
