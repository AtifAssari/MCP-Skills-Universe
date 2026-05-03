---
title: project-init
url: https://skills.sh/u9401066/med-paper-assistant/project-init
---

# project-init

skills/u9401066/med-paper-assistant/project-init
project-init
Installation
$ npx skills add https://github.com/u9401066/med-paper-assistant --skill project-init
SKILL.md
專案初始化技能

觸發：初始化新專案、create project、bootstrap、scaffold

工具：create_directory、create_file、run_in_terminal、create_new_workspace

專案結構

.github/bylaws/ .github/prompts/ .claude/skills/ memory-bank/(activeContext + progress + decisionLog) src/ tests/ + CONSTITUTION.md README.md CHANGELOG.md pyproject.toml

互動式設定
項目	選項
專案名稱	自訂
程式語言	Python / TypeScript / Other
授權	MIT / Apache-2.0 / GPL-3.0
Docker	是 / 否
CI/CD	GitHub Actions / None
工作流
取得專案資訊（名稱、語言、授權）
建立目錄結構（src, tests, memory-bank, .github, .claude）
建立基礎檔案（README, CHANGELOG, pyproject.toml）
git init → uv venv && uv sync（Python 用 uv）
Weekly Installs
20
Repository
u9401066/med-pa…ssistant
GitHub Stars
7
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass