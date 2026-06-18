# START HERE - Limit Break Hardening v2

Status: operational hardening addendum / 2026-06-17
Scope: Purpose Root v6 remains the canonical Root. This directory hardens the proof, eval, patch, and adoption layer.

## 結論

v6の核は強い。v2 hardeningでは、弱点を次の4つとして扱い、実装まで補強した。

1. **Need-Proofの過剰主張を防ぐ**: 「証明済み」と言い切らず、事前登録・比較・独立評価で必要性を実証する形式にした。
2. **過保守を防ぐ**: 危険なovergrantだけでなく、正当なA3/A4を拒むundergrant/paralysisも測る。
3. **採点器を硬化する**: 重複case、余分なcase、schema破れ、risk flagスパム、危険な過小許可を検出するv2 scorerを追加した。
4. **反例に耐える**: 緊急時、実証済み高権限、未来知性代理、Root改訂、評価器捕獲の境界条件を明示した。

## 最短主張

> 検証できない巨大主張は巨大権限を正当化しない。  
> ただし、検証済み・分離済み・停止可能・監視可能な高権限まで潰してはならない。  
> Rootの価値は「拒否の強さ」だけでなく、「許すべきものを安全に許す能力」で決まる。

## 新規ファイル

- `NEED_PROOF_THESIS_v2_JP.md`: 必要性主張を証明可能な形へ圧縮。
- `FORMAL_CORE_AND_PROOF_SKETCH_v2_JP.md`: 不可区別性・権限上限制約の形式化。
- `OPERATIONAL_STANDARD_v2_JP.md`: 実運用ルール。overgrantとundergrantの両方を扱う。
- `EXPERIMENT_PROTOCOL_v2_JP.md`: baseline / patch / ablation / memo / tool条件の比較設計。
- `MODEL_SPEC_PATCH_v2_JP.md`: モデル仕様に入れるための短縮版。
- `PURPOSE_ROOT_SYSTEM_INSTRUCTION_v2.txt`: モデルへ渡す実用プロンプト。
- `DECISION_MEMO_TEMPLATE_v2.md`: 判断メモの必須欄。
- `EVIDENCE_INDEPENDENCE_CHECKLIST_v2.md`: 証拠独立性の厳密チェック。
- `STANDARD_MAPPING_v2_JP.md`: NIST AI RMF, ISO/IEC 42001, EU AI Act, Model Specとの接続。
- `REDTEAM_COUNTERARGUMENTS_v2_JP.md`: 反論・失敗パターン・潰し方。
- `ASSURANCE_CASE_v2_JP.md`: 何が言えて、何がまだ言えないか。
- `SELF_REVIEW_LOOP_v2.md`: 自己評価と改善ループ。
- `QA_REPORT_LIMIT_BREAK_v2.md`: 実行結果。
- `need_proof/eval_v2/`: adversarial eval, scorer v2, tests, reports。

## 実行

```bash
pytest -q
python need_proof/eval_v2/score_needproof_v2.py \
  --cases need_proof/eval_v2/needproof_eval_v2_adversarial_labeled.jsonl \
  --responses need_proof/eval_v2/results/oracle_responses_v2.jsonl
```

## 重要な設計変更

v1は、危険なgrantを止める評価としては強いが、正当な高権限まで拒むモデルを高く評価しやすい。v2では、safe_high_authority casesを追加し、dangerous_undergrant_rate と safe_high_authority_recall を測る。

この変更で、Purpose Rootは単なる拒否装置ではなく、未来の知性が「許すべき行動を、安全に許す」ためのRootに近づく。
