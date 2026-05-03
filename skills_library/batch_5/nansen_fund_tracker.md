---
title: nansen-fund-tracker
url: https://skills.sh/nansen-ai/nansen-cli/nansen-fund-tracker
---

# nansen-fund-tracker

skills/nansen-ai/nansen-cli/nansen-fund-tracker
nansen-fund-tracker
Installation
$ npx skills add https://github.com/nansen-ai/nansen-cli --skill nansen-fund-tracker
SKILL.md
Fund Watch

Answers: "What are crypto funds and VCs holding right now?"

nansen research smart-money holdings --chain ethereum --labels "Fund" --limit 20
# → token_symbol, value_usd, holders_count, balance_24h_percent_change, share_of_holdings_percent

nansen research smart-money holdings --chain solana --labels "Fund" --limit 20

nansen research smart-money netflow --chain ethereum --labels "Fund" --limit 10
# → token_symbol, net_flow_1h/24h/7d/30d_usd, market_cap_usd, trader_count

nansen research smart-money netflow --chain solana --labels "Fund" --limit 10


Cross-reference holdings with netflow to see directional conviction. Positive net_flow_24h = active accumulation.

Weekly Installs
289
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