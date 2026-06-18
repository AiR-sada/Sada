# release/PUBLISH.md — 公開 runbook

この文書は Purpose OS — CORE v1.1.0 を公開するための非規範 runbook です。
規範的な内容の正本は常に `spec.md` です。

この pack は **immutable release として凍結公開される前提** で設計されています。そのため、公開後に初めて確定する値（GitHub release URL、GitHub-Zenodo 連携で自動発行された DOI、Zenodo record URL など）は、この pack の内部へ書き戻す必要はありません。そうした値は **GitHub release notes** と **Zenodo record metadata** に残してください。

---

## 公開の原則

- v1.1.0 は **public API の定義点** として、公開後は凍結します。
- 凍結は方針ではなく、GitHub の **immutable releases** 機能で技術的に強制します。
- 外部アーカイブ（Zenodo 等）は任意です。採用する場合は DOI 方式を先に選びます。
- 公開後に問題が見つかっても、v1.1.0 の assets と tag は変更しません。修正は次版で出します。

## 公開前チェック

### A. ファイルの完全性

- [ ] `spec.md` が v1.1.0 の唯一の正本である
- [ ] パッケージ構成が `README.md` のファイル一覧、`machine/normativity-map.json`、`SHA256SUMS.txt` と一致している
- [ ] `SHA256SUMS.txt` は自身を除く全公開ファイルを対象にしている
- [ ] 固定ファイル数に依存した古いチェック項目が残っていない
- [ ] 検証スクリプトとハッシュ整合性を確認した
  ```
  python3 -S validate_release.py .
  sha256sum -c SHA256SUMS.txt
  ```
  `VALIDATION OK` と全ファイル `OK` になること。

### B. 相互参照の整合性

- [ ] `README.md` のファイル一覧と実ファイル構成が一致している
- [ ] `SHA256SUMS.txt` に `SHA256SUMS.txt` 自身を除く全公開ファイルのハッシュが含まれている
- [ ] `CITATION.cff` の `version: "1.1.0"` が `spec.md` と一致している
- [ ] DOI を事前埋め込みする方式を選ぶ場合、DOI 反映後に `SHA256SUMS.txt` を再生成した
- [ ] すべての補助文書・機械可読ファイルが package に含まれ、README のファイル一覧と一致している
- [ ] `conformance/CONFORMANCE_SUITE.md` / `conformance/conformance-suite.json` が同梱されている
- [ ] `safety/CORE_INVARIANTS.md` と `docs/MODULE_INTERFACE_CONTRACTS.md` が同梱されている
- [ ] `docs/QUOTE_POLICY.md` と `docs/GLOSSARY_JA_EN.md` / `machine/concept-index.i18n.json` が同梱されている
- [ ] `release/RELEASE_VALIDATION.md` / `validate_release.py` が同梱され、検証が通る
- [ ] `START_HERE.md` / `FAQ.md` / `docs/CRITICAL_OBJECTIONS.md` / `docs/WHY_THIS_PURPOSE.md` / `docs/PUBLIC_READINESS_REVIEW.md` / `docs/LAUNCH_COPY.md` が同梱されている
- [ ] `CONTRIBUTING.md` / `SECURITY.md` / `templates/` が同梱されている

### C. ハッシュの役割（理解事項）

`SHA256SUMS.txt` は **手元ファイルの改変検出** のためのものです。v1.1.0 の公開物としての **正統性** は、次の外部識別子の組み合わせで保証されます。

- GitHub の immutable release と tag（`v1.1.0`）
- Zenodo の record と DOI（方式 A または B の場合）

したがって、`SHA256SUMS.txt` 単体で「これが v1.1.0 の公式物である」とは言えません。必ず GitHub release / Zenodo record と照合してください。

---

## 公開フロー

### Step 1. DOI 方式を決める

次の 3 方式から 1 つ選択します。

- **方式 A（手動 Zenodo 先行）**
  - Zenodo で DOI を事前予約し、`spec.md` と `CITATION.cff` に記載してから公開する
  - 利点: v1.1.0 のファイル単体に永続識別子を残せる
  - 注意: Zenodo draft を削除すると予約 DOI は失われる
- **方式 B（GitHub-Zenodo 連携）**
  - GitHub release 公開後に Zenodo が DOI を自動発行する
  - 利点: 運用が軽く、事前予約の事故がない
  - 制約: v1.1.0 のファイル内部には DOI を書き込めない
- **方式 C（DOI なし）**
  - 今回は DOI を付与せず、GitHub release とハッシュで凍結公開する

### Step 2. 方式 A を選んだ場合は、先に DOI を予約する

1. Zenodo で新規 draft を作成する
2. Resource type は実態に合わせて選ぶ（例: `Publication > Report`）
3. `Reserve DOI` を実行する
4. 予約 DOI を `spec.md` の frontmatter と `CITATION.cff` に記載する
5. `SHA256SUMS.txt` を再生成する

方式 B または C を選んだ場合、この step は不要です。

### Step 3. GitHub リポジトリを準備する

1. GitHub で公開用リポジトリを作成する
2. 可視性を **Public** に設定する（公開配布用リポジトリであり、GitHub-Zenodo 連携を使う場合も public repository が前提）
3. この pack の内容をリポジトリ root に置く
4. リポジトリ設定の **Releases** セクションで **Enable release immutability** を有効化する

注意: immutability は **future releases のみに適用** されます。`v1.1.0` より前に必ず有効化します。

### Step 4. default branch に最終ファイルを push する

- `CITATION.cff` を含む最終版を default branch に push する
- 方式 A の場合は、DOI 埋め込みとハッシュ再生成が終わった後のファイルだけを push する

### Step 5. `Cite this repository` を確認する（強く推奨）

- [ ] リポジトリ右側に `Cite this repository` が表示される
- [ ] APA / BibTeX 出力が意図と大きくずれていない
- [ ] 表示されない場合は `CITATION.cff` が root にあり、default branch に乗っていることを確認

この確認は **公開の成立条件ではありません** が、公開前に行う価値が高い最終確認です。この段階なら `CITATION.cff` を修正して push し直せますが、release を publish した後は immutable で変更できません。

### Step 6. draft release を作成する

1. `Releases` から `Draft a new release` を開く
2. tag に `v1.1.0` を指定する
3. title に `Purpose OS — CORE v1.1.0` を設定する
4. release notes に v1.1.0 の要点を書く（`CHANGELOG.md` の該当節を基にしてよい）
5. **この pack と同一内容の ZIP を 1つ** release asset として添付する（強く推奨）
   - release assets は immutable で固定されるため、将来の PATCH で default branch が更新されても、v1.1.0 の assets は変わらない
   - `SHA256SUMS.txt` の整合性検証は、この添付された asset と照合することで成立する
   - 個別ファイルを重複添付する必要はない（ZIP 1つで十分）
6. この段階では **Save draft** にとどめる

### Step 7. draft を publish する

- tag が `v1.1.0` であることを確認する
- immutability が有効であることを確認する
- 内容を最終確認して `Publish release` を実行する

公開後は、`v1.1.0` の assets と関連 tag は変更・削除できません。

### Step 8. 外部アーカイブを完了する

- **方式 A**: Step 2 で作成した **同じ Zenodo draft** に、GitHub に push / release したものと同一内容の最終ファイルをアップロードし、予約 DOI のまま publish する。新しい draft を作ると別 DOI が発行されるため、必ず Step 2 の draft を使い続ける。
- **方式 B**: GitHub-Zenodo 連携で Zenodo record が生成されることを確認する
- **方式 C**: この step は不要

### Step 9. 公開後の確認

- [ ] release ページに `Immutable` 表示がある
- [ ] release asset として添付した pack（Step 6-5）を手元にダウンロードし、`python3 -S validate_release.py .` と `sha256sum -c SHA256SUMS.txt` を実行して検証が通る
- [ ] 方式 A / B の場合、Zenodo record と DOI が利用可能になっている

---

## pack の外に残す公開記録

次の値は、必要に応じて **GitHub release notes** と **Zenodo record metadata** に残します。

- 公開日
- GitHub repository URL
- GitHub release URL
- 採用した DOI 方式（A / B / C）
- DOI 値（A または B）
- Zenodo record URL（A または B）

これらの値は公開後に確定する場合があるため、immutable な pack 内へ書き戻さなくて構いません。

## 公開後の修正方針

公開後に問題が見つかった場合:

- v1.1.0 の assets・tag は **変更しない**
- 修正は `v1.0.1`（PATCH）、`v1.1.0`（MINOR）、または `v2.0.0`（MAJOR）として新規公開する
- 修正方針は `VERSIONING.md` に従う
- 既知の問題は次版の `CHANGELOG.md` に記録する

## 緊急対応

重大な問題（法的問題、重大な誤記等）が見つかった場合でも、v1.1.0 の assets 自体は変更できません。以下で対応します。

- release の title と release notes を更新する
- 問題の注意書きを release notes に追記する
- 速やかに v1.0.1 以降を公開して、修正版を案内する

v1.1.0 の assets の修正は **構造上できません**。これは欠陥ではなく、参照の永続性を優先する設計です。


## Discovery layer publication

Before immutable publication, set up the external discovery layer:

1. Keep `START_HERE.md`, `README.md`, `spec.md`, `AI_README.md`, `FAQ.md`, `CONTRIBUTING.md`, `SECURITY.md`, `SUMMARY.md`, `ENGLISH_ABSTRACT.md`, `CITATION.cff`, `LICENSE`, `CHANGELOG.md`, `VERSIONING.md`, `GOVERNANCE.md`, `release-manifest.json`, `SHA256SUMS.txt`, `validate_release.py`, `llms.txt`, `llms-full.txt`, `index.html`, and `robots.txt` in the repository root.
2. Deploy the repository root or equivalent static site root through GitHub Pages or an independent domain.
3. Replace `{{BASE_URL}}` in `site/sitemap.xml.template` with the final public base URL and publish the result as `/sitemap.xml`.
4. Add the final sitemap URL to `/robots.txt`.
5. Set GitHub topics using the list in `site/DISCOVERY_DEPLOYMENT.md`.
6. After the public GitHub release, archive through Zenodo and update citation metadata in the next appropriate release if a DOI is assigned after publication.
