---
rating: ⭐⭐⭐
title: emblem-token-swap
url: https://skills.sh/emblemcompany/agent-skills/emblem-token-swap
---

# emblem-token-swap

skills/emblemcompany/agent-skills/emblem-token-swap
emblem-token-swap
Installation
$ npx skills add https://github.com/emblemcompany/agent-skills --skill emblem-token-swap
SKILL.md
Emblem Token Swap

Guided token swapping powered by EmblemAI. Swap tokens on Solana, Ethereum, Base, BSC, Polygon, and Hedera with automatic routing. Cross-chain bridging via ChangeNow.

Requires: npm install -g @emblemvault/agentwallet

What This Skill Can Do
Chain	Quote Tool	Swap Tool	Balance Tool	Token Search
Solana	splBuyIntent (quote mode)	splBuyIntent (swap mode)	solanaBalances	findSolanaSwapToken
Ethereum	ethSwapQuote	ethSwap	ethGetBalances	searchCryptoByName
Base	baseSwapQuote	baseSwap	baseGetBalances	searchEvmTokensBirdeye
BSC	bscSwapQuote	bscSwap	bscGetBalances	searchEvmTokensBirdeye
Polygon	polygonSwapQuote	polygonSwap	polygonGetBalances	searchEvmTokensBirdeye
Hedera	hederaTokensSwapQuote	hederaTokensSwap	hederaGetBalances	hederaFindTokens
Cross-chain	getChangeNowSwapQuote	swapUsingChangeNow	—	getChangeNowSupportedCurrencies
Notes
Solana uses splBuyIntent for both quotes and execution — it handles token lookup by name/symbol/CA and flexible amounts ($USD, SOL, or token quantity)
EVM chains (Ethereum, Base, BSC, Polygon) route through automatic DEX aggregation
Cross-chain bridges via ChangeNow support 500+ currencies
Bitcoin has balance support (getBTCBalances) but no on-chain swap tools — use ChangeNow for BTC bridges
Quick Start
npm install -g @emblemvault/agentwallet

# Solana swap (uses splBuyIntent)
emblemai --agent --profile default -m "Use splBuyIntent to swap 5 SOL for USDC on Solana"

# Cross-chain bridge (uses ChangeNow)
emblemai --agent --profile default -m "Use getChangeNowSwapQuote to get a quote for bridging 0.05 ETH from Ethereum to SOL on Solana"


Trigger phrases:

"Swap SOL to USDC"
"Exchange ETH for USDT"
"Convert my tokens"
"Bridge tokens to Base"
Workflow: Safe Token Swap
Step 1: Check Balance

Confirm you have enough of the source token.

emblemai --agent --profile default -m "Use solanaBalances to show my Solana token balances"

Step 2: Get a Quote

Preview the swap before executing.

emblemai --agent --profile default -m "Use splBuyIntent to get a quote for swapping 5 SOL to USDC"

Step 3: Execute the Swap
emblemai --agent --profile default -m "Use splBuyIntent to swap 5 SOL for USDC on Solana"


Safe mode requires your confirmation before executing.

Step 4: Verify

Confirm the new balance.

emblemai --agent --profile default -m "Use solanaBalances to show my updated balances"

Swap Patterns
Solana Swaps
# By token amount
emblemai --agent --profile default -m "Use splBuyIntent to swap 0.5 SOL for USDC"

# By dollar amount
emblemai --agent --profile default -m "Use splBuyIntent to swap $20 of SOL for JUP"

# By token name
emblemai --agent --profile default -m "Use splBuyIntent to swap 100 USDC for BONK"

EVM Swaps
# Ethereum
emblemai --agent --profile default -m "Use ethSwapQuote to get a quote for swapping 0.01 ETH to USDC, then use ethSwap to execute"

# Base
emblemai --agent --profile default -m "Use baseSwapQuote to quote 0.005 ETH to USDC on Base"

# BSC
emblemai --agent --profile default -m "Use bscSwapQuote to quote 0.1 BNB to USDT on BSC"

# Polygon
emblemai --agent --profile default -m "Use polygonSwapQuote to quote 10 POL to USDC on Polygon"

Hedera Swaps
emblemai --agent --profile default -m "Use hederaTokensSwapQuote to get a quote for 100 HBAR to USDC, then use hederaTokensSwap to execute"

Cross-Chain Bridge
emblemai --agent --profile default -m "Use getChangeNowSwapQuote to quote bridging 0.1 ETH to SOL"
emblemai --agent --profile default -m "Use getChangeNowSupportedCurrencies to show available bridge currencies"

Communication Rules

Always include these in swap requests:

Tool name — specify the exact tool for reliable routing
Amount — dollar value or token quantity
Source token — what you're swapping from
Target token — what you're swapping to
Bad	Good
"swap sol usdc"	"Use splBuyIntent to swap 5 SOL for USDC"
"buy eth"	"Use ethSwap to swap 100 USDC to ETH on Ethereum"
"bridge"	"Use getChangeNowSwapQuote to bridge 0.05 ETH to SOL"
Safety

All swaps require explicit user confirmation (safe mode). The agent will:

Show you the swap details (amount, route, estimated output)
Wait for your approval before executing
Report the transaction result

Never bypasses confirmation for any value-moving operation.

Helper Script
bash scripts/swap-helper.sh


See scripts/swap-helper.sh for an interactive swap walkthrough.

Links
Agent Wallet CLI
EmblemVault Docs — canonical
EmblemVault Docs — interactive
Weekly Installs
4.4K
Repository
emblemcompany/a…t-skills
GitHub Stars
10
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn