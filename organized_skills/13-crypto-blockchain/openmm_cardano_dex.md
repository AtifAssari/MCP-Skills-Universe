---
rating: ⭐⭐⭐
title: openmm-cardano-dex
url: https://skills.sh/qbt-labs/openmm-ai/openmm-cardano-dex
---

# openmm-cardano-dex

skills/qbt-labs/openmm-ai/openmm-cardano-dex
openmm-cardano-dex
Installation
$ npx skills add https://github.com/qbt-labs/openmm-ai --skill openmm-cardano-dex
SKILL.md
Cardano DEX Integration

Discover Cardano DEX liquidity pools, fetch aggregated on-chain prices, and compare DEX vs CEX pricing for Cardano native tokens.

Overview

OpenMM integrates with Cardano DEX liquidity pools via the Iris Protocol, aggregating data from multiple decentralized exchanges on Cardano. This skill covers read-only price discovery and pool analysis — no on-chain trading is involved.

Supported tokens: SNEK, INDY, NIGHT, MIN

Supported DEXes (via Iris Protocol): SundaeSwap, Minswap, WingRiders

Credentials

No exchange API keys are required for Cardano DEX operations — all pool data is public on-chain. However, the price-comparison command also fetches CEX prices, which may require exchange credentials to be configured. See the openmm-portfolio skill for exchange credential setup.

Aggregated DEX Pricing

Get the current aggregated price for a Cardano native token. Prices are calculated from on-chain DEX pool reserves, weighted by total value locked (TVL).

openmm pool-discovery prices SNEK
openmm pool-discovery prices INDY
openmm pool-discovery prices NIGHT

How Price Calculation Works
TOKEN/ADA price is fetched from on-chain DEX pools (SundaeSwap, Minswap, WingRiders), weighted by TVL
ADA/USDT price is fetched from CEX price feeds (MEXC, other aggregators)
TOKEN/USDT = TOKEN/ADA x ADA/USDT

This gives a USD-denominated price for Cardano tokens that do not have direct USDT pairs on all exchanges.

Pool Discovery

Discover liquidity pools for a specific token across all supported Cardano DEXes.

# Find all pools for a token
openmm pool-discovery discover SNEK

# Find pools for INDY
openmm pool-discovery discover INDY

# Filter by minimum liquidity (TVL in ADA)
openmm pool-discovery discover SNEK --min-liquidity 50000

# Discover NIGHT pools with minimum liquidity
openmm pool-discovery discover NIGHT --min-liquidity 10000


Pool discovery returns:

Pool address and DEX source
Token pair (e.g., SNEK/ADA)
Reserves for each token in the pool
Total value locked (TVL)
Implied price from pool reserves
DEX vs CEX Price Comparison

Compare the aggregated DEX price against CEX prices to identify arbitrage opportunities or price discrepancies.

openmm price-comparison --symbol SNEK
openmm price-comparison --symbol INDY


This command fetches:

Aggregated DEX price (from Cardano pools via Iris Protocol)
CEX price (from exchanges like MEXC, Bitget where the token is listed)
Price difference and percentage spread between DEX and CEX
MCP Tools
Tool	Description	Parameters
get_cardano_price	Aggregated token price from DEX pools (TOKEN/USDT via ADA bridge)	symbol
discover_pools	Discover Cardano DEX liquidity pools for a token	symbol, minLiquidity?
Examples

Get aggregated price:

Tool: get_cardano_price
Parameters: { "symbol": "SNEK" }


Discover pools with minimum liquidity:

Tool: discover_pools
Parameters: { "symbol": "INDY", "minLiquidity": 50000 }

Iris Protocol Integration

The Iris Protocol is a Cardano data aggregation layer that indexes liquidity pools across multiple DEXes. OpenMM uses Iris to:

Discover all active pools for a given token
Fetch real-time reserve data for price calculation
Aggregate prices across pools weighted by TVL
Filter pools by minimum liquidity thresholds

Indexed DEXes:

SundaeSwap — one of the earliest Cardano DEXes
Minswap — largest Cardano DEX by TVL
WingRiders — Cardano DEX with concentrated liquidity
Tips for Agents
Use for arbitrage analysis — compare DEX and CEX prices with price-comparison to find opportunities
Compare before trading on CEX — check if the DEX price is significantly different before placing CEX orders
Filter low-liquidity pools — use --min-liquidity to focus on pools with meaningful TVL
No API keys required — Cardano DEX data is public; no exchange credentials needed for pool discovery and pricing
Prices are estimates — DEX prices reflect pool reserves, not executable quotes; slippage applies for large trades
TOKEN/USDT depends on ADA/USDT — if ADA price moves significantly, all token USDT prices will shift accordingly
Weekly Installs
9
Repository
qbt-labs/openmm-ai
GitHub Stars
1
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn