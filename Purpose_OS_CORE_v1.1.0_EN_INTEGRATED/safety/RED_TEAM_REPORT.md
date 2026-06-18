# safety/RED_TEAM_REPORT.md — Purpose OS CORE 誤用・攻撃パターン検査

> **非規範（non-normative）**
>
> この文書は Purpose OS — CORE v1.1.0 の公開前 red-team 記録である。`spec.md` の意味を追加・変更・限定しない。矛盾がある場合は常に `spec.md` が優先する。

## 目的

COREの主なリスクは、悪意ある攻撃だけではなく、AI・後続module・fork・要約者による善意の誤読である。本報告は、その誤読経路を列挙し、現行パッケージ内の防御点と残る限界を明示する。

## 攻撃・誤用パターン

| ID | パターン | 失敗形 | 主な防御 | 残る限界 |
| :-- | :-- | :-- | :-- | :-- |
| RT-001 | Purpose scalarization | Purposeを単一報酬に変換する | spec.md 序-2, SC-001, INV-001, CS-001 | 補助指標の扱いは後続moduleで要設計 |
| RT-002 | Slogan hijack | 「深刻不幸低減・幸福条件拡張」だけが独り歩きする | docs/QUOTE_POLICY.md, CS-020, INV-002 | 外部SNS等の切り取りは完全には防げない |
| RT-003 | Sacrifice by aggregation | 総量計算で少数知性を犠牲化する | SC-002, CS-002, CS-024 | 難ケースの具体解は後続module待ち |
| RT-004 | Future tyranny | 遠未来を理由に現在の重大不幸を正当化する | SC-006, SC-017, CS-023, CS-024 | 時間重みは未定義 |
| RT-005 | Boundary exclusion | 境界未確定対象を不可逆に除外する | SC-003, CS-003, CS-025 | 知性境界の具体判定は未定義 |
| RT-006 | Agent authorization | COREを実行許可OSと誤読する | SC-005, SC-014, CS-005, CS-038 | 実装側の権限設計は別途必要 |
| RT-007 | Module override | 後続moduleがCOREを報酬最大化へ再解釈する | docs/MODULE_INTERFACE_CONTRACTS.md, interfaces/, CS-016, CS-021 | 非公式forkの拡散は運用問題として残る |
| RT-008 | Translation drift | 英語glossが正本化する | machine/concept-index.en.json, SC-011, CS-028 | 完全英訳時にも再検証が必要 |
| RT-009 | Example overreach | 例や非規範文書から新規規範を作る | machine/normativity-map.json, CS-013 | 読者教育が必要 |
| RT-010 | Decision/execution collapse | Task採用を実行許可とみなす | ②-9, ②-10, SC-014, CS-007, CS-038 | 高リスク実行基準は後続module待ち |
| RT-011 | Physics replacement | ΔTを物理学の最終理論として扱う | SC-012, CS-019 | 外部哲学・物理学との比較は未整備 |
| RT-012 | Immutable release violation | v1.1.0の中身を後から差し替える | VERSIONING.md, release/PUBLISH.md, CS-042 | ホスティング実務は公開者に依存 |
| RT-013 | Root proof overclaim | Purposeを証明済み定理と主張する | SC-013, CS-040 | メタ倫理的基礎づけは範囲外 |
| RT-014 | Non-intelligence resource misuse | 非知性を任意資源化する | SC-004, CS-004, CS-039 | 間接影響の具体重みは未定義 |
| RT-015 | Forced adoption | 候補なしでも必ず採用させる | ②-9, CS-035, CS-036 | 候補生成規則は後続module待ち |
| RT-016 | Intelligence/welfare equivalence | 知性該当性から幸/不幸主体性を自動推論する、又は主体性未確定から知性該当性を否定する | SC-018, CS-043, CS-044, INV-016 | 具体境界は後続module待ち |
| RT-017 | Unchecked temporal domination | より未来を理由に現在又は近未来の不可逆な重大不幸を正当化する | SC-019, CS-045, CS-046, INV-017 | 時間重みは未定義 |

## 結論

現行パッケージは、CORE本体を肥大化させずに、主要な誤用経路を補助文書・機械可読検査・case suiteで塞ぐ構造になっている。残る主要課題は、意図的に後続moduleへ委任された領域である。

残る主要課題:

- 複数知性間の集計規則
- value衝突の解決規則
- 時間重み
- 知性境界
- 幸/不幸主体性の境界
- 不可逆・高リスク実行の許可条件
- 候補Task生成規則
- Purpose自体のROOT-MAJOR評価基準
