---
rating: ⭐⭐⭐
title: mcp-hub
url: https://skills.sh/claude-office-skills/skills/mcp-hub
---

# mcp-hub

skills/claude-office-skills/skills/mcp-hub
mcp-hub
Installation
$ npx skills add https://github.com/claude-office-skills/skills --skill mcp-hub
SKILL.md
Mcp Hub Skill
Overview

This skill provides access to 1200+ MCP (Model Context Protocol) servers - standardized tools that extend AI capabilities. Connect Claude to filesystems, databases, APIs, and document processing tools.

How to Use
Describe what you want to accomplish
Provide any required input data or files
I'll execute the appropriate operations

Example prompts:

"Access local filesystem to read/write documents"
"Query databases for data analysis"
"Integrate with GitHub, Slack, Google Drive"
"Run document processing tools"
Domain Knowledge
MCP Architecture
Claude ←→ MCP Server ←→ External Resource
        (Protocol)      (Files, APIs, DBs)

Popular Document MCP Servers
Server	Function	Stars
filesystem	Read/write local files	Official
google-drive	Access Google Docs/Sheets	5k+
puppeteer	Browser automation, PDF gen	10k+
sqlite	Database queries	Official
Configuration Example
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/documents"
      ]
    },
    "google-drive": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-google-drive"]
    }
  }
}

MCP Tool Discovery

Browse available servers:

mcp.run - MCP marketplace
awesome-mcp-servers
mcp-awesome.com
Using MCP in Skills
# MCP tools become available to Claude automatically
# Example: filesystem MCP provides these tools:

# read_file(path) - Read file contents
# write_file(path, content) - Write to file
# list_directory(path) - List directory contents
# search_files(query) - Search for files

Best Practices
Only enable MCP servers you need (security)
Use official servers when available
Check server permissions before enabling
Combine multiple servers for complex workflows
Installation
# Install required dependencies
pip install python-docx openpyxl python-pptx reportlab jinja2

Resources
MCP Servers Repository
Claude Office Skills Hub
Weekly Installs
709
Repository
claude-office-s…s/skills
GitHub Stars
94
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn