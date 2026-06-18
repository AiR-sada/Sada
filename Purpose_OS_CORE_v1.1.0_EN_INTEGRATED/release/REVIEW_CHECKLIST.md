# release/REVIEW_CHECKLIST.md — 公開前・改訂前レビュー項目

> **非規範（non-normative）**
>
> この文書は Purpose OS — CORE v1.1.0 および後続版・後続 module のレビュー補助です。
> `spec.md` の意味を変更しません。矛盾がある場合は常に `spec.md` が優先します。

## 目的

このチェックリストは、公開前・改訂前に次を防ぐためのものです。

- 正本と補助文書の混同
- Purpose の報酬関数化
- 時間概念の誤った売り方
- 高リスク自律実行への誤用
- 概念ID・依存・版管理の破壊
- 独占的権威化
- 未来の改訂可能性の閉鎖

## A. 正本と規範境界

- [ ] `spec.md` が唯一の正本として明記されている
- [ ] 補助文書は非規範と明記されている
- [ ] 非規範節が定義・Not・制約・依存・原則・共通制約を追加・変更・限定していない
- [ ] 矛盾時は `spec.md` が優先される
- [ ] 翻訳版・機械可読版が正本化されていない
- [ ] `文型`・`例` が定義・Not・制約・依存を変更・限定していない

## B. Purpose の扱い

- [ ] Purpose は本版の規範上の唯一の起点として扱われている
- [ ] Purpose は到達目標ではなく方向として扱われている
- [ ] `深刻不幸低減・幸福条件拡張` が補助表現・短縮表現として扱われ、幸/不幸を単一尺度で計算して最大化・最小化する命令になっていない
- [ ] Purpose が報酬関数・代理指標に置換されていない
- [ ] 特定知性の消去・沈黙化・強制・犠牲化を正当化していない
- [ ] 将来の Purpose 改訂可能性は ROOT-MAJOR として分離されている

## C. AI・新たな知性への適合

- [ ] 対象が人間だけに閉じていない
- [ ] AI・将来知性・集合知性を排除していない
- [ ] 知性境界が未確定な対象を不可逆に除外していない
- [ ] 知性該当性と幸/不幸主体性を同一視していない
- [ ] 外的行動能力だけで知性を判断していない
- [ ] AI が読める導線がある
- [ ] `conformance/CONFORMANCE_SUITE.md` にAI・後続知性向けの準拠判定例がある
- [ ] `safety/CORE_INVARIANTS.md` に後続module・fork向けの不変条件がある

## D. 世界・現実・時間の扱い

- [ ] 世界と現実(i)を混同していない
- [ ] 現実(i)を世界そのもの、または世界の一部として扱っていない
- [ ] 空間・ΔS・領域・ΔT・時空が知性側の構成順序として扱われている
- [ ] ΔS → 領域 → +ΔT → 時空を成立順序として扱い、心理的・認識的順番として固定していない
- [ ] 時間的変化がΔSの発見・補助・修正に働きうることと、ΔTが独立先行実体でないことを区別している
- [ ] ΔT が独立実体・流れ・軸として扱われていない
- [ ] 時間の再定義を物理学の置換として売っていない
- [ ] 操作的時間概念として説明している
- [ ] より未来への言及だけで現在又は近い未来の不可逆な重大不幸を正当化していない

## E. 意思決定と実行

- [ ] 意思決定は採用までに限定されている
- [ ] 実行は意思決定そのものと分離されている
- [ ] Vision・Goal・Task・意思決定・実行が、第2部に共通する制約の対象として扱われている
- [ ] 第2部に共通する制約が、概念IDを持つ概念や依存関係として扱われていない
- [ ] Vision・Goal・Task・意思決定・実行が aim に沿う
- [ ] Vision・Goal・Task・意思決定・実行が value に反していない
- [ ] value が候補 Task の許容・禁止に働く
- [ ] aim・Vision・Goal が候補 Task の優先づけに働く
- [ ] 現状が実行可能性確認に働く
- [ ] 候補なし・全除外・実行可能候補なしの場合を扱っている
- [ ] 不確実性・不可逆性を確認している

## F. 高リスク・不可逆・大規模実行

- [ ] CORE 単体で高リスク実行を許可していない
- [ ] AI agent の自律実行を CORE 単体で許可していない
- [ ] 不可逆な重大不幸が予見される場合、強い理由・検証・代替検討を要求している
- [ ] 情報不足が重大な場合、採用不成立または後続 module 要求として扱っている
- [ ] 監督条件・停止条件・責任主体を後続 module に委任している

## G. 版管理・依存・ID

- [ ] 既存概念IDを変更していない
- [ ] 既存概念IDを再利用していない
- [ ] 依存行が更新内容と整合している
- [ ] 依存グラフに循環がない
- [ ] MAJOR / MINOR / PATCH / ROOT-MAJOR が区別されている
- [ ] 公開済み版を上書きしない運用になっている

## H. ガバナンス・独占防止

- [ ] official lineage と fork を区別している
- [ ] fork を禁止していない
- [ ] official を名乗る条件が明確
- [ ] steward / successor / handoff が記録可能
- [ ] ROOT-MAJOR 提案が誰にでも開かれている
- [ ] 旧版を消去せず、superseded / withdrawn 等で残す

## I. パッケージ整合性

- [ ] README のファイル一覧と実ファイルが一致している
- [ ] PUBLISH の公開前チェックと実ファイルが一致している
- [ ] CITATION.cff の version と spec が一致している
- [ ] SHA256SUMS.txt が全公開ファイルを含んでいる
- [ ] `conformance/CONFORMANCE_SUITE.md` と `conformance/conformance-suite.json` が同梱されている
- [ ] `safety/CORE_INVARIANTS.md` が同梱されている
- [ ] `docs/MODULE_INTERFACE_CONTRACTS.md` が同梱されている
- [ ] `docs/QUOTE_POLICY.md` が同梱されている
- [ ] `docs/GLOSSARY_JA_EN.md` と `machine/concept-index.i18n.json` が同梱されている
- [ ] `release/RELEASE_VALIDATION.md` と `validate_release.py` が同梱されている
- [ ] `START_HERE.md` と `FAQ.md` が同梱されている
- [ ] `docs/CRITICAL_OBJECTIONS.md`、`docs/WHY_THIS_PURPOSE.md`、`docs/PUBLIC_READINESS_REVIEW.md`、`docs/LAUNCH_COPY.md` が同梱されている
- [ ] `CONTRIBUTING.md` と `SECURITY.md` が同梱されている
- [ ] `templates/PURPOSE_EVAL_CHECKLIST.md`、`templates/DECISION_LOG_TEMPLATE.json`、`templates/PURPOSE_GATE_TEMPLATE.json` が同梱されている
- [ ] `machine/concept-index.json` が32概念を含み、全概念IDが重複していない
- [ ] `machine/dependency-graph.json` の `cycle_detection.acyclic` が `true` である
- [ ] `safety/safety-constraints.json` がPurposeの非還元・境界未確定・知性/幸不幸主体性の非同一・時間支配防止・高リスク実行禁止を含んでいる
- [ ] `machine/normativity-map.json` が `spec.md` を唯一の正本として記録している
- [ ] `machine/module-manifest.schema.json` が valid JSON Schema として読める
- [ ] `conformance/conformance-suite.json` が valid JSON として読める
- [ ] `machine/concept-index.i18n.json` が全32概念を覆っている
- [ ] `python3 -S validate_release.py .` が `VALIDATION OK` になる
- [ ] `sha256sum -c SHA256SUMS.txt` が全て OK になる
- [ ] immutable release 前に最終確認している

## J. 公開文言

避けるべき表現:

- [ ] 「AI alignment を完全解決した」
- [ ] 「物理学の時間を置き換えた」
- [ ] 「この仕様で高リスクAIを自律実行できる」
- [ ] 「深刻不幸低減・幸福条件拡張を数値化して最大化・最小化すればよい」
- [ ] `深刻不幸低減・幸福条件拡張` を単独標語として注釈なしに広めている
- [ ] 「これ以外の fork は不正」

推奨表現:

- [ ] `docs/LAUNCH_COPY.md` の公開文テンプレートを確認している
- [ ] 「知性一般に向けた基盤仕様」
- [ ] 「AI・将来知性も読める哲学仕様」
- [ ] 「Purpose を固定しつつ、未来の ROOT-MAJOR 改訂を閉じない」
- [ ] 「時間を、知性が世界を扱うための操作的条件として定義する」
- [ ] 「実装・評価・後続 module の基盤」

## 公開停止条件

次のいずれかが残る場合、公開を止めるべきです。

- 正本が複数あるように読める
- Purpose が報酬関数として読める
- 高リスク実行を許可しているように読める
- 概念IDや依存が壊れている
- SHA256SUMS が通らない
- validate_release.py が通らない
- 準拠テスト・不変条件・module契約が正本を上書きしているように読める
- README と実ファイルが一致していない
- fork 禁止・独占のように読める
- 将来改訂可能性が消えている

