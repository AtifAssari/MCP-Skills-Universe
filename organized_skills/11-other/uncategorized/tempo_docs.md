---
rating: ⭐⭐
title: tempo-docs
url: https://skills.sh/tempoxyz/docs/tempo-docs
---

# tempo-docs

skills/tempoxyz/docs/tempo-docs
tempo-docs
Installation
$ npx skills add https://github.com/tempoxyz/docs --skill tempo-docs
SKILL.md
Tempo Docs

Skill for navigating Tempo documentation and source code.

Quick Context

Before using MCP tools, try fetching context directly:

llms.txt – Concise index of all pages: https://docs.tempo.xyz/llms.txt
Markdown pages – Append .md to any page URL (e.g. https://docs.tempo.xyz/quickstart/integrate-tempo.md)

Use read_web_page to fetch these when you need broad context or a quick answer.

MCP Tools

Use these tools for structured exploration:

Tool	Description
mcp__tempo_mcp__list_pages	List all documentation pages
mcp__tempo_mcp__read_page	Read a specific documentation page
mcp__tempo_mcp__search_docs	Search documentation
mcp__tempo_mcp__list_sources	List available source repositories
mcp__tempo_mcp__list_source_files	List files in a directory
mcp__tempo_mcp__read_source_file	Read a source code file
mcp__tempo_mcp__get_file_tree	Get recursive file tree
mcp__tempo_mcp__search_source	Search source code
Available Sources
tempoxyz/tempo – Tempo node (Rust)
tempoxyz/tempo-ts – TypeScript SDK
paradigmxyz/reth – Reth Ethereum client
foundry-rs/foundry – Foundry toolkit
wevm/viem – TypeScript Ethereum interface
wevm/wagmi – React hooks for Ethereum
Workflow
Quick lookup: Use read_web_page on https://docs.tempo.xyz/llms.txt for an overview, or fetch a specific page as Markdown
Search docs: Use mcp__tempo_mcp__search_docs to find relevant pages
Read pages: Use mcp__tempo_mcp__read_page with the page path
Explore source: Use mcp__tempo_mcp__search_source or mcp__tempo_mcp__get_file_tree to find implementations
Read code: Use mcp__tempo_mcp__read_source_file to examine specific files
Weekly Installs
158
Repository
tempoxyz/docs
GitHub Stars
12
First Seen
Mar 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass