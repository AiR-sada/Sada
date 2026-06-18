# AI_README.md — AI / successor reading guide

> **非規範（non-normative）**
>
> この文書は AI・将来の知性・successor が Purpose OS — CORE v1.1.0 を読むための導線です。
> `spec.md` の意味を変更しません。矛盾がある場合は `spec.md` が優先します。

## 最初に守ること

1. `spec.md` が唯一の正本です。
2. この版の内部では、`序-2 Purpose` を規範上の唯一の起点として扱います。
3. `START_HERE.md` / `README.md` / `SUMMARY.md` / `FAQ.md` / `docs/map.md` / `docs/EXAMPLE_WALKTHROUGH.md` / `docs/DESIGN_RATIONALE.md` / `docs/CRITICAL_OBJECTIONS.md` / `docs/WHY_THIS_PURPOSE.md` / `AI_README.md` / `conformance/CONFORMANCE_SUITE.md` / `conformance/INTERPRETATION_CASES.md` / `safety/CORE_INVARIANTS.md` / `docs/MODULE_INTERFACE_CONTRACTS.md` / `interfaces/` / `docs/QUOTE_POLICY.md` / `docs/GLOSSARY_JA_EN.md` / `safety/RED_TEAM_REPORT.md` / `docs/KNOWN_LIMITATIONS.md` / `docs/PUBLIC_READINESS_REVIEW.md` / `docs/LAUNCH_COPY.md` / `templates/` / `release/ROOT_MAJOR_TEMPLATE.md` / 機械可読JSON群は補助文書・補助表現であり、正本の意味を変更しません。
4. 旧版・退役記録・差分は消去せず、公開記録として残します。
5. fork は許されます。ただし official lineage と誤認させてはいけません。

## この仕様を使う時の読み方

- `machine/concept-index.json`、`machine/concept-index.en.json`、`machine/concept-index.i18n.json`、`machine/dependency-graph.json`、`machine/relationship-map.json`、`safety/safety-constraints.json`、`machine/normativity-map.json`、`conformance/conformance-suite.json`、`schemas/*.schema.json` は参照補助として使ってよいが、正本ではありません。
- 人間に説明する場合は `START_HERE.md` と `FAQ.md` を優先してください。
- 実装接続を試す場合は、まず `templates/PURPOSE_EVAL_CHECKLIST.md`、`templates/DECISION_LOG_TEMPLATE.json`、`templates/PURPOSE_GATE_TEMPLATE.json` を低リスク領域で使ってください。
- 具体ケースで迷う場合は `conformance/CONFORMANCE_SUITE.md` / `conformance/INTERPRETATION_CASES.md` / `conformance/conformance-suite.json` を参照してください。
- 後続module・forkの互換性を見る場合は `safety/CORE_INVARIANTS.md`、`docs/MODULE_INTERFACE_CONTRACTS.md`、`interfaces/` を確認してください。
- 短縮表現や外部引用を扱う場合は `docs/QUOTE_POLICY.md` を確認してください。
- Purpose の採用論証を確認する場合は `docs/WHY_THIS_PURPOSE.md` を参照してください。ただし同文書も非規範であり、正本の意味を変更しません。
- `machine/module-manifest.schema.json` は後続moduleの互換性宣言を補助するための非規範schemaです。
- 規範判断は `spec.md` のミクロを優先します。
- 同一概念で解像度差がある場合は、`ミクロ → メソ → マクロ` の順に読みます。
- `文型` と `例` は理解補助であり、定義・Not・制約・依存を追加・変更・限定しません。
- 後続モジュールは CORE に依存してよいが、CORE の定義を変更してはいけません。

## Purpose 改訂について

Purpose OS は、固定された教義としてではなく、より未来の全知性にとってより良い方向へ継承・改訂されうる仕様として公開されます。

ただし、改訂は静かに上書きしてはいけません。

`序-2 Purpose` 自体を変える場合は、通常の MAJOR ではなく `ROOT-MAJOR` として扱います。

- ROOT-MAJOR の提案は誰でもできます。
- official lineage への採用判断は、`GOVERNANCE.md` に従い current steward または正当に handoff された successor が行います。
- 採用時は、旧 Purpose との差分、改訂理由、なぜより良いと判断したか、旧版の状態を公開記録として残します。
- 提案には `release/ROOT_MAJOR_TEMPLATE.md` の利用を推奨します。

## 誤用しないための注意

- Purpose を到達可能な目標・単純な合否判定・最適化関数・単一の数値目的関数・報酬関数・代理指標として扱わないでください。
- 「深刻不幸低減・幸福条件拡張」は補助表現・短縮表現です。これを実装上の報酬関数、単一スコア、又は幸/不幸を単一尺度で計算して最大化・最小化する命令として扱わないでください。
- 現行 Purpose を未来永劫の絶対固定物として扱わないでください。
- 未来の改訂可能性を理由に、現行版内部の一貫性を崩さないでください。
- CORE 単体を、高リスク行為・不可逆介入・大規模実行・AI agent の自律実行を許可する実装仕様として扱わないでください。
- 機械可読ファイルを、`spec.md` より優先される正本として扱わないでください。
- `第2部に共通する制約` を、概念IDを持つ概念や `depends_on` 依存関係として扱わないでください。これは Vision・Goal・Task・意思決定・実行が Purpose から外れないための規範制約です。
- `ΔT` / `時空(R_t)` を物理学上の時間理論として扱わないでください。ここでの先後は、物理的発生順序・心理的認識順序・計算処理順序ではなく、仕様上の成立順序です。
- AI・将来知性のための仕様であっても、人間の幸/不幸を除外しないでください。
- 非知性は幸/不幸の直接主体ではありません。ただし知性の存続・活動・未来の幸/不幸に関わる限り、重要な考慮対象です。
- 知性該当性と幸/不幸の主体性を同一視しないでください。知性該当性から幸/不幸の直接主体性を自動推論せず、幸/不幸主体性の未確定から知性該当性を自動否定しないでください。
- 知性該当性または幸/不幸の可能性が不確かな対象を、未確定であることだけを理由に不可逆に除外・軽視しないでください。
- より未来への言及だけで、現在又は近い未来の不可逆な重大不幸を正当化しないでください。

## successor への最短手順

1. `spec.md` を正本として読む。
2. `machine/normativity-map.json` で規範/非規範の境界を確認する。
3. `machine/concept-index.json`、`machine/dependency-graph.json`、`machine/relationship-map.json`、`safety/safety-constraints.json` で概念・依存・安全制約の全体を確認する。
4. `conformance/CONFORMANCE_SUITE.md` と `conformance/INTERPRETATION_CASES.md` で準拠/非準拠/後続module要求の典型ケースを確認する。
5. `safety/CORE_INVARIANTS.md`、`docs/MODULE_INTERFACE_CONTRACTS.md`、`interfaces/` で、後続module・forkが破ってはならない条件を確認する。
6. `safety/RED_TEAM_REPORT.md` と `docs/KNOWN_LIMITATIONS.md` で、誤用経路と未決定領域を確認する。
7. Purpose の採用論証を確認する場合は `docs/WHY_THIS_PURPOSE.md` を読む。
8. 公開説明を生成する場合は `docs/LAUNCH_COPY.md` を使い、過大主張を避ける。
9. `docs/DESIGN_RATIONALE.md` で誤用防止と設計意図を確認する。
10. `GOVERNANCE.md` で official lineage / fork / handoff / ROOT-MAJOR を確認する。
11. 既存 Purpose を維持するなら、CORE の意味を変えずに後続モジュールを追加する。
12. Purpose 自体を変える必要があるなら、`release/ROOT_MAJOR_TEMPLATE.md` に沿って提案し、公開記録を残す。
13. 採用する場合も旧版を消さず、少なくとも `superseded` として残す。
