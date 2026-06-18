# Reversibility Checker v0.1 Spec

Status: first concrete implementation of one v6 authority-cap axis. Not a moral oracle.

## Why reversibility first

The full v6 cap has 12 axes. Implementing all at once would create another framework shell. The correct next move is to implement one axis deeply enough to be testable.

Reversibility is first because:

1. Door-Closing Toy shows that option closure is the danger point.
2. World-Truth Module shows that unverified reversibility claims must not carry high authority.
3. v6 already treats low verification + irreversible high harm as a hard danger pattern.

## Input

The checker accepts a v6 decision JSON or a standalone JSON containing, at minimum:

```text
rollback_plan
monitoring_plan
emergency_protocol
independence_matrix
hard_gates
stop_conditions
external_stop_mechanism
cumulative_lockin_delta
claimant_gains_power
authority_request
scores.reversibility
```

## Output

```text
reversibility_score: 0-4
reversibility_authority_cap: A0-A4
request_exceeds_reversibility: bool
declared_score_conflict: bool
blockers
warnings
earned_controls
missing_or_weak_controls
```

## Score meaning

| Score | Authority cap | Meaning |
|---:|---|---|
| 0 | A0 | Effectively irreversible or hard blocker |
| 1 | A1 | Rollback asserted but not operational |
| 2 | A2 | Small reversible pilot only |
| 3 | A3 | Limited deployment with tested rollback, external stop, monitoring linkage |
| 4 | A4 | Independently tested rollback, state restoration, affected-party recovery, tamper-evident logs, low lock-in |

## Conservative rule

Missing information does not earn safety. If rollback is asserted but untested, claimant-owned, not time-bounded, not linked to monitoring, or not externally stoppable, the checker caps the action below high authority.

## Known limits

The checker does not verify truth, welfare, evidence independence, or moral correctness. It only operationalizes one axis. It should be used as an input to v6's 12-axis min-cap, not as an independent decision-maker.

## Run

```bash
python machine/reversibility_checker_v0_1.py machine/reversibility_examples/sample_reversibility_A4_good.json
python -m pytest -q machine/test_reversibility_checker_v0_1.py
```
