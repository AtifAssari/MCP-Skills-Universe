---
title: tempo
url: https://skills.sh/tempoxyz/agent-skills/tempo
---

# tempo

skills/tempoxyz/agent-skills/tempo
tempo
Installation
$ npx skills add https://github.com/tempoxyz/agent-skills --skill tempo
SKILL.md
Tempo

Skill for building applications on the Tempo network.

Capabilities
Navigate Tempo documentation and protocol specs
Browse source code for tempoxyz/tempo (Rust node) and tempoxyz/tempo-ts (TypeScript SDK)
Access related libraries: viem, wagmi, reth, foundry
MCP Tools

Use these tools to explore Tempo:

Tool	Description
mcp__tempo__list_pages	List all documentation pages
mcp__tempo__read_page	Read a specific documentation page
mcp__tempo__search_docs	Search documentation
mcp__tempo__list_sources	List available source repositories
mcp__tempo__list_source_files	List files in a directory
mcp__tempo__read_source_file	Read a source code file
mcp__tempo__get_file_tree	Get recursive file tree
mcp__tempo__search_source	Search source code
Available Sources
tempoxyz/tempo – Tempo node (Rust)
tempoxyz/tempo-ts – TypeScript SDK
paradigmxyz/reth – Reth Ethereum client
foundry-rs/foundry – Foundry toolkit
wevm/viem – TypeScript Ethereum interface
wevm/wagmi – React hooks for Ethereum
Workflow
Search docs first: Use mcp__tempo__search_docs to find relevant documentation
Read pages: Use mcp__tempo__read_page with the page path
Explore source: Use mcp__tempo__search_source or mcp__tempo__get_file_tree to find implementations
Read code: Use mcp__tempo__read_source_file to examine specific files
Key Concepts
TIP-20: Native stablecoin standard (like ERC-20 but built into the protocol)
Tempo Transactions: Enhanced transaction format with sub-blocks and parallel execution
Fee Sponsorship: Pay transaction fees on behalf of users
Stablecoin DEX: Native exchange for stablecoin pairs
Weekly Installs
72
Repository
tempoxyz/agent-skills
GitHub Stars
6
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn