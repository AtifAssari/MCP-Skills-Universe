---
rating: ⭐⭐⭐
title: nansen-exit-signals
url: https://skills.sh/nansen-ai/nansen-cli/nansen-exit-signals
---

# nansen-exit-signals

skills/nansen-ai/nansen-cli/nansen-exit-signals
nansen-exit-signals
Installation
$ npx skills add https://github.com/nansen-ai/nansen-cli --skill nansen-exit-signals
SKILL.md
Exit Signal

Answers: "Is smart money exiting a token I hold? Should I be worried?"

TOKEN=<address> CHAIN=ethereum

nansen research token flow-intelligence --token $TOKEN --chain $CHAIN
# → net_flow_usd per label: smart_trader, whale, exchange, fresh_wallets (negative = selling)

nansen research token who-bought-sold --token $TOKEN --chain $CHAIN --limit 20
# → address, address_label, bought/sold_volume_usd, trade_volume_usd

nansen research smart-money netflow --chain $CHAIN --limit 10
# → token_symbol, net_flow_1h/24h/7d/30d_usd, trader_count

nansen research token dex-trades --token $TOKEN --chain $CHAIN --limit 20
# → block_timestamp, action (BUY/SELL), trader_address_label, estimated_value_usd


Red flag: negative smart_trader_net_flow_usd + Smart Trader labels in who-bought-sold sellers = exit signal.

Weekly Installs
264
Repository
nansen-ai/nansen-cli
GitHub Stars
121
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn