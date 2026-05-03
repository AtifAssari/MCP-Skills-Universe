---
title: save-thread
url: https://skills.sh/nowledge-co/community/save-thread
---

# save-thread

skills/nowledge-co/community/save-thread
save-thread
Installation
$ npx skills add https://github.com/nowledge-co/community --skill save-thread
Summary

Deprecated compatibility skill for resumable handoffs in generic skill environments, not real thread capture.

Kept for backward compatibility only; use save-handoff instead for generic npx skills environments
Cannot promise lossless thread import in runtimes without stable transcript APIs or session file access
Creates a structured resumable handoff summary (goal, decisions, files, risks, next steps) rather than a full session capture
Real thread save with actual transcript import is only feasible through native integrations like Gemini CLI or Claude Code
SKILL.md
Save Thread
When to Save

Only when user explicitly says: "Save this session" | "Checkpoint this" | "Record conversation"

Never auto-save or suggest.

Tool Usage

Use nmem t save to automatically import the current Claude Code session:

# Save current session for current project
nmem t save --from claude-code

# Save with custom summary
nmem t save --from claude-code -s "Brief summary of what was accomplished"

# Save all sessions for current project
nmem t save --from claude-code -m all

# Save for specific project path
nmem t save --from claude-code -p /path/to/project


Options:

--from: Source app (claude-code for Claude Code)
-s, --summary: Optional brief summary (recommended)
-m, --mode: current (default, latest session) or all (all sessions)
-p, --project: Project directory path (defaults to current directory)
--truncate: Truncate large tool results (>10KB)

Behavior:

Auto-detects sessions from ~/.claude/projects/
Idempotent: Re-running appends only new messages
Thread ID: Auto-generated as claude-code-{session_id}
Thread vs Memory

Thread = real session messages | Memory = distilled insights (different purposes, can do both)

Response
✓ Thread saved
Summary: {summary}
Messages: {count}
Thread ID: claude-code-{session_id}

Troubleshooting

If nmem is not in PATH: pip install nmem-cli

For remote servers: run nmem config client set url https://... and nmem config client set api-key ... once on this machine.

Run /status to check server connection.

Weekly Installs
506
Repository
nowledge-co/community
GitHub Stars
73
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass