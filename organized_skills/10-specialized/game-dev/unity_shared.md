---
rating: ⭐⭐⭐
title: unity-shared
url: https://skills.sh/bigdra50/unity-cli/unity-shared
---

# unity-shared

skills/bigdra50/unity-cli/unity-shared
unity-shared
Installation
$ npx skills add https://github.com/bigdra50/unity-cli --skill unity-shared
SKILL.md
unity-shared

全 unity-* スキルが従う共通ルール。

接続
u instances    # 接続中 Unity 一覧
u state        # エディタ状態


接続不可時: unity-relay --port 6500 で Relay 起動。

Quick Verify

コード変更後に毎回実行する検証シーケンス。

u refresh                          # AssetDatabase リフレッシュ
# u state --json ポーリング (isCompiling == false まで、2秒間隔、最大30秒)
u console clear                    # ログクリア
u console get -l E,W --count 50    # Error/Warning 取得

Error あり → 修正して再実行 (最大3回)
Warning のみ → 報告して続行
フォールバック順

CLI 非対応の操作を行う場合:

1. u <既存コマンド>           最優先
2. u api call Type Method    5,243 メソッド対応
3. YAML 直接編集              最終手段 (.meta インポート設定等)

セキュリティ
u api call は UnityEngine / UnityEditor のみ許可
破壊的操作の実行前にユーザー確認
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