---
title: mcp-codacy
url: https://skills.sh/7spade/black-tortoise/mcp-codacy
---

# mcp-codacy

skills/7spade/black-tortoise/mcp-codacy
mcp-codacy
Installation
$ npx skills add https://github.com/7spade/black-tortoise --skill mcp-codacy
SKILL.md
MCP Skill: Codacy
Scope

Use the MCP server configured as codacy in .vscode/mcp.json to pull static analysis findings and prioritize fixes that reduce risk without adding unnecessary abstraction.

Preconditions
Ensure .vscode/mcp.json contains a server entry named codacy.
Ensure the CODACY_ACCOUNT_TOKEN input is available (the VS Code MCP input prompt will request it).
Operating Rules
Treat findings as a prioritization signal, not an excuse to refactor broadly.
Fix issues at the source with minimal changes; do not suppress unless explicitly approved.
Align with existing gates: ESLint, TypeScript type-check, dependency/architecture gate.
Typical Workflows
Focused scan for touched files
Query findings for files changed in the current task.
Prioritized remediation
Address correctness/security first, then maintainability.
Evidence for PR
Summarize top findings and which commits/changes resolved them.
Prompt Templates
"Run Codacy analysis and list the top issues in . Propose minimal fixes that preserve DDD boundaries."
"Given these Codacy findings: , group by severity and map to concrete code edits."
Weekly Installs
9
Repository
7spade/black-tortoise
First Seen
Feb 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass