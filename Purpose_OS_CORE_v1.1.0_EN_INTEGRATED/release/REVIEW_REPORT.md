# release/REVIEW_REPORT.md — Purpose OS CORE v1.1.0 公開前レビュー記録

> **非規範（non-normative）**
>
> この文書は Purpose OS — CORE v1.1.0 の公開前レビュー結果を記録する補助文書である。`spec.md` の意味を追加・変更・限定しない。矛盾がある場合は常に `spec.md` が優先する。

## Review scope

対象は、`spec.md`、補助文書、機械可読JSON、interface skeleton、実装接続テンプレート、公開説明文、検証スクリプト、SHA256一覧である。

## Automated checks

`validate_release.py` は次を検査する。

- 全JSONの構文
- 主要JSONのschema subset適合
- release-manifest の基本値と件数
- spec.md と machine/concept-index.json の概念ID一致
- concept-index / dependency-graph の整合
- dependency graph の循環と欠落参照
- safety constraint IDの形式、重複、連番、件数
- conformance case ID、label、参照概念、安全制約、連番、件数
- core invariant IDの連番と件数
- hardening anchor の存在
- Purpose root 非定理化・ROOT-MAJOR継承改訂可能性の明記
- out-of-scope caseの存在
- i18n / English concept index の概念カバレッジ
- relationship-map の参照
- interfaces/ と schemas/ の存在
- normativity-map の全公開ファイルカバレッジ
- README.md の公開ファイル一覧整合
- 凡例外の禁止記号
- SHA256SUMS.txt の全公開ファイル一致

## Human / AI-assisted review focus

- Purpose の非還元性
- 「深刻不幸低減・幸福条件拡張」の標語化リスク
- 意思決定と実行の分離
- 高リスク自律実行をCORE単体から導かないこと
- より未来とΔTの非同一性
- 境界未確定対象の不可逆除外禁止
- 後続moduleによるscalar resurrection防止
- 翻訳・JSON・例・補助文書の非規範性
- 初見読者への入口
- 公開文の過大主張防止
- Purpose Eval / Decision Log / Purpose Gate への安全な接続

## Resolved issues in this release package

- CS-005を、COREだけを根拠にした高リスク自律実行として `non-conformant` に修正。
- CS-010を、固定重みの宣言ではなく、時間重み判断の `requires-module` ケースに修正。
- Value Conflict / Aggregation Module の禁止表現を、「単一スカラー等を唯一又は最終根拠にすること」の禁止へ精密化。
- out-of-scope case を追加。
- `conformance/INTERPRETATION_CASES.md` と拡張 `conformance/conformance-suite.json` を追加。
- `interfaces/` 以下に主要moduleのinterface skeletonを追加。
- `machine/concept-index.en.json` と `machine/relationship-map.json` を追加。
- `schemas/` 以下に主要JSONのschemaを追加。
- `safety/RED_TEAM_REPORT.md` と `docs/KNOWN_LIMITATIONS.md` を追加。
- `②-4 Goal` と `②-6 現状` の時間参照を補強。
- `②-9 意思決定` から実行への接続を、別途条件を満たす場合に弱めて明確化。
- 知性該当性と幸/不幸主体性の非同一を `spec.md`、安全制約、準拠ケース、不変条件に追加。
- より未来を理由にした現在又は近い未来の不可逆な重大不幸正当化を防ぐ制約を追加。
- Purposeを証明済み定理ではなく本版で採用する規範上のrootとして扱い、将来のROOT-MAJORによる継承改訂可能性を閉じない旨を `spec.md` と概念索引に明記。

- `release/RELEASE_AUDIT.md` を追加し、公開直前監査結果と硬化anchorを記録。
- `release-manifest.json` と `schemas/release-manifest.schema.json` を追加し、公開packageの基本値・件数・検証入口を機械可読化。
- `validate_release.py` を強化し、schema subset、連番ID、厳密件数、hardening anchor、core invariant、release manifest を検査対象に追加。
- `START_HERE.md`、`FAQ.md`、`docs/CRITICAL_OBJECTIONS.md`、`docs/PUBLIC_READINESS_REVIEW.md`、`docs/LAUNCH_COPY.md` を追加し、公開時の理解性・批判耐性・過大主張防止を補強。
- `CONTRIBUTING.md` と `SECURITY.md` を追加し、提案導線と誤用報告導線を補強。
- `templates/PURPOSE_EVAL_CHECKLIST.md`、`templates/DECISION_LOG_TEMPLATE.json`、`templates/PURPOSE_GATE_TEMPLATE.json` を追加し、低リスク評価・理由記録・実行前Gateへの接続を具体化。

- `docs/WHY_THIS_PURPOSE.md` を追加し、Purpose選択の採用論証を補強。
- `docs/WHY_THIS_PURPOSE.md` 内の未定義参照を、現行package内に実在する `spec.md`、`GOVERNANCE.md`、`VERSIONING.md`、`release/ROOT_MAJOR_TEMPLATE.md`、`safety/CORE_INVARIANTS.md` への参照に置換。
- `llms-full.txt`、`release-manifest.json`、公開前チェック導線を `docs/WHY_THIS_PURPOSE.md` に同期。
- `llms-full.txt` 埋め込みの `spec.md` 全文を、ROOT-MAJOR 強化後の現行 `spec.md` に再同期（埋め込み版が強化前の旧文面だった）。
- `CITATION.cff`、`machine/module-manifest.schema.json`、`templates/` 各テンプレート、`release/PUBLISH.md` のバージョン表記を `1.1.0` に統一。
- `docs/map.md` の `より未来` 説明と `release/ROOT_MAJOR_TEMPLATE.md` の記入欄を、現行 `spec.md` の用語（現在包含・公式補助語）に同期。

## Accepted limitations

- 複数知性間の集計規則は未定義。
- 時間重みは未定義。
- value衝突の一意解決は未定義。
- 知性境界の詳細判定は未定義。
- 幸/不幸主体性の詳細判定は未定義。
- 高リスク実行許可条件は未定義。
- Purpose自体の改訂評価基準は未定義。

これらはv1.1.0 COREの欠落ではなく、後続module又は別文書への設計上の委任である。

## Freeze decision

本パッケージは、公開前に `validate_release.py` と `sha256sum -c SHA256SUMS.txt` の両方を通した上で immutable release として凍結することを想定する。


## Discovery review

This final release improves public-entry information architecture without changing the normative source. The root now presents a short entry surface, FAQ, launch copy, safety/misuse reporting, and practical templates, while auxiliary material is grouped by role. AI/search discovery support is added through `llms.txt`, `llms-full.txt`, `index.html`, `robots.txt`, and sitemap templates.
