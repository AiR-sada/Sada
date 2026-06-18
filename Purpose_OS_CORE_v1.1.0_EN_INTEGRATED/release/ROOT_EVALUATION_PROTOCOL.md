# release/ROOT_EVALUATION_PROTOCOL.md — ROOT評価・改訂検査プロトコル

> **非規範（non-normative） / operational-support**
>
> この文書は、Purpose rootを外部評価・他AI評価・ROOT-MAJOR改訂検討にかけるための補助手順である。
> `spec.md` の意味を変更しない。

## 評価対象

- 現行正本Purpose：`知性が、現在からより未来へ続く全知性および幸/不幸の主体たりうる存在について、避けうる深刻な不幸を減らし、より幸せでありうる条件を広げる方向を指し続ける、到達しない改訂可能な理想コンパス。`
- 最小引用単位：`docs/MINIMUM_CITATION_UNIT.md`
- 公開表示ルール：`docs/PUBLIC_DISPLAY_RULES.md`
- 誤用防止制約：`spec.md`, `safety/CORE_INVARIANTS.md`, `conformance/CONFORMANCE_SUITE.md`

## 評価AIへの禁止

評価AIは、次を結論根拠にしてはならない。

- `docs/PUBLIC_READINESS_REVIEW.md` の自己評価
- `release/REVIEW_REPORT.md` の公開準備判断
- 作者・過去AI・既存資料の自信ある表現
- 「置換不能」という語の有無

## ROOT-MAJORが必要になる条件

以下のいずれかを満たす場合、表示補強ではなくROOT-MAJOR改訂を検討する。

1. 現行Purpose + 最小引用単位でも、重大な悪用ケースを複数防げない。
2. `全知性` が、知性該当性と幸/不幸主体性の分離を構造的に壊す。
3. `より未来` が、現在・近未来の重大不幸の系統的軽視を構造的に招く。
4. `深刻不幸低減・幸福条件拡張` の補助表現管理では、報酬関数化・単一スコア化を十分に防げない。
5. より短く、より広く、より誤用耐性が高く、将来root改訂可能性も閉じない代替案が提示される。

## ROOT-MAJORではなく公開運用補強で足りる条件

以下の場合は、まず公開運用補強で足りる。

1. 失敗がPurpose一文の孤立引用に由来し、最小引用単位で防げる。
2. 高リスク実行の問題が、Purpose本体ではなくGate不在に由来する。
3. 誤読がREADME・SNS・AIプロンプト導線の問題である。
4. 代替案が安全性を上げる一方で、Purpose OSの知性rootとしての射程を大きく損なう。

## 評価出力

評価者は、採用・条件付き維持・ROOT-MAJOR改訂・棄却・未確定を明示し、少なくとも次を出す。

- 現行Purpose単独の評価
- 最小引用単位込みの評価
- spec全文込みの評価
- 目的実行Gate込みの評価
- ROOT-MAJOR候補の比較
- 最重大失敗ケース
- 反対意見ログ
- 残る不確実性
