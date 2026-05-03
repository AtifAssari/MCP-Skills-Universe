---
rating: ⭐⭐⭐
title: readme-i18n
url: https://skills.sh/u9401066/med-paper-assistant/readme-i18n
---

# readme-i18n

skills/u9401066/med-paper-assistant/readme-i18n
readme-i18n
Installation
$ npx skills add https://github.com/u9401066/med-paper-assistant --skill readme-i18n
SKILL.md
README 國際化 (i18n) 技能

觸發：翻譯 README、sync readme、多語言、README 有變更時自動觸發

工具：read_file、replace_string_in_file、get_changed_files

檔案

README.md（英文 Primary）↔ README.zh-TW.md（繁體中文）

同步方向
情況	動作
用戶提供中文	同步到英文版
用戶提供英文 / README.md 變更	同步到中文版
術語對照
EN	中文
Constitution	憲法
Bylaws	子法
Skills	技能
Memory Bank	記憶庫
Domain-Driven Design	領域驅動設計
Data Access Layer	資料存取層
翻譯原則
技術術語一致（查對照表）
程式碼不翻譯（只翻註解）
Markdown 結構完全對應
Emoji 兩版一致
工作流
讀取兩版本 → 比對章節差異（## 標題數、code block 數）
翻譯新增/變更段落 → 更新對應版本
檢查：章節數一致、code block 一致、連結有效、術語一致
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