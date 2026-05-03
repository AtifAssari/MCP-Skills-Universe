---
rating: ⭐⭐
title: index-at-creation
url: https://skills.sh/parcadei/continuous-claude-v3/index-at-creation
---

# index-at-creation

skills/parcadei/continuous-claude-v3/index-at-creation
index-at-creation
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill index-at-creation
SKILL.md
Index at Creation Time

Index artifacts when they're created, not at batch boundaries.

Pattern

If downstream logic depends on artifacts being queryable, index immediately at write time.

DO
Index handoffs in PostToolUse Write hook (immediately after creation)
Use --file flag for fast single-file indexing
Trigger indexing from the same event that creates the artifact
DON'T
Wait for SessionEnd to batch-index
Rely on cron/scheduled jobs for time-sensitive data
Assume data will be available "soon enough"
Source Sessions
a541f08a: "Index at artifact creation time, not at SessionEnd"
1c21e6c8: "If downstream logic depends on artifacts, index at the moment they're created"
Weekly Installs
297
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass