---
title: pancakeswap
url: https://skills.sh/alsk1992/cloddsbot/pancakeswap
---

# pancakeswap

skills/alsk1992/cloddsbot/pancakeswap
pancakeswap
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill pancakeswap
SKILL.md
PancakeSwap

Multi-chain AMM DEX with V3 concentrated liquidity. Swap tokens on BNB Chain, Ethereum, Arbitrum, and Base.

Quick Start
# Set credentials
export EVM_PRIVATE_KEY="0x..."

# Get a quote
/cake quote BNB USDT 1 --chain bsc

# Execute swap
/cake swap BNB USDT 1 --chain bsc

# Check price
/cake price CAKE USDT --chain bsc

Commands
Command	Description
/cake swap <from> <to> <amount> [--chain bsc]	Execute swap
/cake quote <from> <to> <amount> [--chain bsc]	Get quote without executing
/cake price <tokenA> <tokenB> [--chain bsc]	Get relative price
/cake balance <token> [--chain bsc]	Check token balance
/cake help	Show commands
Chain Flag

Use --chain to select network (default: bsc):

Flag	Network
--chain bsc	BNB Smart Chain (default)
--chain eth	Ethereum
--chain arb	Arbitrum
--chain base	Base
Examples
# Swap 1 BNB to USDT on BSC
/cake swap BNB USDT 1

# Swap 100 USDC to CAKE on Ethereum
/cake swap USDC CAKE 100 --chain eth

# Get quote for WETH to USDC on Arbitrum
/cake quote WETH USDC 0.5 --chain arb

# Check CAKE balance on BSC
/cake balance CAKE

Common Tokens
Token	BSC	ETH	ARB	Base
CAKE	Yes	Yes	Yes	Yes
USDC	Yes	Yes	Yes	Yes
USDT	Yes	Yes	Yes	-
WBNB	Yes	-	-	-
WETH	-	Yes	Yes	Yes
Configuration
# Required
export EVM_PRIVATE_KEY="0x..."

# Optional: custom RPC URLs
export BSC_RPC_URL="https://..."
export ETH_RPC_URL="https://..."

Resources
PancakeSwap App
PancakeSwap Docs
Weekly Installs
13
Repository
alsk1992/cloddsbot
GitHub Stars
194
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn