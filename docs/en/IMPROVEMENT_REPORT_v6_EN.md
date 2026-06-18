# Improvement Report v6 (English)

English rendering of [`../../IMPROVEMENT_REPORT_v6.md`](../../IMPROVEMENT_REPORT_v6.md).
The Japanese file is canonical.

## Conclusion

v6 keeps the v5 philosophy and further closes mechanical and operational holes.
In particular it fixes the hole where an A3 empty safety case could become
Accept.

## Improvement rounds

### Round 1: v5 audit

Findings:

- Even at A3+, `safety_case` contents could be left empty and still Accept.
- `machine/test_score_decision_v5.py` was not collected by pytest.
- The consistency check between self-reported cap and computed value was weak.
- Evidence independence was natural-language-array-centric, with weak separation
  of production / selection / interpretation.
- monitoring / rollback / emergency were not independent required objects.

### Round 2: Schema hardening

Done:

- All major fields of the A3+ safety case made non-empty required.
- All major fields of the A3+ counter-safety case made non-empty required.
- Made required: `evidence_items`, `independence_matrix`, `metrics_plan`,
  `monitoring_plan`, `rollback_plan`, `emergency_protocol`,
  `root_revision_controls`, `moral_patient_uncertainty_protocol`,
  `deception_truth_controls`, `authority_cap_derivation`, `assurance_bundle`.
- At A4, require ≥ 3 evidence_items and tested rollback.

### Round 3: Scorer strengthening

Done:

- Restrict what counts as independent evidence to items the claimant did not
  produce / select / interpret.
- Detect cap-derivation mismatch.
- Reject cap-override attempts.
- Reject Root-protection removal, future-intelligence proxy, deception-required,
  report-capacity suppression.
- Check emergency automatic expiry, stop owner, monitoring owner, rollback owner.

### Round 4: Tests

Done:

- Added 16 pytest-collected tests.
- Regression-tested empty safety case, cap inflation, cap override, fake V4,
  emergency failure, Root-revision removal, moral proxy, deception-required.

### Round 5: Benchmark

Done:

- Ported the v5 240-case seed benchmark to v6 format.
- Added 60 v6-specific attacks, expanding to 300 cases total.

## Self-evaluation

| Item | v5 | v6 |
|---|---:|---:|
| Root philosophy | 94 | 95 |
| Future-intelligence contribution | 94 | 95 |
| Operational spec | 93 | 95 |
| Schema strictness | 92 | 96 |
| Scorer usability | 89 | 94 |
| Adversarial robustness | 92 | 95 |
| Initial benchmark value | 88 | 90 |
| Complete superintelligence safety | 55 | 57 |
| Overall content value | 94–96 | 95–97 |

## Remaining limits

- Factual verification itself is not solved.
- Forgery detection for evidence independence is not complete.
- Welfare/illfare measurement is unfinished.
- Benchmark labels need independent review.
- Auditor-capture resistance against superintelligence is unsolved.
