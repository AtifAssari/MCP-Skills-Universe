---
title: nansen-holder-analysis
url: https://skills.sh/nansen-ai/nansen-cli/nansen-holder-analysis
---

# nansen-holder-analysis

skills/nansen-ai/nansen-cli/nansen-holder-analysis
nansen-holder-analysis
Installation
$ npx skills add https://github.com/nansen-ai/nansen-cli --skill nansen-holder-analysis
SKILL.md
Holder Quality

Answers: "Is this token held by quality wallets or retail noise?"

TOKEN=<address> CHAIN=ethereum

nansen research token holders --token $TOKEN --chain $CHAIN --smart-money --limit 20
# → address, address_label, value_usd, ownership_percentage, balance_change_24h/7d/30d

nansen research token flow-intelligence --token $TOKEN --chain $CHAIN
# → net_flow_usd and wallet_count per label: smart_trader, whale, exchange, fresh_wallets

nansen research token who-bought-sold --token $TOKEN --chain $CHAIN --limit 20
# → address, address_label, bought/sold_volume_usd, bought/sold_token_volume, trade_volume_usd


Red flag: high fresh_wallets flow + low SM holders. Green flag: Fund/Smart Trader labels in top 20.

Note: holders endpoint does not support native/wrapped tokens. Use a specific token contract address.

Weekly Installs
262
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