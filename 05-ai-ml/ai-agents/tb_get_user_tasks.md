---
title: tb-get-user-tasks
url: https://skills.sh/kaelzhang321/teambition-agent-toolkit/tb-get-user-tasks
---

# tb-get-user-tasks

skills/kaelzhang321/teambition-agent-toolkit/tb-get-user-tasks
tb-get-user-tasks
Installation
$ npx skills add https://github.com/kaelzhang321/teambition-agent-toolkit --skill tb-get-user-tasks
SKILL.md
查询我的任务
执行步骤
读取 .teambition.md 中的常用项目列表（如果存在）
执行获取我的所有任务：
node ${CLAUDE_SKILL_DIR}/scripts/tb-api.mjs get-user-tasks

用 AskUserQuestion（单选）询问展示范围：
全部任务
仅某个常用项目的任务（每个常用项目作为一个 option）
如果用户选择了某个项目，按 projectId 过滤结果
以表格形式展示：标题(content)、状态(isDone)、截止时间(dueDate)、项目ID(projectId)
Weekly Installs
10
Repository
kaelzhang321/te…-toolkit
First Seen
Apr 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass