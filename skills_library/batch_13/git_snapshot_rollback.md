---
title: git-snapshot-rollback
url: https://skills.sh/cafe3310/public-agent-skills/git-snapshot-rollback
---

# git-snapshot-rollback

skills/cafe3310/public-agent-skills/git-snapshot-rollback
git-snapshot-rollback
Installation
$ npx skills add https://github.com/cafe3310/public-agent-skills --skill git-snapshot-rollback
SKILL.md
Git Snapshot & Rollback

此技能通过自动化脚本确保在回退 Git 提交时，不仅保留了当前的尝试（Snapshot），还通过 ARCHIVE.md 构建了一个可追溯的决策链表。

核心工作流
1. 确认回退目标
获取用户想要回退到的目标 Commit Hash。
询问或总结回退的具体原因（Reason）。
2. 执行自动化回退脚本
在执行前，必须询问用户是否需要将存档分支推送到远端仓库。
使用 run_shell_command 调用技能内置脚本：
如果用户同意推送：python3 <path_to_skill>/scripts/rollback.py <Target_Commit> "<Reason>" --push
如果用户不同意推送（默认）：python3 <path_to_skill>/scripts/rollback.py <Target_Commit> "<Reason>"
脚本将自动完成：
Commit 当前所有未提交的变更。
创建 archive/{current_branch}/YYYY-MM-DD-HH-mm 分支。
更新存档分支的 ARCHIVE.md 记录。
(可选) 将存档分支推送到远端。
回到原分支并执行 git reset --hard。
在原分支更新 ARCHIVE.md 并提交回退记录。
列出当前所有领先于远程（未推送）的分支。
3. 结果验证
检查 ARCHIVE.md 是否已正确记录了本次回退的双向链接。
确认当前分支已处于目标 Commit 状态。
记录规范
关于 ARCHIVE.md 的具体格式，请参考 references/log-format.md。
每次回退的 Commit Message 必须包含来源存档分支的信息。
使用禁令
严禁在没有使用此技能的情况下直接执行 git reset --hard 来放弃大量工作。
不得修改或删除 ARCHIVE.md 中的历史记录。
Weekly Installs
13
Repository
cafe3310/public…t-skills
GitHub Stars
197
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass