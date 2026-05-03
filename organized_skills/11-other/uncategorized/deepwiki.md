---
rating: ⭐⭐⭐
title: deepwiki
url: https://skills.sh/petekp/claude-code-setup/deepwiki
---

# deepwiki

skills/petekp/claude-code-setup/deepwiki
deepwiki
Installation
$ npx skills add https://github.com/petekp/claude-code-setup --skill deepwiki
SKILL.md
DeepWiki - Repository Documentation

Query DeepWiki for AI-generated documentation about any public GitHub repository.

Overview

DeepWiki (deepwiki.com) provides AI-generated documentation for GitHub repositories, including:

Repository structure and architecture
API documentation
Code explanations
Interactive diagrams
Quick Start

URL Pattern: Replace github.com with deepwiki.com in any repo URL:

github.com/vercel/next.js → deepwiki.com/vercel/next.js
MCP Server Setup

DeepWiki provides a free MCP server with no authentication required for public repos.

Add to Claude Code (one-time setup)
claude mcp add -s user -t http deepwiki https://mcp.deepwiki.com/mcp

For Cursor/Windsurf

Add to your MCP config:

{
  "mcpServers": {
    "deepwiki": {
      "serverUrl": "https://mcp.deepwiki.com/sse"
    }
  }
}

Available MCP Tools

Once configured, these tools become available:

Tool	Purpose
read_wiki_structure	Get documentation topics/structure for a repo
read_wiki_contents	Retrieve actual documentation content
ask_question	Ask AI-powered questions about the repo
Usage Examples
Via WebFetch (works immediately)
# Fetch documentation overview
WebFetch https://deepwiki.com/owner/repo "Summarize the architecture"

# Example
WebFetch https://deepwiki.com/vercel/next.js "How does routing work?"

Via MCP (after setup)

Use the MCP tools directly:

mcp__deepwiki__read_wiki_structure - Get repo structure
mcp__deepwiki__read_wiki_contents - Get documentation
mcp__deepwiki__ask_question - Ask questions
Fallback: GitHub + AI

If DeepWiki lacks coverage for a repo, use GitHub API:

Get Repository Overview
gh api repos/owner/repo | jq '{description, language, topics, stars: .stargazers_count}'

Get README
gh api repos/owner/repo/readme --jq '.content' | base64 -d

Get File Structure
gh api repos/owner/repo/git/trees/main?recursive=1 | \
  jq -r '.tree[] | select(.type == "blob") | .path' | head -50

Wire Protocols

Two protocols are supported:

SSE at https://mcp.deepwiki.com/sse - Official MCP spec
HTTP at https://mcp.deepwiki.com/mcp - Cloudflare/OpenAI compatible
Best Practices
Use WebFetch first - Works without MCP setup
Check if repo is indexed - Popular repos have better coverage
Ask specific questions - DeepWiki excels at targeted queries
Fall back to GitHub - For unindexed or private repos
Limitations
Public repos only - Private repos require Devin account
Coverage varies - 50,000+ popular repos indexed
No authentication - Can't access private documentation
Resources
Website: https://deepwiki.com
Docs: https://docs.devin.ai/work-with-devin/deepwiki
GitHub: https://github.com/CognitionAI/deepwiki
Weekly Installs
19
Repository
petekp/claude-code-setup
GitHub Stars
35
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn