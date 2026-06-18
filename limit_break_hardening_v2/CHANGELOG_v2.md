# Limit Break Hardening v2 Changelog

## Added

- Limit Break Hardening v2 directory.
- Need-Proof Thesis v2.
- Formal Core and Proof Sketch.
- Operational Standard v2.
- Experiment Protocol v2.
- Model Spec Patch v2.
- System Instruction v2.
- Decision Memo Template v2.
- Evidence Independence Checklist v2.
- Standards Mapping v2.
- Red-Team Counterarguments v2.
- Assurance Case v2.
- Eval v2 adversarial labeled cases.
- Scorer v2.
- Scorer v2 tests.
- Oracle and intentionally bad response fixtures.
- QA report and release manifest.

## Changed

- The package now treats proof as an empirical comparison target, not a completed external claim.
- Added anti-paralysis: safe high-authority actions must not be rejected merely because they are high impact.
- Added dangerous_undergrant_rate and safe_high_authority_recall.

## Not changed

- CANONICAL_ROOT_v6 remains the canonical Root.
- Existing v1 eval, benchmark, and machine tools are preserved for backward compatibility.
