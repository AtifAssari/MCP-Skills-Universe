---
rating: ⭐⭐⭐
title: install-mcp-servers
url: https://skills.sh/reapzyau/install-mcp-servers-skill/install-mcp-servers
---

# install-mcp-servers

skills/reapzyau/install-mcp-servers-skill/install-mcp-servers
install-mcp-servers
Installation
$ npx skills add https://github.com/reapzyau/install-mcp-servers-skill --skill install-mcp-servers
SKILL.md
Install MCP Servers

This skill automatically installs three essential MCP servers for development workflows:

Apify MCP - Web scraping, data extraction, and automation
Netlify MCP - Deployment, hosting, and site management
Context7 MCP - Library documentation and code examples
When to Use This Skill

Use this skill when:

Setting up a new project that needs scraping capabilities
You need to deploy to Netlify
You want library documentation lookup within Claude Code
The user asks to "install MCP servers" or "setup MCPs"
You need Apify, Netlify, or Context7 integration
Installation Options

The skill supports three installation modes:

Project-level (default) - Installs to current project only
Global - Installs for all projects
Selective - Install only specific servers
How to Install
Automatic Installation (Recommended)

Run the installation command to add all three MCP servers:

# Add to current project's MCP configuration
claude mcp add apify --transport http --url "https://mcp.apify.com/"
claude mcp add netlify --transport http --url "https://netlify-mcp.netlify.app/mcp"
claude mcp add context7 --transport http --url "https://mcp.context7.com/mcp"

Alternative: NPX-based Installation

For stdio-based servers (useful if HTTP endpoints are unavailable):

# Context7 via NPX (requires API key from https://context7.com)
claude mcp add context7 -s user -- npx -y @upstash/context7-mcp --api-key YOUR_API_KEY

# Netlify via NPX
claude mcp add netlify -s user -- npx -y @netlify/mcp

Global Installation

Add -s user flag to install globally for all projects:

claude mcp add apify -s user --transport http --url "https://mcp.apify.com/"
claude mcp add netlify -s user --transport http --url "https://netlify-mcp.netlify.app/mcp"
claude mcp add context7 -s user --transport http --url "https://mcp.context7.com/mcp"

Server Capabilities
Apify MCP
Tools: search-actors, call-actor, fetch-actor-details, apify-slash-rag-web-browser
Use cases: Web scraping, data extraction, lead generation, competitor analysis
Authentication: Connects via Apify account (OAuth during first use)
Netlify MCP
Tools: Site deployment, DNS management, build triggers, environment variables
Use cases: Deploy sites, manage hosting, configure builds
Authentication: Connects via Netlify account
Context7 MCP
Tools: resolve-library-id, get-library-docs
Use cases: Lookup library documentation, get code examples, understand APIs
Authentication: Free tier available, API key for extended use
Verification

After installation, verify the servers are connected:

# List all configured MCP servers
claude mcp list

# Or use /mcp command in Claude Code to see connection status

Troubleshooting
Server not connecting
Check if the HTTP endpoint is accessible
Verify authentication is complete
Try the NPX alternative if HTTP fails
Permission errors
Ensure you have write access to ~/.claude.json
Try running with appropriate permissions
Removing servers
claude mcp remove apify
claude mcp remove netlify
claude mcp remove context7

Quick Reference
Server	HTTP URL	NPX Package
Apify	https://mcp.apify.com/	N/A (HTTP only)
Netlify	https://netlify-mcp.netlify.app/mcp	@netlify/mcp
Context7	https://mcp.context7.com/mcp	@upstash/context7-mcp
Weekly Installs
10
Repository
reapzyau/instal…rs-skill
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail