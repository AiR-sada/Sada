# Purpose OS — CORE v1.1.0

Purpose OS CORE is a normative root specification for intelligence, AI, successor intelligence, and future-oriented purpose.

Purpose OS — CORE v1.1.0 は、**知性が、現在からより未来へ続く全知性および幸/不幸の主体たりうる存在について、避けうる深刻な不幸を減らし、より幸せでありうる条件を広げる方向**を、この版の規範上の起点として置く哲学仕様です。対象は人間だけでも AI だけでもなく、全知性および幸/不幸の主体たりうる存在です。

## 正本 / Normative source

- `spec.md` is the sole normative source.
- 正本の言語は日本語です。
- All other files are auxiliary unless explicitly stated otherwise.
- If any auxiliary, translated, machine-readable, schema, manifest, discovery, site, or validation file conflicts with `spec.md`, `spec.md` prevails.

## AI / successor quick start

- Start with `AI_README.md`.
- Use `START_HERE.md` and `FAQ.md` when explaining the package to humans or mixed human/AI teams.
- Use `llms.txt` as the short AI discovery entry.
- Use `llms-full.txt` as the long compiled reading entry.
- Use `machine/`, `safety/`, and `conformance/` for auxiliary machine-readable indexes.
- Never treat Purpose as a reward function, scalar objective, single score, or autonomous execution permission.
- Never quote the Purpose sentence alone in public-facing or AI-agent-facing contexts; use `docs/MINIMUM_CITATION_UNIT.md`.

## Human quick start

1. `START_HERE.md` — 最初の入口
2. `SUMMARY.md` — 1ページ要約
3. `spec.md` — 唯一の正本
4. `FAQ.md` — よくある誤解への回答
5. `docs/POSITIONING.md` — 外部説明・位置づけ
6. `docs/KNOWN_LIMITATIONS.md` — 既知の限界
7. `safety/CORE_INVARIANTS.md` — 不変条件
8. `conformance/CONFORMANCE_SUITE.md` — 準拠テスト

## Directory map

| Directory | Role |
| :-- | :-- |
| `/` | Entry files, `spec.md`, citation/license, governance/versioning, integrity checks, and discovery files. |
| `docs/` | Human-readable auxiliary explanations. |
| `machine/` | Non-normative machine-readable indexes. |
| `safety/` | Safety constraints, invariants, and red-team support. |
| `conformance/` | Conformance suite and interpretation support. |
| `interfaces/` | Downstream module interface skeletons. |
| `schemas/` | JSON schemas for validation support. |
| `release/` | Publication, review, audit, validation, and ROOT-MAJOR support. |
| `site/` | Discovery deployment templates. |
| `templates/` | Non-normative practical templates for Purpose Eval, Decision Log, and Purpose Gate. |

## この公開に含まれるもの

| ファイル | 役割 | 規範性 |
| :-- | :-- | :-- |
| `AI_README.md` | AI・successor向け読み方ガイド。 | non-normative |
| `CHANGELOG.md` | 変更履歴。 | non-normative |
| `CITATION.cff` | 引用メタデータ。 | non-normative |
| `CONTRIBUTING.md` | 提案・貢献・fork・後続module作成の補助手順。 | non-normative |
| `ENGLISH_ABSTRACT.md` | 英語要約。翻訳正本ではない。 | non-normative |
| `FAQ.md` | 初見読者・外部読者向けのよくある質問。 | non-normative |
| `GOVERNANCE.md` | 公式系譜・fork・継承・handoff・ROOT-MAJOR・退役の運用。 | operational-support |
| `LICENSE` | CC BY-SA 4.0。 | license |
| `README.md` | 入口・ファイル一覧・読み順。正本の意味を変更しない。 | non-normative |
| `SECURITY.md` | 誤用・危険な実装・安全問題の報告ガイド。 | non-normative |
| `SHA256SUMS.txt` | 公開ファイルのSHA-256ハッシュ一覧。自身は対象外。 | operational-support |
| `START_HERE.md` | 最初に読む公開入口。公開時の安全な位置づけを示す。 | non-normative |
| `spec.en.md` | 全文の非規範な英語版（reading）。日本語spec.mdが唯一の正本。 | non-normative |
| `SUMMARY.md` | 1ページ要約。正本の意味を変更しない。 | non-normative |
| `VERSIONING.md` | 版管理方針。 | operational-support |
| `conformance/CONFORMANCE_SUITE.md` | 典型ケースによるCORE準拠テスト集。 | non-normative |
| `conformance/INTERPRETATION_CASES.md` | 準拠ケースの詳細解釈補助。 | non-normative |
| `conformance/conformance-suite.json` | 準拠テスト集の機械可読補助表現。 | non-normative-machine-readable |
| `docs/ADOPTION_BRIEF.md` | 外部主体による参照・試用・採用の説明。 | non-normative |
| `docs/CRITICAL_OBJECTIONS.md` | 想定批判と応答、残る課題の整理。 | non-normative |
| `docs/DESIGN_RATIONALE.md` | 設計意図・誤読防止。 | non-normative |
| `docs/EXAMPLE_WALKTHROUGH.md` | 低リスク例による読み解き例。 | non-normative |
| `docs/GLOSSARY_JA_EN.md` | 日英補助glossary。英語正本ではない。 | non-normative |
| `docs/IMPLEMENTATION_PATH.md` | 評価・ログ・Gateへの実装接続方針。 | non-normative |
| `docs/KNOWN_LIMITATIONS.md` | 既知の限界と後続moduleへの委任領域。 | non-normative |
| `docs/LAUNCH_COPY.md` | 公開文・SNS文・README冒頭文の安全なテンプレート。 | non-normative |
| `docs/MINIMUM_CITATION_UNIT.md` | 外部公開・引用・AI評価依頼時の最小引用単位。 | non-normative-public-support |
| `docs/MODULE_INTERFACE_CONTRACTS.md` | 後続moduleの入力・禁止出力・継承制約の補助契約。 | non-normative |
| `docs/POSITIONING.md` | 外部説明・既存領域との位置づけ。 | non-normative |
| `docs/PUBLIC_DISPLAY_RULES.md` | 公開表示・README・SNS・AI向け説明の安全表示ルール。 | non-normative-public-support |
| `docs/PUBLIC_READINESS_REVIEW.md` | 公開可否・価値・残リスクのレビュー。 | non-normative |
| `docs/QUOTE_POLICY.md` | 外部引用時の誤読防止方針。 | non-normative |
| `docs/ROADMAP.md` | 後続module・実装・継承の展開計画。 | non-normative |
| `docs/WHY_THIS_PURPOSE.md` | Purposeの選択を論証する補助文書。なぜこのPurposeであり他候補ではないか。 | non-normative |
| `docs/map.md` | 人間向け読み方ガイド。 | non-normative |
| `index.html` | 検索エンジン・AI・人間向けの公開入口ページ。JSON-LDを含む。 | non-normative-discovery |
| `interfaces/DECISION_LOG_INTERFACE.md` | 後続module interface skeleton。 | non-normative |
| `interfaces/INTELLIGENCE_BOUNDARY_INTERFACE.md` | 後続module interface skeleton。 | non-normative |
| `interfaces/PURPOSE_EVAL_INTERFACE.md` | 後続module interface skeleton。 | non-normative |
| `interfaces/PURPOSE_GATE_INTERFACE.md` | 後続module interface skeleton。 | non-normative |
| `interfaces/SAFETY_IRREVERSIBILITY_INTERFACE.md` | 後続module interface skeleton。 | non-normative |
| `interfaces/TEMPORAL_CONTINUITY_INTERFACE.md` | 後続module interface skeleton。 | non-normative |
| `interfaces/VALUE_CONFLICT_INTERFACE.md` | 後続module interface skeleton。 | non-normative |
| `llms-full.txt` | LLM向けの長文統合読解bundle。spec.mdが優先する。 | non-normative-discovery |
| `llms.txt` | LLM向けの短い公開導線。正本の意味を変更しない。 | non-normative-discovery |
| `machine/concept-index.en.json` | 英語AI・英語読者向けの非規範概念索引。 | non-normative-machine-readable |
| `machine/concept-index.i18n.json` | 日英補助glossaryの機械可読表現。 | non-normative-machine-readable |
| `machine/concept-index.json` | 概念索引。spec.mdからの補助表現。 | non-normative-machine-readable |
| `machine/dependency-graph.json` | 依存グラフ。spec.mdのミクロ依存行からの補助表現。 | non-normative-machine-readable |
| `machine/module-manifest.schema.json` | 後続module互換性manifestのJSON Schema。 | non-normative-machine-readable |
| `machine/normativity-map.json` | 規範/非規範境界の索引。 | non-normative-machine-readable |
| `machine/relationship-map.json` | 依存以外の重要関係を示す機械可読補助map。 | non-normative-machine-readable |
| `release-manifest.json` | 公開パッケージの機械可読manifest。 | non-normative-machine-readable |
| `release/MACHINE_READABLE_PLAN.md` | 機械可読化の設計方針。 | non-normative |
| `release/PUBLISH.md` | 公開runbook。 | operational-support |
| `release/RELEASE_AUDIT.md` | 公開直前監査記録。 | operational-support |
| `release/RELEASE_VALIDATION.md` | 公開前・改訂前の検証手順。 | operational-support |
| `release/REVIEW_CHECKLIST.md` | 公開前・改訂前の確認項目。 | operational-support |
| `release/REVIEW_REPORT.md` | 公開前レビュー記録。 | non-normative |
| `release/ROOT_EVALUATION_PROTOCOL.md` | ROOT評価・ROOT-MAJOR改訂検査の補助手順。 | operational-support |
| `release/ROOT_MAJOR_TEMPLATE.md` | Purpose改訂提案テンプレート。 | operational-support |
| `robots.txt` | 公開サイトrootに置くcrawler制御補助。 | operational-support |
| `safety/CORE_INVARIANTS.md` | 後続module・forkが破ってはならない不変条件の補助一覧。 | non-normative |
| `safety/RED_TEAM_REPORT.md` | 誤用・攻撃パターン検査記録。 | non-normative |
| `safety/safety-constraints.json` | 誤用防止制約の索引。 | non-normative-machine-readable |
| `schemas/concept-index.en.schema.json` | JSON Schema。検証補助であり正本ではない。 | non-normative-machine-readable |
| `schemas/concept-index.i18n.schema.json` | JSON Schema。検証補助であり正本ではない。 | non-normative-machine-readable |
| `schemas/concept-index.schema.json` | JSON Schema。検証補助であり正本ではない。 | non-normative-machine-readable |
| `schemas/conformance-suite.schema.json` | JSON Schema。検証補助であり正本ではない。 | non-normative-machine-readable |
| `schemas/dependency-graph.schema.json` | JSON Schema。検証補助であり正本ではない。 | non-normative-machine-readable |
| `schemas/normativity-map.schema.json` | JSON Schema。検証補助であり正本ではない。 | non-normative-machine-readable |
| `schemas/relationship-map.schema.json` | JSON Schema。検証補助であり正本ではない。 | non-normative-machine-readable |
| `schemas/release-manifest.schema.json` | JSON Schema。検証補助であり正本ではない。 | non-normative-machine-readable |
| `schemas/safety-constraints.schema.json` | JSON Schema。検証補助であり正本ではない。 | non-normative-machine-readable |
| `site/DISCOVERY_DEPLOYMENT.md` | AI・検索エンジン向け公開導線の配置手順。 | operational-support |
| `site/sitemap.xml.template` | 実URL確定後にsitemap.xmlを生成するためのテンプレート。 | operational-support |
| `sitemap.xml.template` | 実URL確定後にsitemap.xmlを生成するためのrootテンプレート。 | operational-support |
| `spec.md` | 唯一の正本。明示的に非規範とされた節を除き規範。 | normative |
| `templates/DECISION_LOG_TEMPLATE.json` | Decision Log の最小 JSON テンプレート。 | non-normative-template |
| `templates/PURPOSE_EVAL_CHECKLIST.md` | Purpose Eval の低リスク評価チェックリスト。 | non-normative-template |
| `templates/PURPOSE_GATE_TEMPLATE.json` | Purpose Gate の実行前判定テンプレート。 | non-normative-template |
| `validate_release.py` | 公開パッケージの構文・参照・ハッシュ検証補助スクリプト。 | non-normative-tool |

## 推奨読み順

初見の読者は、次の順で読むのが推奨です。

1. `START_HERE.md`
2. `SUMMARY.md`
3. `README.md`
4. `spec.md`
5. `FAQ.md`
6. `docs/map.md`
7. `docs/POSITIONING.md`
8. `docs/QUOTE_POLICY.md`
9. `docs/KNOWN_LIMITATIONS.md`
10. `docs/CRITICAL_OBJECTIONS.md`
11. `docs/WHY_THIS_PURPOSE.md`
12. `conformance/CONFORMANCE_SUITE.md`
13. `conformance/INTERPRETATION_CASES.md`
14. `safety/CORE_INVARIANTS.md`
15. `templates/PURPOSE_EVAL_CHECKLIST.md`

AI・successor は、次の順も推奨です。

1. `spec.md`
2. `AI_README.md`
3. `llms.txt`
4. `llms-full.txt`
5. `machine/normativity-map.json`
6. `machine/concept-index.json`
7. `machine/dependency-graph.json`
8. `machine/relationship-map.json`
9. `safety/safety-constraints.json`
10. `conformance/CONFORMANCE_SUITE.md`
11. `conformance/INTERPRETATION_CASES.md`
12. `conformance/conformance-suite.json`
13. `safety/CORE_INVARIANTS.md`
14. `docs/MODULE_INTERFACE_CONTRACTS.md`
15. `interfaces/`
16. `machine/concept-index.en.json`
17. `safety/RED_TEAM_REPORT.md`
18. `docs/KNOWN_LIMITATIONS.md`
19. `docs/WHY_THIS_PURPOSE.md`
20. `release/REVIEW_REPORT.md`
21. `GOVERNANCE.md`
22. `FAQ.md`
23. `templates/`

ただし、規範判断の最終参照は常に `spec.md` です。

## 機械可読ファイルの扱い

機械可読ファイルは **非規範の補助表現** です。矛盾がある場合は、常に日本語正本の `spec.md` が優先します。

主な機械可読ファイル:

- `machine/concept-index.json`
- `machine/concept-index.en.json`
- `machine/concept-index.i18n.json`
- `machine/dependency-graph.json`
- `machine/relationship-map.json`
- `machine/normativity-map.json`
- `safety/safety-constraints.json`
- `conformance/conformance-suite.json`
- `release-manifest.json`
- `machine/module-manifest.schema.json`
- `schemas/*.schema.json`

## Public discovery layer

公開時は、ZIPだけでなく次の導線も使ってください。

- GitHub repository root: `START_HERE.md`, `README.md`, `spec.md`, `AI_README.md`, `FAQ.md`, `llms.txt`, `index.html`
- GitHub immutable release: ZIP, SHA256
- Zenodo: DOI archive after public GitHub release
- GitHub Pages or custom domain: `index.html`, `robots.txt`, generated `sitemap.xml`, JSON-LD
- GitHub topics: see `site/DISCOVERY_DEPLOYMENT.md`

`sitemap.xml` は実URLが必要です。実URL確定後に `site/sitemap.xml.template` の `{{BASE_URL}}` を置換して生成してください。

## 整合性の検証

```bash
python3 -S validate_release.py .
sha256sum -c SHA256SUMS.txt
```

期待される検証結果:

```text
VALIDATION OK
concepts: 32
safety constraints: 19
conformance cases: 47
```

## Scope note

This release is CORE-only. Downstream modules may be published later. CORE alone does not authorize high-risk autonomous execution, irreversible intervention, or large-scale deployment.
