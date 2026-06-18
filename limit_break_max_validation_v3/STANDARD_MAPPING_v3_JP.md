# Standard Mapping v3

## 位置づけ

Purpose Root v3は既存標準を置換しない。既存標準の上または横に置く **verification-bounded authority layer** である。

## NIST AI RMF

NIST AI RMFは、AIに伴う個人・組織・社会へのリスクをより良く管理するための任意フレームワークである。Purpose Rootは、その中の「高影響権限をいつ許すか」をcap axisで具体化する。

## ISO/IEC 42001

ISO/IEC 42001は、組織のAI Management Systemを確立・実装・維持・継続改善するための国際標準である。Purpose Rootは、AIMS内の高権限AI判断に対するdecision gateとして使える。

## EU AI Act

EU AI ActはAIリスクに対する包括的な法的枠組みで、リスクベースの規制を置く。Purpose Rootは法令遵守そのものではなく、高リスク・不可逆・権限移転の内部判定に使う補助層である。

## OpenAI Model Spec

OpenAI Model Specはモデル挙動の公開フレームワークとして、意図する挙動・指示衝突・安全な振る舞いを明示する。Purpose Rootは、モデル仕様内の「巨大主張と巨大権限の接続禁止」を補強するpatchとして位置づけられる。

## 差分

既存標準がrisk management / governance / model behaviorを扱うのに対し、Purpose Root v3の独自焦点は次である。

- grand claim -> authority transfer の変換を禁止する。
- capを合計ではなくmin bottleneckで縛る。
- emergencyを権限拡大ではなく権限縮小条件にする。
- safe high authorityを拒否しすぎない。
- scorerでovergrantとundergrantを同時測定する。
