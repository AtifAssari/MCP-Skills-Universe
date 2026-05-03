---
title: git-doc-updater
url: https://skills.sh/u9401066/med-paper-assistant/git-doc-updater
---

# git-doc-updater

skills/u9401066/med-paper-assistant/git-doc-updater
git-doc-updater
Installation
$ npx skills add https://github.com/u9401066/med-paper-assistant --skill git-doc-updater
SKILL.md
Git 文檔自動更新技能

觸發：更新文檔、sync docs、準備發布、被 git-precommit 自動調用

工具：read_file、replace_string_in_file、get_changed_files、memory_bank_update_progress

更新對應
文檔	更新條件	調用 Skill
README.md	新功能/依賴變更	readme-updater
CHANGELOG.md	任何代碼變更	changelog-updater
ROADMAP.md	完成里程碑	roadmap-updater
memory-bank/	每次提交	memory-updater
工作流
get_changed_files() 分析變更
判斷更新：src/ 新檔→README、pyproject.toml→README 安裝、任何變更→CHANGELOG、ROADMAP 項目→ROADMAP
依序呼叫對應 Skill
memory_bank_update_progress() 同步
Weekly Installs
22
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