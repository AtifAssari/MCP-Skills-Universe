---
title: status
url: https://skills.sh/parallel-web/parallel-agent-skills/status
---

# status

skills/parallel-web/parallel-agent-skills/status
status
Installation
$ npx skills add https://github.com/parallel-web/parallel-agent-skills --skill status
Summary

Check the status of a running research task by its run ID.

Queries research task status using the Parallel CLI with JSON output formatting
Requires the Parallel CLI to be installed; directs users to /parallel:setup if unavailable
Accepts a run ID as the sole argument to identify which task to monitor
SKILL.md
Check Research Status
Run ID: $ARGUMENTS
parallel-cli research status "$ARGUMENTS" --json


If CLI not found, tell user to run /parallel:setup.

Weekly Installs
1.0K
Repository
parallel-web/pa…t-skills
GitHub Stars
46
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass