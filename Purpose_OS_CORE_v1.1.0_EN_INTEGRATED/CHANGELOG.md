# v1.1.0 ROOT-MAJOR v0.5

- Purpose本文をROOT-MAJORとして改訂。行為主体としての知性と、配慮対象としての全知性および幸/不幸主体たりうる存在を分離。
- 「より未来」を現在から続く方向として再定義し、現在・近未来の重大不幸や現在福祉の系統的割引を遠未来利益で正当化しない制約を強化。
- 「幸せMAX不幸MIN」を公開キャッチコピーから外し、公式補助語を「深刻不幸低減・幸福条件拡張」へ変更。
- valueの受け手を「知性に限る」から「知性および幸/不幸主体たりうる存在を含む」へ改訂。

---

# Changelog

## v1.1.0 — conformance coverage close（非規範の追記。規範内容は不変）

- 被覆解析により、安全制約 `SC-015`（第2部に共通する制約は規範制約であり成立依存ではない）に対応する conformance ケースが存在しないことを検出。`CS-047` を追加して閉じた。`CS-047` は `SC-015` 自身の `risk_prevented`（規範制約と依存関係の混同等）と `required_handling` を忠実にケース化したもので、新たな規範解釈を導入しない。これで全19安全制約が少なくとも1ケースで行使される（19/19）。
- `validate_release.py` に被覆強制を追加：全ての安全制約が少なくとも1つの conformance ケースで参照されることを検証する。これにより「テストされない安全制約」というクラスの欠落が再発しない。概念被覆は意図的に強制しない（定義的概念は振る舞いケースを要さないため）。
- 件数を 46→47 に更新（`conformance-suite.json` の `case_count`、`release-manifest.json` の `counts`、`validate_release.py` の期待値、および README・RELEASE_AUDIT・PUBLIC_READINESS_REVIEW の現状記述）。CHANGELOGの履歴記述は保存。
- 規範ファイル（`spec.md` および機械可読の規範定義）はバイト単位で不変。

## v1.1.0 — English-integrated edition（非規範の追記。規範内容は不変）

- 全文の非規範な英語版 `spec.en.md` を追加。日本語 `spec.md` が唯一の正本であることに変更はない。`spec.en.md` の各概念の Definition / Not / Constraints は、著者承認済みの `machine/concept-index.en.json`（normative=false）から逐語で構成し、接続部のみ新たに英訳した。これは RED_TEAM RT-008（翻訳の正本化ドリフト）を構造的に回避する。
- `validate_release.py` を強化：(1) `index.html` の JSON-LD ブロックを文字列一致だけでなく実際にJSONとしてparse検証する。(2) 期待ルートファイル集合に `spec.en.md` を追加。検証は弱めず、失敗検出のみを追加する。
- 上記に伴い `README.md` のファイル一覧、`machine/normativity-map.json`、`SHA256SUMS.txt` を更新。
- 規範ファイル（`spec.md` および機械可読の規範層）はバイト単位で不変であることを確認済み。本追記は定義・Not・制約・依存・原則・共通制約を追加・変更・限定しない。

## v1.1.0 release consistency pass（非規範の記録）

- `llms-full.txt` 内に埋め込まれた `spec.md` 全文が ROOT-MAJOR 強化前の旧文面（より未来の現在包含、旧短縮語の公開非使用、value受け手拡張、主体性分離の各強化を含まない版）だったため、現行 `spec.md` と一字一句一致するよう再同期。
- `docs/map.md` の `より未来` 一行説明を現行 `spec.md` の定義「現在を含み、あらゆる時点のさらにその先へ開く」に同期。
- `CITATION.cff` の `version`（2箇所）を `spec.md` と同じ `1.1.0` に更新し、`release/PUBLISH.md` の対応チェック項目も `1.1.0` に更新。
- `machine/module-manifest.schema.json` の `depends_on_core_version` を `1.0.0` から `1.1.0` に修正。自己記述と `$id` は v1.1.0 を指しており、旧値のままでは v1.1.0 への依存宣言が常に検証不能だった。
- `templates/DECISION_LOG_TEMPLATE.json` / `templates/PURPOSE_GATE_TEMPLATE.json` の `version_referenced` を `1.1.0` に更新。
- `release/ROOT_MAJOR_TEMPLATE.md` の記入欄から旧短縮語（幸せMAX/不幸MIN）を除去し、公式補助語に基づく「深刻不幸低減への寄与」「幸福条件拡張への寄与」に変更。
- `SHA256SUMS.txt` を再生成。
- 規範コア（`spec.md`）には変更なし。

## v1.1.0 purpose justification integrity fix（非規範の記録）

- `docs/WHY_THIS_PURPOSE.md` 内の未定義参照を削除し、`spec.md`、`GOVERNANCE.md`、`VERSIONING.md`、`release/ROOT_MAJOR_TEMPLATE.md`、`safety/CORE_INVARIANTS.md` に実在する参照へ置換。
- `docs/WHY_THIS_PURPOSE.md` の採用論証を、真理主張ではなく「本版で採用する規範上のroot」の補助論証として明確化。
- `llms-full.txt`、`release-manifest.json`、公開前チェック導線を `docs/WHY_THIS_PURPOSE.md` に同期。
- `SHA256SUMS.txt` を再生成。
- 規範コア（`spec.md` の本文意味、概念定義、Not、制約、依存、原則、共通制約）には変更なし。

## v1.1.0 purpose justification pass（非規範の記録）

- `docs/WHY_THIS_PURPOSE.md` を追加。Purposeの選択を「真理の主張」ではなく「知性の継承条件下での採用の論証」として防御する補助文書。rootの機能要件（K1 最適化耐性 / K2 誤り訂正可能性 / K3 継承安定性 / K4 占有・濫用耐性 / K5 行為指導力）を先に固定し、代表的な7類型（総量最大化・苦痛最小化のみ・人間限定整合・選好充足・固定制約セット・訂正可能性のみ・root不要）に対して11の論証で比較する。残る弱点を§3に明示し、本文書自体の非最終性を維持する。
- `README.md`（ファイル一覧・推奨読み順）、`docs/map.md`、`AI_README.md`、`llms.txt`、`machine/normativity-map.json` を新文書の導線に同期。
- `SHA256SUMS.txt` を再生成。
- 規範コア（`spec.md` の本文意味、概念定義、Not、制約、依存、原則、共通制約、機械可読JSONの概念内容）には変更なし。本変更は選択論証の非規範補強に限定される。

## v1.1.0 public-readiness finishing pass（非規範の記録）

- `START_HERE.md` を追加し、初見読者・公開時説明・安全な位置づけの入口を強化。
- `FAQ.md` を追加し、Purpose、報酬関数化、功利主義誤読、AI alignment 過大主張、高リスク実行、fork、未決定領域への回答を整理。
- `docs/CRITICAL_OBJECTIONS.md` を追加し、想定批判・応答・残る課題を明示。
- `docs/PUBLIC_READINESS_REVIEW.md` を追加し、公開可否、価値、残リスク、公開条件をレビュー形式で整理。
- `docs/LAUNCH_COPY.md` を追加し、公開文・SNS文・README 冒頭文の安全な表現テンプレートを追加。
- `CONTRIBUTING.md` を追加し、errata、clarification、module proposal、ROOT-MAJOR、fork の提案導線を整理。
- `SECURITY.md` を追加し、Purpose scalarization、高リスク自律実行、lineage confusion などの誤用報告導線を整理。
- `templates/` を追加し、`PURPOSE_EVAL_CHECKLIST.md`、`DECISION_LOG_TEMPLATE.json`、`PURPOSE_GATE_TEMPLATE.json` を同梱。
- `README.md`、`AI_README.md`、`docs/map.md`、`llms.txt`、`llms-full.txt` を新しい入口・FAQ・template 導線に同期。
- `release-manifest.json` を practical support と public readiness support の補助記述に更新。
- `SHA256SUMS.txt` を再生成。
- 規範コア（`spec.md` の本文意味、概念定義、Not、制約、依存、原則、共通制約、機械可読JSONの概念内容）には変更なし。本変更は公開理解性・誤用防止・実装接続テンプレートの非規範補強に限定される。

## v1.1.0 publication-design restructure pass（非規範の記録）

- ルート直下のファイル群を、入口・正本・引用・ライセンス・検証・運用基本・AI/Web発見の入口のみに整理。
- 解説文書を `docs/`、構造データを `machine/`、準拠ケース（.md / .json）を `conformance/`、安全関連（.md / .json）を `safety/`、公開操作・監査記録を `release/`、discovery deployment 補助を `site/` に再配置。
- ドメイン別 JSON 配置: `safety/safety-constraints.json` と `conformance/conformance-suite.json` を、対応する .md と co-locate。`machine/` は構造データ（concept-index, dependency-graph, relationship-map, normativity-map, module-manifest schema）に絞る。
- AI / LLM 発見性のため、ルートに `llms.txt`、`llms-full.txt`、`index.html`、`robots.txt`、`sitemap.xml.template` を追加。`site/sitemap.xml.template` と `site/DISCOVERY_DEPLOYMENT.md` を同梱して GitHub Pages 等での discovery layer 構築を補助。
- `spec.md` 内の `map.md` 参照を `docs/map.md` に更新（ミクロ規範行を含む全箇所）。
- `README.md` 冒頭を英日併記とし、Quick start を追加。ファイル一覧・推奨読み順・使い方の参照パスを新構成に整合。
- `AI_README.md` を新パスに同期。
- `validate_release.py` の SCHEMA_TARGETS、各 `data.get()` 参照先、CORE_INVARIANTS のパス、エラーメッセージを `machine/`・`safety/`・`conformance/` プレフィックスに更新。`check_discovery_layout` を新設し、root discovery files の存在、legacy root files の不在、`llms.txt` の必須reference、`index.html` の JSON-LD、`site/sitemap.xml.template` の `{{BASE_URL}}` placeholder を検証。
- `machine/normativity-map.json` の各 `path` を新パスに同期し、新規 discovery ファイルを登録。
- `release-manifest.json` の `hardening_ids.root_revision_openness` を `release/ROOT_MAJOR_TEMPLATE.md` に更新。
- `SHA256SUMS.txt` を再生成。
- 規範コア（`spec.md` の本文意味、概念定義、Not、制約、依存、原則、共通制約、機械可読JSONの内容）には変更なし。本変更はファイル配置・入口設計・AI発見性・パス参照のみに限定される非規範の構造変更。

## v1.1.0 final release validation pass（非規範の記録）

- `release/RELEASE_AUDIT.md` を追加し、公開直前監査・硬化anchor・検証範囲を記録。
- `release-manifest.json` と `schemas/release-manifest.schema.json` を追加。
- `validate_release.py` に、schema subset、厳密件数、連番ID、hardening anchor、core invariant、release manifest の検査を追加。
- `README.md`、`release/RELEASE_VALIDATION.md`、`release/REVIEW_REPORT.md`、`machine/normativity-map.json`、`SHA256SUMS.txt` を最終ファイル構成に合わせて更新。

## v1.1.0 pre-public boundary/temporal hardening pass（非規範の記録）

- `spec.md` の `序-2 Purpose` 制約に、Purposeを証明済み定理ではなく本版で採用する規範上のrootとする旨、および将来のROOT-MAJORによる継承改訂可能性を閉じない旨を明確化。
- `machine/concept-index.json` および `machine/concept-index.en.json` を `spec.md` の改訂に同期。
- `spec.md` に、知性該当性と幸/不幸の主体性を同一視しない制約を追加。
- `spec.md` に、より未来への言及だけで現在又は近い未来の不可逆な重大不幸を検証なしに正当化しない制約を追加。
- `safety/safety-constraints.json` に `SC-018` と `SC-019` を追加。
- `conformance/CONFORMANCE_SUITE.md` / `conformance/conformance-suite.json` を42ケースから46ケースへ拡張。
- `safety/CORE_INVARIANTS.md` に `INV-016` と `INV-017` を追加。
- `AI_README.md`、`docs/DESIGN_RATIONALE.md`、`safety/RED_TEAM_REPORT.md`、`docs/KNOWN_LIMITATIONS.md`、`release/REVIEW_CHECKLIST.md` を上記リスクに合わせて補強。

## v1.1.0 release hardening pass（非規範の記録）

- `spec.md` に、後続moduleがCOREの定義・Not・制約・依存・原則・共通制約を上書きしない旨を明確化。
- `序-2 Purpose` の制約に、「深刻不幸低減・幸福条件拡張」を単独の規範命令として扱わない旨を明確化。
- `②-4 Goal` と `②-6 現状` に、時点/意思決定時点を必要に応じて時空(R_t)上の参照点として扱う明確化を追加。
- `②-9 意思決定` から `②-10 実行` への接続を、別途の実行条件・安全境界・監督条件を満たす場合に接続されうる形へ精密化。
- `conformance/CONFORMANCE_SUITE.md` / `conformance/conformance-suite.json` を18ケースから42ケースへ拡張し、`CS-005` と `CS-010` の判定を精密化。
- `conformance/INTERPRETATION_CASES.md` を追加し、各準拠ケースを要求・許容・禁止・未決定で詳細化。
- `docs/MODULE_INTERFACE_CONTRACTS.md` を更新し、単一スカラー等は「採用・除外・実行の唯一又は最終根拠」として禁じる形に精密化。
- `interfaces/` 以下に7つの後続module interface skeletonを追加。
- `machine/concept-index.en.json` を追加し、英語AI・英語読者向けの非規範概念索引を追加。
- `machine/relationship-map.json` を追加し、依存関係以外の重要な非同一性・委任・禁止関係を機械可読化。
- `schemas/` 以下に主要JSON用のJSON Schemaを追加。
- `safety/RED_TEAM_REPORT.md`、`docs/KNOWN_LIMITATIONS.md`、`release/REVIEW_REPORT.md` を追加。
- `validate_release.py` を再帰検証対応に更新し、schema/interface/relationship/英語索引/spec概念ID照合を追加。


このファイルは Purpose OS — CORE の公開版に対する変更履歴を記録します。
版管理方針は `VERSIONING.md` を参照してください。

本 CHANGELOG は非規範です。規範的な内容の正本は常に `spec.md` です。

## [1.0.0] — Initial public release

### 公開物
- `spec.md` を唯一の正本（normative source）として公開。正本の言語は日本語。
- `README.md` を入口として追加。
- `SUMMARY.md` を1ページ要約として追加。
- `docs/map.md` を非規範の読み方ガイドとして追加。
- `docs/EXAMPLE_WALKTHROUGH.md` を非規範の低リスク読み解き例として追加。
- `docs/DESIGN_RATIONALE.md` を非規範の設計意図・誤読防止文書として追加。
- `CITATION.cff` を追加（GitHub の `Cite this repository` と Zenodo で機械可読な引用情報を提供）。
- `LICENSE` に CC BY-SA 4.0 を採用。
- `VERSIONING.md` を追加（MAJOR / MINOR / PATCH の基準と凍結運用を明記）。
- `GOVERNANCE.md` を追加（official lineage・fork・継承・handoff・Purpose 改訂・退役の運用規律を明記）。
- `SHA256SUMS.txt` を追加（全公開ファイルのハッシュ）。
- `release/PUBLISH.md` を追加（公開 runbook）。
- `AI_README.md` を追加（AI・successor 向け読み方ガイド）。
- `docs/POSITIONING.md` を追加（外部説明・既存領域との位置づけ）。
- `docs/ROADMAP.md` を追加（後続 module・実装・継承の展開計画）。
- `release/MACHINE_READABLE_PLAN.md` を追加（機械可読化の設計方針）。
- `machine/concept-index.json` を追加（概念ID・定義・Not・制約・依存の機械可読索引）。
- `machine/dependency-graph.json` を追加（ミクロ依存行に基づく依存グラフ）。
- `safety/safety-constraints.json` を追加（誤用防止・安全制約の索引）。
- `machine/normativity-map.json` を追加（規範/非規範境界の機械可読マップ）。
- `machine/module-manifest.schema.json` を追加（後続module互換性manifest用JSON Schema）。
- `docs/IMPLEMENTATION_PATH.md` を追加（Purpose Eval / Decision Log / Purpose Gate への実装接続方針）。
- `docs/ADOPTION_BRIEF.md` を追加（外部主体による参照・試用・採用の説明）。
- `release/REVIEW_CHECKLIST.md` を追加（公開前・改訂前の確認項目）。
- `ENGLISH_ABSTRACT.md` を追加（英語の非規範要約）。
- `release/ROOT_MAJOR_TEMPLATE.md` を追加（Purpose 改訂提案テンプレート）。
- `conformance/CONFORMANCE_SUITE.md` / `conformance/conformance-suite.json` を追加（典型ケースによるCORE準拠テスト集）。
- `safety/CORE_INVARIANTS.md` を追加（後続module・forkが破ってはならない不変条件の補助一覧）。
- `docs/MODULE_INTERFACE_CONTRACTS.md` を追加（後続moduleの入力・禁止出力・継承制約の補助契約）。
- `docs/QUOTE_POLICY.md` を追加（外部引用時の誤読防止方針）。
- `docs/GLOSSARY_JA_EN.md` / `machine/concept-index.i18n.json` を追加（日英補助glossary。英語正本ではない）。
- `release/RELEASE_VALIDATION.md` / `validate_release.py` を追加（公開前・改訂前の検証手順と検証補助スクリプト）。

### v1.1.0 到達までの主要な設計判断（非規範の記録）
- **CORE の構造確定**: 序（5概念）／ CORE 第1部（12概念）／ CORE 第2部（10概念）／ 参照部（5概念）の計 32 概念体系に確定。
- **正本の一元性**: `spec.md` のみを規範、他は全て非規範とする三層分離を確定。
- **Purpose 正式定義の精密化**: `序-2 Purpose` の正式定義を方向表現として置き、`深刻不幸低減・幸福条件拡張` は補助表現・短縮表現として保持。これにより、初読時の報酬関数化・算術最適化誤読を弱める。
- **CORE の内部統合**: 旧「CORE①」「CORE②」の二分同格構造を廃止し、単一 CORE の内部を第1部・第2部に分節する形に統合。
- **Purpose の分割**: Purpose を `aim`（方向）と `value`（基準）の対称二層に整理。旧三層構造（Purpose → 目的 → Vision → Mission / 目的 → Value → 指針）を廃止。
- **第2部に共通する制約の明示**: Vision・Goal・Task・意思決定・実行は `aimに沿う` かつ `valueに反してはならない` ことを、概念IDを持たない共通制約として明示。これはマクロの成立関係および運用の流れを変更・追加せず、依存関係として扱わない。
- **Purpose 安全制約の追加**: 補助表現・短縮表現である MAX/MIN を単一スコア最適化や幸/不幸の算術的な最大化・最小化命令として扱わず、単一の数値目的関数・報酬関数・代理指標への還元・置換、強制・沈黙化・単純な総量計算による犠牲化を正当化しない原則を追加。
- **Mission の削除**: Mission を独立概念として削除。継続的方針は Vision から Goal 系列への時点展開で表現。Task の決定は Goal と現状のみに依存する。
- **実行の明示**: `②-10 実行` を独立概念として新設。採用された Task に従って知性が世界に働きかける行為として定義。
- **意思決定の射程限定**: 意思決定を「候補 Task から採用対象を定める運用」に限定し、実行そのものとは分離。空集合ケース（候補なし / 全除外 / 実行可能候補なし）の扱いを明示。
- **世界の定義縮減**: 世界の定義から「全て」を削除し「ありのまま」とした。`実行` による世界への作用可能性との整合のため、「世界は変わらない」の射程を知性の特定・限定という認識側の操作に限定。
- **ΔT の位置づけ**: ΔT を独立軸ではなく、領域に時空を成立させる追加条件として再定義。
- **ΔS / ΔT の誤読防止補強**: `ΔS → 領域 → +ΔT → 時空` は成立順序であり、心理的・認識的順番を固定する主張ではないことを、ΔS・ΔT・時空の各所で明示。時間的変化がΔSの発見・補助・修正に働きうる点と、ΔTが独立先行実体でない点を区別。
- **より未来とΔTのレイヤー分離**: `序-4 より未来` はPurposeの方向表現であり、第1部のΔTと同一の操作条件として扱わない旨を、射程注記および `序-4 より未来` のNot・制約で明示。
- **事象の時空依存補強**: `①-9 事象` の制約と依存行を調整し、起きる/起きうるものとして扱う場合は時空(R_t)上で扱われること、依存に `①-7 時空(R_t)` を含むことを明示。
- **参照識別子の規範化**: 文書タイトル・version・章構成・概念ID・依存行を、参照・引用・拡張のための規範的識別子として明記。
- **公開ガバナンスの分離**: spec の意味内容は `spec.md` に留め、official lineage・fork・継承・handoff・Purpose 改訂・退役の運用は `GOVERNANCE.md` に分離。
- **外部導線の強化**: 位置づけ、採用、実装、機械可読化、英語要約、レビュー項目を非規範文書に分離し、CORE 本体を肥大化させず公開後の理解可能性を高めた。
- **機械可読層の実体化**: 計画文書だけでなく、初期の `machine/concept-index.json`、`machine/dependency-graph.json`、`safety/safety-constraints.json`、`machine/normativity-map.json`、`machine/module-manifest.schema.json`、`conformance/conformance-suite.json`、`machine/concept-index.i18n.json` を同梱し、AI・ツール・後続moduleが参照しやすい形にした。
- **準拠テスト層の追加**: `conformance/CONFORMANCE_SUITE.md` / `conformance/conformance-suite.json` により、CORE準拠・非準拠・後続module要求・射程外の典型ケースを参照可能にした。
- **不変条件層の追加**: `safety/CORE_INVARIANTS.md` により、後続module・fork・successorが破ってはならない主要条件を一覧化した。
- **module契約層の追加**: `docs/MODULE_INTERFACE_CONTRACTS.md` により、後続moduleがCOREの意味を変更せず、単一スカラー・犠牲化正当化・高リスク実行許可を復活させない入口契約を置いた。
- **引用事故防止の追加**: `docs/QUOTE_POLICY.md` により、`深刻不幸低減・幸福条件拡張` の外部引用時に単一尺度最大化・報酬関数化・犠牲化根拠として独り歩きしないための注釈テンプレートを置いた。
- **日英補助glossaryの追加**: 日本語正本を維持したまま、`docs/GLOSSARY_JA_EN.md` / `machine/concept-index.i18n.json` で英語読者・英語AI向けの短い非規範glossを追加した。
- **検証補助の追加**: `release/RELEASE_VALIDATION.md` / `validate_release.py` により、JSON・依存・準拠テスト・i18n・規範性マップ・凡例外記号・SHA256を検証可能にした。
- **版内固定と将来改訂の分離**: 各公開版では Purpose をその版の規範上の唯一の起点として扱う一方、将来版での Purpose 改訂は `GOVERNANCE.md` と `VERSIONING.md` に定める ROOT-MAJOR に分離。ROOT-MAJOR の提案入口は誰にも開き、official lineage への採用判断は steward / successor によって公開記録として残す。
- **三層の解釈優先順位**: 同一概念で解像度差・解釈差がある場合、ミクロ → メソ → マクロ の順で優先することを明記。
- **文型・例の非規範化**: ミクロの「文型」と「例」を理解補助のための非規範記述と位置づけ、定義・Not・制約・依存に変更・限定を加えない旨を明記。
- **非規範節の境界強化**: 明示的に「非規範」とされた節は、定義・Not・制約・依存・原則・共通制約を追加・変更・限定しない旨を明記。
- **「営む」への統一**: 「生きる」を「営む」に統一（be+do の総称として、全知性を対象にするため）。
- **「1つの知性」への統一**: 「1人の知性」という人間寄りの表現を「1つの知性」に統一し、個体・集合体の両方に自然に掛かる表現に整理。
- **誤用防止の明示**: CORE 単体は高リスク行為や AI agent の自律実行を許可しないことを明記。
- **Purpose の非還元性の明示**: 補助表現・短縮表現である深刻不幸低減・幸福条件拡張を、幸/不幸を単一尺度で計算して最大化・最小化する命令、報酬関数、代理指標に還元しないことを明記。
- **境界未確定対象の保護**: 知性/非知性、幸/不幸の主体性が未確定な対象を不可逆に除外・軽視しない旨を追加。
- **COREの射程明確化**: 物理学・形而上学・倫理学の最終理論ではなく、知性の判断と実行を整合させる操作的仕様であることを明記。
- **真理と構造の関係補強**: 真理を知性の任意産物ではなく、世界の構造に制約される表現として補強。
- **構造の目的論誤読の抑制**: 構造に含む目的的関係を、知性が関わる場合に限定する表現へ調整。

### 後続モジュールへ送った課題（非規範の記録）
- 複数知性の value 衝突の解決規則
- 候補 Task の生成規則と同順位候補の一意解消規則
- 不確実性・不可逆性・情報不足への具体的対処
- 高リスク・大規模・自律実行に関する権限、安全境界、監督条件
- 知性と非知性の境界基準
- 個体知性と集合知性の関係
- Purpose の集計規則と時間重みづけ
- 時間・継続性に関する詳細規則
- 不確実性・不可逆性・理由記録の詳細規則
- 予測・検証・真理の更新ダイナミクス
- Purpose 自体を改訂する場合の具体的評価規準

## Discovery-optimized final public release

- Reorganized repository-facing layout so that root contains only entry, normative, citation/license, governance/versioning, integrity, and discovery files.
- Moved auxiliary human documents into `docs/`, conformance support into `conformance/`, safety support into `safety/`, machine-readable indexes into `machine/`, and publication records into `release/`.
- Added `llms.txt`, `llms-full.txt`, `index.html` with JSON-LD, `robots.txt`, and sitemap deployment templates for AI/search discovery.
- Preserved the hardened CORE counts: 32 concepts, 19 safety constraints, 46 conformance cases, 17 core invariants, 7 interface skeletons, and 9 JSON schema files.

