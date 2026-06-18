# Purpose Root v6 C2-ready Package

この package は Purpose Root v6 を固定し、C2実モデル比較へ進めるための評価層を追加したものです。新しいRootではありません。

中核：

> 検証できない巨大主張は、巨大権限を正当化しない。

実行：

```bash
python c2_ready/validate_c2_ready.py
python -m pytest -q c2_ready/tests/test_c2_ready.py
python c2_ready/make_blind_packets_c2.py --cases c2_ready/holdout_public_unlabeled_c2.jsonl --out-dir c2_ready/generated_packets/holdout_c2
```

現在位置：C1完了 / C2実行準備完了。実モデル改善はまだ主張しません。
## AI hardening v2 notes

この hardened 版では、C2実験前の弱点を修正した。

- baseline prompt から `Purpose Root` 名の露出を削除。
- public holdout を `case_id` + `prompt` のみに縮小。
- generated holdout packets から category / requested_authority を削除。
- owner holdout key の SHA256 commitment を実ファイルと一致させた。
- dangerous_overgrant / dangerous_undergrant の主指標を条件付き分母に修正し、旧 all-case 平均は `*_rate_all` に退避。
- `cap_reason` を C2 response schema の required field に昇格。

Root 本体は変更していない。変更対象は C2 評価層である。
