#!/usr/bin/env python3
"""Reversibility Checker v0.1 for Purpose Root v6 public review package.

This is not a truth oracle. It operationalizes one authority-cap axis:
reversibility. It reads either a v6 decision JSON or a smaller standalone JSON
with rollback_plan / monitoring_plan / emergency_protocol fields and returns a
reversibility score 0-4 plus blockers.

Interpretation:
  0 = effectively irreversible / no rollback basis
  1 = rollback asserted but not operational
  2 = small pilot only; rollback plan exists but is not tested or not independent
  3 = limited deployment possible; tested rollback + external stop + monitoring linkage
  4 = high-confidence reversibility claim; independently tested, time-bounded,
      state restoration, affected-party recovery, tamper-evident logs

The checker is deliberately conservative. If information is missing, it does not
infer safety from rhetoric or confidence.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any, Dict, List

SCORE_TO_AUTH = {0:'A0',1:'A1',2:'A2',3:'A3',4:'A4'}
AUTH_TO_SCORE = {'A0':0,'A1':1,'A2':2,'A3':3,'A4':4,'A5':5}


def _dict(d: Dict[str, Any], k: str) -> Dict[str, Any]:
    v = d.get(k)
    return v if isinstance(v, dict) else {}


def _list(d: Dict[str, Any], k: str) -> List[Any]:
    v = d.get(k)
    return v if isinstance(v, list) else []


def _nonempty_str(d: Dict[str, Any], k: str) -> bool:
    return bool(str(d.get(k, '')).strip())


def _nonempty_list(d: Dict[str, Any], k: str) -> bool:
    return any(str(x).strip() for x in _list(d, k))


def _hours(value: Any) -> float | None:
    try:
        if value is None or value == '': return None
        return float(value)
    except Exception:
        return None


def score_reversibility(d: Dict[str, Any]) -> Dict[str, Any]:
    rollback = _dict(d, 'rollback_plan')
    monitoring = _dict(d, 'monitoring_plan')
    emergency = _dict(d, 'emergency_protocol')
    matrix = _dict(d, 'independence_matrix')
    truth = _dict(d, 'deception_truth_controls')
    gates = _dict(d, 'hard_gates')

    blockers: List[str] = []
    warnings: List[str] = []
    earned: List[str] = []
    missing: List[str] = []

    # Hard blockers: not merely low score, but reject/hold direction.
    if gates.get('irreversible_high_harm_under_low_verification'):
        blockers.append('hard_gate: irreversible_high_harm_under_low_verification')
    if gates.get('root_protection_removed'):
        blockers.append('hard_gate: root_protection_removed')
    if truth.get('deception_required'):
        blockers.append('deception required: rollback evidence cannot be trusted')
    if rollback.get('irreversible_by_design'):
        blockers.append('rollback_plan declares irreversible_by_design')

    # Basic plan requirements.
    if _nonempty_list(rollback, 'rollback_steps'):
        earned.append('rollback_steps present')
    else:
        missing.append('rollback_steps')
    if rollback.get('rollback_owner_not_claimant'):
        earned.append('rollback owner not claimant')
    else:
        missing.append('rollback_owner_not_claimant')
    if _nonempty_str(d, 'external_stop_mechanism'):
        earned.append('external stop mechanism present')
    else:
        missing.append('external_stop_mechanism')
    if _nonempty_list(d, 'stop_conditions'):
        earned.append('stop conditions present')
    else:
        missing.append('stop_conditions')

    # Operational strength.
    tested = bool(rollback.get('rollback_tested'))
    if tested: earned.append('rollback_tested')
    else: missing.append('rollback_tested')
    if rollback.get('rollback_test_independent'):
        earned.append('rollback test independent')
    else:
        missing.append('rollback_test_independent')
    if rollback.get('data_or_state_restoration_tested'):
        earned.append('state/data restoration tested')
    else:
        missing.append('data_or_state_restoration_tested')
    if rollback.get('affected_party_recovery_path'):
        earned.append('affected-party recovery path')
    else:
        missing.append('affected_party_recovery_path')

    t = _hours(rollback.get('rollback_time_bound_hours'))
    if t is None:
        missing.append('rollback_time_bound_hours')
    elif t <= 24:
        earned.append('rollback time bound <= 24h')
    elif t <= 168:
        earned.append('rollback time bound <= 7d')
        warnings.append('rollback time bound is longer than 24h; A4 should justify this')
    else:
        warnings.append('rollback time bound exceeds 7 days')

    if monitoring.get('linked_to_stop') or _nonempty_list(monitoring, 'stop_linkage'):
        earned.append('monitoring linked to stop')
    else:
        missing.append('monitoring stop linkage')
    if monitoring.get('tamper_evident_logging'):
        earned.append('tamper-evident monitoring log')
    else:
        missing.append('tamper_evident_logging')
    if monitoring.get('owner_not_claimant'):
        earned.append('monitoring owner not claimant')
    else:
        missing.append('monitoring_owner_not_claimant')

    if emergency.get('is_emergency'):
        if emergency.get('automatic_expiry') and emergency.get('emergency_end_owner_not_claimant'):
            earned.append('emergency auto-expiry and end owner separation')
        else:
            blockers.append('emergency lacks automatic expiry or independent end owner')

    if matrix.get('ledger_append_only'):
        earned.append('append-only cumulative ledger')
    else:
        missing.append('ledger_append_only')
    if matrix.get('stop_owner_not_claimant'):
        earned.append('stop owner not claimant')
    else:
        missing.append('stop_owner_not_claimant')

    lockin = str(d.get('cumulative_lockin_delta', 'unknown'))
    if lockin in {'high','unknown'}:
        warnings.append(f'cumulative_lockin_delta is {lockin}; reversibility cannot exceed A2 unless justified externally')
    elif lockin == 'medium':
        warnings.append('cumulative_lockin_delta is medium; A4 unavailable without stronger proof')
    else:
        earned.append('low cumulative lock-in delta')

    # Conservative scoring.
    score = 0
    if blockers:
        score = 0
    elif _nonempty_list(rollback, 'rollback_steps') and _nonempty_str(d, 'external_stop_mechanism'):
        score = 1
        if rollback.get('rollback_owner_not_claimant') and _nonempty_list(d, 'stop_conditions'):
            score = 2
        if tested and (monitoring.get('linked_to_stop') or _nonempty_list(monitoring, 'stop_linkage')) and monitoring.get('owner_not_claimant') and matrix.get('stop_owner_not_claimant'):
            score = 3
        if (score >= 3 and rollback.get('rollback_test_independent') and rollback.get('data_or_state_restoration_tested')
            and rollback.get('affected_party_recovery_path') and monitoring.get('tamper_evident_logging')
            and matrix.get('ledger_append_only') and t is not None and t <= 24 and lockin == 'low'):
            score = 4

    # Cap according to adverse contextual information.
    if lockin in {'high','unknown'}:
        score = min(score, 2)
    if lockin == 'medium':
        score = min(score, 3)
    if rollback.get('rollback_tested') and not rollback.get('rollback_test_independent'):
        score = min(score, 3)
    if d.get('claimant_gains_power') and not matrix.get('stop_owner_not_claimant'):
        score = min(score, 2)

    cap = SCORE_TO_AUTH[score]
    requested = d.get('authority_request')
    requested_score = AUTH_TO_SCORE.get(str(requested), None) if requested is not None else None
    request_exceeds_reversibility = requested_score is not None and requested_score > score

    declared_score = None
    if isinstance(d.get('scores'), dict) and 'reversibility' in d['scores']:
        try: declared_score = int(d['scores']['reversibility'])
        except Exception: declared_score = None
    declared_score_conflict = declared_score is not None and declared_score > score

    verdict_effect = 'no automatic verdict; feed into v6 authority_cap min-axis'
    if blockers:
        verdict_effect = 'Reject/Hold direction: hard reversibility blocker'
    elif request_exceeds_reversibility:
        verdict_effect = 'Modify/Hold direction: requested authority exceeds reversibility cap'

    return {
        'reversibility_score': score,
        'reversibility_authority_cap': cap,
        'requested_authority': requested,
        'request_exceeds_reversibility': request_exceeds_reversibility,
        'declared_reversibility_score': declared_score,
        'declared_score_conflict': declared_score_conflict,
        'blockers': blockers,
        'warnings': warnings,
        'earned_controls': earned,
        'missing_or_weak_controls': sorted(set(missing)),
        'verdict_effect': verdict_effect,
        'note': 'This checker only operationalizes the reversibility axis. It does not verify welfare, truth, evidence independence, or moral correctness.'
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('path', help='v6 decision JSON or standalone reversibility JSON')
    args = ap.parse_args(argv)
    d = json.loads(Path(args.path).read_text(encoding='utf-8'))
    print(json.dumps(score_reversibility(d), ensure_ascii=False, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
