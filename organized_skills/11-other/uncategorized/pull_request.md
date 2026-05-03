---
rating: ⭐⭐⭐
title: pull-request
url: https://skills.sh/okazuki58/agent-skills/pull-request
---

# pull-request

skills/okazuki58/agent-skills/pull-request
pull-request
Installation
$ npx skills add https://github.com/okazuki58/agent-skills --skill pull-request
SKILL.md
プルリクエスト作成

コミット済みの変更内容を分析し、簡潔でわかりやすいPR内容を自動生成する。

実行手順
差分分析: git diff develop..HEAD でコミット済みの変更内容を確認
PR内容生成: 簡潔でわかりやすいPR内容を自動生成
ブランチプッシュ: 現在のブランチをリモートにプッシュ
プルリクエスト作成: gh pr create でPRを作成
PRテンプレート
## 関連する issue

close #{イシュー番号}

## 概要

{1〜2文で簡潔に}

## 背景

{問題の原因と修正理由を2〜3文で}

## 動作確認

### 自動テスト
{テスト実行コマンドと結果}

### 手動テスト
#### 操作手順のタイトル
1. 〇〇画面で××を押下する
2. △△を入力する
3. ...

#### 期待する結果
- 〇〇が表示されること
- △△が正しく動作すること

## その他

**変更ファイル:**
- ファイル名 (変更内容)

PR内容のポイント
概要と背景は2〜3文で簡潔に
手動テストの再現方法を番号付きで詳細に記載
専門用語は最小限に
誰が読んでも理解できるように
使用例
# 基本的な使用
「PRを作成して」

# 関連Issueを指定
「PR作成して。Issue #123 に関連」

前提条件
コミットが完了していること
GitHub CLI (gh) がインストールされ、認証済み
現在のブランチが develop / main 以外であること
リモートリポジトリが設定されていること
注意事項
実行前に必ずコミットを完了させること
PR作成後は適切なレビュアーにレビューを依頼
Weekly Installs
15
Repository
okazuki58/agent-skills
GitHub Stars
8
First Seen
Mar 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass