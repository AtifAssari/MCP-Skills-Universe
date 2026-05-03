---
title: openai-docs-skill
url: https://skills.sh/am-will/codex-skills/openai-docs-skill
---

# openai-docs-skill

skills/am-will/codex-skills/openai-docs-skill
openai-docs-skill
Installation
$ npx skills add https://github.com/am-will/codex-skills --skill openai-docs-skill
Summary

Query OpenAI's official developer documentation via MCP server for API, SDK, and platform guidance.

Search and fetch docs on OpenAI APIs (Chat Completions, Realtime, Responses), SDKs, ChatGPT Apps, Codex, and migrations using a CLI wrapper around the OpenAI Docs MCP server
Includes subcommands for discovery (search, list), retrieval (fetch), and schema inspection (endpoints, openapi)
Supports optional anchors for fetching specific doc sections and code sample generation in multiple languages
Returns markdown content with source URLs for transparent, authoritative reference
SKILL.md
OpenAI Docs MCP Skill
Overview

Use the OpenAI developer documentation MCP server from the shell to search and fetch authoritative docs. Always do this for OpenAI platform work instead of relying on memory or non-official sources.

Core rules
Always use this skill for OpenAI API/SDK/Apps/Codex questions or when precise, current docs are required.
Query the MCP server via the CLI wrapper in scripts/openai-docs-mcp.sh (do not rely on Codex MCP tools).
Use search or list to find the best doc page, then fetch the page (or anchor) for exact text.
Surface the doc URL you used in your response so sources are clear.
Quick start
scripts/openai-docs-mcp.sh search "Responses API" 5
scripts/openai-docs-mcp.sh fetch https://platform.openai.com/docs/guides/migrate-to-responses

Workflow
Discover: search with a focused query. If unsure, use list to browse.
Read: fetch the most relevant URL (optionally add an anchor).
Apply: summarize and/or quote relevant sections; include the URL.
Script reference

The CLI wrapper is at scripts/openai-docs-mcp.sh and uses curl + jq against https://developers.openai.com/mcp.

Subcommands:

init: initialize and inspect server capabilities.
tools: list available tools on the MCP server.
search <query> [limit] [cursor]: return JSON hits from the docs index.
list [limit] [cursor]: browse docs index.
fetch <url> [anchor]: return markdown for a doc page or section.
endpoints: list OpenAPI endpoints.
openapi <endpoint-url> [lang1,lang2] [code-only]: fetch OpenAPI schema or code samples.

Environment:

MCP_URL: override the default MCP endpoint.
Weekly Installs
1.2K
Repository
am-will/codex-skills
GitHub Stars
907
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn