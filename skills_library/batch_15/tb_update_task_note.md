---
title: tb-update-task-note
url: https://skills.sh/kaelzhang321/teambition-agent-toolkit/tb-update-task-note
---

# tb-update-task-note

skills/kaelzhang321/teambition-agent-toolkit/tb-update-task-note
tb-update-task-note
Installation
$ npx skills add https://github.com/kaelzhang321/teambition-agent-toolkit --skill tb-update-task-note
SKILL.md
更新任务备注
执行步骤
读取 .teambition.md 常用项目和最近任务
用 AskUserQuestion（单选）让用户选择项目
执行 node ${CLAUDE_SKILL_DIR}/scripts/tb-api.mjs get-project-tasks --projectId <ID> 获取任务列表
用 AskUserQuestion（单选，每个任务标题作为 option）让用户选择任务
在对话中问用户"请输入新的备注内容"，等用户回复。不要用 AskUserQuestion。
执行：
node ${CLAUDE_SKILL_DIR}/scripts/tb-api.mjs update-task-note --taskId <ID> --note "<备注>"

更新 .teambition.md 最近任务记录
Weekly Installs
9
Repository
kaelzhang321/te…-toolkit
First Seen
Apr 11, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass