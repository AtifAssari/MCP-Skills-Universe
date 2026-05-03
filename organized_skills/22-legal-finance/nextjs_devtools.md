---
rating: ⭐⭐⭐
title: nextjs-devtools
url: https://skills.sh/bilalmk/todo_correct/nextjs-devtools
---

# nextjs-devtools

skills/bilalmk/todo_correct/nextjs-devtools
nextjs-devtools
Installation
$ npx skills add https://github.com/bilalmk/todo_correct --skill nextjs-devtools
SKILL.md
Next.js DevTools

Inspect and debug Next.js applications via MCP server.

Quick Start
# Start server (spawns on-demand)
bash scripts/start-server.sh

# Or use directly via mcp-client
python3 scripts/mcp-client.py call \
  -s "npx next-devtools-mcp@latest" \
  -t list-routes

Available Tools
Tool	Description
list-routes	Get all app routes
get-route-info	Details for specific route
list-components	React components in app
get-build-info	Build configuration
get-config	next.config.js settings
Workflow Patterns
Pattern 1: Route Inspection
# List all routes
python3 scripts/mcp-client.py call \
  -s "npx next-devtools-mcp@latest" \
  -t list-routes

# Get specific route details
python3 scripts/mcp-client.py call \
  -s "npx next-devtools-mcp@latest" \
  -t get-route-info \
  -p '{"route": "/api/auth"}'

Pattern 2: Debug Build Issues
# Check build config
python3 scripts/mcp-client.py call \
  -s "npx next-devtools-mcp@latest" \
  -t get-build-info

# Check next.config.js
python3 scripts/mcp-client.py call \
  -s "npx next-devtools-mcp@latest" \
  -t get-config

Pattern 3: Component Discovery
python3 scripts/mcp-client.py call \
  -s "npx next-devtools-mcp@latest" \
  -t list-components

Scripts
start-server.sh

For persistent server (multiple calls):

bash scripts/start-server.sh
# Server runs on default port
# Use mcp-client.py with -u flag instead of -s

On-Demand (Recommended)

For single calls, use -s flag which spawns server per-call:

python3 scripts/mcp-client.py call \
  -s "npx next-devtools-mcp@latest" \
  -t <tool-name>

Troubleshooting
Issue	Solution
Server not starting	Check npx next-devtools-mcp@latest works manually
No routes found	Ensure running from Next.js project root
Build info empty	Run next build first
Weekly Installs
18
Repository
bilalmk/todo_correct
GitHub Stars
1
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykPass