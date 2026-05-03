---
title: agent-observability
url: https://skills.sh/zpankz/mcp-skillset/agent-observability
---

# agent-observability

skills/zpankz/mcp-skillset/agent-observability
agent-observability
Installation
$ npx skills add https://github.com/zpankz/mcp-skillset --skill agent-observability
SKILL.md
Agent Observability Skill
Prerequisites
Bun runtime installed
Claude Code with hooks configured
PAI_DIR environment variable set
Installation

See SETUP.md for complete installation instructions.

Quick Setup:

# 1. Set environment variable
export PAI_DIR="$HOME/.claude"  # Add to ~/.zshrc or ~/.bashrc

# 2. Configure hooks (merge into ~/.claude/settings.json)
cat settings.json.example

# 3. Create directory structure
mkdir -p ~/.claude/history/raw-outputs

# 4. Install dependencies
cd apps/server && bun install
cd ../client && bun install

Usage
Start the Observability Dashboard

Terminal 1 - Server:

cd ~/Projects/PAI/skills/agent-observability/apps/server
bun run dev


Terminal 2 - Client:

cd ~/Projects/PAI/skills/agent-observability/apps/client
bun run dev


Open browser: http://localhost:5173

Using Claude Code

Once the dashboard is running, any Claude Code activity will appear in real-time:

Open Claude Code
Use any tool (Read, Write, Bash, etc.)
Launch subagents with Task tool
Watch events appear in the dashboard
Event Types Captured
SessionStart - New Claude Code session begins
UserPromptSubmit - User sends a message
PreToolUse - Before a tool is executed
PostToolUse - After a tool completes
Stop - Main agent task completes
SubagentStop - Subagent task completes
SessionEnd - Session ends
Features
Real-Time Visualization
Agent Swim Lanes: See multiple agents (kai, designer, engineer, etc.) running in parallel
Event Timeline: Chronological view of all events
Tool Usage Charts: Visualize which tools are being used most
Session Tracking: Track individual sessions and their lifecycles
Filtering & Search
Filter by agent name (kai, designer, engineer, pentester, etc.)
Filter by event type (PreToolUse, PostToolUse, etc.)
Filter by session ID
Search event payloads
Data Storage

Events are stored in JSONL (JSON Lines) format:

~/.claude/history/raw-outputs/YYYY-MM/YYYY-MM-DD_all-events.jsonl


Each line is a complete JSON object:

{"source_app":"kai","session_id":"abc123","hook_event_type":"PreToolUse","payload":{...},"timestamp":1234567890,"timestamp_pst":"2025-01-28 14:30:00 PST"}

In-Memory Streaming
Server keeps last 1000 events in memory
Low memory footprint
Fast real-time updates via WebSocket
No database overhead
Architecture
┌─────────────────┐
│  Claude Code    │  Executes hooks on events
│   (with hooks)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ capture-all-    │  Appends events to JSONL
│ events.ts hook  │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ ~/.claude/history/raw-outputs/      │  Daily JSONL files
│ 2025-01/2025-01-28_all-events.jsonl │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────┐
│ file-ingest.ts  │  Watches files, streams to memory
│  (Bun server)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Vue 3 Client   │  Real-time dashboard visualization
│  (Vite + Tail)  │
└─────────────────┘

Configuration
Environment Variables

PAI_DIR: Path to your PAI directory (defaults to ~/.claude/)

export PAI_DIR="/Users/yourname/.claude"

Hooks Configuration

Add to ~/.claude/settings.json (see settings.json.example for full template):

{
  "hooks": {
    "PreToolUse": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "${PAI_DIR}/skills/agent-observability/hooks/capture-all-events.ts --event-type PreToolUse"
      }]
    }],
    // ... other hooks
  }
}

Troubleshooting
No events appearing
Check PAI_DIR is set: echo $PAI_DIR
Verify directory exists: ls ~/.claude/history/raw-outputs/
Check hook is executable: ls -l hooks/capture-all-events.ts
Look for today's events file: ls ~/.claude/history/raw-outputs/$(date +%Y-%m)/
Server won't start
Check Bun is installed: bun --version
Verify dependencies: cd apps/server && bun install
Check port 3001 isn't in use: lsof -i :3001
Client won't connect
Ensure server is running first
Check WebSocket connection in browser console
Verify no firewall blocking localhost:3001
Credits

Inspired by @indydevdan's pioneering work on multi-agent observability for Claude Code.

Our implementation differs by using filesystem-based event capture and in-memory streaming instead of SQLite database persistence. Both approaches have their merits! Check out indydevdan's work for a database-backed solution with full historical persistence.

Development
Running in Development
# Server (hot reload)
cd apps/server
bun --watch src/index.ts

# Client (Vite dev server)
cd apps/client
bun run dev

Building for Production
# Client build
cd apps/client
bun run build
bun run preview

Adding New Event Types
Update capture-all-events.ts hook if needed
Add hook configuration to settings.json
Client will automatically display new event types
Documentation
README.md - Complete documentation
SETUP.md - Installation guide
history-structure/ - Data storage structure
settings.json.example - Hook configuration template
License

Part of the PAI (Personal AI Infrastructure) project.

Contributing

Contributions welcome! Areas for improvement:

Historical data persistence options
Export functionality (CSV, JSON)
Alert/notification system
Advanced filtering and search
Session replay capability
Integration with other PAI skills
Weekly Installs
10
Repository
zpankz/mcp-skillset
GitHub Stars
2
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass