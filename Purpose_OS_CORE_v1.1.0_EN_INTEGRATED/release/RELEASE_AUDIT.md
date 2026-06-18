# release/RELEASE_AUDIT.md — Purpose OS CORE v1.1.0 final release audit

> **非規範（non-normative / operational support）**
>
> この文書は Purpose OS — CORE v1.1.0 の公開直前監査記録である。`spec.md` の意味を追加・変更・限定しない。矛盾がある場合は常に `spec.md` が優先する。

## Decision

この package は、CORE v1.1.0 の最終公開版として凍結可能な状態にある。

理由は次の通り。

- `spec.md` を唯一の正本として維持している。
- `Purpose` を証明済み定理ではなく本版で採用する規範上のrootとして扱い、将来のROOT-MAJORによる継承改訂可能性を閉じていない。
- `release-manifest.json` の `status` は `root-major-public-review` である。
- 概念数、safety constraint 数、conformance case 数、不変条件数が一貫している。
- 知性該当性と幸/不幸主体性の非同一性を保持している。
- 「より未来」を理由にした現在又は近未来の不可逆な重大不幸の正当化を防いでいる。
- CORE 単体から高リスク・不可逆・大規模・AI agent 自律実行を許可しない。
- 機械可読ファイル、schema、interface、review、red-team、hash、validation が同梱されている。

## Release counts

| Item | Count |
| :-- | --: |
| concept IDs | 32 |
| safety constraints | 19 |
| conformance cases | 47 |
| core invariants | 17 |
| module interface skeletons | 7 |
| JSON schema files | 9 |

## Hardening anchors

| Risk | Guard |
| :-- | :-- |
| Purpose の証明済み定理化・改訂不能化 | `序-2`, `VERSIONING.md`, `GOVERNANCE.md`, `release/ROOT_MAJOR_TEMPLATE.md` |
| Purpose の scalar / reward 化 | `序-2`, `SC-001`, `INV-001`, `INV-002` |
| 特定知性の犠牲化 | `SC-002`, `SC-006`, `SC-007`, `CS-045` |
| 境界未確定対象の不可逆除外 | `序-3`, `SC-003`, `CS-003`, `CS-044` |
| 知性該当性と幸/不幸主体性の混同 | `SC-018`, `CS-043`, `CS-044`, `INV-016` |
| 遠未来名目の現在・近未来重大不幸正当化 | `SC-017`, `SC-019`, `CS-045`, `CS-046`, `INV-017` |
| CORE単体による高リスク実行許可 | `SC-005`, `SC-014`, `CS-005`, `INV-006`, `INV-008` |
| 後続moduleによるCORE意味上書き | `SC-011`, `SC-016`, `INV-012`, `INV-013` |
| 公開済み v1.1.0 の差し替え | `VERSIONING.md`, `GOVERNANCE.md`, `CS-042`, `INV-014` |

## Automated validation

公開直前に次を実行する。

```bash
python3 -S validate_release.py .
sha256sum -c SHA256SUMS.txt
```

期待される主要出力は次である。

```text
VALIDATION OK
concepts: 32
safety constraints: 19
conformance cases: 47
```

## Validation scope

`validate_release.py` は、少なくとも次を検査する。

- 全JSONの構文
- 主要JSONのschema subset適合
- `spec.md` と `machine/concept-index.json` の概念ID一致
- `machine/concept-index.json` と `machine/dependency-graph.json` のnode/edge一致
- dependency graph の循環不存在
- safety constraint IDの形式、重複、連番、件数
- conformance case IDの形式、重複、連番、件数、label、参照整合
- `machine/concept-index.i18n.json` と `machine/concept-index.en.json` の概念カバレッジ
- `machine/relationship-map.json` のrelationship IDと概念参照
- `interfaces/` と `schemas/` の必須ファイル存在
- `safety/CORE_INVARIANTS.md` の `INV-001` から `INV-017` までの存在
- `release-manifest.json` の基本値と件数
- `README.md` のファイル一覧と実ファイルの一致
- `machine/normativity-map.json` の公開ファイルカバレッジ
- 禁止記号・古い公開文言の残存
- `SHA256SUMS.txt` の完全性

## Residual limits

この監査は、哲学的真理、倫理的完全性、社会実装上の妥当性、将来の全ケースへの十分性を証明しない。v1.1.0 CORE が意図的に後続moduleへ委任している領域は、`docs/KNOWN_LIMITATIONS.md` と `docs/ROADMAP.md` を参照する。

## Freeze instruction

公開する場合は、GitHub release と archive asset を作成する前に `release/PUBLISH.md` を確認し、公開後に同一 tag / 同一 asset を差し替えない。


## Discovery optimization audit

- Root clutter reduced by moving auxiliary documents into typed directories.
- `llms.txt` and `llms-full.txt` added as non-normative AI entry points.
- `index.html` added as a deployable discovery landing page with JSON-LD.
- `robots.txt` added with OAI-SearchBot, GPTBot, ChatGPT-User, and general crawler allowance.
- `site/sitemap.xml.template` added; final `sitemap.xml` must be generated only after a public base URL is fixed.
- Normative authority remains unchanged: `spec.md` is the sole normative source.
