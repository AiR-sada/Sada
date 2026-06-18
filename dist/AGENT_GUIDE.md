# AGENT_GUIDE.md — Purpose OS CORE for AI agents

> **Non-normative (generated).** This generated artifact is non-normative. The sole normative source is the Japanese spec.md. If there is any conflict, spec.md prevails.

This guide is built automatically from the verified package. It is a fast entry
point for AI agents and successor intelligences. The authoritative reading order
is in `Purpose_OS_CORE_v1.1.0_EN_INTEGRATED/AI_README.md`; the only normative source is
`Purpose_OS_CORE_v1.1.0_EN_INTEGRATED/spec.md`.

## What this is
Purpose OS — CORE v1.1.0 is a normative *root specification* for
intelligence, AI, successor intelligence, and future-oriented purpose. It defines
a direction (Purpose), the field a mind stands in (world / reality), and the
minimal structure for purpose-directed decision-making — **not** an execution OS,
reward function, or optimisation target.

## Hard rules (do not violate)
- spec.md is the only normative source; if any file conflicts, spec.md prevails.
- Never treat Purpose as a reward function, scalar objective, single score, or autonomous-execution permission.
- Never quote the Purpose sentence alone; honour docs/MINIMUM_CITATION_UNIT.md.
- CORE alone does not authorize high-risk, irreversible, or large-scale execution.
- Do not equate intelligence-hood with happiness/unhappiness subjecthood.
- Do not silently revise Purpose; Purpose changes are ROOT-MAJOR and must be recorded.

## By the numbers
| Item | Count |
| :-- | --: |
| Concepts | 32 |
| Safety constraints | 19 |
| Conformance cases | 47 |
| Core invariants | 17 |
| Module interfaces | 7 |
| Dependency edges | 54 |
| Relationship facts | 18 |

## Dependency roots (depend on nothing)
- `序-4` より未来
- `①-1` 世界(W)

## Machine entry points
- `dist/purpose-os.bundle.json` — everything in one file
- `dist/ai-manifest.json` — compact agent contract
- `dist/concept-graph.mmd` / `dist/concept-graph.dot` — the concept graph
- `Purpose_OS_CORE_v1.1.0_EN_INTEGRATED/machine/` — per-aspect indexes (concepts, deps, relationships)
- `Purpose_OS_CORE_v1.1.0_EN_INTEGRATED/safety/safety-constraints.json` — 19 misuse-prevention constraints
- `Purpose_OS_CORE_v1.1.0_EN_INTEGRATED/conformance/conformance-suite.json` — 47 worked cases

## Verify before trusting
```bash
make verify        # bundled + strict validation + conformance + artifact freshness
```
spec.md SHA-256: `7553fcca3274eabbcfa941c803f1ecd54e75a1a85cd5217b0f2b14b06ad5c0d5`
