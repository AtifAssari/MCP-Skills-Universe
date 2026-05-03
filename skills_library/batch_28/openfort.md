---
title: openfort
url: https://skills.sh/openfort-xyz/agent-skills/openfort
---

# openfort

skills/openfort-xyz/agent-skills/openfort
openfort
Installation
$ npx skills add https://github.com/openfort-xyz/agent-skills --skill openfort
SKILL.md
Openfort

Skill for navigating Openfort documentation, browsing SDK source code, and executing platform operations via MCP tools.

Capabilities
Navigate Openfort documentation and SDKs
Browse source code for openfort-xyz/openfort-js (low level typescript library), openfort-xyz/openfort-react (React TypeScript SDK), openfort-xyz/react-native (React Native SDK), openfort-xyz/node (TypeScript Node SDK), openfort-xyz/openfort-csharp-unity (Unity SDK), openfort-xyz/swift-sdk (Swift SDK)
Access related libraries: viem, wagmi
Execute Openfort CLI commands via MCP tools

For MCP tool details, see references/mcp-tools.md.

Available Sources
openfort-xyz/openfort-js – Low level TypeScript SDK
openfort-xyz/openfort-react – React SDK
openfort-xyz/react-native – React Native SDK
openfort-xyz/cli – CLI
openfort-xyz/openfort-node – Node TypeScript SDK
openfort-xyz/swift-sdk – Swift SDK
openfort-xyz/openfort-csharp-unity – Unity SDK
wevm/viem – TypeScript Ethereum interface
wevm/wagmi – React hooks for Ethereum
Workflow
Search docs first: Use mcp__openfort-docs__search_docs to find relevant documentation
Read pages: Use mcp__openfort-docs__read_page with the page path
Explore source: Use mcp__openfort-docs__search_source or mcp__openfort-docs__get_file_tree to find implementations
Read code: Use mcp__openfort-docs__read_source_file to examine specific files
Key Concepts
Openfort Embedded Wallets: Give each user a wallet tied to your app with regular auth methods (EVM and Solana).
Openfort Backend Wallets: Running onchain AI agents or trading bots with programmatic control. Managing app-wide funds like fees and rewards. (EVM and Solana).
Fee Sponsorship: Sending transactions from wallets without requiring native chain tokens. Fully sponsor the transaction or charge custom tokens (e.g. stablecoins like USDT or USDC).
Policies: set of rules and conditions that must be fulfilled. Can be applied to both fee-sponsorship or backend wallet operations.
Weekly Installs
26
Repository
openfort-xyz/ag…t-skills
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn