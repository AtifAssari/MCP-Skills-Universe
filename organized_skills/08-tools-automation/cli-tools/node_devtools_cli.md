---
rating: ⭐⭐⭐
title: node-devtools-cli
url: https://skills.sh/serkan-ozal/browser-devtools-skills/node-devtools-cli
---

# node-devtools-cli

skills/serkan-ozal/browser-devtools-skills/node-devtools-cli
node-devtools-cli
Installation
$ npx skills add https://github.com/serkan-ozal/browser-devtools-skills --skill node-devtools-cli
SKILL.md
Node DevTools CLI

Command-line interface for non-blocking debugging of Node.js backend processes. Connects via the Inspector Protocol (Chrome DevTools Protocol) and provides tracepoints, logpoints, exceptionpoints, and watch expressions without pausing execution.

Installation

Same package as browser-devtools-mcp:

npm install -g browser-devtools-mcp

Quick Start
# 1. Start daemon (if not running)
node-devtools-cli daemon start

# 2. Connect to a Node.js process (by PID)
node-devtools-cli --session-id my-debug debug connect --pid 12345

# 3. Set a tracepoint on server.js line 42
node-devtools-cli --session-id my-debug debug put-tracepoint \
  --url-pattern "server.js" \
  --line-number 42

# 4. Trigger the code path (e.g., make API request to your app)
# 5. Get captured snapshots
node-devtools-cli --session-id my-debug --json debug get-probe-snapshots

Global Options
Option	Description	Default
--port <number>	Daemon server port	2020
--session-id <string>	Session for Node connection persistence	auto
--json	Output as JSON (recommended for AI)	false
--quiet	Suppress log messages	false
--verbose	Enable debug output	false
--timeout <ms>	Operation timeout	30000

AI Agent Recommended:

node-devtools-cli --json --quiet --session-id "debug-session" <command>

Tool Domains
Domain	Description	Reference
debug	Connection, tracepoints, logpoints, exceptionpoints, watch, snapshots	
Connection Methods

Connect via debug connect with one of:

Method	Option	Example
PID	--pid <number>	--pid 12345
Process name	--process-name <pattern>	--process-name "server.js"
Docker container	--container-id or --container-name	--container-name my-api
Inspector port	--inspector-port <number>	--inspector-port 9229
WebSocket URL	--ws-url <url>	--ws-url "ws://127.0.0.1:9229/abc"

If the process doesn't have --inspect active, the CLI activates it via SIGUSR1 (no code changes). For Docker: expose port 9229 and use --inspect=0.0.0.0:9229.

CLI Management Commands
Daemon
node-devtools-cli daemon status
node-devtools-cli daemon start
node-devtools-cli daemon stop
node-devtools-cli daemon restart
node-devtools-cli daemon info

Session
node-devtools-cli session list
node-devtools-cli session info <session-id>
node-devtools-cli session delete <session-id>

Tools
node-devtools-cli tools list
node-devtools-cli tools search <query>
node-devtools-cli tools info <tool-name>

Config & Updates
node-devtools-cli config
node-devtools-cli update --check

Examples
Connect by PID
SESSION="--session-id api-debug"

# Connect
node-devtools-cli $SESSION debug connect --pid $(pgrep -f "node server.js")

# Set tracepoint on route handler
node-devtools-cli $SESSION debug put-tracepoint \
  --url-pattern "routes/api.ts" \
  --line-number 25

# Trigger: curl http://localhost:3000/api/users
# Get snapshots
node-devtools-cli $SESSION --json debug get-probe-snapshots

Connect by Process Name
node-devtools-cli debug connect --process-name "api"

Docker Container
# App runs in container with -p 9229:9229
node-devtools-cli debug connect \
  --container-name my-node-app \
  --host host.docker.internal \
  --inspector-port 9229

Exception Catching
SESSION="--session-id exc-debug"

node-devtools-cli $SESSION debug connect --pid 12345
node-devtools-cli $SESSION debug put-exceptionpoint --state uncaught

# Trigger error in app
# Check snapshots
node-devtools-cli $SESSION --json debug get-probe-snapshots --types exceptionpoint

Interactive Mode
node-devtools-cli interactive

Command	Description
help	Show commands
exit, quit	Exit
debug connect	Connect to process
debug status	Connection status
<domain> <tool>	Execute tool
Shell Completions
eval "$(node-devtools-cli completion bash)"
eval "$(node-devtools-cli completion zsh)"

Weekly Installs
26
Repository
serkan-ozal/bro…s-skills
GitHub Stars
7
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass