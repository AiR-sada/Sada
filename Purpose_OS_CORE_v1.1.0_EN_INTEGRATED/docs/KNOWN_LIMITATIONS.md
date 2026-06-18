# docs/KNOWN_LIMITATIONS.md — Purpose OS CORE 既知の限界

> **非規範（non-normative）**
>
> この文書は Purpose OS — CORE v1.1.0 が意図的に扱わない領域を明示する補助文書である。`spec.md` の意味を追加・変更・限定しない。矛盾がある場合は常に `spec.md` が優先する。

## 基本方針

CORE v1.1.0 は「全てを決める仕様」ではない。Purposeをrootとして置き、知性・現実・意思決定・実行の最小骨格と安全制約を定める。詳細規則は後続moduleへ委任する。

## 既知の限界

| 領域 | COREで扱うこと | COREで扱わないこと | 想定される後続module |
| :-- | :-- | :-- | :-- |
| 幸/不幸 | 総合として置く | 集計規則、単一尺度化 | Value Conflict / Aggregation |
| 複数知性 | 全知性を対象にする | 個体間の優先順位 | Value Conflict / Aggregation |
| 時間 | より未来とΔTを分け、より未来だけによる現在・近未来の不可逆な重大不幸正当化を禁じる | 時間重み、割引率、遅延不幸、継続性の具体規則 | Temporal / Continuity |
| 境界 | 境界未確定対象の不可逆除外を禁じ、知性該当性と幸/不幸主体性を同一視しない | 知性/非知性、幸/不幸主体性、集合知性の具体判定 | Intelligence Boundary |
| 実行 | 意思決定と実行を分ける | 高リスク実行の許可条件 | Safety / Irreversibility, Purpose Gate |
| ログ | 重大判断で理由記録を要求する | ログschemaの詳細 | Decision Log |
| 候補生成 | Task概念を定義する | 候補Task生成アルゴリズム | Purpose Eval / Decision support |
| ROOT-MAJOR | 改訂可能性を閉じない | 改訂案の採用基準 | Governance / ROOT-MAJOR review |
| 物理学 | 操作的な時間・空間語を使う | 物理学の最終理論 | 範囲外 |
| メタ倫理 | Purposeを採用rootとして置く | 完全なメタ倫理的証明 | 範囲外又は別文書 |

## 読み方

この限界は弱点ではなく、COREをroot specとして保つための射程管理である。COREが未決定にした領域を、CORE単体で埋めたように扱うことは避ける。
