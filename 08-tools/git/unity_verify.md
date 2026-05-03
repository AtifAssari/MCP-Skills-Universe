---
rating: ⭐⭐
title: unity-verify
url: https://skills.sh/bigdra50/unity-cli/unity-verify
---

# unity-verify

skills/bigdra50/unity-cli/unity-verify
unity-verify
Installation
$ npx skills add https://github.com/bigdra50/unity-cli --skill unity-verify
SKILL.md
unity-verify

PREREQUISITE: ../unity-shared/SKILL.md

Quick Verify

コード変更するたびに実行。unity-shared の Quick Verify そのもの。

u refresh → isCompiling ポーリング → u console clear → u console get -l E,W
→ Error あり: 修正して再実行 (最大3回)
→ クリーン: 完了

Full Verify

ユーザーが要求した場合のみ。Quick Verify + EditMode テスト。

Quick Verify 実行
→ クリーンなら u tests run edit → 結果確認
→ Fail あり: 報告、修正して Quick Verify から再実行

Runtime Check

要求された場合のみ。Play Mode でランタイムエラーを検出。

u console clear → u play → isPlaying ポーリング → 3秒待機 → u console get -l +E+X → u stop


報告のみ。自動修正せずユーザーに判断を委ねる。

Auto-trigger

以下の編集後に Quick Verify を自動実行:

.cs / .shader / .compute
.asmdef / .asmref
Unity パッケージ関連 (package.json / manifest.json)

スキップ: コメントのみの変更、プロジェクト外ファイル、ユーザー指示。

Weekly Installs
8
Repository
bigdra50/unity-cli
GitHub Stars
36
First Seen
Mar 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass