---
title: lighter
url: https://skills.sh/alsk1992/cloddsbot/lighter
---

# lighter

skills/alsk1992/cloddsbot/lighter
lighter
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill lighter
SKILL.md
Lighter

On-chain orderbook DEX on Arbitrum. Trade perpetual futures with deep liquidity and low fees.

Quick Start
# Set credentials
export EVM_PRIVATE_KEY="0x..."

# Check markets
/lighter markets

# Get price
/lighter price ETH-USD

# Open positions
/lighter long ETH-USD 1
/lighter short BTC-USD 0.1 45000

Commands
Market Data
Command	Description
/lighter markets	List available markets
/lighter price <market>	Get current price
/lighter book <market>	Show orderbook depth
Account
Command	Description
/lighter balance	Show balances
/lighter positions	Show open positions
/lighter orders	List open orders
Trading
Command	Description
/lighter long <market> <size> [price]	Open long position
/lighter short <market> <size> [price]	Open short position
/lighter close <market>	Close position
/lighter closeall	Close all positions
/lighter cancel <orderId>	Cancel order
/lighter cancelall	Cancel all orders

Examples:

/lighter long ETH-USD 1           # Market long 1 ETH
/lighter long ETH-USD 1 3000      # Limit long at $3,000
/lighter short BTC-USD 0.1        # Market short 0.1 BTC
/lighter close ETH-USD            # Close ETH position

Configuration
# Required
export EVM_PRIVATE_KEY="0x..."

# Optional
export DRY_RUN=true

Resources
Lighter App
Lighter Docs
Weekly Installs
10
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