---
title: cron
url: https://skills.sh/hkuds/nanobot/cron
---

# cron

skills/hkuds/nanobot/cron
cron
Installation
$ npx skills add https://github.com/hkuds/nanobot --skill cron
SKILL.md
Cron

Use the cron tool to schedule reminders or recurring tasks.

Three Modes
Reminder - message is sent directly to user
Task - message is a task description, agent executes and sends result
One-time - runs once at a specific time, then auto-deletes
Examples

Fixed reminder:

cron(action="add", message="Time to take a break!", every_seconds=1200)


Dynamic task (agent executes each time):

cron(action="add", message="Check HKUDS/nanobot GitHub stars and report", every_seconds=600)


One-time scheduled task (compute ISO datetime from current time):

cron(action="add", message="Remind me about the meeting", at="<ISO datetime>")


Timezone-aware cron:

cron(action="add", message="Morning standup", cron_expr="0 9 * * 1-5", tz="America/Vancouver")


List/remove:

cron(action="list")
cron(action="remove", job_id="abc123")

Time Expressions
User says	Parameters
every 20 minutes	every_seconds: 1200
every hour	every_seconds: 3600
every day at 8am	cron_expr: "0 8 * * *"
weekdays at 5pm	cron_expr: "0 17 * * 1-5"
9am Vancouver time daily	cron_expr: "0 9 * * *", tz: "America/Vancouver"
at a specific time	at: ISO datetime string (compute from current time)
Timezone

Use tz with cron_expr to schedule in a specific IANA timezone. Without tz, the server's local timezone is used.

Weekly Installs
20
Repository
hkuds/nanobot
GitHub Stars
40.5K
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass