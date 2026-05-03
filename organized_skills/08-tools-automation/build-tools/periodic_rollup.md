---
rating: ⭐⭐
title: periodic-rollup
url: https://skills.sh/nweii/agent-stuff/periodic-rollup
---

# periodic-rollup

skills/nweii/agent-stuff/periodic-rollup
periodic-rollup
Installation
$ npx skills add https://github.com/nweii/agent-stuff --skill periodic-rollup
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Vault rollups

Today's daily note: !obsidian daily:path

Two operations for aggregating periodic note content into consolidated artifacts. Determine which to run based on what's asked:

Operation	When to use	Reference
History rollup	"Roll up history for [[Project]]", "compile mentions of [[Topic]]"	references/history-rollup.md
Periodic rollup	"Roll up my weekly", "summarize this quarter", "generate description for [[2026-W07]]"	references/periodic-rollup.md

If $ARGUMENTS is provided, use it to identify the project, topic, or periodic note to target. If ambiguous between the two operations, ask before proceeding.

Shared workflow

Both operations follow the same pattern:

Gather — Search for source notes using obsidian CLI or MCP vault search
Synthesize — Process gathered content according to the operation's rules
Write — Produce or update the output note
Shared principles
Preserve source wikilinks back to origin notes for traceability
Respect the hierarchy: daily → weekly → quarterly → yearly
Preserve detail in archives; don't summarize what should be kept verbatim
Update related properties bidirectionally when creating new notes
Weekly Installs
14
Repository
nweii/agent-stuff
GitHub Stars
2
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass