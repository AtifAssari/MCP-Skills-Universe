---
rating: ⭐⭐
title: context-status
url: https://skills.sh/pedrohcgs/claude-code-my-workflow/context-status
---

# context-status

skills/pedrohcgs/claude-code-my-workflow/context-status
context-status
Installation
$ npx skills add https://github.com/pedrohcgs/claude-code-my-workflow --skill context-status
SKILL.md
/context-status — Check Session Health

Show the current session status including context usage estimate, active plan, and preservation state.

What This Skill Shows
Context usage estimate — Approximate % of context window used
Active plan — Current plan file and status
Session log — Most recent session log
Preservation state — What will survive compaction
Workflow
Step 1: Check Context Monitor Cache

Read the context monitor cache to get the current estimate:

cat ~/.claude/sessions/*/context-monitor-cache.json 2>/dev/null | head -20

Step 2: Find Active Plan
ls -lt quality_reports/plans/*.md 2>/dev/null | head -3

Step 3: Find Session Log
ls -lt quality_reports/session_logs/*.md 2>/dev/null | head -1

Step 4: Report Status

Format the output:

📊 Session Status
─────────────────────────────────
Context Usage:  ~XX% (estimated)
Auto-compact:   [approaching | not imminent]

📋 Active Plan
File:   quality_reports/plans/YYYY-MM-DD_description.md
Status: [draft | approved | in_progress | completed]
Task:   [current unchecked task or "none"]

📝 Session Log
File:   quality_reports/session_logs/YYYY-MM-DD_description.md

✓ Preservation Check
  • Pre-compact hook: [configured | missing]
  • Post-compact restore: [configured | missing]
  • Session state will be saved before compaction

Notes
Context % is an estimate based on tool call count
Actual compaction is triggered by Claude Code automatically
All important state is saved to disk (plans, logs, MEMORY.md)
Weekly Installs
18
Repository
pedrohcgs/claud…workflow
GitHub Stars
1.0K
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass