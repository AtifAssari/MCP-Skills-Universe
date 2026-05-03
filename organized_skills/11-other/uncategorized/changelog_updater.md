---
rating: ⭐⭐⭐
title: changelog-updater
url: https://skills.sh/u9401066/med-paper-assistant/changelog-updater
---

# changelog-updater

skills/u9401066/med-paper-assistant/changelog-updater
changelog-updater
Installation
$ npx skills add https://github.com/u9401066/med-paper-assistant --skill changelog-updater
SKILL.md
CHANGELOG 更新技能

觸發：更新 changelog、發布、新版本、被 git-precommit 自動調用

工具：read_file("CHANGELOG.md")、replace_string_in_file、get_changed_files

格式（Keep a Changelog）

## [Unreleased] → ### Added/Changed/Deprecated/Removed/Fixed/Security

分類規則
類型	關鍵字
Added	feat, 新增, add
Changed	change, update, 變更
Deprecated	deprecate, 棄用
Removed	remove, delete, 移除
Fixed	fix, bug, 修復
Security	security, 安全
版本號（SemVer）

MAJOR：Breaking Changes | MINOR：新功能（向下相容）| PATCH：Bug 修復

工作流
read_file("CHANGELOG.md") + get_changed_files()
分類：新檔案→Added、修改→Changed/Fixed、刪除→Removed
更新 [Unreleased] 區塊
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