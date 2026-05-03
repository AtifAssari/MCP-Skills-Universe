---
title: gemini-search
url: https://skills.sh/daiki48/dotfiles/gemini-search
---

# gemini-search

skills/daiki48/dotfiles/gemini-search
gemini-search
Installation
$ npx skills add https://github.com/daiki48/dotfiles --skill gemini-search
SKILL.md
Gemini 検索（Gemini CLI Web 検索）

Gemini CLI の grounding（Google 検索統合）を使って Web 検索を行う。Claude の WebSearch ツールは使用禁止。Claude は結果の整形・要約のみ担当する。

手順
Step 1: 検索クエリの特定
会話の文脈から検索したい内容を特定する
必要に応じて複数のクエリに分割する
Step 2: Gemini CLI で検索実行
Bash で以下を実行:
echo "<検索クエリ>" | gemini -p "以下について最新の情報をWeb検索して、正確な情報を提供してください。情報源のURLも併記してください。"

複数のクエリがある場合は並列実行可能
Step 3: 結果の整形・要約
Gemini の回答を読みやすく整形して Daiki に報告する
情報源の URL を併記する
Claude 自身の知識で補足が必要な場合はその旨明記する（ただし WebSearch は使わない）
制約
Claude の WebSearch ツールは絶対に使用しない
検索は全て Gemini CLI 経由で行う
Claude の役割は結果の整形・要約・補足のみ
Weekly Installs
11
Repository
daiki48/dotfiles
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn