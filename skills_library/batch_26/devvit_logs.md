---
title: devvit-logs
url: https://skills.sh/reddit/devvit-skills/devvit-logs
---

# devvit-logs

skills/reddit/devvit-skills/devvit-logs
devvit-logs
Installation
$ npx skills add https://github.com/reddit/devvit-skills --skill devvit-logs
SKILL.md
Devvit Logs

Stream log events from an installed Devvit app for quick debugging. This skill wraps devvit logs and auto-exits after a short window (5 seconds) to avoid hanging on a streaming command.

How It Works
Ask the user for the target subreddit (required).
Optionally accept an app name and --since=... flag.
Run devvit logs and capture output.
Exit automatically after the first burst of output or 5 seconds, whichever comes first.
Usage
node ./scripts/devvit-logs.cjs <subreddit> [app-name] [--since=1h]


Script path is relative to this skill's directory.

Arguments:

subreddit - Required. Subreddit to stream logs from.
app-name - Optional. App name if streaming from another folder.
--since=Xd - Optional. Historical logs window (e.g., --since=30m, --since=1d).

Examples:

node ./scripts/devvit-logs.cjs my-subreddit
node ./scripts/devvit-logs.cjs my-subreddit my-app --since=1h

Output
{
  "ok": true,
  "reason": "timeout",
  "exitCode": null,
  "signal": null,
  "stdout": "=============================== streaming logs for my-app on my-subreddit ================================\n[DEBUG] Dec 8 15:55:23 Action called!",
  "stderr": ""
}

Present Results to User
If the user did not provide a subreddit, ask for it explicitly.
Summarize the captured logs (if any) and mention the 5-second capture window.
If no logs were captured, say so and suggest retrying with activity or --since=....
Troubleshooting
Devvit CLI not found: Install or ensure devvit is in PATH.
Not logged in: Run devvit login and try again.
No logs: Trigger an action in the app or use --since=....
Permission errors: Confirm the app is installed in the subreddit and you have access.
Weekly Installs
26
Repository
reddit/devvit-skills
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn