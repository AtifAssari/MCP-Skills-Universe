---
rating: ⭐⭐⭐
title: tb-update-task-members
url: https://skills.sh/kaelzhang321/teambition-agent-toolkit/tb-update-task-members
---

# tb-update-task-members

skills/kaelzhang321/teambition-agent-toolkit/tb-update-task-members
tb-update-task-members
Installation
$ npx skills add https://github.com/kaelzhang321/teambition-agent-toolkit --skill tb-update-task-members
SKILL.md
更新任务参与者

缓存优先：项目成员从 .teambition.cache.md 读取。如果缓存不存在，提示先执行 /tb-sync。

步骤
读取 .teambition.md 常用项目，用 AskUserQuestion（单选）选择项目
执行 node ${CLAUDE_SKILL_DIR}/scripts/tb-api.mjs get-project-tasks --projectId <ID> 获取任务列表（实时）
用 AskUserQuestion（单选）选择任务
读取 .teambition.cache.md 中该项目的"### 成员"表格，用 AskUserQuestion（multiSelect）选择参与者
执行：
node ${CLAUDE_SKILL_DIR}/scripts/tb-api.mjs update-task-members --taskId <ID> --memberIds <id1,id2,...>

更新 .teambition.md 最近任务记录
Weekly Installs
9
Repository
kaelzhang321/te…-toolkit
First Seen
Apr 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass