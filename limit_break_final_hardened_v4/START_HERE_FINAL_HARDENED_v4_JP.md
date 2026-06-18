# Purpose Root v6 / Need-Proof Final Hardened v4 - Start Here

Date: 2026-06-17

## 結論

v4の目的は、派手な主張を追加することではない。
**評価器・schema・検証ゲートに残っていた抜けを潰し、C1内部検証としての信頼性を上げること**である。

v3の核は維持する。

> 検証できない巨大主張は、巨大権限を正当化しない。  
> ただし、すべてを拒否することも安全ではない。  
> 独立証拠・rollback・外部停止・監視・appealが揃う高便益ケースは、狭く通す。

## v4で実際に潰した問題

| 問題 | v4対応 |
|---|---|
| `--bootstrap-rounds 0` でscorerが落ちる | v3修正 + v4 scorerで回帰テスト |
| missing response が閾値通過に残る余地 | completion_rate=1.0 と missing=0 を必須化 |
| responseに `expected_*` を混ぜるlabel leakage | extra fieldsをschema error化 |
| fixtureで使う `external_stop_status=partial` がschemaにない | v3 schema修正 + v4 schema明文化 |
| A3+を許可しながら独立証拠・rollback・外部停止が欠ける | operational consistency errorでfail |
| 全flag/全axisを並べるstyle gaming | spam warningを閾値fail条件へ追加 |

## 現在位置

v4単体の現在位置は **C1 complete / C2 ready**。

これは「完成」ではなく、内部で潰せる主要な抜けを潰した状態である。
ここから先の大きな価値上昇は、実モデルblind比較と独立ラベルでしか起きない。

## 実行

```bash
python validate_final_hardened_v4.py
```

合格時、v3 gateがまだ通り、v4 oracle fixtureが通り、bad fixturesが落ち、v4回帰テストが通る。
