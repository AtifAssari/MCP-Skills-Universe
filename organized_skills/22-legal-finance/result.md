---
rating: ⭐⭐
title: result
url: https://skills.sh/parallel-web/parallel-agent-skills/result
---

# result

skills/parallel-web/parallel-agent-skills/result
result
Installation
$ npx skills add https://github.com/parallel-web/parallel-agent-skills --skill result
Summary

Retrieve completed research task results using a run ID.

Polls research task status and returns results in JSON format via the parallel-cli tool
Requires a valid run ID as input; displays setup instructions if the CLI is not installed
Presents output in a clear, organized format for easy consumption
SKILL.md
Get Research Result
Run ID: $ARGUMENTS
parallel-cli research poll "$ARGUMENTS" --json


Present results in a clear, organized format.

If CLI not found, tell user to run /parallel:setup.

Weekly Installs
998
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