---
title: opc-architecture
url: https://skills.sh/parcadei/continuous-claude-v3/opc-architecture
---

# opc-architecture

skills/parcadei/continuous-claude-v3/opc-architecture
opc-architecture
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill opc-architecture
SKILL.md
OPC Architecture Understanding

OPC (Orchestrated Parallel Claude) extends Claude Code - it does NOT replace it.

Core Concept

Claude Code CLI is the execution engine. OPC adds orchestration via:

Hooks - Intercept Claude Code events (PreToolUse, PostToolUse, SessionStart, etc.)
Skills - Load prompts into Claude Code
Scripts - Called by hooks/skills for coordination
Database - Store state between Claude Code instances
How Agents Work

When you spawn an agent:

Main Claude Code instance (your terminal) runs hook on Task tool
Hook calls subprocess.Popen(["claude", "-p", "prompt"])
A NEW Claude Code instance spawns as child process
Child runs independently, reads/writes to coordination DB
Parent tracks child via PID in DB
$ claude                         ← Main Claude Code (your terminal)
    ↓ Task tool triggers hook
    ↓ subprocess.Popen(["claude", "-p", "..."])
        ├── claude -p "research..."   ← Child agent 1
        ├── claude -p "implement..."  ← Child agent 2
        └── claude -p "test..."       ← Child agent 3

What OPC Is NOT
OPC is NOT a separate application
OPC does NOT run without Claude Code
OPC does NOT intercept Claude API calls directly
OPC does NOT modify Claude Code's internal behavior
What OPC IS
OPC IS hooks that Claude Code loads from .claude/hooks/
OPC IS skills that Claude Code loads from .claude/skills/
OPC IS scripts that hooks/skills call for coordination
OPC IS a database backend for state across Claude Code instances
Key Files
.claude/
├── hooks/           ← TypeScript hooks that Claude Code runs
├── skills/          ← SKILL.md prompts that Claude Code loads
├── settings.json    ← Hook registration, Claude Code reads this
└── cache/           ← State files, agent outputs

opc/
├── scripts/         ← Python scripts called by hooks
├── docker-compose.yml ← PostgreSQL, Redis, PgBouncer
└── init-db.sql      ← Database schema

Coordination Flow
User runs claude in terminal
Claude Code loads hooks from .claude/settings.json
User says "spawn a research agent"
Claude uses Task tool
PreToolUse hook fires, checks resources
Hook spawns claude -p "research..." as subprocess
Hook stores PID in PostgreSQL
Child agent runs, writes output to .claude/cache/agents/<id>/
Child completes, broadcasts "done" to PostgreSQL
Parent checks DB, reads child's output file
Remember
Every "agent" is just another claude -p process
Hooks intercept events, they don't create new functionality
All coordination happens via files and PostgreSQL
Claude Code is always the execution engine
Weekly Installs
303
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass