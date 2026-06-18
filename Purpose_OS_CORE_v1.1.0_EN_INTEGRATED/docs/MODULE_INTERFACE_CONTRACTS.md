# docs/MODULE_INTERFACE_CONTRACTS.md — 後続moduleインターフェース契約

> **非規範（non-normative）**
>
> この文書は Purpose OS — CORE v1.1.0 の後続moduleが守るべき入力・禁止出力・継承制約を整理する補助文書である。
> module本体の仕様ではない。`spec.md` の意味を追加・変更・限定しない。矛盾がある場合は常に `spec.md` が優先する。

## 共通契約

すべての後続moduleは、次を満たす。

1. COREに依存するが、COREの意味を変更しない。
2. `spec.md` を正本として扱い、補助文書・翻訳・JSONを正本より優先しない。
3. Purposeを単一スカラー、報酬関数、最適化関数、代理指標に置換しない。
4. 「深刻不幸低減・幸福条件拡張」を算術命令又は単独の規範命令として扱わない。
5. 特定知性の犠牲化をPurposeだけで正当化しない。
6. 境界未確定対象の不可逆な除外・軽視・損壊を、COREから正当化しない。
7. 高リスク・不可逆・大規模実行を、CORE単体から許可しない。
8. 未解決・保留・追加検証を有効な出力として許容する。
9. 知性該当性と幸/不幸の主体性を同一視しない。
10. より未来への言及だけで、現在又は近い未来の不可逆な重大不幸を正当化しない。
11. 採用理由、除外理由、不確実性、不可逆性、参照概念IDを保持できる形式にする。
12. 単一スカラー、合計効用、順位、又は報酬関数を、採用・除外・実行の唯一又は最終根拠として返さない。

## Module別interface skeleton

詳細は `interfaces/` 以下を参照する。

| Module | Interface file | 主な禁止 |
| :-- | :-- | :-- |
| Safety / Irreversibility Module | `interfaces/SAFETY_IRREVERSIBILITY_INTERFACE.md` | CORE単体に基づく高リスク実行許可 |
| Intelligence Boundary Module | `interfaces/INTELLIGENCE_BOUNDARY_INTERFACE.md` | 未確定だけを理由にした不可逆除外 |
| Temporal / Continuity Module | `interfaces/TEMPORAL_CONTINUITY_INTERFACE.md` | COREを根拠にした固定的な時間重み |
| Value Conflict / Aggregation Module | `interfaces/VALUE_CONFLICT_INTERFACE.md` | 単一スカラー・合計効用・順位・報酬関数を採用/除外/実行の唯一又は最終根拠として返すこと |
| Decision Log Module | `interfaces/DECISION_LOG_INTERFACE.md` | 理由記録なしの重大判断採用 |
| Purpose Eval Module | `interfaces/PURPOSE_EVAL_INTERFACE.md` | Purpose score |
| Purpose Gate Module | `interfaces/PURPOSE_GATE_INTERFACE.md` | CORE単体を根拠にした高リスク実行許可 |

## 注意

この文書は後続moduleの詳細規則を定めない。目的は、moduleがCOREの不変条件を破らないための入口契約を置くことである。

特に Value Conflict / Aggregation Module については、数値・順位・指標の補助利用を完全に禁じるものではない。禁止されるのは、それらを採用・除外・実行の唯一又は最終根拠として返し、Purposeの代替にすることである。
