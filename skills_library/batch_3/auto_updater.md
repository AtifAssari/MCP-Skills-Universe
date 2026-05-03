---
title: auto-updater
url: https://skills.sh/teylersf/openclaw-auto-updater/auto-updater
---

# auto-updater

skills/teylersf/openclaw-auto-updater/auto-updater
auto-updater
Installation
$ npx skills add https://github.com/teylersf/openclaw-auto-updater --skill auto-updater
SKILL.md
Auto-Updater Skill

This skill keeps OpenClaw updated by running a nightly cron job that executes an external shell script — so the update works even when the gateway restarts.

Quick Setup

To enable auto-updates, say "set up auto-updater" and I'll:

Copy the update script to your home folder
Create a cron job that runs the script at 4 AM daily
Why a Script?

The agent can't run commands while the gateway is restarting. We use a standalone shell script that runs independently of the agent.

The Update Script
#!/bin/bash
# OpenClaw Auto-Updater

openclaw gateway stop
openclaw update.run
openclaw gateway start

Change Update Time

Tell me "change update time to [time]" and I'll update the cron schedule.

Manual Update

Say "update yourself now" and I'll run the script immediately.

Troubleshooting

Check the log file: ~/openclaw-update.log

Weekly Installs
803
Repository
teylersf/opencl…-updater
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn