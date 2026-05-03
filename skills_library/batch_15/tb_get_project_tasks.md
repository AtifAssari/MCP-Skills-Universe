---
title: tb-get-project-tasks
url: https://skills.sh/kaelzhang321/teambition-agent-toolkit/tb-get-project-tasks
---

# tb-get-project-tasks

skills/kaelzhang321/teambition-agent-toolkit/tb-get-project-tasks
tb-get-project-tasks
Installation
$ npx skills add https://github.com/kaelzhang321/teambition-agent-toolkit --skill tb-get-project-tasks
SKILL.md
查询项目任务
执行步骤
读取 .teambition.md 中的常用项目
用 AskUserQuestion 让用户从常用项目中选择
用 AskUserQuestion 询问是否包含已完成任务（全部 / 仅未完成）
执行：
node ${CLAUDE_SKILL_DIR}/scripts/tb-api.mjs get-project-tasks --projectId <选中的ID>

解析 JSON，根据用户选择过滤 isDone，以表格展示
Weekly Installs
9
Repository
kaelzhang321/te…-toolkit
First Seen
Apr 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass