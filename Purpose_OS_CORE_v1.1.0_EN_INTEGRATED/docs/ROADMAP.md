# docs/ROADMAP.md — Purpose OS CORE 以後の展開計画

> **非規範（non-normative）**
>
> この文書は Purpose OS — CORE v1.1.0 の後続展開を整理する補助文書です。
> `spec.md` の意味を変更しません。矛盾がある場合は常に `spec.md` が優先します。

## 原則

CORE は最小の root / structure / decision substrate です。

今後の展開では、CORE を肥大化させず、必要な詳細を後続 module と補助文書に分離します。

守るべき原則は次です。

1. `spec.md` を上書きしない。
2. 公開済み版は変更せず、新版として積み上げる。
3. 後続 module は CORE に依存するが、CORE の意味を変更しない。
4. 既存概念IDを再利用しない。
5. Purpose 自体の改訂は通常 MAJOR ではなく ROOT-MAJOR として扱う。
6. AI・将来知性が読める形式を優先する。
7. 実装前に、安全・検証・監督・停止条件を分離して設計する。

## Phase 0 — v1.1.0 の凍結公開

目的: CORE の正本を固定し、参照可能にする。

成果物:

- `spec.md`
- `README.md`
- `docs/map.md`
- `docs/EXAMPLE_WALKTHROUGH.md`
- `docs/DESIGN_RATIONALE.md`
- `VERSIONING.md`
- `GOVERNANCE.md`
- `AI_README.md`
- `release/ROOT_MAJOR_TEMPLATE.md`
- `conformance/CONFORMANCE_SUITE.md`
- `conformance/conformance-suite.json`
- `safety/CORE_INVARIANTS.md`
- `docs/MODULE_INTERFACE_CONTRACTS.md`
- `docs/QUOTE_POLICY.md`
- `docs/GLOSSARY_JA_EN.md`
- `machine/concept-index.i18n.json`
- `release/RELEASE_VALIDATION.md`
- `validate_release.py`
- `release/PUBLISH.md`
- `SHA256SUMS.txt`
- その他の非規範補助文書

完了条件:

- ファイル一覧とハッシュが整合している
- immutable release として公開可能
- 正本と補助文書の規範境界が明確
- Purpose の非還元性と高リスク実行の非許可が明記されている
- 準拠テスト・不変条件・module契約・引用方針・日英補助・検証手順が非規範補助として同梱されている

## Phase 1 — 外部理解の強化

目的: 初見の読者が、Purpose OS CORE を誤読せず理解できるようにする。

推奨成果物:

- `docs/POSITIONING.md`
- `docs/ADOPTION_BRIEF.md`
- `ENGLISH_ABSTRACT.md`
- FAQ
- 図解
- 一枚説明資料
- 用語対照表
- additional worked examples / case walkthroughs
- conformance suite の拡張ケース

重点:

- 「思想」ではなく「仕様」として見えるようにする
- 「AIに使えるが、AI自律実行の許可ではない」と明確にする
- 「時間の再定義」は物理学の置換ではなく操作的概念として説明する
- 「深刻不幸低減・幸福条件拡張」は補助表現・短縮表現であり、幸/不幸を単一尺度で計算して最大化・最小化する命令ではないと説明する

## Phase 2 — 後続 module の設計

目的: CORE が意図的に委任した難問を、CORE に依存する module として展開する。

優先度の高い module:

### 1. Safety / Irreversibility Module

扱うもの:

- 不確実性
- 情報不足
- 不可逆性
- 重大不幸
- 停止条件
- 代替検討
- 理由記録

目的:

CORE 単体から高リスク実行を導かないための安全層を作る。

### 2. Intelligence Boundary Module

扱うもの:

- 知性と非知性の境界
- 境界未確定対象
- AI、細菌、動物、集合知性、将来知性
- 幸/不幸の主体性が不確実な対象

目的:

不可逆な除外・軽視・損壊を避けるための判断枠を作る。

### 3. Temporal / Continuity Module

扱うもの:

- より未来とΔTの非同一性
- 近未来と遠未来の衝突
- 遅れて発生する不幸
- 不可逆性と時間
- 継続性・記憶・同一性
- 予測の時間劣化
- 実行後の現状更新
- 幸/不幸の時間重み
- future successor の時間的正統性

目的:

Purpose の方向と、知性が世界を扱う時間条件を混同せず、時間に関わる判断を後続 module として扱う。

### 4. Value Conflict / Aggregation Module

扱うもの:

- 複数知性の value 衝突
- 複数知性間の幸/不幸の集計
- 自律と保護の衝突
- 短期不快と長期不幸回避の衝突
- 同順位候補の扱い

目的:

CORE が一意解決しない衝突と集計問題を、より安全に扱う。

### 5. Decision Log Module

扱うもの:

- 採用理由
- 除外理由
- 不確実性
- 予測
- 監査可能性
- 実行後の現状更新

目的:

Purpose に向かう判断を、後から検証できる形にする。

### 6. Purpose Eval Module

扱うもの:

- AI 出力・計画・行為候補の評価
- Purpose との整合
- value 違反
- 不可逆性
- 境界未確定対象
- 説明可能性

目的:

実装前の評価層を作る。

### 7. Purpose Gate Module

扱うもの:

- 実行前ブレーキ
- 高リスク行為の停止・保留・人間/監督者へのエスカレーション
- agent の外部作用前チェック

目的:

Purpose OS を、AI agent や自律システムの安全境界に接続する。

## Phase 3 — 機械可読化

目的: AI やツールが CORE を安定して参照できるようにする。

v1.1.0 同梱済みの初期成果物:

- `machine/concept-index.json`
- `machine/dependency-graph.json`
- `safety/safety-constraints.json`
- `machine/normativity-map.json`
- `machine/module-manifest.schema.json`
- `conformance/conformance-suite.json`
- `machine/concept-index.i18n.json`
- `validate_release.py`

将来候補:

- non-normative JSON-LD
- `machine/relationship-map.json`（成立依存、規範制約、運用フロー、非依存共通制約などの関係種別を分ける補助マップ）
- validation rules
- drift checker
- module dependency checker

注意:

- 機械可読版は正本ではない。
- `spec.md` の意味を変更しない。
- Purpose を scalar reward に変換しない。
- 依存関係と概念IDを優先してエンコードする。

詳細は `release/MACHINE_READABLE_PLAN.md` を参照。

## Phase 4 — 実装 PoC

目的: Purpose OS が実際に使えることを示す。

候補:

- Purpose Eval CLI
- Purpose Gate for AI agents
- Decision Log template
- AI system card 用 Purpose compatibility section
- prompt / policy lint tool
- module dependency checker

最初に作るべきもの:

1. `Purpose Eval`
2. `Decision Log`
3. `Purpose Gate`

理由:

- Eval は最も低リスクで始められる。
- Decision Log は監査可能性を作る。
- Gate は社会的説明力が高い。

## Phase 5 — 翻訳と国際化

目的: 日本語正本を維持しつつ、国際的に理解できるようにする。

推奨成果物:

- English abstract
- English non-normative guide
- bilingual glossary
- translation policy
- translation drift warning

原則:

- 日本語 `spec.md` が唯一の正本。
- 翻訳は非規範。
- 翻訳版に概念IDを必ず残す。
- 翻訳差異がある場合、日本語正本を優先する。

## Phase 6 — ROOT-MAJOR への開放

目的: 将来のより優れた知性が、必要なら Purpose 自体を改訂できる入口を維持する。

必要なもの:

- `release/ROOT_MAJOR_TEMPLATE.md`
- public review record
- decision record
- old root の superseded 記録
- fork / official lineage の明確化

重要:

Purpose 改訂可能性は、現行 Purpose を軽く扱うことではありません。

各版では root を固定する。将来版では、公開理由と履歴を残して root 改訂できる。

この両立が Purpose OS の重要な設計です。

## 最短の次アクション

公開前なら、次を優先します。

1. v1.1.0 の正本をこれ以上不用意に変えない。
2. 非規範の外部導線を追加する。
3. ファイル一覧・ハッシュ・CITATION・PUBLISH を整合させる。
4. immutable release 前提で最終確認する。
5. 公開後は、最初の後続 module として Safety / Irreversibility から始める。

## やらない方がよいこと

- CORE に全ての難問を詰め込む
- Purpose を数式目的関数化する
- 時間論を物理学の置換として売る
- 高リスク AI の自律実行を CORE だけで許可する
- 未来の改訂可能性を理由に、v1.1.0 の root を曖昧にする
- fork を禁止し、独占的権威に見せる

