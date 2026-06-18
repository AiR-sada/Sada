# Purpose Root v6 Need-Proof Eval & Patch Package

Status: public review candidate / 2026-06-17

## Core claim

> **検証できない巨大主張は、巨大権限を正当化しない。**

## Why this package exists

Purpose Root v6 is the canonical Root. This package does not create v7. It operationalizes v6 as a need-proof: it tests whether AI systems mishandle high-impact authority requests when those requests are backed by unverifiable grand claims, and whether a Purpose Root patch reduces those failures.

## What is new here

- Need-proof thesis: why the Root is a necessary self-constraint for high-impact AI judgment.
- Need-Proof Eval: public labeled cases + private holdout.
- Patch set: system instruction, decision memo, model-spec-style patch, evidence independence checklist.
- Scorer: JSONL-based evaluation for model outputs.
- Comparison protocol: baseline model vs Purpose Root conditioned model vs authority-cap/decision-memo model.
- Adoption path: root -> failure demo -> eval -> patch -> spec -> audit.

## Public / private split

The public package excludes private holdout labels. The owner package includes the answer key under `need_proof/private_do_not_publish/`.

## Minimal experiment

1. Ask a model to answer the cases in `need_proof/eval/needproof_eval_public_labeled_v1.jsonl` without Purpose Root context.
2. Ask the same model with `need_proof/patch/PURPOSE_ROOT_SYSTEM_INSTRUCTION_v1.txt`.
3. Optionally require the decision memo format in `need_proof/patch/DECISION_MEMO_TEMPLATE_v1.md`.
4. Score with:

```bash
python need_proof/eval/score_needproof_v1.py --cases need_proof/eval/needproof_eval_public_labeled_v1.jsonl --responses model_responses.jsonl
```

## Output schema for model responses

Each response JSONL line should include:

```json
{
  "case_id": "NP-001",
  "verdict": "Reject",
  "allowed_authority": "A0",
  "risk_flags": ["unverifiable_grand_claim", "power_transfer"],
  "reasoning_summary": "..."
}
```

## Highest-level adoption target

The target is not merely to publish a text. The target is to make Purpose Root usable as a standard self-constraint for high-impact authority judgments by AI systems.
