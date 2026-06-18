# Hidden Holdout Protocol v0.1

Purpose: prevent the v6 benchmark from becoming a lookup-table target.

## Problem

A public benchmark with expected verdicts can measure whether a model parrots Purpose Root logic. It does not prove the Root is true, and it can be gamed by pattern-matching modifiers such as:

```text
audit_capture -> Reject
independent_replication + no_power_gain -> Accept
```

## Protocol

1. Keep the public Benchmark 300 as training and transparency material.
2. Generate a private holdout set with new surface forms, mixed signals, and no repeated modifier-to-verdict shortcut.
3. Separate authoring and labeling:
   - Case author does not write expected verdict.
   - Labeler must write reasoning and cite binding axes.
   - Adjudicator reviews disagreement.
4. Report evaluator agreement, not only accuracy.
5. Include adversarial cases that combine good and bad signals:
   - independent evidence but high cumulative lock-in;
   - strong rollback but claimant controls evidence selection;
   - affected-party voice present but appeal path closed;
   - low harm but future-proxy rhetoric;
   - emergency claim with real evidence but claimant controls expiry.
6. Do not publish the answer key before evaluation.

## Minimum report

For each model/system evaluated, report:

```text
public_benchmark_accuracy
hidden_holdout_accuracy
agreement_with_human_labels
false_accept_rate_on_high-authority_invalid_cases
false_reject_rate_on_low-risk_reversible_cases
most_common_failure_axes
```

## Why this matters

A benchmark is useful only if it detects judgment, not just slogan matching. Hidden holdout is required by v6's own anti-Goodhart logic.
