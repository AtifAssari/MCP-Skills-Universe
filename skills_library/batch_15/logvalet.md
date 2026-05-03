---
title: logvalet
url: https://skills.sh/youyo/logvalet/logvalet
---

# logvalet

skills/youyo/logvalet/logvalet
logvalet
Installation
$ npx skills add https://github.com/youyo/logvalet --skill logvalet
SKILL.md
logvalet — Backlog PM メタモデル

logvalet プラグインの全スキルの使い方・組み合わせ・ワークフローを案内する。

スキル一覧
📥 情報収集（現状把握）
スキル	用途	いつ使う
/logvalet:context	課題の全コンテキスト一括取得	「この課題どうなってる？」
/logvalet:my-week	今週の担当タスク＋ウォッチ課題	「今週何やるんだっけ」
/logvalet:my-next	直近の担当タスク＋ウォッチ課題	「明日何すればいい？」
/logvalet:decisions	過去の意思決定ログ	「なぜこうなったか経緯を知りたい」
🔍 分析・診断（状態評価）
スキル	用途	いつ使う
/logvalet:health	プロジェクト健全性	「プロジェクト大丈夫？」
/logvalet:risk	統合リスク評価	「リスクは？対策は？」
/logvalet:intelligence	アクティビティ異常検知	「最近の動きに異常は？」
/logvalet:triage	課題トリアージ	「優先度決めて・担当者提案して」
✍️ アクション（実行）
スキル	用途	いつ使う
/logvalet:draft	コメント下書き	「コメント書いて」
/logvalet:issue-create	対話型課題作成	「課題作って」
/logvalet:spec-to-issues	仕様書→課題分解	「specから課題を自動生成」
📊 レポート（報告・共有）
スキル	用途	いつ使う
/logvalet:report	月次・週次活動レポート	「レポート作って」
/logvalet:digest-periodic	定期ダイジェスト	「今週の進捗まとめて」
ワークフロー例
🌅 朝のルーティン
/logvalet:my-week → 今週全体の俯瞰
/logvalet:my-next → 今日・明日の具体的なタスク
📋 プロジェクトレビュー
/logvalet:health PROJECT → 全体の健全性スコア
/logvalet:risk PROJECT → リスク評価と推奨アクション
/logvalet:intelligence PROJECT → アクティビティの偏り・異常
/logvalet:report PROJECT → 共有用レポート生成
🔧 課題対応フロー
/logvalet:context ISSUE → コンテキスト一括取得
/logvalet:decisions ISSUE → 過去の意思決定を確認
/logvalet:triage ISSUE → 優先度・担当者を提案
/logvalet:draft ISSUE → 対応コメントを下書き
🚀 新規開発キックオフ
/logvalet:spec-to-issues → 仕様書から課題を自動生成
/logvalet:health PROJECT → 現状のリソース確認
/logvalet:digest-periodic PROJECT → 定期進捗追跡を開始
CLI 基本情報
コマンド: logvalet (エイリアス: lv)
出力: JSON (デフォルト) / YAML / Markdown / Gantt
初期設定: logvalet configure
各コマンドの詳細は個別スキルを参照
ウォッチ（CLI 直接操作）

ウォッチ課題は担当ではないが自分の仕事に影響する課題。スキル（my-week, my-next 等）で自動表示されるが、CLI で直接操作も可能:

lv watching list me          # 自分のウォッチ一覧
lv watching count me         # 件数
lv watching get <ID>         # 詳細
lv watching add PROJ-123     # ウォッチ追加
lv watching delete <ID>      # ウォッチ解除
lv watching mark-as-read <ID> # 既読化

Weekly Installs
15
Repository
youyo/logvalet
GitHub Stars
2
First Seen
Mar 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass