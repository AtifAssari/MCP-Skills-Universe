---
rating: ⭐⭐⭐
title: mcp-spy
url: https://skills.sh/johnlindquist/claude/mcp-spy
---

# mcp-spy

skills/johnlindquist/claude/mcp-spy
mcp-spy
Installation
$ npx skills add https://github.com/johnlindquist/claude --skill mcp-spy
SKILL.md
MCP Spy - Debug MCP Communication

Debug Model Context Protocol server integrations.

Overview

MCP Spy helps debug:

Message traffic between Claude and MCP servers
Latency issues
Failed requests
Protocol compliance
Traffic Analysis
View Recent Traffic
# Check MCP logs
tail -f ~/.claude/debug/mcp-*.log

# Or specific server
tail -f ~/.claude/debug/mcp-cm.log

Filter by Type
# Tool calls only
grep "tool_use" ~/.claude/debug/mcp-*.log

# Errors only
grep -i "error\|failed" ~/.claude/debug/mcp-*.log

# Specific tool
grep "beads_add" ~/.claude/debug/mcp-*.log

Latency Analysis
Measure Response Times
# Time a specific tool
time claude --print "Run beads_ready" --dangerously-skip-permissions 2>&1 | head -1

Find Slow Calls
# Look for latency warnings in logs
grep -i "timeout\|slow\|latency" ~/.claude/debug/mcp-*.log

Failed Request Analysis
Find Failures
# All errors
grep -i "error" ~/.claude/debug/mcp-*.log

# Parse error responses
grep "\"error\":" ~/.claude/debug/mcp-*.log | jq '.'

Common Issues
Connection refused - Server not running
Timeout - Server too slow
Invalid JSON - Malformed request/response
Unknown tool - Tool not registered
MCP Server Debug
Check Server Status
# Test server connection
curl -X POST http://localhost:3000/mcp/list_tools \
  -H "Content-Type: application/json" \
  -d '{}'

Server Logs
# View server logs (if running as process)
tail -f logs/mcp-server.log

# Or in terminal running server
# Logs appear in stdout

Test Tool Directly
# Call tool directly
curl -X POST http://localhost:3000/mcp/call_tool \
  -H "Content-Type: application/json" \
  -d '{
    "name": "beads_ready",
    "args": {}
  }'

Protocol Debugging
Inspect Messages
# Pretty print JSON messages
grep "message" ~/.claude/debug/mcp-*.log | jq '.'

Validate Requests
# Check request format
gemini -m pro -o text -e "" "Validate this MCP request format:

$(grep "request" ~/.claude/debug/mcp-*.log | tail -1)

Check:
1. Required fields present
2. Types correct
3. Schema compliance"

Troubleshooting Guide
Server Won't Start
# Check if port in use
lsof -i :3000

# Check server process
ps aux | grep mcp

# Start with verbose
node server/index.ts --verbose

Tool Not Found
# List available tools
curl http://localhost:3000/mcp/list_tools | jq '.tools[].name'

# Check tool registration
grep "registerTool\|toolRegistry" server/*.ts

Slow Responses
# Profile tool execution
time curl -X POST http://localhost:3000/mcp/call_tool \
  -H "Content-Type: application/json" \
  -d '{"name": "slow_tool", "args": {}}'

# Check for blocking operations
grep -i "await\|sync" tools/slow_tool/index.ts

JSON Parse Errors
# Find malformed JSON
grep -B 5 "JSON\|parse" ~/.claude/debug/mcp-*.log | grep -i error

# Validate JSON
echo '{"test": ...}' | jq '.'

Monitoring
Watch Traffic Live
# Real-time log monitoring
tail -f ~/.claude/debug/mcp-*.log | grep --line-buffered "tool_use\|result"

Traffic Stats
# Count calls per tool
grep "tool_use" ~/.claude/debug/mcp-*.log | \
  grep -oP '"name":"[^"]*"' | \
  sort | uniq -c | sort -rn

Health Dashboard
#!/bin/bash
# mcp-health.sh

echo "=== MCP Server Health ==="

# Check server
if curl -s http://localhost:3000/health > /dev/null 2>&1; then
  echo "Server: UP"
else
  echo "Server: DOWN"
fi

# Recent errors
ERRORS=$(grep -c "error" ~/.claude/debug/mcp-*.log 2>/dev/null || echo 0)
echo "Recent errors: $ERRORS"

# Tool count
TOOLS=$(curl -s http://localhost:3000/mcp/list_tools 2>/dev/null | jq '.tools | length' || echo 0)
echo "Registered tools: $TOOLS"

Best Practices
Enable logging - Keep debug logs on during development
Check health first - Verify server running before debugging
Test isolation - Test tools directly before through Claude
Monitor latency - Watch for degradation
Log rotation - Don't let logs grow unbounded
Error alerts - Set up monitoring for failures
Weekly Installs
27
Repository
johnlindquist/claude
GitHub Stars
23
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass