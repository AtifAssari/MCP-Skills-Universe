---
title: design-mcp-workflow
url: https://skills.sh/anthropics/knowledge-work-plugins/design-mcp-workflow
---

# design-mcp-workflow

skills/anthropics/knowledge-work-plugins/design-mcp-workflow
design-mcp-workflow
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill design-mcp-workflow
SKILL.md
Design MCP Workflow

Use this skill when the user wants Claude or another MCP-capable client to interact with Zoom via tool calls instead of only deterministic API code.

Covers
MCP fit assessment
REST API vs MCP boundaries
Hybrid architectures
Connector expectations
Whiteboard-specific MCP routing
Workflow
Decide whether the problem is agentic tooling, deterministic automation, or both.
Route MCP-only tasks to zoom-mcp.
Route hybrid tasks to both zoom-mcp and rest-api.
If Whiteboard is central, route to zoom-mcp/whiteboard.
Call out transport, auth, and client capability assumptions explicitly.
Common Mistakes
Using MCP for deterministic backend jobs that should stay in REST
Treating MCP as a replacement for all API design
Ignoring client transport support and auth requirements
Weekly Installs
312
Repository
anthropics/know…-plugins
GitHub Stars
11.7K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass