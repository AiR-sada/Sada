# Purpose OS — CORE · hardened verification & machine/AI layer

This repository wraps the **Purpose OS — CORE v1.1.0** philosophy specification
package with a defence-in-depth verification harness and a generated
machine-readable / AI-integration layer.

> The sole normative source is the Japanese **`Purpose_OS_CORE_v1.1.0_EN_INTEGRATED/spec.md`**.
> Everything in `tools/`, `dist/`, this README, and CI is **non-normative**: it
> proves *integrity and internal consistency*, never the philosophical content.
> If any file conflicts with `spec.md`, `spec.md` prevails. The normative core
> and the normative machine layer are kept **byte-stable** — this layer is purely
> additive, in line with the package's own governance (`GOVERNANCE.md`,
> `VERSIONING.md`: Purpose changes are ROOT-MAJOR and must be recorded, never
> silently overwritten).

## Layout

| Path | Role | Normativity |
| :-- | :-- | :-- |
| `Purpose_OS_CORE_v1.1.0_EN_INTEGRATED/` | The pristine, verified release package (`spec.md` is the normative source). | as published |
| `tools/validate_strict.py` | Superset validator: runs the bundled validator **plus** deeper structural checks. | non-normative tool |
| `tools/conformance_runner.py` | Treats each conformance case as a structural test; emits coverage matrices. | non-normative tool |
| `tools/test_guardrails.py` | Adversarial mutation tests that prove the validators reject real drift. | non-normative test |
| `tools/build_artifacts.py` | Generates the machine/AI artifact layer into `dist/`. | non-normative tool |
| `tools/normative.lock` | SHA-256 anchor of the normative source (`spec.md`); enforces byte-stability. | governance anchor |
| `dist/` | Generated machine/AI assets (graphs, unified bundle, agent manifest/guide, JSON-LD, coverage matrix). | non-normative, generated |
| `.github/workflows/ci.yml` | Runs every check on every push/PR. | non-normative |
| `Makefile` | Local entry point (`make verify`). | non-normative |

## Quick start

```bash
make verify        # bundled + strict validation, conformance, guardrail tests, checksums, artifact build
make test          # adversarial guardrail tests only
make help          # list all targets
```

Expected baseline: **32 concepts · 19 safety constraints · 47 conformance cases
· 17 core invariants · 19/19 safety coverage**.

## What the hardening adds (beyond the bundled validator)

The package already ships a strong `validate_release.py`. This layer never
weakens it (it runs it first), and adds guarantees it did not previously make:

1. **Normative-source → machine-layer structural sync.** Every `依存` (dependency)
   line in `spec.md` must match `concept-index.json` dependencies exactly. This
   closes the spec↔machine boundary the bundled validator left unchecked.
2. **Declared-count integrity.** Every `*_count` field (concepts, nodes, edges,
   relationships, constraints, cases) must equal its actual array length.
3. **Gap-free ID sequences** for relationship IDs (`REL-001…`).
4. **`llms-full.txt` embedding freshness.** The embedded `spec.md` must match the
   current `spec.md` — a class of drift the changelog records as a real defect.
5. **Conservative dead-link detection** across all Markdown/text files.
6. **Conformance coverage matrices** with full safety-constraint coverage as a
   hard gate (every constraint exercised by ≥1 case).
7. **Non-normative text-drift report.** Surfaces (without failing) where the
   non-normative machine layer's field text differs from `spec.md`, so drift is
   intentional and visible rather than silent.
8. **Artifact freshness gate.** CI rebuilds `dist/` and fails if the committed
   artifacts are stale, so the machine/AI layer can never silently rot.
9. **Normative-source lock.** `tools/normative.lock` pins the `spec.md` SHA-256.
   The validator (and CI) fail if `spec.md` changes without a deliberate re-lock,
   mechanically enforcing the governance rule that Purpose changes are ROOT-MAJOR
   and never silent. A legitimate ROOT-MAJOR runs `make lock` with a recorded
   rationale.
10. **Adversarial guardrail tests.** `tools/test_guardrails.py` injects known
    defects (corrupted counts, dropped dependency, dropped conformance case,
    silent `spec.md` edit, dead link, non-sequential IDs) into a temp copy and
    asserts the validator rejects each — proving the checks have teeth, not just
    that the current package happens to pass.

## Machine / AI integration layer (`dist/`)

Generated deterministically from the verified package:

- **`purpose-os.bundle.json`** — the whole spec (concepts, dependency edges,
  relationships, safety constraints, conformance cases) in one file, with the
  `spec.md` SHA-256.
- **`ai-manifest.json`** — a compact contract an AI agent reads first: where the
  normative source is, hard rules, counts, integrity, and artifact pointers.
- **`AGENT_GUIDE.md`** — human/AI-readable integration guide.
- **`concept-graph.svg` / `.html` / `.mmd` / `.dot`** — the concept dependency
  graph as a standalone SVG (no external renderer required), a self-contained
  interactive HTML page, Mermaid, and Graphviz.
- **`knowledge-graph.jsonld`** — the concept graph as JSON-LD for AI/semantic-web
  discovery.
- **`coverage-matrix.md`** — human-readable safety-constraint × conformance matrix.
- **`conformance-report.json`** — machine-readable conformance coverage summary.

## Integrity

```bash
cd Purpose_OS_CORE_v1.1.0_EN_INTEGRATED
python3 -S validate_release.py .
sha256sum -c SHA256SUMS.txt
```
