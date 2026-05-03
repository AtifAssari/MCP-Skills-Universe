---
title: tb-set-parent-task
url: https://skills.sh/kaelzhang321/teambition-agent-toolkit/tb-set-parent-task
---

# tb-set-parent-task

skills/kaelzhang321/teambition-agent-toolkit/tb-set-parent-task
tb-set-parent-task
Installation
$ npx skills add https://github.com/kaelzhang321/teambition-agent-toolkit --skill tb-set-parent-task
SKILL.md
设置父子任务
执行步骤
读取 .teambition.md 常用项目和最近任务
用 AskUserQuestion 让用户选择项目
获取任务列表，用 AskUserQuestion 让用户选择父任务
用 AskUserQuestion 让用户选择子任务
执行：
node ${CLAUDE_SKILL_DIR}/scripts/tb-api.mjs set-parent-task --taskId <子任务ID> --parentTaskId <父任务ID>

更新 .teambition.md 最近任务记录
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