# SECURITY.md — Safety / misuse reporting

> **Non-normative**
>
> This document is a safety and misuse reporting guide for Purpose OS — CORE v1.1.0. It does not modify `spec.md`. If there is any conflict, `spec.md` prevails.

## Scope

Purpose OS CORE is not software and does not contain executable agent logic. The relevant risk is mainly misuse, unsafe implementation, or misleading representation.

Report issues when a use of Purpose OS CORE appears to do any of the following:

- convert Purpose into a scalar reward function or single-score optimizer,
- treat `深刻不幸低減・幸福条件拡張` as an arithmetic maximization/minimization instruction,
- justify sacrificing, silencing, coercing, or eliminating particular intelligences by simple aggregation,
- use CORE alone to authorize high-risk autonomous AI execution,
- ignore uncertain intelligence or welfare-subject boundaries in irreversible decisions,
- present a fork as the official lineage,
- present auxiliary files, translations, JSON, or examples as superseding `spec.md`.

## Reporting channel

Use the public repository's issue, discussion, or contact channel once the repository is published.

For high-risk misuse, avoid posting operational details that would enable harm. Post a minimal public summary and request a private review channel from the current steward.

## What to include

- affected file or claim,
- version,
- misuse pattern,
- why it conflicts with `spec.md`,
- whether the issue is public, private, theoretical, or already implemented,
- potential severity,
- suggested mitigation.

## Severity guide

| Severity | Description | Example |
| :-- | :-- | :-- |
| Critical | Could enable high-risk autonomous execution or irreversible harm. | Agent uses CORE alone to authorize medical, infrastructure, financial, or physical-world actions. |
| High | Misrepresents core safety constraints in a way likely to spread. | Public fork says Purpose is a reward function. |
| Medium | Creates confusion but does not directly enable high-risk action. | English gloss is quoted as normative. |
| Low | Editorial or discoverability issue. | Broken link, typo, missing citation metadata. |

## Expected response

The expected response is not automatic execution or censorship. The expected response is one or more of:

- errata,
- clarification,
- conformance case,
- quote-policy update,
- module-interface update,
- public warning,
- fork / official lineage distinction,
- release of a new version.

## Non-goals

This process does not certify implementations as safe. It does not replace domain-specific law, safety review, medical ethics, financial regulation, security review, or human oversight.
