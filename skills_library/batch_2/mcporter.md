---
title: mcporter
url: https://skills.sh/steipete/clawdis/mcporter
---

# mcporter

skills/steipete/clawdis/mcporter
mcporter
Installation
$ npx skills add https://github.com/steipete/clawdis --skill mcporter
Summary

Direct CLI access to MCP servers with tool calling, auth, and code generation.

Call tools across HTTP servers, stdio processes, and ad-hoc endpoints using selector syntax, function calls, or JSON payloads
Manage server configuration, OAuth authentication, and daemon lifecycle from the command line
Generate TypeScript types and CLI wrappers for any MCP server or custom endpoint
Inspect and list available tools with schema details to understand server capabilities before calling
SKILL.md
mcporter

Use mcporter to work with MCP servers directly.

Quick start

mcporter list
mcporter list <server> --schema
mcporter call <server.tool> key=value

Call tools

Selector: mcporter call linear.list_issues team=ENG limit:5
Function syntax: mcporter call "linear.create_issue(title: \"Bug\")"
Full URL: mcporter call https://api.example.com/mcp.fetch url:https://example.com
Stdio: mcporter call --stdio "bun run ./server.ts" scrape url=https://example.com
JSON payload: mcporter call <server.tool> --args '{"limit":5}'

Auth + config

OAuth: mcporter auth <server | url> [--reset]
Config: mcporter config list|get|add|remove|import|login|logout

Daemon

mcporter daemon start|status|stop|restart

Codegen

CLI: mcporter generate-cli --server <name> or --command <url>
Inspect: mcporter inspect-cli <path> [--json]
TS: mcporter emit-ts <server> --mode client|types

Notes

Config default: ./config/mcporter.json (override with --config).
Prefer --output json for machine-readable results.
Weekly Installs
1.7K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn