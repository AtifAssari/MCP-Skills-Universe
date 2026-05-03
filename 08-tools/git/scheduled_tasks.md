---
title: scheduled-tasks
url: https://skills.sh/cklxx/elephant.ai/scheduled-tasks
---

# scheduled-tasks

skills/cklxx/elephant.ai/scheduled-tasks
scheduled-tasks
Installation
$ npx skills add https://github.com/cklxx/elephant.ai --skill scheduled-tasks
SKILL.md
scheduled-tasks

管理 cron 调度任务：创建、列表、删除。

调用
python3 skills/scheduled-tasks/run.py '{"action":"create","name":"daily-report","cron":"0 9 * * *","command":"echo hello"}'
python3 skills/scheduled-tasks/run.py '{"action":"list"}'
python3 skills/scheduled-tasks/run.py '{"action":"delete","name":"daily-report"}'

Weekly Installs
9
Repository
cklxx/elephant.ai
GitHub Stars
10
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn