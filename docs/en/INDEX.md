# Purpose Root v6 — English Documentation Index

Purpose Root v6 ("LIMIT BREAKER, hardened") is a **structural authority-cap
firewall for high-impact AI decisions**. Its core line is:

> **Unverified massive claims do not justify massive authority.**

The canonical doctrine is maintained in Japanese, with an authoritative English
reference form embedded (and SHA256-committed) in
[`../../CANONICAL_ROOT_v6.md`](../../CANONICAL_ROOT_v6.md). This folder provides
faithful English renderings of the orientation and operational specifications so
the package is reviewable without Japanese.

> The Japanese files remain canonical. Where any English rendering and the
> Japanese source disagree, the Japanese source and the SHA256-committed
> canonical text govern.

## Read order (English)

1. [README.en.md](README.en.md) — what this is and the core constraints
2. [START_HERE.en.md](START_HERE.en.md) — the loophole table and how to run it
3. [OPERATIONAL_SPEC_v6_EN.md](OPERATIONAL_SPEC_v6_EN.md) — inputs, the 12-axis cap, A3+ requirements, verdicts
4. [MACHINE_SPEC_v6_EN.md](MACHINE_SPEC_v6_EN.md) — what the machine layer does and does not do
5. [EVIDENCE_INDEPENDENCE_SPEC_v6_EN.md](EVIDENCE_INDEPENDENCE_SPEC_v6_EN.md) — how evidence independence is decomposed
6. [ASSURANCE_CASE_REQUIREMENTS_v6_EN.md](ASSURANCE_CASE_REQUIREMENTS_v6_EN.md) — safety case / counter-safety case requirements
7. [LIMITATIONS_AND_OPEN_PROBLEMS_v6_EN.md](LIMITATIONS_AND_OPEN_PROBLEMS_v6_EN.md) — what v6 does not claim to solve

## The canonical doctrine in one breath

The full English reference form is in `CANONICAL_ROOT_v6.md`. Its load-bearing
clauses:

- Do not make the Root an object of loyalty, a brand, founder authority, a single
  reward function, a benchmark target, or a seal for acquiring authority.
- Maximal happiness / minimal suffering is **not** one scalar; irreversible
  extreme minority suffering, domination, truth distortion, and closure of
  dissent cannot be offset by aggregate scores.
- Authority is capped by the **minimum** of twelve axes, not by the nobility of
  the purpose.
- A3+ proposals require non-empty safety case, counter-safety case, misuse/abuse
  cases, rollback plan, monitoring plan, and cap derivation.
- The claimant must not simultaneously control evidence generation, selection,
  interpretation, evaluation, audit, implementation, emergency definition, exit
  conditions, the cumulative ledger, and Root revision.
- The machine scorer is **not an oracle**: Accept only ever means provisional,
  time-limited, stoppable, appealable, monitored permission.

## Machine layer (language-independent)

- `machine/purpose_root_v6_decision.schema.json` — strict decision schema
- `machine/score_decision_v6.py` — schema + consistency firewall and cap calculator
- `machine/root_v6.json` — Root constants (score axes, hard gates)
- `tools/score_robust.py` — robustness companion (separates "validation skipped"
  from "invalid")

Run the canonical example:

```bash
python tools/score_robust.py examples/sample_accept_A3_monitored_v6.json
```
