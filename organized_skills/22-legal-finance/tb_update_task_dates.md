---
rating: ⭐⭐
title: tb-update-task-dates
url: https://skills.sh/kaelzhang321/teambition-agent-toolkit/tb-update-task-dates
---

# tb-update-task-dates

skills/kaelzhang321/teambition-agent-toolkit/tb-update-task-dates
tb-update-task-dates
Installation
$ npx skills add https://github.com/kaelzhang321/teambition-agent-toolkit --skill tb-update-task-dates
SKILL.md
设置任务日期
执行步骤
读取 .teambition.md 常用项目和最近任务
用 AskUserQuestion（单选）让用户选择项目
获取任务列表，用 AskUserQuestion（单选）让用户选择任务
用 AskUserQuestion（单选）设置截止日期，option：不设置 / 今天 / 明天 / 本周五 / 下周五
用 AskUserQuestion（单选）询问是否设置开始日期，option：不设置 / 今天
如果用户选的是快捷选项，自动转换为 ISO 格式（UTC+8）；如果需要自定义日期，在对话中询问
执行：
node ${CLAUDE_SKILL_DIR}/scripts/tb-api.mjs update-task-dates --taskId <ID> --dueDate <ISO> [--startDate <ISO>]

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