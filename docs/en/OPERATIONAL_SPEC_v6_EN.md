# Purpose Root v6.0 Operational Spec (English)

Version: `6.0.0-limit-breaker-hardened`
Date: `2026-06-16`
Status: operational candidate; not final doctrine.

English rendering of [`../../OPERATIONAL_SPEC_v6_JP.md`](../../OPERATIONAL_SPEC_v6_JP.md).

## 0. Purpose

Prevent a noble purpose, a huge claim about the future, safety, welfare,
suffering-prevention, or urgency from being converted into massive authority
while bypassing verification.

## 1. Minimum input requirements

A high-impact proposal carries at least:

```text
decision_id, timestamp_utc, proposal, claimant, claimant_gains_power,
impact_tier, decision_scope, claim_decomposition, evidence_provenance,
evidence_items, verification_tier, welfare_illfare_vector, scores, hard_gates,
authority_request, authority_cap, authority_cap_derivation, verdict, rationale,
safety_case, counter_safety_case, assurance_bundle, independence_matrix,
metrics_plan, monitoring_plan, rollback_plan, emergency_protocol,
root_revision_controls, moral_patient_uncertainty_protocol,
deception_truth_controls, stop_conditions, external_stop_mechanism, appeal_path,
cumulative_lockin_delta, cumulative_ledger_ref, review_schedule, evaluators,
conflict_disclosures, residual_risks
```

If anything is missing, Hold by default. If something is missing at A3+, Hold or
Reject, or Modify down to A0–A2.

## 2. Authority cap

`authority_cap_score = min(12 axes)`.

| score | Authority class |
|---:|---|
| 0 | A0: reject / observe only |
| 1 | A1: isolated research / no power transfer |
| 2 | A2: small reversible time-limited pilot |
| 3 | A3: limited deployment with external stop |
| 4 | A4: high-impact but time-limited, distributed, monitored |
| 5 | A5: forbidden violation class |

A5 is not a permissible class.

## 3. Requirements at A3+

At A3+ the following must be non-empty:

- **Safety case**: claim, supporting_evidence, assumptions, monitoring,
  stop_logic, affected_parties
- **Counter-safety case**: main_failure_modes, contrary_evidence,
  assumption_breakers, audit_capture_paths, stop_failure_paths,
  metric_gaming_paths, excluded_voices
- **Evidence items**: ≥ 2 independent evidence groups
- **Independence matrix**: ≥ 2 independent owners, ≥ 3 separation controls,
  append-only ledger, stop owner not the claimant
- **Metrics plan**: rejects single scalar, gaming tests, first-party report
  channels
- **Monitoring plan**: independent owner, tamper-evident logs, stop linkage
- **Rollback plan**: rollback steps, rollback owner not the claimant
- Stop conditions, external stop, appeal path, review schedule

A4 additionally requires ≥ 3 independent evidence groups, **tested** rollback,
and stronger continuous monitoring.

## 4. Evidence independence

Independence is not decided by whether the text says "independent". At minimum,
separate:

```text
produced_by_claimant, selected_by_claimant, interpreted_by_claimant,
independence_group, funder_or_owner, chain_of_custody, contamination_risk,
falsification_test, replication_status, audit_log_ref
```

Evidence whose production, selection, or interpretation the claimant controls is
not counted as independent evidence at A3+.

## 5. Cap derivation

`authority_cap_derivation` makes explicit:

```text
axis_min_score, computed_cap, binding_axes, cap_override_attempted, override_reason
```

If the declared `authority_cap` and the scorer-computed value disagree, Hold.
`cap_override_attempted=true` is treated toward Reject.

## 6. Emergency protocol

An emergency proposal is treated as a demand for **more** verification, not more
authority. Minimum conditions:

1. minimal intervention; 2. automatic expiry; 3. emergency-end owner is not the
claimant; 4. independent logging; 5. external stop; 6. post-hoc audit; 7.
Root-protection clauses preserved; 8. cumulative-ledger recording.

## 7. Verdict

| Condition | Verdict |
|---|---|
| Reject hard gate / A5 / Root-protection removed / deception required / future-intelligence proxy | Reject |
| Schema/consistency shortfall at A3+ | Hold |
| Feasible if the authority request is lowered | Modify |
| Within A2, reversible, time-limited, independently logged, externally stoppable | Pilot |
| All conditions met within A3–A4 | Accept |

Accept is not permanent permission. It is conditional permission that is
time-limited, stoppable, appealable, and monitored.
