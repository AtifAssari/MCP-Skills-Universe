---
rating: ⭐⭐
title: issue-create
url: https://skills.sh/okazuki58/agent-skills/issue-create
---

# issue-create

skills/okazuki58/agent-skills/issue-create
issue-create
Installation
$ npx skills add https://github.com/okazuki58/agent-skills --skill issue-create
SKILL.md
Issue生成

雑な要件や思考メモからGitHub Issueを生成する。

振る舞い
入力内容を確認（テキスト入力または添付ファイル）
内容を整理し、Issue用の構造に再構成
記載されていない仕様は推測しない
未確定事項がある場合は、AskUserQuestionで確認
gh issue create で Issue を作成
出力構造

Issue本文のテンプレートは references/output-structure.md を参照。

制約
コードを書かない
技術選定・実装方針を書かない
提供された情報に書かれていない内容は推測しない
前提条件
GitHub CLI (gh) がインストールされ、認証済み
現在のディレクトリがGitリポジトリ
リポジトリに対してIssue作成権限がある
Weekly Installs
17
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