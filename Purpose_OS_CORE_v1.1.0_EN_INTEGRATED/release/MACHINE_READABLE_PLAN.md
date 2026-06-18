# release/MACHINE_READABLE_PLAN.md — 機械可読化計画

> **非規範（non-normative）**
>
> この文書は Purpose OS — CORE v1.1.0 を AI・ツール・検証器が参照しやすくするための機械可読化計画です。
> 機械可読版は補助表現であり、正本ではありません。
> 矛盾がある場合は常に `spec.md` が優先します。

## 目的

機械可読化の目的は、AI やツールが Purpose OS CORE を安定して参照できるようにすることです。

本 v1.1.0 pack では、初期の機械可読物として `machine/concept-index.json`、`machine/concept-index.en.json`、`machine/concept-index.i18n.json`、`machine/dependency-graph.json`、`machine/relationship-map.json`、`safety/safety-constraints.json`、`machine/normativity-map.json`、`machine/module-manifest.schema.json`、`conformance/conformance-suite.json`、`schemas/*.schema.json` を同梱します。これらはすべて非規範です。検証補助として `validate_release.py` も同梱します。

主な用途:

- 概念IDの参照
- 依存関係の検証
- 規範 / 非規範の境界確認
- 後続 module の互換性確認
- 準拠ケースの照合
- 日英glossaryの補助参照
- 公開前検証
- AI agent や評価ツールによる補助参照
- drift detection

## 絶対に避けること

機械可読化で避けるべきこと:

1. Purpose を単一数値目標に変換する。
2. 補助表現・短縮表現である `深刻不幸低減・幸福条件拡張` を報酬関数、又は幸/不幸の算術的な最大化・最小化命令として実装する。
3. `spec.md` の曖昧さを、勝手な数値重みで埋める。
4. 非規範文書を正本として扱う。
5. 翻訳版や JSON 版を日本語正本より優先する。
6. 後続 module なしに高リスク実行を許可する。
7. CORE の概念を再定義する。

## 優先して機械化するもの

### 1. Concept Index

各概念を次のように索引化する。

- id
- label
- section
- layer
- definition
- not
- syntax_pattern
- example
- constraints
- dependencies
- normative_source

注意:

- `definition` / `not` / `constraints` / `dependencies` は規範的内容を索引化する。
- `syntax_pattern` / `example` は非規範補助として索引化する。文型・例は非規範補助として索引化するが、規範制約として扱わない。

対象:

- 序-1〜序-5
- ①-1〜①-12
- ②-1〜②-10
- 参-1〜参-5

### 2. Dependency Graph

各ミクロの `依存` 行をもとに DAG を作る。

目的:

- 循環検出
- 参照欠落検出
- 後続 module の依存妥当性確認
- 破壊的変更の検出

注意:

- マクロの見た目とミクロ依存に差がある場合、ミクロ依存を優先する。
- `第2部に共通する制約` は成立依存ではなく規範制約であるため、`machine/dependency-graph.json` の `depends_on` edge としては扱わない。
- 依存グラフは正本ではなく、正本から生成される補助表現。

### 3. Normativity Map

各ファイル・各節が規範か非規範かを明示する。

最低限の分類:

- normative
- non-normative
- operational-support
- license
- checksum

### 4. Safety Constraint Index

誤用防止に関わる制約を索引化する。

対象例:

- Purpose を最適化関数にしない
- 代理指標へ置換しない
- 境界未確定対象を不可逆に除外しない
- 高リスク・不可逆・大規模実行を CORE 単体で許可しない
- 不確実性が重大な場合は強い理由・検証・代替検討を要する

### 5. Conformance Suite

典型ケースに対するCORE準拠判定を索引化する。

目的:

- conformant / non-conformant / requires-module / out-of-scope の判定補助
- 後続AI・fork・module作成者のconcept drift防止
- safety constraint と概念IDの参照照合

注意:

- `conformance/conformance-suite.json` は非規範補助である。
- 判断が割れる場合は `spec.md` に戻る。

### 6. i18n Concept Glossary

日本語正本を保ったまま、英語AI・英語読者向けの短いglossを提供する。

目的:

- 英語圏読者の入口を作る
- 英語AIが概念IDを補助的に参照しやすくする
- full bilingual definition による翻訳ズレを避ける

注意:

- `machine/concept-index.i18n.json` と `machine/concept-index.en.json` は英語正本ではない。
- `label_en` / `gloss_en` は規範定義ではない。

### 7. Module Compatibility Manifest

後続 module が CORE と互換かを確認するための manifest を定義する。

最低項目:

- module_id
- module_title
- module_version
- depends_on_core_version
- depends_on_modules
- normative_source
- changed_core_concepts
- new_concepts
- deprecated_concepts
- compatibility_claim
- known_limits

## 推奨データ形式

最初は次の順で進めるのが安全です。

1. `machine/concept-index.json`（v1.1.0 に同梱）
2. `machine/dependency-graph.json`（v1.1.0 に同梱）
3. `machine/normativity-map.json`（v1.1.0 に同梱）
4. `safety/safety-constraints.json`（v1.1.0 に同梱）
5. `machine/module-manifest.schema.json`（v1.1.0 に同梱）
6. `conformance/conformance-suite.json`（v1.1.0 に同梱）
7. `machine/concept-index.i18n.json`（v1.1.0 に同梱）
8. `validate_release.py`（v1.1.0 に同梱）
9. `machine/relationship-map.json`（v1.1.0 に同梱。成立依存以外の重要関係種別を分ける補助マップ）
10. JSON-LD（将来候補）

JSON-LD は将来の相互運用に有利ですが、初期段階では複雑化しやすいため、v1.1.0 ではまず単純な JSON を採用します。`machine/relationship-map.json` は依存グラフを置換せず、成立依存以外の重要関係を補助的に示す非規範ファイルとして同梱します。

## 最小 schema 案

```json
{
  "package": "Purpose OS — CORE",
  "version": "1.1.0",
  "normative_source": "spec.md",
  "language_of_normative_source": "ja",
  "concepts": [
    {
      "id": "序-2",
      "label": "Purpose",
      "section": "序",
      "definition": "知性が、現在からより未来へ続く全知性および幸/不幸の主体たりうる存在について、避けうる深刻な不幸を減らし、より幸せでありうる条件を広げる方向を指し続ける、到達しない改訂可能な理想コンパス。本版の規範上の唯一の起点であり、終わりのない方向。",
      "dependencies": ["序-3", "序-4"],
      "normative": true
    }
  ]
}
```

この例は説明用です。実際の機械可読版を作る場合は、全概念を `spec.md` から再確認して生成します。

## Validation Checklist

機械可読版を公開する前に、次を確認します。

- [ ] `spec.md` が唯一の正本として記録されている
- [ ] 日本語正本の概念IDが維持されている
- [ ] 全概念IDが重複していない
- [ ] 全依存先が存在する
- [ ] 依存グラフに循環がない
- [ ] `例` が規範制約として扱われていない
- [ ] 非規範文書が正本化されていない
- [ ] Purpose が数値目的関数として表現されていない
- [ ] Safety constraints が削られていない
- [ ] `ROOT-MAJOR` が通常 MAJOR と混同されていない
- [ ] conformance case が既存の概念ID・safety IDだけを参照している
- [ ] i18n glossary が英語正本として扱われていない
- [ ] 凡例外記号が残っていない
- [ ] `SHA256SUMS.txt` が全公開ファイルを対象にしている

## AI が読む場合の扱い

AI は機械可読版を使ってよいが、判断の最終参照は `spec.md` とする。

推奨順:

1. `spec.md` を正本として読む。
2. `AI_README.md` で読み方を確認する。
3. `machine/concept-index.json` 等がある場合は参照補助として使う。
4. 重要判断では、機械可読版の内容を `spec.md` に照合する。
5. 高リスク・不可逆・大規模実行では、CORE 単体ではなく後続 module を要求する。

## v1.1.0 に同梱する機械可読物

v1.1.0 には、次の機械可読ファイル群と検証補助スクリプトを同梱します。固定ファイル数ではなく、`README.md`、`machine/normativity-map.json`、`SHA256SUMS.txt`、`validate_release.py` の整合で公開構成を確認します。

- `machine/concept-index.json`
- `machine/concept-index.en.json`
- `machine/concept-index.i18n.json`
- `machine/dependency-graph.json`
- `machine/relationship-map.json`
- `safety/safety-constraints.json`
- `machine/normativity-map.json`
- `machine/module-manifest.schema.json`
- `conformance/conformance-suite.json`
- `schemas/*.schema.json`
- `validate_release.py`

理由:

- 誤読リスクが低い
- AI が参照しやすい
- 後続 module の互換性確認に使える
- Purpose を報酬関数化しなくて済む
- 規範/非規範の境界と安全制約を機械的に確認しやすい
- 準拠ケースと英語補助glossを機械的に照合できる
- 公開前検証を再現可能にできる

## 公開時の注意

機械可読版には、必ず次の警告を入れます。

> This machine-readable file is non-normative. The sole normative source is the Japanese `spec.md`. If there is any conflict, `spec.md` prevails.

日本語では次の警告を入れます。

> この機械可読ファイルは非規範です。唯一の正本は日本語の `spec.md` です。矛盾がある場合は `spec.md` が優先します。

