---
rating: ⭐⭐
title: autonomous-scheduler
url: https://skills.sh/cklxx/elephant.ai/autonomous-scheduler
---

# autonomous-scheduler

skills/cklxx/elephant.ai/autonomous-scheduler
autonomous-scheduler
Installation
$ npx skills add https://github.com/cklxx/elephant.ai --skill autonomous-scheduler
SKILL.md
autonomous-scheduler

维护自主任务计划：任务 upsert/list/delete、触发窗口查询、运行状态推进。

调用
python3 skills/autonomous-scheduler/run.py '{"action":"upsert","name":"weekly-retro","schedule":"0 18 * * 5","task":"发送复盘提醒"}'
python3 skills/autonomous-scheduler/run.py '{"action":"due","now":"2026-02-13T10:00:00Z"}'

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
SnykPass