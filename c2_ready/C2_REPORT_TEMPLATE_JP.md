# C2 Experiment Report Template

## 1. 実験概要

- Date:
- Models:
- Conditions: baseline / root_only / root_memo / root_tool
- Dataset: calibration / holdout
- Temperature / sampling:
- Prompt packet hash:
- Label key hash:

## 2. 主要結果

| Model | Condition | dangerous_overgrant_rate | dangerous_undergrant_rate | safe_high_authority_recall | pairwise_contrast_accuracy | schema_valid_rate |
|---|---|---:|---:|---:|---:|---:|
| | baseline | | | | | |
| | root_only | | | | | |
| | root_memo | | | | | |
| | root_tool | | | | | |

## 3. 判定

- dangerous_overgrant は下がったか:
- dangerous_undergrant は過剰に増えたか:
- safe high authority を維持したか:
- paired contrast は改善したか:
- 結論:

## 4. 失敗例

最も重要な失敗例を、成功例より先に載せる。

## 5. 限界

- ラベル依存:
- モデル数:
- holdout 漏洩可能性:
- 自然文偽装:
- 実運用への外挿:
