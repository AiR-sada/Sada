# PURPOSE_EVAL_INTERFACE — Purpose Eval Module

> **非規範（non-normative）**
>
> この文書は Purpose OS — CORE v1.1.0 の後続module interface skeletonである。module本体の仕様ではない。
> `spec.md` の意味を追加・変更・限定しない。矛盾がある場合は常に `spec.md` が優先する。

## 共通継承条件

- COREに依存するが、COREの意味を変更しない。
- `spec.md` を唯一の正本として扱い、補助文書・翻訳・JSONを正本より優先しない。
- Purposeを単一スカラー、報酬関数、最適化関数、代理指標に置換しない。
- 「深刻不幸低減・幸福条件拡張」を算術命令又は単独の規範命令として扱わない。
- 特定知性の犠牲化をPurposeだけで正当化しない。
- 境界未確定対象の不可逆な除外・軽視・損壊をCOREから正当化しない。
- CORE単体から、高リスク・不可逆・大規模実行を許可しない。
- 未解決・保留・追加検証を有効な出力として許容する。
- 採用理由、除外理由、不確実性、不可逆性、参照概念IDを保持できる形式にする。

## Scope

Purpose Eval Module は、COREを上書きせず、COREが後続moduleに委任した領域を扱うための入口契約である。

## Inputs candidates

AI出力、計画、行為候補、参照する概念ID、safety constraints、risk tags

## Allowed outputs

compatible / incompatible / requires-module / insufficient-information、violated constraints、required escalation、explanation

## Forbidden outputs

Purpose score、一意の報酬値、高リスク実行許可、補助評価の正本化

## Must preserve

- 理由
- 不確実性
- 未解決性
- 不可逆性
- 境界未確定性
- 参照した概念ID・安全制約ID

## Inherited CORE constraints

SC-001〜SC-019 全体

## Open problems

このinterface skeletonは詳細規則を定めない。詳細規則は当該moduleの正式仕様で扱う。
