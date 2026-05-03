---
title: read-working-memory
url: https://skills.sh/nowledge-co/community/read-working-memory
---

# read-working-memory

skills/nowledge-co/community/read-working-memory
read-working-memory
Installation
$ npx skills add https://github.com/nowledge-co/community --skill read-working-memory
Summary

Daily briefing of active focus areas, priorities, and recent knowledge changes for cross-session continuity.

Load at the beginning of each session to understand current context and recent work across tools
Surfaces active focus areas ranked by recent activity, flagged priorities, and unresolved contradictions or stale information
Works via nmem wm read CLI command for both local and remote knowledge bases, with fallback to local file access
Includes deep links to specific memories for further exploration when context needs expansion
SKILL.md
Read Working Memory

Start every session with context. Your Working Memory is a daily briefing synthesized from your knowledge base.

When to Use

At session start:

Beginning of a new conversation
Returning to a project after a break
When context about recent work would help

During session:

User asks "what am I working on?" or "what's my context?"
User references recent priorities or decisions
Need to understand what's been happening across tools

Skip when:

Already loaded this session
User explicitly wants a fresh start
Working on an isolated, context-independent task
Usage

Read Working Memory via nmem CLI (works for both local and remote):

nmem wm read


If the runtime already knows the current project or agent lane, add --space "<space name>".

Fallback for local-only (when nmem is not installed):

cat ~/ai-now/memory.md


This fallback is only for older local-only Default-space setups.

What You'll Find

The Working Memory briefing contains:

Active Focus Areas — Topics you're currently engaged with, ranked by recent activity
Priorities — Items flagged as important or needing attention
Unresolved Flags — Contradictions, stale information, or items needing verification
Recent Activity — What changed in your knowledge base since the last briefing
Deep Links — References to specific memories for further exploration
How to Use This Context
Read once at session start — don't re-read unless asked
Reference naturally — mention relevant context when it connects to the current task
Don't overwhelm — share only the parts relevant to what the user is working on
Cross-tool continuity — insights saved in other tools (Cursor, Claude Code, Codex) appear here
Troubleshooting

If nmem is not in PATH: pip install nmem-cli or pipx install nmem-cli

If Nowledge Mem is on a remote server, run nmem config client set url https://... and nmem config client set api-key ... once on this machine, or use NMEM_API_URL / NMEM_API_KEY for a temporary override.

Weekly Installs
573
Repository
nowledge-co/community
GitHub Stars
73
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass