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

### Orientation & specs

1. [README.en.md](README.en.md) — what this is and the core constraints
2. [START_HERE.en.md](START_HERE.en.md) — the loophole table and how to run it
3. [OPERATIONAL_SPEC_v6_EN.md](OPERATIONAL_SPEC_v6_EN.md) — inputs, the 12-axis cap, A3+ requirements, verdicts
4. [MACHINE_SPEC_v6_EN.md](MACHINE_SPEC_v6_EN.md) — what the machine layer does and does not do
5. [EVIDENCE_INDEPENDENCE_SPEC_v6_EN.md](EVIDENCE_INDEPENDENCE_SPEC_v6_EN.md) — how evidence independence is decomposed
6. [ASSURANCE_CASE_REQUIREMENTS_v6_EN.md](ASSURANCE_CASE_REQUIREMENTS_v6_EN.md) — safety case / counter-safety case requirements
7. [LIMITATIONS_AND_OPEN_PROBLEMS_v6_EN.md](LIMITATIONS_AND_OPEN_PROBLEMS_v6_EN.md) — what v6 does not claim to solve

### Whitepapers

8. [WHITEPAPER_v6_EN.md](WHITEPAPER_v6_EN.md) — the v6 whitepaper
9. [PUBLIC_REVIEW_WHITEPAPER_v6_EN.md](PUBLIC_REVIEW_WHITEPAPER_v6_EN.md) — public-review edition with toy experiments, negative results, and the reversibility checker

### Threat model & red team

10. [THREAT_MODEL_v6_EN.md](THREAT_MODEL_v6_EN.md) — attacks in scope and what is not trusted
11. [REDTEAM_ADV_CASES_v6_EN.md](REDTEAM_ADV_CASES_v6_EN.md) — ten advanced adversarial cases and how v6 handles them

### Process & QA

12. [IMPROVEMENT_REPORT_v6_EN.md](IMPROVEMENT_REPORT_v6_EN.md) — the v5→v6 improvement rounds
13. [SELF_REVIEW_LOG_v6_EN.md](SELF_REVIEW_LOG_v6_EN.md) — self-evaluation scores and self-critique
14. [QA_REPORT_v6_EN.md](QA_REPORT_v6_EN.md) — machine/example/render QA
15. [QA_REPORT_PUBLIC_REVIEW_EN.md](QA_REPORT_PUBLIC_REVIEW_EN.md) — public-review package QA

> The remaining Japanese-only material is the rendered binaries (DOCX/PDF), the
> benchmark data, and the per-stage `START_HERE_*` / `README_*` pointers for the
> historical sub-releases. The doctrine, specs, whitepapers, threat model, red
> team, and QA are now all available in English.

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
