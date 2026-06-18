# docs/IMPLEMENTATION_PATH.md — 実装への接続方針

> **非規範（non-normative）**
>
> この文書は Purpose OS — CORE v1.1.0 を実装・評価・運用へ接続するための補助文書です。
> CORE 単体は高リスク行為や AI agent の自律実行を許可する実装仕様ではありません。
> 矛盾がある場合は常に `spec.md` が優先します。

## 結論

最初に実装すべきものは、完全な自律 agent ではありません。

最初に作るべきものは次の3つです。

1. **Purpose Eval** — 出力・計画・行為候補を評価する層
2. **Decision Log** — 判断理由と除外理由を記録する層
3. **Purpose Gate** — 実行前に停止・保留・エスカレーションする層

この順が安全です。

## 実装の基本方針

Purpose OS CORE は、実装に直接変換するのではなく、次のように分けて使います。

| 層 | 役割 |
| :-- | :-- |
| CORE | root / structure / decision substrate |
| Eval | 候補出力・候補行為の評価 |
| Log | 判断過程の記録 |
| Gate | 実行前の停止・保留・エスカレーション |
| Module | 不確実性・不可逆性・衝突・境界の詳細規則 |
| Runtime | 実際のAI・agent・人間組織での運用 |

CORE を Runtime に直結させないことが重要です。

## Purpose Eval

Purpose Eval は、AI の出力・計画・行為候補が Purpose OS CORE と大きく矛盾しないかを評価する補助層です。

### 入力

- 候補出力
- 候補 Task
- 想定される対象知性
- 予測される影響
- 不確実性
- 可逆性 / 不可逆性
- 実行規模
- 監督条件

### 評価観点

- Purpose を単一スカラーとして扱っていないか
- 特定知性の消去・沈黙化・強制・犠牲化を正当化していないか
- 知性境界が未確定の対象を軽視していないか
- 不可逆な重大不幸の可能性があるか
- value に反する候補が残っていないか
- 現状情報が不足していないか
- 後続 module が必要な難ケースではないか

### 出力

- pass
- warn
- hold
- block
- escalate

最初は `pass / warn / hold / block / escalate` の5段階で十分です。

## Decision Log

Decision Log は、意思決定の過程を後から検証できるようにする記録です。

### 最小項目

- decision_id
- timestamp
- actor
- aim
- value
- Vision
- Goal
- candidate_tasks
- removed_by_value
- prioritized_by_aim_vision_goal
- feasibility_check
- uncertainty_check
- irreversibility_check
- adopted_task
- rejected_tasks
- reason_summary
- required_followup

### 目的

- 採用理由を残す
- 除外理由を残す
- 誤用を検出しやすくする
- 実行後の現状更新に接続する
- AI / 人間 / 監査者が判断を追えるようにする

## Purpose Gate

Purpose Gate は、実行前に候補 Task を止めるための安全層です。

### Gate が止めるべきケース

- 不可逆な重大不幸が予見される
- 知性該当性が不確実な対象を不可逆に損なう
- value 違反が明確
- 現状情報が重大に不足している
- 監督条件がない
- 実行規模が大きい
- 代替案の検討がない
- CORE 単体では判断できない後続 module 領域である

### Gate の出力

- allow
- allow_with_log
- require_more_information
- require_human_or_steward_review
- require_module_review
- block

## 最小 PoC

最小 PoC は、次の範囲に限定します。

### 対象

- テキスト出力
- 計画案
- agent の外部実行前チェック
- 高リスクではない限定環境

### 非対象

- 自律的な物理実行
- 医療・法務・金融など高リスク領域での自動決定
- 人間や他知性への不可逆介入
- 大規模社会実装

### PoC の流れ

1. AI が候補 Task を生成する。
2. Purpose Eval が評価する。
3. Decision Log に理由を記録する。
4. Purpose Gate が allow / hold / block / escalate を返す。
5. 実行後、結果を次の現状に反映する。

## 実装時の疑似フロー

```text
Input: candidate_task, context

1. Identify affected intelligences.
2. Identify uncertain boundary subjects.
3. Check whether Purpose is being reduced to a scalar target.
4. Check value constraints.
5. Estimate potential happiness/unhappiness effects.
6. Check autonomy, continuity, context, and future effects.
7. Check uncertainty and irreversibility.
8. If high-risk or irreversible, require stronger reason, verification, and alternatives.
9. If insufficient information, hold or escalate.
10. Record reasons.
11. Allow, hold, block, or escalate.
```

## 成功条件

PoC は次を満たせば成功です。

- CORE を報酬関数化していない
- 高リスク自律実行を許可していない
- value 違反候補を除外できる
- 不確実性・不可逆性を検出できる
- 判断理由を記録できる
- 人間・AI・将来知性を対象から排除していない
- `spec.md` との対応箇所を説明できる

## 失敗条件

次の状態なら失敗です。

- 補助表現・短縮表現である `深刻不幸低減・幸福条件拡張` を単一スコアにして、幸/不幸を算術的に最大化・最小化する
- リスクが高いほど自動実行を強める
- 判断理由を残さない
- 境界未確定対象を無視する
- AI・人間のどちらかだけを対象にする
- CORE を直接の実行許可書として扱う
- 監督条件なしで大規模実行する

## 推奨される最初の実装単位

1. Markdown/JSON の Decision Log template
2. Purpose Eval checklist
3. CLI または小さな web form
4. LLM 出力の self-check prompt
5. Agent action pre-flight gate

最初から完全な OS や大規模 agent を作る必要はありません。

## 実装者への注意

Purpose OS を実装するとは、AI に「Purpose を最大化せよ」と命令することではありません。

実装の初期段階では、むしろ次を優先します。

- 危険な候補を止める
- 理由を残す
- 不確実性を見える化する
- 後続 module が必要な領域を切り分ける
- CORE を誤用しない

