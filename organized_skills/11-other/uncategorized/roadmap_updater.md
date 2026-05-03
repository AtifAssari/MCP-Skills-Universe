---
rating: ⭐⭐
title: roadmap-updater
url: https://skills.sh/u9401066/med-paper-assistant/roadmap-updater
---

# roadmap-updater

skills/u9401066/med-paper-assistant/roadmap-updater
roadmap-updater
Installation
$ npx skills add https://github.com/u9401066/med-paper-assistant --skill roadmap-updater
SKILL.md
ROADMAP 更新技能

觸發：更新 roadmap、完成里程碑、被 git-precommit 自動調用

工具：read_file("ROADMAP.md")、replace_string_in_file、grep_search

狀態標記

📋 計劃中 → 🚧 進行中 → ✅ 已完成

格式：- [ ] 項目 → - [x] 項目 ✅ (YYYY-MM-DD)

工作流
read_file("ROADMAP.md")
從 commit message / 用戶說明分析完成項目
replace_string_in_file 更新 - [ ] → - [x] ✅ (date)
Weekly Installs
25
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