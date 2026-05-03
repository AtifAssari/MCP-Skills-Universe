---
title: feishu-docs
url: https://skills.sh/m1heng/feishu-doc-cli/feishu-docs
---

# feishu-docs

skills/m1heng/feishu-doc-cli/feishu-docs
feishu-docs
Installation
$ npx skills add https://github.com/m1heng/feishu-doc-cli --skill feishu-docs
SKILL.md
Feishu Open Platform Docs

Read Feishu developer documentation directly from the terminal via feishu-doc CLI.

Prerequisites

Install once (requires Node.js >= 18):

npm install -g feishu-doc-cli

Commands
feishu-doc search "<keyword>"     # Search docs by title
feishu-doc read "<path>"          # Read a document (outputs Markdown)
feishu-doc tree --depth 2         # Browse the doc tree
feishu-doc tree "<path>"          # Browse a subtree


Add --lang en for English.

Workflow

Start with search to find relevant documents:

feishu-doc search "知识库"


Read a document using the path from search results:

feishu-doc read "/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-overview"


Follow links — document content contains links in various formats. Copy any link href and pass it directly to read:

# All these formats work — just copy the href as-is:
feishu-doc read "/ssl:ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/space/list"
feishu-doc read "https://open.feishu.cn/document/client-docs/intro"
feishu-doc read "https://open.larkoffice.com/document/client-docs/bot-v3/bot-overview"


Browse by category if you need to explore an area:

feishu-doc tree "/uAjLw4CM/ukTMukTMukTM" --depth 2   # Server APIs

Top-level doc categories
Category	Tree path
Developer Guides	/uAjLw4CM/ukzMukzMukzM
Developer Tutorials	/uAjLw4CM/uMzNwEjLzcDMx4yM3ATM
Server API	/uAjLw4CM/ukTMukTMukTM
Client API	/uAjLw4CM/uYjL24iN
MCP	/mcp_open_tools
Weekly Installs
91
Repository
m1heng/feishu-doc-cli
GitHub Stars
6
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass