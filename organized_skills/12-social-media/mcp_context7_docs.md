---
rating: ⭐⭐
title: mcp-context7-docs
url: https://skills.sh/vaayne/cc-plugins/mcp-context7-docs
---

# mcp-context7-docs

skills/vaayne/cc-plugins/mcp-context7-docs
mcp-context7-docs
Installation
$ npx skills add https://github.com/vaayne/cc-plugins --skill mcp-context7-docs
SKILL.md
Context7 Documentation

MCP service at https://mcp.context7.com/mcp (http) with 2 tools.

Requirements
mh CLI must be installed. If not available, install with:
curl -fsSL https://raw.githubusercontent.com/vaayne/mcphub/main/scripts/install.sh | sh

Usage
List tools: `mh list -u https://mcp.context7.com/mcp -t http`
Get tool details: `mh inspect -u https://mcp.context7.com/mcp -t http <tool-name>`
Invoke tool: `mh invoke -u https://mcp.context7.com/mcp -t http <tool-name> '{"param": "value"}'`

Notes
Run inspect before invoking unfamiliar tools to get full parameter schema
Timeout: 30s default, use --timeout <seconds> to adjust
Important: Always call resolveLibraryId first to get the Context7-compatible library ID before calling queryDocs, unless user provides ID in /org/project format
Do not call either tool more than 3 times per question
Tools
Tool	Description
resolveLibraryId	Resolves a package/product name to a Context7-compatible library ID. Must be called before queryDocs to get a valid library ID.
queryDocs	Retrieves and queries up-to-date documentation and code examples from Context7 for any programming library or framework. Requires a Context7-compatible library ID.
Tool Parameters
resolveLibraryId
Required:
  libraryName (string)  — library name to search for, e.g. "react", "nextjs"
  query (string)        — the question or task you need help with (used for ranking)

queryDocs
Required:
  libraryId (string)    — exact Context7 ID, e.g. "/vercel/next.js" or "/vercel/next.js/v14"
  query (string)        — specific question, e.g. "How to set up JWT authentication in Express.js"

Workflow

Resolve library ID — get the Context7-compatible ID for the library:

mh invoke -u https://mcp.context7.com/mcp -t http resolveLibraryId '{"libraryName": "react", "query": "useState hook examples"}'


Query documentation — use the resolved ID to fetch docs:

mh invoke -u https://mcp.context7.com/mcp -t http queryDocs '{"libraryId": "/facebook/react", "query": "how to use useState hook"}'

Weekly Installs
13
Repository
vaayne/cc-plugins
GitHub Stars
41
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykFail