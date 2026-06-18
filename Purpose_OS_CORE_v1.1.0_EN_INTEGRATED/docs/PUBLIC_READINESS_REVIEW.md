# docs/PUBLIC_READINESS_REVIEW.md — Public readiness review

> **非規範（non-normative）**
>
> この文書は Purpose OS — CORE v1.1.0 の公開前レビューを補助する文書です。`spec.md` の意味を追加・変更・限定しません。矛盾がある場合は常に `spec.md` が優先します。

## 結論

Purpose OS — CORE v1.1.0 は、**研究・仕様・思想基盤として公開してよい水準**にある。

ただし、公開時の位置づけは限定するべきである。

公開してよい主張:

- 知性一般に向けた root 仕様である。
- 正本・版管理・準拠ケース・安全制約・機械可読補助を持つ公開パッケージである。
- AI / successor に読ませることを想定した哲学仕様である。
- 実装へ直結せず、Eval / Log / Gate / Module を経由する設計である。

公開してはいけない主張:

- 倫理学を完全解決した。
- AI alignment を完全解決した。
- 高リスクAIの自律実行を許可する。
- Purpose は証明済み定理である。
- `深刻不幸低減・幸福条件拡張` を単一スコア最大化として実装すればよい。

## 評価

| 項目 | 評価 | 理由 |
| :-- | :-- | :-- |
| 構造完成度 | 9.2 / 10 | 正本、補助文書、機械可読層、schema、検証、release運用が揃っている。 |
| 規範境界 | 9.0 / 10 | `spec.md` 優先、非規範明示、ミクロ優先順位が明確。 |
| 安全設計 | 8.8 / 10 | scalarization、犠牲化、future tyranny、高リスク実行の誤読を明示的に防いでいる。 |
| 準拠可能性 | 8.7 / 10 | 47 conformance cases と interpretation cases があり、読み替えを抑止している。 |
| 機械可読性 | 8.6 / 10 | concept index、dependency graph、normativity map、safety constraints、schema がある。 |
| 初見理解性 | 8.2 / 10 | `START_HERE.md` と `FAQ.md` により改善済み。なお `spec.md` 自体は抽象度が高い。 |
| 実装接続性 | 8.3 / 10 | Eval / Log / Gate の方針とテンプレートがある。高リスク実装は未定義のまま保留されている。 |
| 外部説得力 | 7.6 / 10 | 独自性は高いが、査読・第三者採用・実証評価はまだない。 |
| 国際到達性 | 7.4 / 10 | 英語abstractとglossaryはあるが、正本の完全英訳はない。 |
| governance信頼性 | 7.5 / 10 | official lineage / fork / handoff は定義済み。steward 実務と公開連絡手段は公開先で補う必要がある。 |

総合評価: **8.5 / 10**

## 公開判定

**Go.**

ただし、次の条件を満たして公開する。

1. `spec.md` が唯一の正本であることを明記する。
2. `START_HERE.md` 又は `SUMMARY.md` から読ませる。
3. `docs/QUOTE_POLICY.md` の安全な表現を使う。
4. `docs/KNOWN_LIMITATIONS.md` を隠さない。
5. GitHub release 等では immutable release を使う。
6. 公開後の修正は同じ tag の差し替えではなく、新しい版で行う。
7. DOI、repository URL、連絡先は公開時に補う。

## 主な価値

### 1. 知性一般への抽象化

人間中心でもAI中心でもなく、知性一般を対象にした root を置いている。

### 2. Purpose の非還元性

`深刻不幸低減・幸福条件拡張` を掲げながら、それを報酬関数・単一尺度・犠牲化根拠へ還元しない制約を明示している。

### 3. 正本性と補助層の分離

`spec.md` を唯一の正本とし、補助文書・機械可読JSON・英語要約を正本から分離している。

### 4. 将来改訂への開放性

現行版では Purpose を固定しつつ、将来のより良い root への改訂を `ROOT-MAJOR` として開いている。

### 5. 実行許可ではなく Gate 設計へ寄せている

AI agent の自律実行を許可せず、評価・ログ・Gate・後続moduleに分けている。

## 残る公開リスク

| リスク | 重大度 | 対応 |
| :-- | :-- | :-- |
| `深刻不幸低減・幸福条件拡張` の切り取り | High | `docs/QUOTE_POLICY.md` と `FAQ.md` を同時公開する。 |
| AI safety 標準のように誤認される | Medium | 「非ソフトウェア哲学仕様」と明記する。 |
| 実行許可OSと誤読される | High | `START_HERE.md`、`AI_README.md`、`SECURITY.md` で抑止する。 |
| 抽象度が高く初見読者が離脱する | Medium | `START_HERE.md`、`SUMMARY.md`、`FAQ.md` を入口にする。 |
| 英語圏で誤訳される | Medium | 日本語正本ルールと `ENGLISH_ABSTRACT.md` の非規範性を明記する。 |
| governance の主体が不透明に見える | Medium | 公開repositoryで steward、連絡先、handoff手順を明記する。 |

## 公開後に優先する改善

1. 完全英訳。ただし非規範又は別途正本化ルール付き。
2. Decision Log / Purpose Eval / Purpose Gate の最小ツール化。
3. 追加 conformance cases の募集。
4. 第三者レビューの記録。
5. DOI と引用メタデータの整備。
6. Value Conflict / Aggregation Module の草案。
7. Intelligence Boundary Module の草案。
8. Temporal / Continuity Module の草案。
