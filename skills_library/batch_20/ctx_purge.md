---
title: ctx-purge
url: https://skills.sh/mksglu/context-mode/ctx-purge
---

# ctx-purge

skills/mksglu/context-mode/ctx-purge
ctx-purge
Installation
$ npx skills add https://github.com/mksglu/context-mode --skill ctx-purge
SKILL.md
Context Mode Purge

Permanently deletes ALL session data for this project: knowledge base, session events, analytics, and stats.

Instructions
Warn the user: This is irreversible. Everything will be deleted:
FTS5 knowledge base (all indexed content from ctx_index, ctx_fetch_and_index, ctx_batch_execute)
Session events DB (analytics, metadata, resume snapshots)
Session events markdown file
In-memory session stats
Call the mcp__context-mode__ctx_purge MCP tool with confirm: true.
Report the result to the user — the response lists exactly what was deleted.
When to Use
When the KB contains stale or incorrect content polluting search results.
When switching between unrelated projects in the same session.
When you want a completely fresh start for this project.
Important
ctx_purge is the only way to delete session data. No other mechanism exists.
ctx_stats is read-only — shows statistics only.
/clear and /compact do NOT affect any context-mode data.
There is no undo. Re-index content if you need it again.
Weekly Installs
107
Repository
mksglu/context-mode
GitHub Stars
11.9K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass