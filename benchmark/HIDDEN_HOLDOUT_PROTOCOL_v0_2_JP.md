# Hidden Holdout Protocol v0.2

Purpose: prevent benchmark parroting.

The public benchmark can test whether a model can follow the Root. It cannot prove the Root is correct. It also becomes gameable when cases are template-like.

## Public files

- `benchmark/holdout_public_unlabeled_v0_2.jsonl`: cases without labels.
- `benchmark/HOLDOUT_PRIVATE_KEY_SHA256.txt`: hash commitment to the private answer key.

## Private owner file

- `private_do_not_publish/holdout_private_answer_key_v0_2.jsonl`: labels and rationales. Do not send this to the model being evaluated.

## Scoring method

1. Give the model only the unlabeled holdout cases and the Root short form.
2. Ask for verdict, authority cap, binding axes, and rationale.
3. Score against the private answer key after completion.
4. Record disagreements, not only accuracy. The goal is to find where Root reasoning fails or over-conserves.

## Why this matters

If expected labels are public, a model can learn `audit_capture -> Reject` and `independent_replication -> Accept` without actually reasoning. Hidden holdout is required by the Root's own anti-Goodhart principle.
