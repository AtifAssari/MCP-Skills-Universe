---
title: nansen-perp-screener
url: https://skills.sh/nansen-ai/nansen-cli/nansen-perp-screener
---

# nansen-perp-screener

skills/nansen-ai/nansen-cli/nansen-perp-screener
nansen-perp-screener
Installation
$ npx skills add https://github.com/nansen-ai/nansen-cli --skill nansen-perp-screener
SKILL.md
Perp Market Scan

Answers: "What's the state of the Hyperliquid perp market right now?"

nansen research perp screener --sort volume:desc --limit 20
# → token_symbol, volume, buy/sell_volume, buy_sell_pressure, open_interest, funding, mark_price

nansen research perp leaderboard --days 7 --limit 20
# → trader_address, trader_address_label, total_pnl, roi, account_value

nansen research smart-money perp-trades --limit 20
# → token_symbol, side, action (Open/Close), value_usd, price_usd, trader_address_label

Weekly Installs
261
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