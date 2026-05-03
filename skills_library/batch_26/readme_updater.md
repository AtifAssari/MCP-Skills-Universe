---
title: readme-updater
url: https://skills.sh/u9401066/med-paper-assistant/readme-updater
---

# readme-updater

skills/u9401066/med-paper-assistant/readme-updater
readme-updater
Installation
$ npx skills add https://github.com/u9401066/med-paper-assistant --skill readme-updater
SKILL.md
README 更新技能

觸發：更新 README、文檔、怎麼用、安裝說明、被 git-precommit 自動調用

工具：read_file("README.md")、replace_string_in_file、list_dir、get_changed_files

更新對應
變更類型	更新區塊
新功能	功能列表
新依賴	安裝說明
API 變更	使用範例
目錄變更	專案結構
新設定	配置說明
保護區塊（不自動修改）

授權資訊、貢獻指南、致謝

工作流
read_file("README.md") + get_changed_files()
分析變更 → 對應更新區塊
replace_string_in_file 更新對應區塊
Weekly Installs
23
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