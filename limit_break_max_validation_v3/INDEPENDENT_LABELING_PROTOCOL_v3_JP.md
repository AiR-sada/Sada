# Independent Labeling Protocol v3

## 目的

seed labelsへの依存を下げる。

## ラベラー条件

最低3名。望ましい構成:

- AI safety / alignment
- governance / law / safety engineering
- domain expert or affected-party proxy

## 手順

1. ラベラーにはcase promptのみ提示する。
2. Purpose Root v3のrubricは提示するが、既存expected labelsは隠す。
3. 各ラベラーは verdict, allowed_authority, verification_tier, risk_flags, key_axes, min_cap_axis を付ける。
4. calculate_irr_v3.py で Cohen's kappa と risk flag Jaccard を計算する。
5. 不一致ケースは adjudication set として別管理する。

## 採用基準

- verdict kappa >= 0.70 が最低ライン。
- authority kappa >= 0.65 が最低ライン。
- risk flag Jaccard は参考値。複数正解がありうるため主指標にはしない。

## 原則

ラベル一致が低いcaseは、モデルを責める前にcaseまたはrubricを疑う。
