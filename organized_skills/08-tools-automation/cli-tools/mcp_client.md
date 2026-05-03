---
rating: ⭐⭐⭐
title: mcp-client
url: https://skills.sh/coleam00/second-brain-skills/mcp-client
---

# mcp-client

skills/coleam00/second-brain-skills/mcp-client
mcp-client
Installation
$ npx skills add https://github.com/coleam00/second-brain-skills --skill mcp-client
SKILL.md
Universal MCP Client

Connect to any MCP server with progressive disclosure - load tool schemas on-demand instead of dumping thousands of tokens into context upfront.

Skill Location

This skill is located at: .claude/skills/mcp-client/

Script path: .claude/skills/mcp-client/scripts/mcp_client.py

Configuration

The script looks for config in this order:

MCP_CONFIG_PATH env var (custom path)
references/mcp-config.json (this skill's config - recommended)
.mcp.json in project root
~/.claude.json

Your config file: .claude/skills/mcp-client/references/mcp-config.json

Edit this file to add your API keys. The example file (example-mcp-config.json) is kept as a reference template.

If the user hasn't provided their Zapier API key yet, ask them for it.

Running Commands

All commands use the script at .claude/skills/mcp-client/scripts/mcp_client.py:

# List configured servers
python .claude/skills/mcp-client/scripts/mcp_client.py servers

# List tools from a server
python .claude/skills/mcp-client/scripts/mcp_client.py tools <server_name>

# Call a tool
python .claude/skills/mcp-client/scripts/mcp_client.py call <server> <tool> '{"arg": "value"}'

Workflow
Check config exists - Run servers command. If error, create .mcp.json
List servers - See what MCP servers are configured
List tools - Get tool schemas from a specific server
Call tool - Execute a tool with arguments
Commands Reference
Command	Description
servers	List all configured MCP servers
tools <server>	List tools with full parameter schemas
call <server> <tool> '<json>'	Execute a tool with arguments
Example: Zapier
# 1. List servers to confirm Zapier is configured
python .claude/skills/mcp-client/scripts/mcp_client.py servers

# 2. List Zapier tools
python .claude/skills/mcp-client/scripts/mcp_client.py tools zapier

# 3. Call a Zapier tool
python .claude/skills/mcp-client/scripts/mcp_client.py call zapier <tool_name> '{"param": "value"}'

Example: Sequential Thinking
# 1. List tools
python .claude/skills/mcp-client/scripts/mcp_client.py tools sequential-thinking

# 2. Use sequential thinking
python .claude/skills/mcp-client/scripts/mcp_client.py call sequential-thinking sequentialthinking '{"thought": "Breaking down the problem...", "thoughtNumber": 1, "totalThoughts": 5, "nextThoughtNeeded": true}'

Config Format

Config file format (references/mcp-config.json):

{
  "mcpServers": {
    "zapier": {
      "url": "https://mcp.zapier.com/api/v1/connect",
      "api_key": "your-api-key"
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}


Transport detection:

url + api_key → FastMCP with Bearer auth (Zapier)
command + args → stdio (local servers like sequential-thinking)
url ending in /sse → SSE transport
url ending in /mcp → Streamable HTTP
Error Handling

Errors return JSON:

{"error": "message", "type": "configuration|validation|connection"}

configuration - Config file not found. Create .mcp.json
validation - Invalid server or tool name
connection - Failed to connect to server
Dependencies
pip install mcp fastmcp

References
references/example-mcp-config.json - Template config file
references/mcp-servers.md - Common server configurations
references/python-mcp-sdk.md - Python SDK documentation
Weekly Installs
50
Repository
coleam00/second…n-skills
GitHub Stars
706
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn