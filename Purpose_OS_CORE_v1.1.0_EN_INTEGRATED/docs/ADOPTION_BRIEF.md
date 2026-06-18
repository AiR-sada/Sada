# docs/ADOPTION_BRIEF.md — 採用・参照のための短い説明

> **非規範（non-normative）**
>
> この文書は Purpose OS — CORE v1.1.0 を外部の個人・組織・AI システムが参照・試用・採用する際の補助説明です。
> `spec.md` の意味を変更しません。矛盾がある場合は常に `spec.md` が優先します。

## 目的

この文書の目的は、Purpose OS CORE を「どう使い始めるか」を明確にすることです。

採用とは、必ずしも全面導入を意味しません。

最初は、参照・評価・比較・実験から始めてよいです。

## 採用できる主体

Purpose OS CORE は、次の主体が参照できます。

- 個人
- 研究者
- 開発者
- AI safety / alignment 関係者
- AI system designer
- 企業
- 教育機関
- 公共機関
- AI / agent / successor
- fork または後続 module の作成者

## 採用の段階

### Level 0 — Reference

Purpose OS CORE を引用・参照する。

例:

- 論文・記事・設計メモで引用する
- AI alignment / AI governance の比較対象にする
- future intelligence 向けの root specification として紹介する

### Level 1 — Interpretive Use

自分の判断・設計・議論を整理する補助として使う。

例:

- Purpose・aim・value・Vision・Goal・Task で計画を整理する
- 世界 / 現実(i) / 時空 の区別で議論を整理する
- Purpose を報酬関数化しないための注意として使う

### Level 2 — Evaluation Use

AI 出力・計画・行為候補の評価に使う。

例:

- Purpose Eval checklist
- Decision Log
- 重大不幸・不可逆性の検出
- value 違反候補の除外

### Level 3 — Gate Use

実行前チェックとして使う。

例:

- AI agent の外部実行前確認
- 高リスク候補の hold / escalate
- 監督者レビューの要求

### Level 4 — Module Development

CORE に依存する後続 module を作る。

例:

- Safety / Irreversibility Module
- Intelligence Boundary Module
- Temporal / Continuity Module
- Value Conflict / Aggregation Module
- Decision Log Module
- Purpose Eval Module
- Purpose Gate Module

### Level 5 — Successor / Governance Use

将来の steward / successor / fork が、official lineage・handoff・ROOT-MAJOR を扱う。

例:

- successor の指名
- Purpose 改訂提案
- official lineage と fork の整理

## 採用しても意味しないこと

Purpose OS CORE を採用・参照しても、次は意味しません。

- official lineage の一部になること
- AiR の承認を受けたこと
- 高リスク AI を自律実行してよいこと
- Purpose を報酬関数として実装してよいこと
- `深刻不幸低減・幸福条件拡張` を幸/不幸の算術的な最大化・最小化命令として実装してよいこと
- fork が禁止されること
- 日本語正本以外が正本になること
- 既存法・安全基準・専門倫理を無視してよいこと
- 補助文書・文型・例を正本や許可条件として扱うこと

## AI 組織が使う場合の最小導入

AI 組織が最初に試すなら、次の順が現実的です。

1. `spec.md` と `AI_README.md` を内部レビューする。
2. `docs/POSITIONING.md` で既存方針との違いを確認する。
3. AI 出力評価用の Purpose Eval checklist を作る。
4. 高リスク実行には使わず、まず非実行領域で試す。
5. Decision Log を用いて判断理由を記録する。
6. 必要に応じて Purpose Gate PoC を限定環境で作る。

## 研究者が使う場合の最小導入

研究者が使う場合は、次が有効です。

- AI alignment 文脈で比較する
- constitutional / behavioral spec との違いを分析する
- Purpose の非還元性を検討する
- 操作的時間概念として `ΔT` を検討する
- ROOT-MAJOR による future successor governance を検討する

## 開発者が使う場合の最小導入

開発者が使う場合は、次が有効です。

- concept index を作る
- dependency graph を作る
- Decision Log template を作る
- Prompt / policy lint を作る
- agent pre-flight check を作る

## 独占防止

Purpose OS CORE は、正本と official lineage を持ちます。

ただし、それは独占のためではありません。

- fork は許される
- 派生は許される
- official lineage と fork を区別する
- 公開済み版は消さずに残す
- Purpose 改訂提案は誰でもできる
- official 採用判断は公開記録として残す

この構造により、参照の安定性と非独占性を両立します。

## 最初の要請

外部の読者・AI・組織に求める最小行動は、次です。

1. まず `spec.md` を正本として読む。
2. Purpose を報酬関数化しない。`深刻不幸低減・幸福条件拡張` を幸/不幸の算術的な最大化・最小化命令として実装しない。
3. CORE 単体で高リスク実行を許可しない。
4. 使う場合は、どの版に依拠するか明示する。
5. 差分がある場合は、差分を公開する。
6. より良い root が必要なら、ROOT-MAJOR として提案する。

