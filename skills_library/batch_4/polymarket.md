---
title: polymarket
url: https://skills.sh/machina-sports/sports-skills/polymarket
---

# polymarket

skills/machina-sports/sports-skills/polymarket
polymarket
Installation
$ npx skills add https://github.com/machina-sports/sports-skills --skill polymarket
SKILL.md
Polymarket — Sports Prediction Markets

Before writing queries, consult references/api-reference.md for sport codes, command parameters, and price format.

Quick Start

Prefer the CLI — it avoids Python import path issues:

sports-skills polymarket search_markets --sport=nba --sports_market_types=moneyline
sports-skills polymarket get_todays_events --sport=epl
sports-skills polymarket search_markets --sport=epl --query="Leeds" --sports_market_types=moneyline
sports-skills polymarket get_sports_config


Python SDK (alternative):

from sports_skills import polymarket

polymarket.search_markets(sport='nba', sports_market_types='moneyline')
polymarket.get_todays_events(sport='epl')
polymarket.search_markets(sport='epl', query='Leeds')
polymarket.get_sports_config()

CRITICAL: Before Any Query

CRITICAL: Before calling any market endpoint, verify:

The sport parameter is always passed to search_markets and get_todays_events for single-game markets.
Prices are probabilities on a 0-1 scale (0.65 = 65%) — no conversion needed.
For price/orderbook endpoints, use token_id (CLOB), not market_id (Gamma). Call get_market_details first to get clobTokenIds.

Without the sport parameter:

WRONG: search_markets(query="Leeds")           → 0 results
RIGHT: search_markets(sport='epl', query='Leeds') → returns all Leeds markets

Prerequisites

Core commands (no dependencies, no API keys): All read commands work out of the box.

Trading commands require py_clob_client:

pip install sports-skills[polymarket]


Additionally requires a configured wallet:

export POLYMARKET_PRIVATE_KEY=0x...

Workflows
Find Single-Game Markets for a Sport
search_markets --sport=nba (or epl, nfl, bun, etc.)
Each market includes outcomes with prices (price = probability).
For detailed prices, use get_market_prices --token_id=<clob_token_id>.
Today's Events for a League
get_todays_events --sport=epl — returns events sorted by start date.
Each event includes nested markets (moneyline, spreads, totals, props).
Pick a market, get clob_token_id from outcomes, then get_market_prices.
Live Odds Check
search_markets --sport=nba --query="Lakers" --sports_market_types=moneyline
get_market_prices --token_id=<id> for live CLOB prices.
Present probabilities.
Price Trend Analysis
Find market via search_markets --sport=nba.
Get clob_token_id from the outcomes.
get_price_history --token_id=<id> --interval=1w
Present price movement.
Commands
Command	Description
get_sports_config	Available sport codes
get_todays_events	Today's events for a league
search_markets	Find markets by sport, keyword, and type
get_sports_markets	Browse all sports markets
get_sports_events	Browse sports events
get_series	List series (leagues)
get_market_details	Single market details
get_event_details	Single event details
get_market_prices	Current CLOB prices
get_order_book	Full order book
get_price_history	Historical prices
get_last_trade_price	Most recent trade

See references/api-reference.md for full parameter lists and return shapes.

Examples

Example 1: Tonight's NBA favorites User says: "Who's favored in tonight's NBA games?" Actions:

Call search_markets(sport='nba', sports_market_types='moneyline') Result: Each matchup with implied win probabilities (price = probability)

Example 2: Team-specific odds User says: "Show me Leeds vs Man City odds" Actions:

Call search_markets(sport='epl', query='Leeds', sports_market_types='moneyline') Result: Leeds moneyline market with outcome prices

Example 3: Today's EPL events User says: "What EPL matches are on today?" Actions:

Call get_todays_events(sport='epl') Result: Today's EPL events with nested markets (moneyline, spreads, totals, props)

Example 4: League winner futures User says: "Who will win the Premier League?" Actions:

Call search_markets(query='Premier League') — returns futures
Sort results by Yes outcome price descending Result: Top contenders ranked by win probability

Example 5: Bundesliga odds User says: "Show me Bundesliga odds for Dortmund vs Bayern" Actions:

Call search_markets(sport='bun', query='Dortmund', sports_market_types='moneyline') Result: Dortmund/Bayern moneyline market with outcome prices
Commands that DO NOT exist — never call these
cli_search_markets — does not exist. Use search_markets instead.
cli_sports_list — does not exist. Use get_sports_config instead.
get_market_odds / get_odds / get_current_odds — prices ARE probabilities. Use get_market_prices(token_id=...).
get_implied_probability — the price IS the implied probability.
get_markets — use get_sports_markets (browse) or search_markets (search).
get_team_schedule — this is a football-data command, not polymarket.

If a command is not listed in references/api-reference.md, it does not exist.

Troubleshooting

Error: search_markets returns 0 results Cause: The sport parameter is missing — without it, search only checks high-volume markets and misses single-game events Solution: Always pass sport='<code>' to search_markets. Check references/api-reference.md for valid sport codes

Error: get_market_prices fails or returns wrong data Cause: market_id (Gamma) was used instead of token_id (CLOB) Solution: Call get_market_details(market_id=<id>) first to get the CLOB clobTokenIds, then use those with get_market_prices

Error: Prices seem stale or unchanged Cause: Low-liquidity market — may have wide spreads and infrequent trades Solution: Check get_last_trade_price(token_id=<id>) for the most recent actual trade price

Error: Trading commands fail Cause: py_clob_client is not installed or wallet is not configured Solution: Run pip install sports-skills[polymarket] and set POLYMARKET_PRIVATE_KEY environment variable

Weekly Installs
490
Repository
machina-sports/…s-skills
GitHub Stars
90
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail