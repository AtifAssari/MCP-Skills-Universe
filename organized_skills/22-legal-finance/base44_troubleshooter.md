---
rating: ⭐⭐
title: base44-troubleshooter
url: https://skills.sh/base44/skills/base44-troubleshooter
---

# base44-troubleshooter

skills/base44/skills/base44-troubleshooter
base44-troubleshooter
Installation
$ npx skills add https://github.com/base44/skills --skill base44-troubleshooter
Summary

Fetch and analyze backend function logs to diagnose production issues in Base44 apps.

Requires Base44 authentication (npx base44 login) and must run from the project directory containing base44/.app.jsonc
Primary command base44 logs supports filtering by error level, function name, time range, and result limit
Typical workflow: pull recent errors across all functions, drill into a specific function, inspect a time range, then analyze stack traces and timestamps to correlate with user reports
SKILL.md
Troubleshoot Production Issues
Prerequisites

Verify authentication before fetching logs:

npx base44 whoami


If not authenticated or token expired, instruct user to run npx base44 login.

Must be run from the project directory (where base44/.app.jsonc exists):

cat base44/.app.jsonc

Available Commands
Command	Description	Reference
base44 logs	Fetch function logs for this app	project-logs.md
Troubleshooting Flow
1. Check Recent Errors

Start by pulling the latest errors across all functions:

npx base44 logs --level error

2. Drill Into a Specific Function

If you know which function is failing:

npx base44 logs --function <function_name> --level error

3. Inspect a Time Range

Correlate with user-reported issue timestamps:

npx base44 logs --function <function_name> --since <start_time> --until <end_time>

4. Analyze the Logs
Look for stack traces and error messages in the output
Check timestamps to correlate with user-reported issues
Use --limit to fetch more entries if the default 50 isn't enough
Weekly Installs
799
Repository
base44/skills
GitHub Stars
73
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass