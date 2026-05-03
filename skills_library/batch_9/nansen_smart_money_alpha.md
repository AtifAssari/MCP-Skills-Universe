---
title: nansen-smart-money-alpha
url: https://skills.sh/nansen-ai/nansen-cli/nansen-smart-money-alpha
---

# nansen-smart-money-alpha

skills/nansen-ai/nansen-cli/nansen-smart-money-alpha
nansen-smart-money-alpha
Installation
$ npx skills add https://github.com/nansen-ai/nansen-cli --skill nansen-smart-money-alpha
SKILL.md
Alpha Discovery

Answers: "What tokens is smart money accumulating before they pump?"

CHAIN=solana

nansen research token screener --chain $CHAIN --timeframe 24h --smart-money --limit 20
# → token_symbol, price_usd, price_change, volume, buy_volume, market_cap_usd, fdv, liquidity, token_age_days

nansen research smart-money netflow --chain $CHAIN --labels "Smart Trader" --limit 10
# → token_symbol, net_flow_1h/24h/7d/30d_usd, trader_count

# Confirm SM flow on a specific token from screener results
TOKEN=<address_from_screener>
nansen research token flow-intelligence --token $TOKEN --chain $CHAIN
# → net_flow_usd per label: smart_trader, whale, exchange, fresh_wallets


Cross-reference screener results with positive netflow to find early accumulation.

Source
npm: https://www.npmjs.com/package/nansen-cli
GitHub: https://github.com/nansen-ai/nansen-cli
Weekly Installs
308
Repository
nansen-ai/nansen-cli
GitHub Stars
121
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass