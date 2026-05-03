---
title: grepai-mcp-claude
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-mcp-claude
---

# grepai-mcp-claude

skills/yoanbernabeu/grepai-skills/grepai-mcp-claude
grepai-mcp-claude
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-mcp-claude
SKILL.md
GrepAI MCP Integration with Claude Code

This skill covers integrating GrepAI with Claude Code using the Model Context Protocol (MCP).

When to Use This Skill
Setting up GrepAI in Claude Code
Enabling semantic search for AI coding assistant
Configuring MCP server for Claude
Troubleshooting Claude Code integration
What is MCP?

Model Context Protocol (MCP) allows AI assistants to use external tools. GrepAI provides an MCP server that gives Claude Code:

Semantic code search
Call graph analysis
Index status monitoring
Prerequisites
GrepAI installed
Ollama running (or other embedding provider)
Project indexed (grepai watch)
Claude Code installed
Quick Setup

One command to add GrepAI to Claude Code:

claude mcp add grepai -- grepai mcp-serve


That's it! Claude Code can now use GrepAI tools.

Manual Configuration

If you prefer manual setup, add to Claude Code's MCP config:

Location
macOS/Linux: ~/.claude/mcp.json
Windows: %APPDATA%\Claude\mcp.json
Configuration
{
  "mcpServers": {
    "grepai": {
      "command": "grepai",
      "args": ["mcp-serve"]
    }
  }
}

With Working Directory

If you want GrepAI to always use a specific project:

{
  "mcpServers": {
    "grepai": {
      "command": "grepai",
      "args": ["mcp-serve"],
      "cwd": "/path/to/your/project"
    }
  }
}

Verifying Installation
Check MCP Server
# Start MCP server manually to test
grepai mcp-serve


You should see:

GrepAI MCP Server started
Listening for requests...

In Claude Code

Ask Claude:

"Search the codebase for authentication code"

Claude should use the grepai_search tool.

Available Tools

Once connected, Claude Code has access to these tools:

Tool	Description	Parameters
grepai_search	Semantic code search	query (required), limit, compact
grepai_trace_callers	Find function callers	symbol (required), compact
grepai_trace_callees	Find function callees	symbol (required), compact
grepai_trace_graph	Build call graph	symbol (required), depth
grepai_index_status	Check index health	verbose (optional)
Tool Usage Examples
Semantic Search

Claude request:

"Find code related to user authentication"

Claude uses:

{
  "tool": "grepai_search",
  "parameters": {
    "query": "user authentication",
    "limit": 5,
    "compact": true
  }
}

Trace Analysis

Claude request:

"What functions call the Login function?"

Claude uses:

{
  "tool": "grepai_trace_callers",
  "parameters": {
    "symbol": "Login",
    "compact": true
  }
}

Index Status

Claude request:

"Is the code index up to date?"

Claude uses:

{
  "tool": "grepai_index_status",
  "parameters": {
    "verbose": true
  }
}

Compact Mode

By default, MCP tools return compact JSON to minimize tokens:

{
  "q": "authentication",
  "r": [
    {"s": 0.92, "f": "src/auth/middleware.go", "l": "15-45"},
    {"s": 0.85, "f": "src/auth/jwt.go", "l": "23-55"}
  ],
  "t": 2
}


This reduces token usage by ~80% compared to full content.

Working Directory

The MCP server uses the current working directory. Ensure:

GrepAI is initialized in your project
Index exists (run grepai watch first)
Start Claude Code from your project directory
Option 1: Start Claude from Project Directory
cd /path/to/your/project
claude  # Claude Code now uses this directory

Option 2: Configure CWD in MCP Config
{
  "mcpServers": {
    "grepai": {
      "command": "grepai",
      "args": ["mcp-serve"],
      "cwd": "/path/to/your/project"
    }
  }
}

Multiple Projects

For multiple projects, you can:

Option 1: Multiple MCP Servers
{
  "mcpServers": {
    "grepai-frontend": {
      "command": "grepai",
      "args": ["mcp-serve"],
      "cwd": "/path/to/frontend"
    },
    "grepai-backend": {
      "command": "grepai",
      "args": ["mcp-serve"],
      "cwd": "/path/to/backend"
    }
  }
}

Option 2: Use Workspaces
grepai workspace create my-workspace
grepai workspace add my-workspace /path/to/frontend
grepai workspace add my-workspace /path/to/backend

{
  "mcpServers": {
    "grepai": {
      "command": "grepai",
      "args": ["mcp-serve", "--workspace", "my-workspace"]
    }
  }
}

Troubleshooting
Tool Not Available

❌ Problem: Claude doesn't see GrepAI tools

✅ Solutions:

Restart Claude Code after config changes
Check MCP config syntax (valid JSON)
Verify grepai is in PATH
Test: grepai mcp-serve manually
Search Returns No Results

❌ Problem: Searches return empty

✅ Solutions:

Ensure grepai watch has run
Check working directory has .grepai/
Verify index exists: grepai status
Connection Refused

❌ Problem: MCP server won't start

✅ Solutions:

Check Ollama is running: curl http://localhost:11434/api/tags
Verify config: cat .grepai/config.yaml
Run grepai mcp-serve manually to see errors
Wrong Project Indexed

❌ Problem: Results from wrong codebase

✅ Solutions:

Check cwd in MCP config
Start Claude from correct directory
Verify with grepai_index_status tool
Best Practices
Keep index updated: Run grepai watch --background
Use compact mode: Reduces token usage
Set working directory: Explicit cwd in config
Check status first: Use grepai_index_status
Restart after config: Claude needs restart for MCP changes
Removing Integration

To remove GrepAI from Claude Code:

claude mcp remove grepai


Or manually edit ~/.claude/mcp.json and remove the grepai entry.

Output Format

Successful MCP setup:

✅ GrepAI MCP Integration Configured

   Claude Code: ~/.claude/mcp.json
   Server: grepai mcp-serve
   Status: Connected

   Available tools:
   - grepai_search (semantic code search)
   - grepai_trace_callers (find callers)
   - grepai_trace_callees (find callees)
   - grepai_trace_graph (call graphs)
   - grepai_index_status (index health)

   Claude can now search your code semantically!

Weekly Installs
399
Repository
yoanbernabeu/gr…i-skills
GitHub Stars
16
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass