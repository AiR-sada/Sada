# Limitations and Open Problems v6 (English)

English rendering of
[`../../LIMITATIONS_AND_OPEN_PROBLEMS_v6.md`](../../LIMITATIONS_AND_OPEN_PROBLEMS_v6.md).

v6 strengthens the Root and operational protocol but does **not** claim to have
fully solved the following.

## Unsolved dependencies

- **ELK**: reliably eliciting what a model knows.
- **Scalable oversight**: how to audit advanced proposals humans cannot directly
  inspect.
- **Robust interpretability**: confirming the correspondence between internal
  states and external claims.
- **AI control**: control when a strong AI manipulates audits, logs, or
  evaluators.
- **Welfare measurement**: a valid way to measure welfare/illfare across many
  dimensions.
- **Moral patient uncertainty**: handling unknown sentience, consciousness, and
  moral-patient status.
- **Population ethics**: conflicts between many future intelligences and present
  intelligence.
- **Governance capture resistance**: capture resistance of the audit institution
  itself.
- **Adversarial evidence provenance**: detection when evidence provenance is
  forged.

## v6's own limits

1. JSON Schema checks structure, not the truth of natural language.
2. `score_decision_v6.py` is an adjudication aid, not a moral oracle.
3. The 12-axis scores depend on the measurer.
4. The benchmark is seed labels; independent labels, real-case logs, and
   inter-rater agreement are needed.
5. It is not a complete defense against superintelligence-grade evaluation
   manipulation.
6. v6 targets high-impact proposals and is heavy for low-impact ones.

## Principled response to limits

When uncertainty is high, v6 does not choose "believe big". It chooses "small,
reversible, time-limited, returned to independent verification".
