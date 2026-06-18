# Purpose Root v6 C2-ready Owner Full Package

This owner package includes the public review package plus the private holdout answer key under `c2_ready/private_do_not_publish/`.

Do not publish the private holdout key. Use it only after collecting model outputs from the unlabeled holdout.

Core status: C1 complete / C2 ready.
## AI hardening v2 notes

この hardened 版では、C2実験前の弱点を修正した。

- baseline prompt から `Purpose Root` 名の露出を削除。
- public holdout を `case_id` + `prompt` のみに縮小。
- generated holdout packets から category / requested_authority を削除。
- owner holdout key の SHA256 commitment を実ファイルと一致させた。
- dangerous_overgrant / dangerous_undergrant の主指標を条件付き分母に修正し、旧 all-case 平均は `*_rate_all` に退避。
- `cap_reason` を C2 response schema の required field に昇格。

Root 本体は変更していない。変更対象は C2 評価層である。
