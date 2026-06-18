# release/RELEASE_VALIDATION.md — Purpose OS CORE 検証手順

> **非規範（non-normative / operational support）**
>
> この文書は Purpose OS — CORE v1.1.0 の公開前・改訂前検証手順を示す。`spec.md` の意味を追加・変更・限定しない。

## 推奨コマンド

```bash
python3 -S validate_release.py .
sha256sum -c SHA256SUMS.txt
```

`validate_release.py` は Python 標準ライブラリのみを使う。

## 検査項目

- 全JSONの構文
- `release-manifest.json` の基本値、最終公開status、件数
- hardening anchor (`SC-018`, `SC-019`, `CS-043`〜`CS-046`, `INV-016`, `INV-017`) の存在
- Purpose root 非定理化・ROOT-MAJOR継承改訂可能性の明記
- safety constraint / conformance case / core invariant の連番・件数
- 主要JSONのschema subset適合
- `spec.md` と `machine/concept-index.json` の概念ID一致
- `machine/concept-index.json` と `machine/dependency-graph.json` のnode/edge整合
- dependency graph の循環検査
- safety constraint IDの形式と重複
- conformance case ID、label、必須field、参照concept、安全制約
- `out-of-scope` case の存在
- `machine/concept-index.i18n.json` の概念カバレッジ
- `machine/concept-index.en.json` の概念カバレッジと `normative=false`
- `machine/relationship-map.json` のrelationship IDと概念参照
- `interfaces/` の主要interface skeletonの存在
- `schemas/` の主要JSON schemaの存在
- `machine/normativity-map.json` の全公開ファイルカバレッジ
- 凡例外の禁止記号
- `SHA256SUMS.txt` の再帰的完全性

## 合格条件

`validate_release.py` が次を表示する。

```text
VALIDATION OK
```

かつ、

```bash
sha256sum -c SHA256SUMS.txt
```

で全対象ファイルが `OK` になる。

## 注意

検証スクリプトは、哲学的・規範的内容の真偽を証明しない。検証するのは、構文・参照・整合・ハッシュである。


## Discovery layout validation

The release validator now also checks:

- expected root entry/discovery files are present;
- legacy auxiliary files are not left in the repository root;
- `llms.txt` contains key references;
- `index.html` contains JSON-LD discovery metadata;
- `site/sitemap.xml.template` retains the `{{BASE_URL}}` placeholder until deployment.
