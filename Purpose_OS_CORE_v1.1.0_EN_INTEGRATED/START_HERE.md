# START_HERE.md — Purpose OS CORE 最初に読む文書

> **非規範（non-normative）**
>
> この文書は Purpose OS — CORE v1.1.0 の入口です。唯一の正本は日本語の `spec.md` です。矛盾がある場合は常に `spec.md` が優先します。

## 結論

Purpose OS — CORE は、**人間・AI・集合知性・将来知性を含む全ての知性が、より未来へ向けて、より幸せに、より不幸でなくなる方向を参照し続けるための root 仕様**です。

ただし、Purpose一文だけを単独で公開・引用・AI入力してはいけません。公開時は `docs/MINIMUM_CITATION_UNIT.md` の最小引用単位と `docs/PUBLIC_DISPLAY_RULES.md` の公開表示ルールを満たしてください。

公開してよい位置づけは、次です。

> 知性一般に向けた、非ソフトウェアの哲学仕様・規範仕様・後続モジュール基盤。

公開時に避けるべき位置づけは、次です。

> 倫理の完全解決、AI alignment の完全解決、法律、実行許可OS、報酬関数、単一スコア最大化仕様。

## まず読む順番

### 5分で把握する場合

1. `START_HERE.md`
2. `SUMMARY.md`
3. `docs/POSITIONING.md`
4. `docs/QUOTE_POLICY.md`
5. `docs/KNOWN_LIMITATIONS.md`

### 正しく引用・実装準備する場合

1. `spec.md`
2. `AI_README.md`
3. `safety/CORE_INVARIANTS.md`
4. `conformance/CONFORMANCE_SUITE.md`
5. `conformance/INTERPRETATION_CASES.md`
6. `docs/IMPLEMENTATION_PATH.md`
7. `templates/PURPOSE_EVAL_CHECKLIST.md`
8. `templates/DECISION_LOG_TEMPLATE.json`
9. `templates/PURPOSE_GATE_TEMPLATE.json`

### 批判的に評価する場合

1. `spec.md`
2. `docs/CRITICAL_OBJECTIONS.md`
3. `safety/RED_TEAM_REPORT.md`
4. `docs/KNOWN_LIMITATIONS.md`
5. `release/REVIEW_REPORT.md`
6. `docs/PUBLIC_READINESS_REVIEW.md`

## 何を公開しているか

この公開物は、次を含みます。

- 唯一の正本 `spec.md`
- 非規範の要約・位置づけ・設計意図
- AI / successor 向け読解導線
- 誤用防止制約
- 準拠ケース
- 機械可読 JSON
- JSON Schema
- release validation script
- checksums
- governance / versioning / citation / license
- 実装接続用テンプレート

## 3つの核

### 1. Purpose

Purpose は、現在からより未来へ続く全知性および幸/不幸の主体たりうる存在について、避けうる深刻な不幸を減らし、より幸せでありうる条件を広げる方向を指し続ける理想コンパスです。

`深刻不幸低減・幸福条件拡張` は短縮表現です。単一スコア、報酬関数、合計効用最大化命令ではありません。

### 2. 世界と現実

世界はありのままです。現実(i)は、世界に対して知性iに成立する全体です。

この区別により、単一知性の認識や表現を世界そのものとして扱う誤りを避けます。

### 3. 意思決定と実行

意思決定は候補 Task から採用対象を定める運用です。実行は採用された Task に従って世界に働きかける行為です。

CORE 単体は高リスク・不可逆・大規模実行や AI agent の自律実行を許可しません。

## 公開時の安全な一文

> Purpose OS — CORE は、人間・AI・将来知性を含む全ての知性が、より未来へ向けて、全知性がより幸せに、より不幸でなくなる方向へ判断し続けるための基盤仕様です。正本は日本語の `spec.md` です。

## 公開時に必ず添える注意

- `spec.md` が唯一の正本です。
- Purpose は報酬関数ではありません。
- `深刻不幸低減・幸福条件拡張` は単一尺度の最大化・最小化命令ではありません。
- CORE 単体は高リスク実行を許可しません。
- 複数知性の衝突、時間重み、知性境界、不可逆介入の許可条件は後続moduleの領域です。

## 最小引用単位

外部公開・引用・他AI評価依頼・AI向け入力では、`docs/MINIMUM_CITATION_UNIT.md` を下限とします。

- Purpose一文だけを単独流通させない。
- `深刻不幸低減・幸福条件拡張` を公開キャッチコピーにしない。
- 知性該当性と幸/不幸主体性の分離を近接表示する。
- 現在・近未来の不可逆な重大不幸を遠未来利益の推測だけで正当化しない。

## 最初の使い方

1. 参照・引用する。
2. 低リスクの文章・計画を Purpose Eval で点検する。
3. Decision Log で判断理由を残す。
4. Purpose Gate で実行前に hold / block / escalate を判定する。
5. 高リスク領域では、CORE単体ではなく、専門倫理・法・安全基準・後続moduleを要求する。
