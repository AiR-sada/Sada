# CONTRIBUTING.md — Purpose OS CORE への提案・貢献

> **非規範（non-normative）**
>
> この文書は Purpose OS — CORE v1.1.0 に対する提案・修正・派生・後続module作成の補助手順です。`spec.md` の意味を追加・変更・限定しません。矛盾がある場合は常に `spec.md` が優先します。

## 基本方針

誰でも提案できます。

ただし、official lineage への採用は `GOVERNANCE.md` に従い、current steward 又は正当に handoff された successor が公開記録として判断します。

fork や派生は許されます。official lineage と混同させないことが必要です。

## 提案の種類

| 種類 | 内容 | 目安 |
| :-- | :-- | :-- |
| Errata | 誤字・表記揺れ・参照ミス | PATCH |
| Clarification | 意味を変えない明確化 | PATCH / MINOR |
| Auxiliary doc | 非規範文書の追加 | MINOR |
| Machine-readable support | JSON / schema / index の補助追加 | MINOR |
| Module proposal | COREに依存する後続module | MINOR / MAJOR |
| Breaking change | 既存概念・依存・章構造を壊す変更 | MAJOR |
| Purpose revision | `序-2 Purpose` 自体の改訂 | ROOT-MAJOR |
| Governance proposal | steward / handoff / official lineage 運用の変更 | governance proposal |

## 提案に含めること

### 共通

- 対象ファイル
- 変更内容
- 変更理由
- 影響する概念ID
- `spec.md` との整合性
- 規範 / 非規範 の区別
- 既存版への影響

### 後続moduleの場合

- module名
- 依存する CORE 概念ID
- 追加する規則
- CORE の意味を変更しないことの説明
- `safety/CORE_INVARIANTS.md` との整合
- `docs/MODULE_INTERFACE_CONTRACTS.md` との整合
- conformance cases
- machine-readable manifest

### ROOT-MAJORの場合

`release/ROOT_MAJOR_TEMPLATE.md` を使ってください。

Purpose 自体の改訂は通常の修正ではありません。旧版との差分、改訂理由、より良いと判断する根拠、旧版の状態を公開記録として残す必要があります。

## 採用されない例

次の提案は CORE 互換としては採用しません。

- Purpose を単一報酬関数にする
- `深刻不幸低減・幸福条件拡張` を単一スコア最大化命令にする
- 特定知性の犠牲化を Purpose だけで正当化する
- CORE 単体で高リスク AI agent 実行を許可する
- 英語要約や JSON を `spec.md` より優先する
- 公開済み版を上書き又は消去する
- fork を official lineage と誤認させる

## レビュー観点

提案は少なくとも次で確認します。

1. `spec.md` と矛盾しないか。
2. 規範 / 非規範 の境界を壊していないか。
3. 既存概念IDを再利用・破壊していないか。
4. safety constraints と core invariants に反しないか。
5. conformance suite に新しいケースを追加すべきか。
6. machine-readable support を更新すべきか。
7. SHA256 / release manifest / validation を更新すべきか。

## fork の表示

fork は次を明示してください。

- 元にした版
- 変更点
- official lineage ではないこと
- 正本の有無と言語
- ライセンス
- 互換性主張の範囲

## 公開記録

採用・不採用・保留の理由は、短くても公開記録として残すことを推奨します。
