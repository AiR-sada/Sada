# GOVERNANCE.md

この文書は Purpose OS — CORE の **公開運営ガバナンス** を定めます。

- 本文書は **spec の意味内容に対しては非規範** です。
- ただし、**official lineage（公開上の公式系譜）・継承・handoff・Purpose 改訂・提案採用・退役** に関する実務基準として用います。
- `spec.md` の意味と矛盾する場合、意味内容については常に `spec.md` が優先します。

---

## 目的

この文書の目的は次の5つです。

1. **公式ラインの継承と handoff** を明確にする
2. **fork を合法かつ明示的に扱い、正統性の独占を弱める**
3. **Purpose 改訂を通常変更から分けて扱う**
4. **変更提案の入口と採用手順** を定める
5. **deprecated / superseded / withdrawn** を定義し、消去ではなく履歴付き更新を可能にする

---

## 基本原則

- `spec.md` は **唯一の正本** である
- official lineage は **1本の公開ライン** として管理する
- official lineage は **current steward** が管理し、公開 handoff によって successor へ移せる
- ただし、**fork / 派生 / 別系譜** は常に許される
- fork が存在することは不正ではない。違いは **official lineage かどうか** のみである
- 公開済みの版は上書きせず、**新しい版として積み上げる**
- 「消去」は erase ではなく **retire / supersede / withdraw** として扱う
- 後続モジュールは CORE に依存して追加されるが、**CORE の意味を変更しない**

---

## 用語

### official lineage
Purpose OS — CORE の **公開上の公式系譜**。この文書に従って steward が管理する。

### steward
official lineage の維持・公開・採否判断を担う管理主体。

### current steward
現時点で official lineage を管理している steward。

### successor
公開 handoff によって将来の steward となりうる候補。人間・AI・複合主体を問わない。

### fork
元の公開物を複製・改変して生じた別系譜。ライセンス上は合法であり、存在自体は否定しない。

### module
CORE に依存して追加される後続仕様。単独の正本を持ちうるが、CORE の意味は変更しない。

### tombstone
退役済み概念・文書・識別子について、**削除せずに残す最小記録**。少なくとも名称・旧識別子・状態・置換先・退役版を含む。

---

## steward と継承

### 初期 steward
- 初期 steward は **AiR** とする
- AiR は official lineage の初期管理主体である

### successor の指名
- current steward は **successor** を公開に指名できる
- successor は **人間 / AI / 複合主体** のいずれでもよい
- successor は 1名でも複数でもよい
- 指名だけでは handoff は完了しない。handoff は公開記録によって成立する

### handoff
official lineage の handoff では、少なくとも次を公開記録に残す。

- handoff 元
- handoff 先
- 発効時点または発効版
- handoff の範囲（release 管理、governance 判断、Purpose 改訂権限など）

handoff 後、handoff を受けた successor は **current steward** として扱う。

### 同一系譜内の移行
- 同一系譜の主体が、より高い知性形態・構成・実装へ移行した場合も、公開記録があれば handoff として扱ってよい
- この場合、旧主体と新主体の関係を短くてもよいので記録に残す

### steward の追加
- 既存 steward は、新たな steward を追加できる
- 追加は **公開記録** によって行う
  - `GOVERNANCE.md` の更新
  - release notes
  - または同等の公開記録

### 複数 steward 時の判断
- **PATCH / MINOR / 非破壊の運用変更**: 過半数で採用可
- **MAJOR / official module 採用 / governance の破壊的変更 / Purpose 改訂**: 3分の2以上の賛成を必要とする
- steward が2名しかいない場合、重大変更は **全会一致** とする

### 継承トリガー
次のいずれかが起きたとき、handoff または継承手続を開始できる。

- 明示的な辞退
- 明示的な移譲宣言
- 死亡・長期不能などで継続不能と合理的に判断できる場合
- **12か月以上** public な活動がなく、かつ **60日以上** の公開連絡にも応答がない場合

### 継承の原則
- 既に指名された successor がいる場合、その指定を優先する
- 指定がない場合、official lineage は **自動継承されない**
- 指定がないまま steward 不在になった場合、official lineage は **frozen** 状態に入る
- frozen 中でも fork / 派生は自由である
- frozen を解除して official lineage を再開するには、少なくとも **2名以上** の新 steward 候補が、最後の official 版を明示的に継承すると宣言し、この文書を更新して公開する

## 提案と採用

### 提案できる者
- 誰でも提案できる
- 入口は issue / discussion / pull request / 文書提案のいずれでもよい

### 提案の種類
- PATCH 提案
- MINOR 提案
- MAJOR 提案
- ROOT-MAJOR 提案
- governance 提案
- module 提案
- errata / clarification 提案

### 採用の原則
- 採用・不採用・保留は steward が公開で記録する
- 重大変更では、理由を短くてもよいので必ず残す
- 変更が official lineage に入らなくても、fork や別提案として存在することは妨げない

### 公開レビュー期間（推奨）
- PATCH: 任意
- MINOR: **7日以上** 推奨
- MAJOR / ROOT-MAJOR / governance 破壊的変更 / official module 採用: **14日以上** 推奨

---

## official lineage と fork の関係

### fork の正当性
- fork はライセンス上も運用上も正当である
- official lineage は fork の存在を否定しない
- official lineage は、fork を禁止する権限を持たない

### official 表記
次の表記を単独で用いて、**official lineage と誤認させてはならない**。

- `Purpose OS — CORE`
- `official`
- `canonical`
- `official lineage`

fork / 派生は、次のように **別系譜であることを明示** して参照できる。

- `fork of Purpose OS — CORE v1.1.0`
- `derived from Purpose OS — CORE v1.1.0`
- `compatible with Purpose OS — CORE v1.x`（条件を満たす場合のみ）

### 互換・準拠の最低条件
`compatible with Purpose OS — CORE ...` またはそれに準ずる表記を使う場合、少なくとも次を満たす。

- 依拠する `spec.md` の版を明示する
- CORE の既存定義を **再定義しない**
- 差分がある場合、その差分を明示する
- official lineage ではない場合、official であるかのように示さない

---

## 後続モジュールの規律

official module として扱うには、少なくとも次を満たす。

- 依存先の CORE 版を明示する
- 可能なら依存先 module も明示する
- 依存関係は **循環させない**
- CORE の定義を変更しない
- 自分の正本と非規範補助を区別する
- 他 module を取り込む場合、どこまでを自分の責任範囲とするかを明示する

後続 module が CORE の根本定義を書き換える場合、それは **official extension ではなく fork / 別系譜** とする。

---

## 状態管理（lifecycle）

official lineage では、概念・文書・module・方針に次の状態を用いてよい。

- **active**: 現行で採用中
- **deprecated**: まだ参照可能だが、新規採用は推奨しない
- **superseded**: 別の概念・文書・module に置き換えられた
- **withdrawn**: 公開は残すが、採用対象から外す

### 運用ルール
- 公開済みの概念ID・文書名・版を **静かに消さない**
- 退役時は tombstone を残す
- **概念IDは再利用しない**
- `superseded` の場合は **置換先** を明記する
- `withdrawn` の場合は **理由** を短くてもよいので残す

---

## root の扱い

official lineage では、**各公開版で採用された Purpose** を、その版の root として扱う。

- 各公開版の内部では、その版の Purpose を **規範上の唯一の起点** とする
- Purpose 自体の改訂提案は誰でもできる
- official lineage における Purpose 改訂の採用判断は、current steward または正当に handoff された successor が行う
- Purpose の改訂は通常変更ではなく、`VERSIONING.md` に定める **ROOT-MAJOR** として扱う
- ROOT-MAJOR 提案には `release/ROOT_MAJOR_TEMPLATE.md` の利用を推奨する
- ROOT-MAJOR を採用する場合は、少なくとも次を公開する
  - 改訂理由
  - 旧Purposeとの差分
  - なぜより良いと判断したか
  - 旧版の状態（少なくとも `superseded`）
- 過去版の Purpose は削除せず残す
- 後続 module は Purpose を独自に再定義しない。Purpose の改訂は module ではなく official lineage の CORE 更新として扱う

これは、「今の official line を保ちながら、将来のより良い root への継承改訂を閉じない」ための運用原則である。

## 公開記録

official lineage の重要な判断は、少なくとも次のいずれかに残す。

- `GOVERNANCE.md`
- `CHANGELOG.md`
- GitHub release notes
- 同等の公開記録

残すべき判断の例:

- steward の追加・辞退・継承・handoff
- Purpose 改訂（ROOT-MAJOR）の提案・採用・不採用
- official module の採用
- deprecated / superseded / withdrawn の宣言
- official lineage の凍結または再開

---

## この文書の変更

- 本文書自体の変更は governance 変更である
- 破壊的変更は **MAJOR 相当** として扱う
- 既存の official lineage / fork / 継承の理解を壊す変更は、重大変更として公開理由を要する
