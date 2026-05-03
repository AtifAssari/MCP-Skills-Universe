---
title: wiki-history-ingest
url: https://skills.sh/ar9av/obsidian-wiki/wiki-history-ingest
---

# wiki-history-ingest

skills/ar9av/obsidian-wiki/wiki-history-ingest
wiki-history-ingest
Installation
$ npx skills add https://github.com/ar9av/obsidian-wiki --skill wiki-history-ingest
SKILL.md
Unified History Ingest Router

This is a thin router for history sources only. It does not replace wiki-ingest for documents.

Subcommands

If the user invokes /wiki-history-ingest <target> (or equivalent text command), dispatch directly:

Subcommand	Route To
claude	claude-history-ingest
copilot	copilot-history-ingest
codex	codex-history-ingest
hermes	hermes-history-ingest
openclaw	openclaw-history-ingest
auto	infer from context using rules below
Routing Rules
If the user explicitly says claude, copilot, codex, hermes, or openclaw, route directly.
If the user provides a path/source:
~/.claude or Claude memory/session JSONL artifacts -> claude-history-ingest
~/.copilot, session-store.db, VS Code copilot-chat transcripts -> copilot-history-ingest
~/.codex or rollout/session index artifacts -> codex-history-ingest
~/.hermes or Hermes memories/session artifacts -> hermes-history-ingest
~/.openclaw or OpenClaw MEMORY.md/session JSONL artifacts -> openclaw-history-ingest
If ambiguous, ask one short clarification:
"Should I ingest claude, copilot, codex, hermes, or openclaw history?"
Execution Contract
After routing, execute the destination skill's workflow exactly.
Do not duplicate destination logic in this file.
Leave manifest/index/log update semantics to the destination skill.
UX Convention
Use wiki-ingest for documents/content sources
Use wiki-history-ingest for agent history sources

Examples:

/wiki-history-ingest claude
/wiki-history-ingest copilot
/wiki-history-ingest codex
/wiki-history-ingest hermes
/wiki-history-ingest openclaw
$wiki-history-ingest claude (agents that use $skill invocation)
$wiki-history-ingest copilot
Weekly Installs
896
Repository
ar9av/obsidian-wiki
GitHub Stars
893
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass