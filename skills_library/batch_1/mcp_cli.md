---
title: mcp-cli
url: https://skills.sh/github/awesome-copilot/mcp-cli
---

# mcp-cli

skills/github/awesome-copilot/mcp-cli
mcp-cli
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill mcp-cli
Summary

Command-line interface for discovering and executing MCP server tools and external integrations.

Five core commands cover server discovery, tool exploration, schema inspection, execution, and grep-based searching across all available tools
Supports JSON input/output for scripting, raw text extraction, and description flags for verbose tool documentation
Handles complex JSON arguments via heredoc, stdin piping, or file input to accommodate special characters and multi-line payloads
Distinguishes exit codes by error type: client errors (1), server/tool failures (2), and network issues (3) for reliable error handling in automation
SKILL.md
MCP-CLI

Access MCP servers through the command line. MCP enables interaction with external systems like GitHub, filesystems, databases, and APIs.

Commands
Command	Output
mcp-cli	List all servers and tool names
mcp-cli <server>	Show tools with parameters
mcp-cli <server>/<tool>	Get tool JSON schema
mcp-cli <server>/<tool> '<json>'	Call tool with arguments
mcp-cli grep "<glob>"	Search tools by name

Add -d to include descriptions (e.g., mcp-cli filesystem -d)

Workflow
Discover: mcp-cli → see available servers and tools
Explore: mcp-cli <server> → see tools with parameters
Inspect: mcp-cli <server>/<tool> → get full JSON input schema
Execute: mcp-cli <server>/<tool> '<json>' → run with arguments
Examples
# List all servers and tool names
mcp-cli

# See all tools with parameters
mcp-cli filesystem

# With descriptions (more verbose)
mcp-cli filesystem -d

# Get JSON schema for specific tool
mcp-cli filesystem/read_file

# Call the tool
mcp-cli filesystem/read_file '{"path": "./README.md"}'

# Search for tools
mcp-cli grep "*file*"

# JSON output for parsing
mcp-cli filesystem/read_file '{"path": "./README.md"}' --json

# Complex JSON with quotes (use heredoc or stdin)
mcp-cli server/tool <<EOF
{"content": "Text with 'quotes' inside"}
EOF

# Or pipe from a file/command
cat args.json | mcp-cli server/tool

# Find all TypeScript files and read the first one
mcp-cli filesystem/search_files '{"path": "src/", "pattern": "*.ts"}' --json | jq -r '.content[0].text' | head -1 | xargs -I {} sh -c 'mcp-cli filesystem/read_file "{\"path\": \"{}\"}"'

Options
Flag	Purpose
-j, --json	JSON output for scripting
-r, --raw	Raw text content
-d	Include descriptions
Exit Codes
0: Success
1: Client error (bad args, missing config)
2: Server error (tool failed)
3: Network error
Weekly Installs
9.0K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn