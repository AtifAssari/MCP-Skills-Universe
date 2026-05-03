---
title: delayed-command
url: https://skills.sh/paulrberg/agent-skills/delayed-command
---

# delayed-command

skills/paulrberg/agent-skills/delayed-command
delayed-command
Installation
$ npx skills add https://github.com/paulrberg/agent-skills --skill delayed-command
SKILL.md
Delayed Command Execution

Wait for a specified duration, then execute a Bash command.

Arguments
duration: Time to wait before execution (e.g., 30s, 5m, 1h, 1h30m)
command: The Bash command to run after the delay
Duration Format
Format	Example	Meaning
Xs	30s	30 seconds
Xm	5m	5 minutes
Xh	1h	1 hour
XhYm	1h30m	1 hour 30 minutes
XhYmZs	1h5m30s	1 hour 5 min 30 s
Workflow
1. Parse Duration

Convert the duration argument to seconds:

Extract hours (h), minutes (m), and seconds (s) components
Calculate total seconds: hours * 3600 + minutes * 60 + seconds

Parsing logic:

duration="$1"
seconds=0

# Extract hours
if [[ $duration =~ ([0-9]+)h ]]; then
  seconds=$((seconds + ${BASH_REMATCH[1]} * 3600))
fi

# Extract minutes
if [[ $duration =~ ([0-9]+)m ]]; then
  seconds=$((seconds + ${BASH_REMATCH[1]} * 60))
fi

# Extract seconds
if [[ $duration =~ ([0-9]+)s ]]; then
  seconds=$((seconds + ${BASH_REMATCH[1]}))
fi

2. Execute with Delay

For durations up to 10 minutes (600 seconds):

Run synchronously using the Bash tool with appropriate timeout:

sleep <seconds> && <command>


Set the Bash tool's timeout parameter to at least (seconds + 60) * 1000 milliseconds.

For durations over 10 minutes:

Run in background using run_in_background: true:

sleep <seconds> && <command>


Inform the user the command is running in background and provide the task ID for checking status.

3. Report Result

After execution completes:

Display command output
Report exit status
Note total elapsed time
Examples
Short Delay (Synchronous)

User: /delayed-command 5m npm test

Parse: 5 minutes = 300 seconds
Execute: sleep 300 && npm test (timeout: 360000ms)
Report test results
Long Delay (Background)

User: /delayed-command 1h git commit -m "auto-commit"

Parse: 1 hour = 3600 seconds
Execute in background: sleep 3600 && git commit -m "auto-commit"
Return task ID for status checking
Combined Duration

User: /delayed-command 1h30m ./deploy.sh

Parse: 1h30m = 5400 seconds
Execute in background (>600s): sleep 5400 && ./deploy.sh
Inform user of background task
Error Handling
Error	Response
Invalid duration format	Show supported formats and examples
Missing command argument	Prompt for the command to execute
Command not found	Report error after delay completes
Duration exceeds 24h	Warn user and suggest alternative (cron, at)
Weekly Installs
132
Repository
paulrberg/agent-skills
GitHub Stars
51
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail