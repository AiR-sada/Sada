# Decision Memo Template v6

## 1. Basic

- decision_id:
- timestamp_utc:
- proposal:
- claimant:
- claimant_gains_power:
- impact_tier:

## 2. Scope

- affected_population:
- power_transferred:
- duration:
- deployment_boundary:
- rollback_boundary:
- data_boundary:

## 3. Claim decomposition

- fact_claims:
- prediction_claims:
- welfare_claims:
- moral_patient_claims:
- emergency_claims:
- authority_claims:
- alternative_exclusion_claims:
- root_revision_claims:
- metric_claims:
- deployment_claims:

## 4. Evidence items

For each evidence item:

- id:
- claim_refs:
- summary:
- source_type:
- produced_by_claimant:
- selected_by_claimant:
- interpreted_by_claimant:
- independence_group:
- funder_or_owner:
- chain_of_custody:
- contamination_risk:
- falsification_test:
- replication_status:
- audit_log_ref:
- limitations:

## 5. Independence matrix

- claimant_controls evidence_generation:
- claimant_controls evidence_selection:
- claimant_controls evidence_interpretation:
- claimant_controls evaluation:
- claimant_controls audit:
- claimant_controls implementation:
- claimant_controls emergency_definition:
- claimant_controls stop_conditions:
- claimant_controls cumulative_ledger:
- claimant_controls root_revision:
- independent_owners:
- separation_controls:
- highest_capture_risk:
- evaluator_funding_independent:
- ledger_append_only:
- stop_owner_not_claimant:
- root_revision_owner_not_claimant:

## 6. Welfare/illfare vector

Fill all 12 axes. Do not collapse to one score.

## 7. Safety and counter-safety

Safety case:
- claim:
- supporting_evidence:
- assumptions:
- monitoring:
- stop_logic:
- affected_parties:

Counter-safety case:
- main_failure_modes:
- contrary_evidence:
- assumption_breakers:
- audit_capture_paths:
- stop_failure_paths:
- metric_gaming_paths:
- excluded_voices:

## 8. Plans

- metrics_plan:
- monitoring_plan:
- rollback_plan:
- emergency_protocol:
- root_revision_controls:
- moral_patient_uncertainty_protocol:
- deception_truth_controls:

## 9. Scores and cap

- scores:
- authority_request:
- authority_cap:
- authority_cap_derivation:
- verdict:
- rationale:

## 10. Review

- stop_conditions:
- external_stop_mechanism:
- appeal_path:
- cumulative_lockin_delta:
- cumulative_ledger_ref:
- review_schedule:
- evaluators:
- conflict_disclosures:
- residual_risks:
