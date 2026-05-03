---
title: tb-delete-task
url: https://skills.sh/kaelzhang321/teambition-agent-toolkit/tb-delete-task
---

# tb-delete-task

skills/kaelzhang321/teambition-agent-toolkit/tb-delete-task
tb-delete-task
Installation
$ npx skills add https://github.com/kaelzhang321/teambition-agent-toolkit --skill tb-delete-task
SKILL.md
删除 TeamBition 任务
执行步骤
读取 .teambition.md 常用项目和最近任务
用 AskUserQuestion 让用户选择项目，获取任务列表后用 AskUserQuestion 选择要删除的任务
用 AskUserQuestion 再次确认删除（展示任务标题和 ID，选项：确认删除 / 取消）
确认后执行：
node ${CLAUDE_SKILL_DIR}/scripts/tb-api.mjs delete-task --taskId <ID>

从 .teambition.md 最近任务记录中移除该任务
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