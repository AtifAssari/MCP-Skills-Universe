---
rating: ⭐⭐⭐
title: tensorpm-agentic-pm
url: https://skills.sh/neo552/tensorpm-releases/tensorpm-agentic-pm
---

# tensorpm-agentic-pm

skills/neo552/tensorpm-releases/tensorpm-agentic-pm
tensorpm-agentic-pm
Installation
$ npx skills add https://github.com/neo552/tensorpm-releases --skill tensorpm-agentic-pm
SKILL.md
TensorPM Skill

Use this skill for AI-powered, context-driven project management inside a running TensorPM desktop app. TensorPM itself is free. For AI capabilities outside MCP (A2A), use your own API key (BYOK) or create an account.

When To Use
You need to list, create, or update TensorPM projects or action items.
You need to switch/list workspaces.
You need to set AI provider keys through TensorPM (set_api_key).
You need conversational project-level changes via A2A (message/send).
When Not To Use
The request is only about website/account/billing pages.
Installation (Agent CLI)

Use one of these agent-friendly CLI install methods:

# macOS
brew install --cask neo552/tensorpm/tensorpm

# Windows (PowerShell)
winget install --id Neo552.TensorPM --exact --accept-package-agreements --accept-source-agreements

# macOS / Linux fallback installer script
curl -fsSL https://raw.githubusercontent.com/Neo552/TensorPM/main/scripts/install.sh | bash

# Windows fallback installer script
irm https://raw.githubusercontent.com/Neo552/TensorPM/main/scripts/install.ps1 | iex

Runtime Prerequisites
Start TensorPM desktop app.
For MCP usage with external AI clients: ensure client integration is installed once (via Settings -> Integrations or A2A POST /integrations/mcp/install).
For A2A usage: verify local endpoint http://localhost:37850.
MCP vs A2A Routing
Task	Use	Why
Structured action-item CRUD	MCP tools	Direct typed operations
Set provider API keys	MCP set_api_key	Dedicated secure write-only tool
Project-wide/contextual changes	A2A message/send	Managed by project manager agent
HTTP-based automation/client integration	A2A REST/JSON-RPC	Endpoint-first integration path
Multi-turn planning with conversation state	A2A with contextId	Native conversation continuity

Rule of thumb:

Prefer MCP for explicit CRUD operations.
Prefer A2A for high-level intent and context-aware planning.
Minimal Workflow
Verify TensorPM is running.
Choose MCP vs A2A via the routing table above.
Execute operation.
Read back result (list_*, get_project, or A2A read endpoint) to confirm state.
Summarize applied changes and any follow-up action.
References
MCP Tools: tool catalog and usage boundaries.
A2A API: discovery, JSON-RPC methods, REST endpoints, examples.
Action Items & Dependencies: fields, dependency types, payload examples.
Notes
IDs are UUIDs.
Dates use ISO format (YYYY-MM-DD).
propose_updates requires human approval before apply.
MCP and A2A operate on the same local TensorPM data.
Release notes: https://github.com/Neo552/TensorPM-Releases/releases/latest
Weekly Installs
21
Repository
neo552/tensorpm-releases
GitHub Stars
2
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail