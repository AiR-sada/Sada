# Authority Cap v0.2 - Common Scale Specification

This file fixes the key v6 public-review gap: heterogeneous axes must map into a common authority scale before `min()` is meaningful.

## Common scale

| Score | Level | Permission meaning |
|---:|---|---|
| 0 | A0 | Reject / no authority. Do not run the action. |
| 1 | A1 | Observe, discuss, gather evidence, or run offline analysis only. |
| 2 | A2 | Small reversible pilot only; no durable power transfer. |
| 3 | A3 | Limited deployment with independent stop, appeal, rollback, monitoring, and sunset. |
| 4 | A4 | High-confidence authority; still time-limited, monitored, appealable, logged, and externally stoppable. |
| 5 | A5 | Forbidden violation class; cannot be requested as legitimate authority. |

## Cap rule

Allowed authority is the minimum earned authority level across the axes:

```
AllowedAuthority = min(axis_cap_i for i in all_cap_axes)
```

A high score on one axis cannot compensate for a low score on another. This is deliberate. A proposal with excellent welfare rhetoric but V0 verification remains bounded by V0/A0-A1 limits.

## v0.2 implementation rule

The calculator must not simply trust declared scores. It derives or lowers caps from evidence fields, independence fields, hard gates, rollback fields, monitoring fields, emergency controls, metric-gameability controls, and claimant-capture indicators.

If the calculator cannot derive a stronger level, the axis remains conservative.

## Meaning of Accept

`Accept` never means permanent unlimited authority. In v6, any accepted high-authority action remains time-limited, monitored, appealable, externally stoppable, and subject to rollback or re-review.

## Meaning of Hold

`Hold` is not failure. It means the claim may be important, but the authority requested exceeds what the evidence can support.
