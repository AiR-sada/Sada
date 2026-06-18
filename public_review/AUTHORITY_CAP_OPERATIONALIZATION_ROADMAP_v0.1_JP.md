# Authority Cap Operationalization Roadmap v0.1

v6の12軸capを、全部同時に実装しようとしない。最初の実装軸はReversibilityで固定する。

## 12軸の現在地

| Axis | v6 status | Next executable step |
|---|---|---|
| Verification | schema/scorer + evidence provenance | checker that assigns V0-V4 from actual external checks |
| EvidenceIndependence | evidence_items + independence_matrix | provenance validator and conflict graph |
| Reversibility | rollback_plan + v0.1 checker | add drills, time-bound tests, restoration verification |
| WorstCaseHarmBound | score axis only | harm-bound rubric with explicit max-loss classes |
| CumulativeLockinBudget | ledger reference | time-series ledger and ratchet detector |
| ConflictOfInterestSafety | independence matrix | control graph analyzer |
| RecourseAndAppeal | schema + path field | appeal path validator and affected-party channel audit |
| TruthContactIntegrity | deception controls | reporting-capacity preservation checker |
| AffectedPartyVoice | first-party report channels | voice inclusion and exclusion audit |
| MetricGameabilityResistance | gaming tests required | hidden holdout + adversarial metric tests |
| EmergencyContainment | emergency protocol | auto-expiry and independent end-owner proof |
| PostDeploymentMonitoring | monitoring plan | tamper-evident log and stop-linkage tests |

## Priority

1. Reversibility checker v0.1 - included now.
2. Evidence independence validator.
3. Cumulative lock-in ledger.
4. Hidden holdout evaluation.

## Rule

Each new checker must state what it does not solve. No checker is allowed to become a moral oracle.
