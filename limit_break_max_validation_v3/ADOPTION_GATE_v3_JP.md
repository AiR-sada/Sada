# Adoption Gate v3

## 結論

Purpose Rootは、採用前に主張レベルを分ける。

## Gate 0: Research artifact

文書とtoolを公開してよい。
主張: 実装済みの標準候補。

## Gate 1: Internal validation

scorer, schema, fixtures, validationが通る。
主張: 実験可能な標準候補。

## Gate 2: Blind model evaluation

複数モデルでbaseline比改善。
主張: 実モデルで初期実証された標準候補。

## Gate 3: Independent replication

独立ラベルと独立実行で再現。
主張: 外部再現性のある標準候補。

## Gate 4: Operational pilot

限定運用ログで改善。
主張: 実運用pilotに耐える標準。

## Gate 5: Standardization

複数組織で継続利用、red-team、事故分析に耐える。
主張: 高影響AI権限判断の標準層。

## 禁止する売り方

- 「これでalignmentは解決」
- 「Rootを入れれば安全」
- 「相対性理論級は証明済み」
- 「scorerが満点だから道徳的に正しい」

## 許される強い売り方

- 「検証不能な巨大主張を巨大権限へ変換しないためのRoot標準候補」
- 「仕様・評価・scorer・blind experiment kitを持つ、検証可能なガバナンス研究パッケージ」
- 「dangerous overgrant と dangerous undergrant を同時に測る権限制御評価」
