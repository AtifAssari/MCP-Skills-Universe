---
title: sweepi
url: https://skills.sh/jjenzz/sweepi/sweepi
---

# sweepi

skills/jjenzz/sweepi/sweepi
sweepi
Installation
$ npx skills add https://github.com/jjenzz/sweepi --skill sweepi
SKILL.md
Sweepi Orchestrator

Parent orchestrates only. Parent does not run Sweepi directly.

Trigger
User asks for sweepi or linting
Parent is preparing to propose a commit
Changed files may violate lint rules
Flow

COLLECT_FILES -> LINT -> RESULT

COLLECT_FILES: determine lint scope (changed files or --all)
LINT: invoke lint sub-agent
RESULT:
BLOCKED: retry with clarified scope or escalate to user with blocker details
CLEAN: report success
Sub-Agent Invocation Contract

Parent prompt to lint sub-agent MUST include:

Load and obey role instructions in <SKILL-ROOT-DIR>/AGENTS.md

And must specify lint scope:

sweepi . --file "<path>" ... for changed files
sweepi . --all when linting everything

Parent MUST NOT load lint instruction files into parent context.

Guardrails
Do not suppress rules or disable linting
Do not make speculative fixes without rule guidance/docs
Return only: CLEAN or BLOCKED with structured blockers
Weekly Installs
78
Repository
jjenzz/sweepi
GitHub Stars
32
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn