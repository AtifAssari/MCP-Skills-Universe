---
rating: ⭐⭐⭐
title: nansen-prediction-markets
url: https://skills.sh/nansen-ai/nansen-cli/nansen-prediction-markets
---

# nansen-prediction-markets

skills/nansen-ai/nansen-cli/nansen-prediction-markets
nansen-prediction-markets
Installation
$ npx skills add https://github.com/nansen-ai/nansen-cli --skill nansen-prediction-markets
SKILL.md
Prediction Market Screeners

All commands: nansen research prediction-market <sub> [options] (alias: nansen research pm <sub>)

No --chain flag needed — Polymarket runs on Polygon.

# Top events (groups of related markets)
nansen research pm event-screener --sort-by volume_24hr --limit 20
# → event_title, market_count, total_volume, total_volume_24hr, total_liquidity, total_open_interest, tags

# Top markets by 24h volume
nansen research pm market-screener --sort-by volume_24hr --limit 20
# → market_id, question, best_bid, best_ask, volume_24hr, liquidity, open_interest, unique_traders_24h

# Search for specific markets
nansen research pm market-screener --query "bitcoin" --limit 10

# Find resolved/closed markets
nansen research pm market-screener --status closed --limit 10

# Browse categories
nansen research pm categories --pretty
# → category, active_markets, total_volume_24hr, total_open_interest


Sort options: volume_24hr, volume, volume_1wk, volume_1mo, liquidity, open_interest, unique_traders_24h, age_hours

Screeners return active/open markets by default. Use --status closed for resolved markets.

Weekly Installs
300
Repository
nansen-ai/nansen-cli
GitHub Stars
121
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn