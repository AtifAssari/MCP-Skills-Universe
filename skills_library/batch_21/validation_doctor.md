---
title: validation-doctor
url: https://skills.sh/mverab/egeoagents/validation-doctor
---

# validation-doctor

skills/mverab/egeoagents/validation-doctor
validation-doctor
Installation
$ npx skills add https://github.com/mverab/egeoagents --skill validation-doctor
SKILL.md
Validation Doctor
Diagnostics

Chrome DevTools MCP

Probe by calling list_pages (may appear as mcp6_list_pages depending on the client).

Brave Search MCP

Probe by calling brave_web_search with a trivial query and count=1.
Status Report
Component	Status	Action Required
Market Validator (Brave)	✅ / ❌	[Config Snippet / None]
Technical Validator (Chrome)	✅ / ❌	[Config Snippet / None]
Setup Snippets
Chrome DevTools (NPX)
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}

Brave Search (NPX)
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@brave/brave-search-mcp-server", "--transport", "stdio"],
      "env": {
        "BRAVE_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}

Runtime Policy
If chrome-devtools is unavailable, allow fetch fallback but mark results as Low Confidence.
If brave-search is unavailable, do not claim competitor positioning; only score the page itself.
Weekly Installs
29
Repository
mverab/egeoagents
GitHub Stars
104
First Seen
Feb 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn