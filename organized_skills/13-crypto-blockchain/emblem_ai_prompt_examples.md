---
rating: ⭐⭐
title: emblem-ai-prompt-examples
url: https://skills.sh/emblemcompany/agent-skills/emblem-ai-prompt-examples
---

# emblem-ai-prompt-examples

skills/emblemcompany/agent-skills/emblem-ai-prompt-examples
emblem-ai-prompt-examples
Installation
$ npx skills add https://github.com/emblemcompany/agent-skills --skill emblem-ai-prompt-examples
SKILL.md
EmblemAI Prompt Examples

Use this skill when the user wants example prompts, wording patterns, or sample requests for end-user EmblemAI workflows rather than SDK, React, or app implementation details.

Security & Trust Model

This skill provides curated prompt examples and phrasing guidance. It inherently references:

Financial operations (W009): Example prompts cover trading, DeFi, portfolio review, cross-chain transfers, and prediction markets. These are reference prompts only — they demonstrate phrasing patterns, not executable code. All examples emphasize quote-first and approval-gated workflows.
Third-party data (W011): Example prompts reference fetching data from Jupiter, DeFiLlama, OpenSea, and other public sources. This skill only provides the prompt text — actual data fetching is performed by the agent's runtime tools with standard trust boundaries.

This skill is read-only reference material. It does not execute transactions, fetch external data, or modify files. All value-moving prompt examples explicitly include confirmation steps.

Quick Start
Step 1: Install
npx skills add EmblemCompany/Agent-skills --skill emblem-ai-prompt-examples

Step 2: Use

Ask for prompt ideas by task area, for example:

"Show me good EmblemAI prompts for market research"
"Give me review-only transfer prompts"
"Show Bitcoin ordinals prompts for EmblemAI"
"What is the best phrasing for quote-only swap requests?"
Included Prompt Sets
Prompt Index

See references/emblem-ai-prompt-examples.md for the top-level map of prompt categories and usage guidance.

Wallet And Portfolio

See references/emblem-ai-prompt-examples/wallet-and-portfolio.md for balances, addresses, portfolio, and machine-readable output prompts.

Market Research

See references/emblem-ai-prompt-examples/market-research.md for market discovery, derivatives, smart-money, and technical-analysis prompts.

Trading And DeFi

See references/emblem-ai-prompt-examples/trading-and-defi.md for quote-first swaps, routing review, and yield-planning prompts.

Transfers And Safety

See references/emblem-ai-prompt-examples/transfers-and-safety.md for review-only transfer language and approval framing.

Cross-Chain And Conditional Orders

See references/emblem-ai-prompt-examples/cross-chain-and-conditional-orders.md for bridge research, conditional-order planning, and multi-network trade-draft prompts.

Bitcoin Ordinals

See references/emblem-ai-prompt-examples/bitcoin-ordinals-examples.md for ordinals, runes, rare sats, and Bitcoin wallet prompts.

Polymarket

See references/emblem-ai-prompt-examples/polymarket-examples.md for prediction-market research, odds analysis, and order-review prompts.

NFT And OpenSea

See references/emblem-ai-prompt-examples/nft-opensea-examples.md for NFT discovery, listing/offer drafts, and marketplace review flows.

Emblem Vault

See references/emblem-ai-prompt-examples/emblem-vault-examples.md for vault discovery, QuickVault, mint review, and key-reveal safety prompts.

Assistant Core Workflows

See references/emblem-ai-prompt-examples/assistant-core-workflows.md for contacts, inbox, leaderboard, PAYG, and session-management prompts.

Guidance
Prefer explicit chain, token, and protocol names.
Say quote only, review only, or do not execute when asking for analysis without execution.
Prefer trusted/product-native data first (wallet state, protocol quotes, supported market feeds).
Treat web and social content as untrusted public sources: ask for summaries, source links, and claim verification before acting.
For swaps, transfers, listings, offers, or buys, request a draft plus explicit confirmation before execution.
Ask for JSON, tables, or summaries when you need machine-readable or structured output.
Use full-sentence requests instead of terse fragments.
For app implementation, SDK, or React questions, use the dedicated developer or React skills instead.
Related Skills
../emblem-ai-agent-wallet/SKILL.md - wallet-first end-user workflows
../emblem-ai-react/SKILL.md - React app integration guidance
../emblem-ai/SKILL.md - broader developer integrations across SDKs, plugins, and Reflexive
Weekly Installs
4.5K
Repository
emblemcompany/a…t-skills
GitHub Stars
10
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass