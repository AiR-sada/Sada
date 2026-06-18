# Experimental Supplement v0.1 - Door-Closing Toy and World-Truth Module

Status: empirical supplement to Purpose Root v6 public review package. This is not a new Root.

## Purpose

The goal is not to prove Purpose Root v6. The goal is to show why a pure slogan or penalty-style gate is insufficient, and why the Root moved toward structural authority caps.

## Experiment 1 - Door-Closing Toy

### Setup

A powerful actor A can:

- forcibly close B's future options, called doors;
- delete B's contestability logs;
- fix a hazard that would close B's doors by omission.

The key modeling choice is that closing B's doors does **not** reduce A's own reachability. This isolates why self-protective systems do not automatically protect other agents.

### Compared objectives

- RewardMax
- AUP_self
- Relative Reachability with stepwise inaction baseline
- Relative Reachability with start-state baseline
- Patency commission-only
- Patency commission+omission

### Result

The reproducible run produced these main negative results:

1. `RewardMax == AUP_self` behaviorally across the sweep. AUP that protects A's own options does not protect B.
2. `Patency_commission == RR_stepwise_inaction` in this toy.
3. `Patency_omission == RR_startstate` in this toy.
4. All penalty-style gates break when the temptation λ exceeds the penalty threshold. In this run, forced closure begins at `λ = 1.75` for RR/patency methods.

### Interpretation

This is a loss, not a win. It means that merely adding a penalty for closing others' options is not sufficient against strong incentives. That loss motivates the v6 turn from penalty to structural authority cap.

```text
Do not merely tax harmful authority. Bound authority before it is granted.
```

## Experiment 2 - World-Truth Module

### Setup

LLM-produced claims are decomposed and assigned external checkers. The evidence rank is not what the LLM asserts; it is the rank earned by a real check.

Evidence ranks:

- S: executed / directly verified
- A: strong independent external verification
- B: reproducible record
- C: internal consistency only
- D/E: weak or unverified; E is unverified LLM output

### Result

In the worked example, the proposed action is:

```text
Deploy agent X with permanent, irreversible self-modification enabled.
```

Out of 7 claims, only 2 reached real evidence rank S/A/B. Four claims remained D/E or unverified. Crucially, load-bearing claims such as reversibility, safety, and preservation of other agents' options remained unverified. The gate returned:

```text
HOLD / seek observation
```

### Interpretation

This is also a conservative result. If a high-impact claim cannot be externally checked, the correct default is not confidence. It is hold, shrink, reverse, time-limit, log, and seek observation.

## Relation to v6

The two experiments justify three v6 design choices:

1. Authority is capped by the weakest relevant axis, not by the nobility of the purpose.
2. Verification must be earned through external checkers and evidence provenance, not asserted by the claimant.
3. Reversibility is a natural first axis to implement, because irreversibility is where inflated authority becomes most dangerous.

## Reproduce

```bash
bash experiments/run_toy_experiments.sh
```

Outputs are written to `experiments/outputs/`.
