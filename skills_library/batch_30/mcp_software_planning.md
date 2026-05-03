---
title: mcp-software-planning
url: https://skills.sh/7spade/black-tortoise/mcp-software-planning
---

# mcp-software-planning

skills/7spade/black-tortoise/mcp-software-planning
mcp-software-planning
Installation
$ npx skills add https://github.com/7spade/black-tortoise --skill mcp-software-planning
SKILL.md
MCP Skill: Software Planning
Scope

Use the MCP server configured as Software-planning-mcp in .vscode/mcp.json to produce planning artifacts that align with Black-Tortoise governance (DDD boundaries, append-before-publish, minimalism).

Preconditions
Ensure .vscode/mcp.json contains a server entry named Software-planning-mcp.
Planning output must be compatible with the repo workflow (requirements/design/tasks + audit notes when needed).
Operating Rules
Keep plans minimal and verifiable (Occam's Razor): only create artifacts that will be used.
Tie every plan step to a concrete file/command in this repo (e.g., pnpm run architecture:gate).
Do not invent APIs or layers; follow existing module boundaries.
Typical Workflows
Requirements drafting
Input: feature goal, constraints, affected bounded context/capability.
Output: acceptance criteria + non-functional constraints.
Design outline
Input: existing module location + eventing/state constraints.
Output: dependency direction, events, store changes, UI signals, persistence.
Task breakdown
Output: ordered tasks with explicit validation steps (lint/build/gate/tests).
Prompt Templates
"Create a requirements.md and tasks.md plan for: . Constraints: Angular 20 zoneless, signals-first, event-first flow, DDD boundaries. List files to touch and commands to run."
"Draft a design.md for capability using append-before-publish, include event schema and causality IDs. Keep it minimal."
Validation Checklist
Architecture direction preserved (Presentation -> Application -> Domain; Infrastructure implements ports).
Append -> Publish -> React ordering explicit.
Testing/gates listed when the change touches architecture, eventing, or integration.
Weekly Installs
8
Repository
7spade/black-tortoise
First Seen
Feb 1, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass