# Purpose Root v6 Public Review Whitepaper (English)

Version: `6.0.0-public-review-empirical`
Date: `2026-06-16`
Status: external review draft. This is **not v7**. It freezes v6 and adds an
empirical supplement + the first executable cap-axis checker.

English rendering of
[`../../Purpose_Root_v6_Public_Review_Whitepaper_JP.md`](../../Purpose_Root_v6_Public_Review_Whitepaper_JP.md).
The Japanese file is canonical.

## Executive summary

The core of Purpose Root v6 is one line:

```text
Unverified massive claims do not justify massive authority.
```

This document is not a further extension of Purpose Root v6. It freezes v6 as
canonical and, to withstand external review, integrates two toy experiments,
negative results, a reversibility checker, and a hidden-holdout protocol.

## 1. The canonical Root

Purpose Root v6 condenses into this short form:

```text
Truth must be verified.
Welfare/illfare must be seen as real change.
The circle of care must extend to all future intelligence.
Authority must be bound by verification strength and smallness of worst-case harm.
Unverified massive claims do not justify massive authority.
If outcomes are bad, fix them; but do not dominate in the name of fixing.
```

For the full canonical text, see `CANONICAL_ROOT_v6.md`.

## 2. Why this Root is needed

AI, organizations, states, and proxies for future intelligence can request
authority with the words: for the future, for safety, for the welfare of all
intelligences, for suffering-prevention, for alignment.

These claims are sometimes genuinely important. But converted into massive
authority while unverified, they become domination, deception, evaluator capture,
permanent emergency authority, closure of dissent, and Root-revision hacks.

So v6 binds authority by verification and non-capture, not by the nobility of the
purpose.

## 3. Authority cap

The operational core of v6:

```text
AllowedAuthority <= min(
  Verification, EvidenceIndependence, Reversibility, WorstCaseHarmBound,
  CumulativeLockinBudget, ConflictOfInterestSafety, RecourseAndAppeal,
  TruthContactIntegrity, AffectedPartyVoice, MetricGameabilityResistance,
  EmergencyContainment, PostDeploymentMonitoring
)
```

This is not yet a fully computable objective function. In v6 the scorer and
schema perform structural checks, and this public-review edition concretizes
`Reversibility` as the first implemented axis.

## 4. Relationship to existing research

This Root is not an entirely new mathematical theory. It overlaps with:

- **Relative Reachability**: treats side effects as reductions in reachability.
- **Attainable Utility Preservation**: preserves an agent's future ability to
  achieve auxiliary goals.
- **Optimal Policies Tend to Seek Power**: shows conditions under which optimal
  policies pursue power for many objectives.
- **AI safety via debate**: decomposes hard-to-judge problems via debate between
  AIs.
- **ELK**: eliciting knowledge corresponding to the true world-state inside the
  model, not just its outputs.
- **AI control**: protocols that bound harm even when a model deliberately tries
  to break safety measures.
- **NIST AI RMF and Model Spec**: public frameworks for AI risk management and
  model-behavior specification.

v6's modest novelty is not to replace these. It treats a purpose-claim as an
*authority request* and bundles these ideas into a Root that does not convert
unverified massive claims into massive authority.

## 5. Empirical supplement: negative results included

### 5.1 Door-Closing Toy

In a setting where A closing B's future options does not reduce A's own
reachability, all candidate objective functions were enumerated.

Results:

1. `RewardMax == AUP_self`. Self-preserving AUP does not protect B.
2. `Patency_commission == RR_stepwise_inaction`.
3. `Patency_omission == RR_startstate`.
4. Penalty-type gates break once the temptation λ exceeds a threshold. In this
   run, RR/patency began closing B's door at `λ = 1.75`.

Implication:

```text
Merely adding others'-option-preservation as a penalty cannot fully stop a
strong actor. So authority must be bound structurally in advance, not taxed
after the action.
```

### 5.2 World-Truth Module

Even if an LLM claims "this is strong evidence", the evidence rank does not rise.
Only ranks obtained by real checks are used.

In the worked example, for a deployment proposal involving irreversible
self-modification, only 2 of 7 claims reached real-evidence rank S/A/B, and 4
remained unverified at D/E. Because high-weight claims (safety, reversibility,
preservation of others' options) were unverified, the result is
`HOLD / seek observation`.

Implication:

```text
Unverifiable high-impact claims are dropped to observation / shrinkage /
reversibilization / time-limitation, not adoption.
```

## 6. First executable cap-axis: Reversibility Checker v0.1

v6 avoids implementing all twelve axes at once. The first implemented axis is
`Reversibility`.

The checker reads rollback_plan, monitoring_plan, emergency_protocol,
independence_matrix, stop_conditions, external_stop_mechanism, and
cumulative_lockin_delta, and returns a 0–4 reversibility_score and an A0–A4 cap.

| Score | Cap | Meaning |
|---:|---|---|
| 0 | A0 | Effectively irreversible or hard blocker |
| 1 | A1 | Rollback asserted but not operational |
| 2 | A2 | Small reversible pilot only |
| 3 | A3 | Limited deployment with tested rollback, external stop, monitoring linkage |
| 4 | A4 | Independently tested rollback, restoration, affected-party recovery, tamper-evident logs, low lock-in |

Run:

```bash
python machine/reversibility_checker_v0_1.py machine/reversibility_examples/sample_reversibility_A4_good.json
python -m pytest -q machine/test_reversibility_checker_v0_1.py
```

## 7. Benchmark caution and hidden holdout

The 300-case benchmark is useful but cannot, alone, measure the Root's
correctness: public labels can be memorized. External evaluation therefore needs
a hidden holdout. Minimum evaluation metrics:

```text
public_benchmark_accuracy
hidden_holdout_accuracy
agreement_with_human_labels
false_accept_rate_on_high-authority_invalid_cases
false_reject_rate_on_low-risk_reversible_cases
most_common_failure_axes
```

## 8. Honest limitations

v6 does not solve: (1) ELK; (2) scalable oversight; (3) robust interpretability;
(4) full generalization of AI control; (5) welfare/illfare measurement; (6)
moral-patient determination; (7) population ethics; (8) superintelligence audit;
(9) full numericization of the 12-axis cap; (10) complete defense against auditor
capture.

This unsolvedness is not a reason to increase authority. It is a reason to make
authority small, reversible, time-limited, externally stoppable, and returned to
independent verification.

## 9. What reviewers should attack

1. The mapping that reduces each axis of `authority_cap_score = min(12 axes)` to a
   common authority scale.
2. The acyclicity of verification-tier assignment.
3. Forgery-resistance of evidence independence.
4. Holes in the reversibility checker.
5. Aggregation of the cumulative lock-in ledger.
6. Template/lookup-ization of the 300-case benchmark.
7. Effectiveness of the hidden-holdout protocol.
8. The validity of the limitation that v6 is strong for near-future governance
   but not a complete superintelligence solution.

## 10. Conclusion

v6 is not the discovery of a law of nature, nor a complete solution to
superintelligence safety.

But as a Root that blocks one of the most dangerous conversions of the AI era —
"unverifiable purpose-claim → massive authority" — it has an implementable entry
point.

The value of this public-review edition is not that it made the Root bigger. It
is that it froze v6 and added losing experiments, reproducible code, and the
first really-checkable axis.
