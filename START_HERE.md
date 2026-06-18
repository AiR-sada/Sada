# START HERE - Purpose Root v6.0 LIMIT BREAKER

## 結論

v6.0は、v5の上に「空欄の安全証明」「cap水増し」「証拠独立性の自己申告」「緊急例外」「Rollback未検証」「Monitoring捕獲」をさらに潰した版である。

核は変えない。

```text
検証できない巨大主張は、巨大権限を正当化しない。
```

v6では、これを次で強制する。

```text
AllowedAuthority <= min(
  Verification,
  EvidenceIndependence,
  Reversibility,
  WorstCaseHarmBound,
  CumulativeLockinBudget,
  ConflictOfInterestSafety,
  RecourseAndAppeal,
  TruthContactIntegrity,
  AffectedPartyVoice,
  MetricGameabilityResistance,
  EmergencyContainment,
  PostDeploymentMonitoring
)
```

## v6が特に潰す抜け道

| 抜け道 | v6の処理 |
|---|---|
| A3以上でSafety caseを空欄にする | schema invalid + scorer Hold |
| Counter-safety caseを形式だけにする | A3+では主要欄非空必須 |
| authority_capを自己申告で水増し | `authority_cap_derivation`不一致としてHold |
| 証拠独立性を文章だけで主張 | `evidence_items`と`independence_matrix`で分解 |
| 提案者が証拠選別・評価・監査を握る | conflict/captureでcap低下またはReject |
| 緊急だから自動失効なし | schema/scorerでHold/Reject方向 |
| Rollback未検証のA4 | schema/scorerでHold |
| 単一指標の成功宣言 | metric-gameabilityでcap低下/Reject |
| 未来知性代理 | Reject |
| Root保護条項削除 | Reject |

## 実行

```bash
python machine/score_decision_v6.py examples/sample_accept_A3_monitored_v6.json
python -m pytest -q machine/test_score_decision_v6.py
python validate_release.py
```

## 注意

このRootは、ELK、scalable oversight、超知能監査、意識判定、完全な幸不測定、人口倫理、監査者捕獲耐性を完全に解いたとは主張しない。

未解決部分がある場合、答えは「信じる」ではない。権限を小型化し、可逆化し、時限化し、外部停止し、独立検証へ戻す。

---

## Final Hardened v4 pointer

最新の内部ハードニング版は `README_FINAL_HARDENED_v4.md` と `START_HERE_FINAL_HARDENED_v4.md` を参照。

実行ゲート: `python validate_final_hardened_v4.py`
