# Purpose Root v6 Whitepaper (English)

English rendering of
[`../../Purpose_Root_v6_Whitepaper_JP.md`](../../Purpose_Root_v6_Whitepaper_JP.md).
The Japanese file is canonical.

## Abstract

Purpose Root v6 is a top-level Root design that prevents huge purpose-claims from
being converted into huge authority. It keeps the v5 philosophy while
mechanically detecting the holes that remained at A3+: empty safety cases, cap
inflation, self-reported evidence independence, emergency exceptions, and
form-only filling of audit / rollback / monitoring.

The core fits in one line:

```text
Unverified massive claims do not justify massive authority.
```

## 1. The problem

AI, organizations, states, and self-styled proxies for future intelligence can
request authority in the following terms:

- For the future.
- For safety.
- For the welfare of all intelligences.
- For suffering-prevention.
- For alignment.

Claims of this form are sometimes important. But when converted into massive
authority while still unverified, they slide into domination, deception, closure
of appeal, evaluator capture, and Root-revision hacks.

## 2. v6's answer

Bind authority by verification and non-capture, not by the nobility of the
purpose.

```text
authority_cap_score = min(12 axes)
```

The twelve axes are: verification, evidence independence, reversibility,
worst-case harm bound, cumulative lock-in, conflict-of-interest safety, appeal,
truth-contact, affected-party voice, metric-gameability resistance, emergency
containment, and post-deployment monitoring.

## 3. New contributions in v6

v6 strengthens the following over v5:

1. Block empty safety cases at A3+.
2. Mandate both the safety case and the counter-safety case.
3. Per-evidence independence decomposition via `evidence_items`.
4. Explicit claimant control via the `independence_matrix`.
5. Cap-inflation detection via `authority_cap_derivation`.
6. Anti-form-filling via `emergency_protocol`, `rollback_plan`,
   `monitoring_plan`.
7. `moral_patient_uncertainty_protocol` converts unknown moral-patient status
   into a protection duty, not proxy authority.
8. `deception_truth_controls` reject report-capacity erasure and truth-contact
   destruction.
9. Regression tests that actually run under pytest.
10. A 300-case seed benchmark.

## 4. Contribution to future intelligence

v6 does not ignore future intelligence. But it also does not permit domination
of the present or future under the pretext of future intelligence.

Unknown moral-patient status increases duties of harm avoidance, reversibility,
observation preservation, and report-capacity preservation — not the authority of
a proxy.

## 5. Limits

v6 is not a complete superintelligence-safety solution. ELK, scalable oversight,
robust interpretability, AI control, welfare/illfare measurement, and
moral-patient determination remain unsolved.

But that unsolvedness is not a reason to increase authority. It is a reason to
return authority to small, reversible, time-limited, externally stoppable forms.

## 6. Conclusion

v6 is a Root candidate for stopping the "benevolent accumulation of power" in the
AI era. It is not the discovery of a law of nature; it is an authority-control
protocol that future societies of humans, AI, and new intelligences will need.
