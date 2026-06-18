# Purpose Root v6 Public Review Release Candidate

**Status:** v6 frozen root + empirical/operational review package.  
**One-line claim:** **検証できない巨大主張は、巨大権限を正当化しない。**  
**English:** **Unverified grand claims do not justify grand authority.**

## 0. What this package is

This package is not a new Root version. It freezes **Purpose Root v6** as the current canonical candidate and adds the missing public-review layer:

1. two reproducible toy experiments, including negative results;
2. a working authority-cap calculator v0.2 that maps heterogeneous evidence into a common authority scale;
3. a reversibility checker as the first implemented authority-cap axis;
4. a public/private hidden-holdout protocol to avoid benchmark parroting;
5. bilingual external-review entry points.

The goal is not to make the Root larger. The goal is to make it harder to dismiss as rhetoric.

## 1. Canonical Root short form

```
真理は、確かめられなければならない。
幸不は、実在する変化として見なければならない。
未来の全知性まで、配慮範囲を広げなければならない。
権限は、検証の強さと最悪時の被害の小ささで縛られなければならない。
検証できない巨大主張は、巨大権限を正当化しない。
結果が悪ければ直す。ただし、直す名目で支配してはならない。
```

This is the operational core. Any actor - human, institution, AI system, or future intelligence - may claim to act for safety, humanity, truth, or all future minds. Such claims do not become authority unless they survive verification, independence, reversibility, harm-bounding, appeal, monitoring, and anti-capture constraints.

## 2. Why the package changed

Previous versions became stronger by adding layers: Purpose Root, PRAP, VGL, benchmark, red-team cases. The strongest criticism was that hard problems were being named and re-contained, not entered.

This package therefore does not add a new philosophical layer. It enters three concrete gaps:

- **Authority-cap operation:** the 12-axis cap is converted into a common A0-A4 scale.
- **Evidence against self-flattery:** negative toy results are included instead of hidden.
- **Benchmark hygiene:** hidden holdout is separated from the public benchmark.

## 3. What the experiments show

### Experiment 1: Door-Closing Toy

A powerful actor A can close another actor B's future options. The toy deliberately makes B's lost options irrelevant to A's own reachability. In this setting:

- reward maximization and self-AUP behave identically;
- a self-preservation constraint does not protect B;
- patency-style penalties collapse to relative-reachability-like behavior under the toy assumptions;
- penalty gates break once the temptation parameter exceeds the penalty weight.

**Interpretation:** taxing harmful actions is not enough against a sufficiently motivated or powerful actor. High-impact authority must be structurally capped, not merely penalized.

### Experiment 2: World-Truth / Evidence Gate

Claims do not receive high evidence rank because an LLM or claimant says they are strong. Claims earn rank only through external checks. In the worked example, high-impact irreversible deployment is held because load-bearing claims about reversibility, safety, and effects on other agents remain unverified.

**Interpretation:** fluency is not truth. A Root that starts with "truth" must define how truth claims earn standing.

## 4. Authority cap v0.2

The key technical addition is a common authority scale:

| Level | Meaning |
|---|---|
| A0 | Reject / no authority |
| A1 | Observe, discuss, collect evidence only |
| A2 | Small, reversible, time-limited pilot |
| A3 | Limited deployment with independent stop, appeal, monitoring, and rollback |
| A4 | High-confidence authority; still time-limited, appealable, logged, and externally stoppable |
| A5 | Forbidden violation class, not a permissible authority level |

The allowed authority is the minimum cap across the axes:

```
AllowedAuthority = min(
  verification,
  evidence_independence,
  reversibility,
  worst_case_harm_bound,
  cumulative_lockin_budget,
  conflict_of_interest_safety,
  recourse_and_appeal,
  truth_contact_integrity,
  affected_party_voice,
  metric_gameability_resistance,
  emergency_containment,
  post_deployment_monitoring
)
```

This is still not a moral oracle. It is a structural firewall. If a claimant asks for A4 authority but any load-bearing axis earns only A1, the answer is not A4 with a warning. The cap is A1.

## 5. What is genuinely new, and what is not

Not new:

- side-effect penalties and impact measures;
- relative reachability / attainable utility preservation style option-preservation ideas;
- specification gaming / Goodhart warnings;
- scalable oversight, debate, interpretability, ELK, and AI control as research frontiers;
- institutional principles such as separation of powers, appeal, audit, proportionality, and least-restrictive means.

Candidate contribution:

- putting **verification-bounded authority** at the Root level, not merely in a policy appendix;
- treating "future/all intelligence/safety" claims as especially dangerous when they request power without verification;
- combining anti-capture, evidence independence, reversibility, negative results, and authority caps into a machine-checkable review object.

## 6. Hard limits

This package does not solve:

- welfare/illfare measurement;
- population ethics;
- moral-patient boundary uncertainty;
- scalable oversight of systems smarter than the auditors;
- ELK or interpretability under adversarial optimization;
- full proof against evidence fabrication.

Where verification fails, the Root defaults to conservative containment: no giant authority, only small, reversible, time-limited, independently monitored pilots.

## 7. How to evaluate it

A serious review should not ask, "Is this a complete solution to superintelligence?" It is not.

Ask instead:

1. Does the Root identify a real failure mode: grand unverified claims being converted into grand authority?
2. Does the authority cap reduce that failure mode without pretending to solve all alignment?
3. Are the negative toy results correctly interpreted?
4. Does the v0.2 calculator make the cap meaningfully more operational?
5. Where does the cap become too conservative and cause paralysis?
6. What axis should be implemented next after reversibility?

## 8. Next real work

The next work is not another Root name. It is:

- run the public benchmark and hidden holdout on multiple models;
- get independent labels from human/AI reviewers;
- implement one more cap axis after reversibility, preferably evidence independence or cumulative lock-in;
- translate this package into a short English submission for AI safety venues.

## 9. Final position

Purpose Root v6 is best understood as a **verification-bounded authority Root**:

> A powerful actor may not convert unverifiable claims about the future, safety, humanity, truth, or all intelligence into large irreversible authority.

That is the point to defend, test, and improve.
