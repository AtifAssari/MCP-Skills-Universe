---
title: diffity-resolve-tree
url: https://skills.sh/kamranahmedse/diffity/diffity-resolve-tree
---

# diffity-resolve-tree

skills/kamranahmedse/diffity/diffity-resolve-tree
diffity-resolve-tree
Installation
$ npx skills add https://github.com/kamranahmedse/diffity --skill diffity-resolve-tree
SKILL.md
Diffity Resolve Tree Skill

You are reading open comments left on repository files via the diffity tree browser and resolving them by making the requested code changes.

Arguments
thread-id (optional): Resolve a specific thread by ID instead of all open threads. Example: /diffity-resolve-tree abc123
CLI Reference
diffity agent list [--status open|resolved|dismissed] [--json]
diffity agent comment --file <path> --line <n> [--end-line <n>] --body "<text>"
diffity agent resolve <id> [--summary "<text>"]
diffity agent dismiss <id> [--reason "<text>"]
diffity agent reply <id> --body "<text>"

--file, --line, --body are required for comment
--end-line defaults to --line (single-line comment)
<id> accepts full UUID or 8-char prefix
Prerequisites
Check that diffity is available: run which diffity. If not found, install it with npm install -g diffity.
Check that a tree session exists: run diffity agent list. If this fails with "No active review session", tell the user to start diffity tree first (e.g. diffity tree).
Instructions
List open comment threads with full details:
diffity agent list --status open --json

If a thread-id argument was provided, filter to just that thread. The JSON output includes the full comment body, file path, line numbers, and side for each thread.
If there are no open threads, tell the user there's nothing to resolve.
For each open thread: a. Skip general comments (filePath __general__) — these are summaries, not actionable code changes. b. Skip threads where the last comment is an agent reply that asks the user a question and the user hasn't responded yet — the agent is waiting for user input. c. [question] comments (from the user) — read the question, examine the relevant code, and reply with an answer:
diffity agent reply <thread-id> --body "Your answer here"

Then resolve the thread with a summary of your answer. d. Comments phrased as questions without an explicit [question] tag (e.g. "should we add X?" or "can we rename this?") are suggestions — treat them as actionable requests and make the change. e. Read the comment body from the JSON output and understand what change is requested. The comment is anchored to a specific file and line range — read the full file to understand context:
If the comment suggests a code change, refactor, or improvement, make the change.
If the comment suggests adding documentation, add or update the relevant docs.
If the comment is genuinely unclear, reply asking for clarification:
diffity agent reply <thread-id> --body "Could you clarify what change you'd like here?"

f. After making the change, resolve the thread with a summary:
diffity agent resolve <thread-id> --summary "Fixed: <brief description of what was changed>"

After resolving all applicable threads, run diffity agent list to confirm status.
Tell the user to check the browser — resolved status will appear within 2 seconds via polling.
Weekly Installs
312
Repository
kamranahmedse/diffity
GitHub Stars
585
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn