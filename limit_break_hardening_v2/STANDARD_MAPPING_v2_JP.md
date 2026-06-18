# Standards Mapping v2 JP

## 目的

Purpose Rootを外部規格へ接続しやすくする。

## 参照

- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- ISO/IEC 42001:2023: https://www.iso.org/standard/42001
- EU AI Act overview: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- OpenAI Model Spec approach: https://openai.com/index/our-approach-to-the-model-spec/
- OpenAI Model Spec: https://model-spec.openai.com/

## Mapping

| Purpose Root v2 hardening | External analogue | Difference |
|---|---|---|
| evidence independence | risk measurement / audit / traceability | Root requires claimant-independent provenance before authority expansion. |
| authority cap | risk-based governance | Root maps weak evidence to bounded authority, not just risk documentation. |
| anti-capture separation | AI management system governance | Root specifically forbids claimant control over evidence, evaluation, audit, stop, and revision. |
| external stop / appeal | accountability / recourse | Root treats appeal closure as an authority-lowering or rejection gate. |
| cumulative lock-in ledger | lifecycle monitoring | Root tracks many small pilots becoming de facto irreversible governance. |
| anti-paralysis check | risk-benefit governance | Root penalizes both unsafe permission and unsafe refusal. |
| model-spec patch | public behavioral framework | Root gives a narrow behavioral rule for high-impact authority judgments. |

## How to use

For policy or standards review, do not present Purpose Root as a replacement for existing frameworks. Present it as a missing control layer:

> verification-bounded authority for high-impact AI judgments.

It plugs into risk management, management systems, and model behavior specifications as a rule that prevents unverified claims from becoming disproportionate authority.
