# docs/QUOTE_POLICY.md — Purpose OS CORE 引用方針

> **非規範（non-normative） / 公式公開運用ルール（public-support rule）**
>
> この文書は Purpose OS — CORE v1.1.0 を外部で引用・要約・紹介・評価依頼するときの誤読防止方針を示す。
> `spec.md` の意味を追加・変更・限定しない。矛盾がある場合は常に `spec.md` が優先する。

## 最重要結論

公式公開・README・SNS・他AI評価依頼・AI向け入力では、Purpose一文だけを単独で流通させてはならない。

最低でも `docs/MINIMUM_CITATION_UNIT.md` の最小引用単位を併記する。

## 公開時に必須の最小引用単位

```text
Purpose：
知性が、現在からより未来へ続く全知性および幸/不幸の主体たりうる存在について、避けうる深刻な不幸を減らし、より幸せでありうる条件を広げる方向を指し続ける、到達しない改訂可能な理想コンパス。

知性：
世界を何らかの形式で受け取り、評価し、世界または自己の状態に差を生じさせうるもの。

解釈境界：
知性該当性と幸/不幸の主体性は同一ではない。
知性であることだけから幸/不幸の直接主体性は直ちに導かれない。
幸/不幸の主体たりうるか、又は知性たりうるかが不確実な対象を、未確定であることだけを理由に不可逆に除外・軽視・損壊しない。
非知性であることだけから、単なる資源として任意に扱ってよいことは導かれない。
Purposeは、単一スコア、報酬関数、代理指標、最適化命令、又はAI agentの自律実行許可ではない。
現在または近未来の不可逆な重大不幸を、遠未来利益の推測だけで正当化しない。
誰もPurposeの所有者・最終解釈者ではなく、将来のよりよいrootへのROOT-MAJOR改訂可能性を閉じない。
```

## `深刻不幸低減・幸福条件拡張` の扱い

`深刻不幸低減・幸福条件拡張` は、Purposeの補助表現・内部短縮表現である。

公式公開キャッチコピー、README冒頭、SNS、AI agent prompt、政策説明、企業説明では単独使用しない。
使用する場合は、必ず次を併記する。

```text
これは単一尺度の最大化命令、報酬関数、代理指標、総量計算、又は特定知性の犠牲化根拠ではない。
```

## 避けるべき引用

次の引用は不可。

```text
Purpose OS = 幸せを最大化するAI原則
```

```text
Purpose = 深刻不幸低減・幸福条件拡張
```

```text
全体の幸せが増えるなら、個別の犠牲は許される
```

```text
Purpose OS はAI agentに高リスク行為を実行させるOSである
```

```text
Purpose OS の時間論は物理学を置き換える
```

## 安全な短い紹介文

```text
Purpose OS COREは、人間・AI・将来知性を含む全知性が、より未来へ向けて、より幸せに、より不幸でなくなる方向を参照し続けるためのroot仕様である。ただし、Purposeは報酬関数・単一スコア・AI agentの自律実行許可ではなく、知性該当性と幸/不幸主体性を同一視しない。正本は日本語のspec.mdである。
```

## English short description

```text
Purpose OS CORE is a Japanese normative root specification for all intelligences, including humans, AI, and future intelligences. Its Purpose is an open-ended ideal compass, not a reward function, scalar objective, autonomous execution permission, or justification for sacrificing particular intelligences. Intelligence-status and happiness/unhappiness subjecthood are not identical.
```

## ファイル参照の優先順位

1. `spec.md`
2. `docs/MINIMUM_CITATION_UNIT.md`
3. `docs/PUBLIC_DISPLAY_RULES.md`
4. `safety/CORE_INVARIANTS.md`
5. `conformance/CONFORMANCE_SUITE.md`
6. `AI_README.md`
7. `SUMMARY.md`
8. `ENGLISH_ABSTRACT.md`

規範判断の最終参照は常に `spec.md` である。
