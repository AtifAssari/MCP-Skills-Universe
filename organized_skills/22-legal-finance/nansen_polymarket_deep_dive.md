---
rating: ⭐⭐⭐
title: nansen-polymarket-deep-dive
url: https://skills.sh/nansen-ai/nansen-cli/nansen-polymarket-deep-dive
---

# nansen-polymarket-deep-dive

skills/nansen-ai/nansen-cli/nansen-polymarket-deep-dive
nansen-polymarket-deep-dive
Installation
$ npx skills add https://github.com/nansen-ai/nansen-cli --skill nansen-polymarket-deep-dive
SKILL.md
Prediction Market Deep Dive

Answers: "What's happening in this specific market? Who holds it, who's trading it?"

Use market_id from the screener (nansen-prediction-market skill).

MID=<market_id>

nansen research pm ohlcv --market-id $MID --sort period_start:desc --limit 50
# → period_start, open, high, low, close, volume

nansen research pm orderbook --market-id $MID
# → bids[], asks[] with price and size

nansen research pm top-holders --market-id $MID --limit 20
# → address, side, position_size, avg_entry_price, current_price, unrealized_pnl_usd

nansen research pm position-detail --market-id $MID --limit 20
# → address, side, size, avg_entry_price, current_price, pnl

nansen research pm trades-by-market --market-id $MID --limit 20
# → timestamp, buyer, seller, taker_action, side, size, price, usdc_value

nansen research pm pnl-by-market --market-id $MID --limit 20
# → address, side_held, net_buy_cost_usd, unrealized_value_usd, total_pnl_usd


Notes:

--market-id is a numeric ID from the screener, not a slug.
Works with any market ID regardless of status (active or closed/resolved).
All addresses are Polygon (EVM).
Weekly Installs
273
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