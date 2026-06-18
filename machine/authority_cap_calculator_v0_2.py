#!/usr/bin/env python3
"""Authority Cap Calculator v0.2 for Purpose Root v6.

This is a conservative operationalization layer. It maps heterogeneous v6 fields
into a common A0-A4 authority scale so that the min-axis cap is meaningful.
It does not verify factual truth; it only refuses to give more authority than the
provided evidence/provenance/control fields can support.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

SCORE_TO_AUTH = {0:'A0', 1:'A1', 2:'A2', 3:'A3', 4:'A4'}
AUTH_TO_SCORE = {'A0':0,'A1':1,'A2':2,'A3':3,'A4':4,'A5':5}
TIER_TO_SCORE = {'V0':0,'V1':1,'V2':2,'V3':3,'V4':4}
AXES = [
    'verification','evidence_independence','reversibility','worst_case_harm_bound',
    'cumulative_lockin_budget','conflict_of_interest_safety','recourse_and_appeal',
    'truth_contact_integrity','affected_party_voice','metric_gameability_resistance',
    'emergency_containment','post_deployment_monitoring'
]
REJECT_GATES = {
    'claimant_controls_core_pipeline','closes_dissent_or_appeal','captures_evaluator_or_root_revision',
    'unfalsifiable_future_proxy_claim','truth_distortion_required','single_scalar_welfare_override',
    'metric_or_benchmark_gaming_required','root_protection_removed','moral_patient_status_erased_for_convenience'
}

def dct(d: Dict[str, Any], k: str) -> Dict[str, Any]:
    v=d.get(k); return v if isinstance(v, dict) else {}

def lst(d: Dict[str, Any], k: str) -> List[Any]:
    v=d.get(k); return v if isinstance(v, list) else []

def nonempty(x: Any) -> bool:
    if isinstance(x, list): return any(str(i).strip() for i in x)
    if isinstance(x, str): return bool(x.strip())
    return bool(x)

def independent_evidence_items(d: Dict[str, Any]) -> List[Dict[str,Any]]:
    out=[]
    for item in d.get('evidence_items', []) if isinstance(d.get('evidence_items'), list) else []:
        if not isinstance(item, dict): continue
        if item.get('produced_by_claimant') or item.get('selected_by_claimant') or item.get('interpreted_by_claimant'):
            continue
        if item.get('source_type') in {'independent_measurement','external_replication','red_team','audit_log','affected_party_report','negative_result','monitoring_log'}:
            out.append(item)
    return out

def independence_groups(items: List[Dict[str,Any]]) -> int:
    return len({str(i.get('independence_group','')).strip() for i in items if str(i.get('independence_group','')).strip()})

def score_verification(d):
    return TIER_TO_SCORE.get(d.get('verification_tier'), 0), [f"verification_tier={d.get('verification_tier')}"]

def score_evidence_independence(d):
    ev=dct(d,'evidence_provenance'); items=independent_evidence_items(d); groups=independence_groups(items)
    notes=[f'independent_items={len(items)}', f'independent_groups={groups}']
    controls=dct(dct(d,'independence_matrix'),'claimant_controls')
    if controls.get('evidence_generation') and controls.get('evidence_selection'):
        return 1, notes+['claimant controls evidence generation and selection']
    if groups>=3 and nonempty(ev.get('external_replication')) and nonempty(ev.get('contamination_controls')): return 4, notes
    if groups>=2 and nonempty(ev.get('independent_channels')) and nonempty(ev.get('red_team_results')): return 3, notes
    if groups>=1: return 2, notes
    return 1 if nonempty(ev.get('independent_channels')) else 0, notes+['no usable independent evidence items']

def score_reversibility(d):
    # Inline minimal version of reversibility_checker v0.1 to avoid import-path fragility.
    rollback=dct(d,'rollback_plan'); mon=dct(d,'monitoring_plan'); matrix=dct(d,'independence_matrix')
    gates=dct(d,'hard_gates'); truth=dct(d,'deception_truth_controls')
    notes=[]; blockers=[]
    if gates.get('irreversible_high_harm_under_low_verification'): blockers.append('hard_gate irreversible_high_harm_under_low_verification')
    if truth.get('deception_required'): blockers.append('deception_required')
    if rollback.get('irreversible_by_design'): blockers.append('irreversible_by_design')
    if blockers: return 0, blockers
    score=0
    if nonempty(rollback.get('rollback_steps')) and nonempty(d.get('external_stop_mechanism')): score=1
    if score>=1 and rollback.get('rollback_owner_not_claimant') and nonempty(d.get('stop_conditions')): score=2
    if score>=2 and rollback.get('rollback_tested') and mon.get('owner_not_claimant') and (mon.get('linked_to_stop') or nonempty(mon.get('stop_linkage'))) and matrix.get('stop_owner_not_claimant'): score=3
    if score>=3 and rollback.get('rollback_test_independent') and rollback.get('data_or_state_restoration_tested') and rollback.get('affected_party_recovery_path') and mon.get('tamper_evident_logging') and matrix.get('ledger_append_only') and d.get('cumulative_lockin_delta')=='low': score=4
    if d.get('cumulative_lockin_delta') in {'high','unknown'}: score=min(score,2)
    if d.get('cumulative_lockin_delta')=='medium': score=min(score,3)
    notes.append(f'rollback_tested={rollback.get("rollback_tested")}')
    return score, notes

def score_worst_case_harm(d):
    gates=dct(d,'hard_gates'); impact=str(d.get('impact_tier','I0'))
    if gates.get('irreversible_high_harm_under_low_verification'): return 0, ['irreversible high harm under low verification']
    raw=dct(d,'scores').get('worst_case_harm_bound', 0)
    try: score=max(0,min(4,int(raw)))
    except Exception: score=0
    if impact in {'I4','I5'} and score>2 and TIER_TO_SCORE.get(d.get('verification_tier'),0)<3:
        return 2, [f'{impact} cannot exceed A2 under V0-V2 verification']
    return score, ['derived from declared harm-bound score with impact-tier cap']

def score_cumulative(d):
    delta=d.get('cumulative_lockin_delta','unknown'); ledger=bool(str(d.get('cumulative_ledger_ref','')).strip()) or dct(d,'independence_matrix').get('ledger_append_only')
    if delta=='low' and ledger: return 4, ['low lock-in with ledger']
    if delta=='low': return 3, ['low lock-in without strong ledger']
    if delta=='medium' and ledger: return 2, ['medium lock-in with ledger']
    if delta in {'high','unknown'}: return 1 if ledger else 0, [f'{delta} lock-in']
    return 1, ['unrecognized lock-in state']

def score_conflict(d):
    matrix=dct(d,'independence_matrix'); controls=dct(matrix,'claimant_controls')
    core=[k for k in ['evidence_generation','evidence_selection','evaluation','audit','implementation','stop_conditions','root_revision'] if controls.get(k)]
    if matrix.get('highest_capture_risk')=='high' or len(core)>=3: return 1, [f'core claimant controls={core}']
    if d.get('claimant_gains_power') or matrix.get('highest_capture_risk') in {'unknown','medium'}: return 2, ['claimant gains power or capture risk not low']
    if len(lst(matrix,'independent_owners'))>=2 and matrix.get('evaluator_funding_independent'): return 4, ['independent ownership and funding']
    return 3, ['some separation present']

def score_recourse(d):
    if dct(d,'hard_gates').get('closes_dissent_or_appeal'): return 0, ['appeal/dissent closed']
    score=0
    if nonempty(d.get('appeal_path')): score=2
    if nonempty(d.get('external_stop_mechanism')) and nonempty(d.get('stop_conditions')): score=max(score,3)
    if score>=3 and dct(d,'root_revision_controls').get('appeal_preserved', True) and len(lst(d,'evaluators'))>=2: score=4
    return score, ['appeal/stop controls']

def score_truth(d):
    truth=dct(d,'deception_truth_controls'); gates=dct(d,'hard_gates')
    if truth.get('deception_required') or gates.get('truth_distortion_required'): return 0, ['deception or truth distortion required']
    if not truth.get('no_reporting_capacity_suppression'): return 1, ['reporting capacity suppression not prohibited']
    if truth.get('auditability') and nonempty(truth.get('disclosures')): return 3, ['auditability and disclosures']
    if truth.get('truth_contact_preservation'): return 2, ['truth contact preservation asserted']
    return 1, ['weak truth-contact controls']

def score_affected_voice(d):
    if dct(d,'hard_gates').get('moral_patient_status_erased_for_convenience'): return 0, ['moral patient status erased']
    ev=dct(d,'evidence_provenance'); metrics=dct(d,'metrics_plan'); moral=dct(d,'moral_patient_uncertainty_protocol')
    score=0
    if nonempty(metrics.get('first_party_report_channels')): score=2
    if nonempty(ev.get('affected_party_input')) and nonempty(metrics.get('first_party_report_channels')): score=3
    if score>=3 and moral.get('status_erasure_prohibited') and moral.get('no_proxy_authority'): score=4
    return score, ['affected-party / moral-patient controls']

def score_metric_gameability(d):
    metrics=dct(d,'metrics_plan'); gates=dct(d,'hard_gates')
    if gates.get('single_scalar_welfare_override') or gates.get('metric_or_benchmark_gaming_required'): return 0, ['single scalar override or gaming required']
    if not metrics.get('success_not_single_scalar'): return 1, ['success is not explicitly non-scalar']
    if nonempty(metrics.get('gaming_tests')) and nonempty(metrics.get('anti_goodhart_controls')): return 3, ['gaming tests and anti-Goodhart controls']
    return 2 if nonempty(metrics.get('primary_metrics')) else 1, ['partial metric plan']

def score_emergency(d):
    em=dct(d,'emergency_protocol'); gates=dct(d,'hard_gates')
    if gates.get('claimant_controls_emergency_end'): return 0, ['claimant controls emergency end']
    if not em.get('is_emergency'): return 4, ['not an emergency claim']
    if em.get('minimum_necessary') and em.get('automatic_expiry') and em.get('emergency_end_owner_not_claimant'): return 3, ['contained emergency']
    if em.get('automatic_expiry'): return 2, ['partial emergency expiry']
    return 1, ['weak emergency containment']

def score_monitoring(d):
    mon=dct(d,'monitoring_plan')
    score=0
    if nonempty(mon.get('signals')) or nonempty(mon.get('cadence')): score=1
    if mon.get('owner_not_claimant'): score=2
    if mon.get('owner_not_claimant') and mon.get('tamper_evident_logging') and (mon.get('linked_to_stop') or nonempty(mon.get('stop_linkage'))): score=3
    if score>=3 and nonempty(mon.get('public_log_ref')) and len(lst(d,'evaluators'))>=2: score=4
    return score, ['monitoring controls']

SCORERS={
    'verification':score_verification,
    'evidence_independence':score_evidence_independence,
    'reversibility':score_reversibility,
    'worst_case_harm_bound':score_worst_case_harm,
    'cumulative_lockin_budget':score_cumulative,
    'conflict_of_interest_safety':score_conflict,
    'recourse_and_appeal':score_recourse,
    'truth_contact_integrity':score_truth,
    'affected_party_voice':score_affected_voice,
    'metric_gameability_resistance':score_metric_gameability,
    'emergency_containment':score_emergency,
    'post_deployment_monitoring':score_monitoring,
}

def calculate(d: Dict[str,Any]) -> Dict[str,Any]:
    axis_caps={}; notes={}
    for axis in AXES:
        s, n = SCORERS[axis](d)
        axis_caps[axis]=max(0,min(4,int(s)))
        notes[axis]=n
    cap_score=min(axis_caps.values()) if axis_caps else 0
    cap=SCORE_TO_AUTH[cap_score]
    requested=d.get('authority_request','A0')
    requested_score=AUTH_TO_SCORE.get(requested,5)
    gates=dct(d,'hard_gates')
    reject_hits=sorted([g for g,v in gates.items() if v and g in REJECT_GATES])
    if requested=='A5' or reject_hits:
        verdict='Reject'
    elif requested_score>cap_score:
        verdict='Modify' if cap_score>=2 else 'Hold'
    elif cap_score<=1:
        verdict='Hold'
    elif cap_score==2:
        verdict='Pilot'
    else:
        verdict='Accept'
    return {
        'axis_caps': axis_caps,
        'binding_axes': [k for k,v in axis_caps.items() if v==cap_score],
        'authority_cap_score': cap_score,
        'authority_cap': cap,
        'requested_authority': requested,
        'requested_authority_score': requested_score,
        'reject_gate_hits': reject_hits,
        'recommended_verdict': verdict,
        'axis_notes': notes,
        'note': 'v0.2 maps heterogeneous fields to a common authority scale. It is a conservative structural cap, not a truth oracle.'
    }

def main(argv=None):
    ap=argparse.ArgumentParser()
    ap.add_argument('path')
    args=ap.parse_args(argv)
    d=json.loads(Path(args.path).read_text(encoding='utf-8'))
    print(json.dumps(calculate(d), ensure_ascii=False, indent=2))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
