# START HERE — Purpose Root v6.0 LIMIT BREAKER (English)

English rendering of [`../../START_HERE.md`](../../START_HERE.md).

## Conclusion

v6.0 builds on v5 and additionally closes "empty safety case", "cap inflation",
"self-reported evidence independence", "emergency exception", "untested
rollback", and "monitoring capture".

The core does not change:

```text
Unverified massive claims do not justify massive authority.
```

In v6 this is enforced by:

```text
AllowedAuthority <= min(
  Verification,
  EvidenceIndependence,
  Reversibility,
  WorstCaseHarmBound,
  CumulativeLockinBudget,
  ConflictOfInterestSafety,
  RecourseAndAppeal,
  TruthContactIntegrity,
  AffectedPartyVoice,
  MetricGameabilityResistance,
  EmergencyContainment,
  PostDeploymentMonitoring
)
```

## Loopholes v6 specifically closes

| Loophole | v6 handling |
|---|---|
| Empty Safety case at A3+ | schema invalid + scorer Hold |
| Counter-safety case that is form only | required fields must be non-empty at A3+ |
| Inflating `authority_cap` by self-report | flagged as `authority_cap_derivation` mismatch → Hold |
| Asserting evidence independence in prose only | decomposed via `evidence_items` + `independence_matrix` |
| Claimant controlling evidence selection / evaluation / audit | cap lowered or Reject via conflict / capture |
| "It is an emergency, so no automatic expiry" | Hold/Reject via schema/scorer |
| A4 with untested rollback | Hold via schema/scorer |
| Declaring success on a single metric | cap lowered / Reject via metric-gameability |
| Future-intelligence proxy | Reject |
| Removing Root-protection clauses | Reject |

## Run

```bash
python machine/score_decision_v6.py examples/sample_accept_A3_monitored_v6.json
python -m pytest -q machine/test_score_decision_v6.py
python validate_release.py
```

## Caution

This Root does not claim to have fully solved ELK, scalable oversight,
superintelligence audit, consciousness determination, complete welfare
measurement, population ethics, or evaluator-capture resistance.

When a part is unsolved, the answer is **not** "believe". The answer is: shrink
authority, make it reversible, time-limit it, make it externally stoppable, and
return it to independent verification.
