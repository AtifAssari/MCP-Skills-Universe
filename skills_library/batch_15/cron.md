---
title: cron
url: https://skills.sh/zhihaoairobotic/clawphd/cron
---

# cron

skills/zhihaoairobotic/clawphd/cron
cron
Installation
$ npx skills add https://github.com/zhihaoairobotic/clawphd --skill cron
SKILL.md
Cron

Use the cron tool to schedule reminders or recurring tasks.

Two Modes
Reminder - message is sent directly to user
Task - message is a task description, agent executes and sends result
Examples

Fixed reminder:

cron(action="add", message="Time to take a break!", every_seconds=1200)


Dynamic task (agent executes each time):

cron(action="add", message="Check ClawPhD/ClawPhD GitHub stars and report", every_seconds=600)


List/remove:

cron(action="list")
cron(action="remove", job_id="abc123")

Time Expressions
User says	Parameters
every 20 minutes	every_seconds: 1200
every hour	every_seconds: 3600
every day at 8am	cron_expr: "0 8 * * *"
weekdays at 5pm	cron_expr: "0 17 * * 1-5"
Weekly Installs
48
Repository
zhihaoairobotic/clawphd
GitHub Stars
151
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass