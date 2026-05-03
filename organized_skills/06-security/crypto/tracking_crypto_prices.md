---
rating: ⭐⭐⭐
title: tracking-crypto-prices
url: https://skills.sh/jeremylongshore/claude-code-plugins-plus-skills/tracking-crypto-prices
---

# tracking-crypto-prices

skills/jeremylongshore/claude-code-plugins-plus-skills/tracking-crypto-prices
tracking-crypto-prices
Installation
$ npx skills add https://github.com/jeremylongshore/claude-code-plugins-plus-skills --skill tracking-crypto-prices
SKILL.md
Tracking Crypto Prices
Contents

Overview | Prerequisites | Instructions | Output | Error Handling | Examples | Resources

Overview

Foundation skill providing real-time and historical cryptocurrency price data for 10,000+ coins. This is the data layer for the crypto plugin ecosystem -- 10+ other skills depend on it for price information.

Prerequisites
Install dependencies: pip install requests pandas yfinance
Optional: pip install python-dotenv for API key management
Optional: Get free API key from https://www.coingecko.com/en/api for higher rate limits
Add API key to ${CLAUDE_SKILL_DIR}/config/settings.yaml or set COINGECKO_API_KEY env var
Instructions
Check current prices for one or more symbols:
python ${CLAUDE_SKILL_DIR}/scripts/price_tracker.py --symbol BTC
python ${CLAUDE_SKILL_DIR}/scripts/price_tracker.py --symbols BTC,ETH,SOL

Use watchlists to scan predefined groups (available: top10, defi, layer2, stablecoins, memecoins):
python ${CLAUDE_SKILL_DIR}/scripts/price_tracker.py --watchlist top10     # Top 10 by market cap
python ${CLAUDE_SKILL_DIR}/scripts/price_tracker.py --watchlist defi      # DeFi tokens
python ${CLAUDE_SKILL_DIR}/scripts/price_tracker.py --watchlist layer2    # Layer 2 tokens

Fetch historical data by period or custom date range:
python ${CLAUDE_SKILL_DIR}/scripts/price_tracker.py --symbol BTC --period 30d
python ${CLAUDE_SKILL_DIR}/scripts/price_tracker.py --symbol BTC --period 90d --output csv
python ${CLAUDE_SKILL_DIR}/scripts/price_tracker.py --symbol ETH --start 2024-01-01 --end 2024-12-31  # 2024 full year

Configure settings by editing ${CLAUDE_SKILL_DIR}/config/settings.yaml to customize cache TTLs, default currency, and custom watchlists. See references/implementation.md for the full configuration reference.
Output
Table (default): Symbol, price, 24h change, volume, market cap in formatted columns
JSON (--format json): Machine-readable with prices array and metadata
CSV (--output csv): OHLCV historical data export to ${CLAUDE_SKILL_DIR}/data/

See ${CLAUDE_SKILL_DIR}/references/implementation.md for detailed output format examples.

Error Handling
Error	Cause	Solution
Unknown symbol: XYZ	Invalid ticker	Check spelling, use --list to search
Rate limit exceeded	Too many API calls	Wait 60s, or add API key for higher limits
Network error	No internet	Check connection; cached data used automatically
Cache stale	Data older than TTL	Shown with warning, refreshes on next call

The skill auto-manages rate limits: cache first, exponential backoff, yfinance fallback, stale cache as last resort.

Examples

Quick price check:

python ${CLAUDE_SKILL_DIR}/scripts/price_tracker.py --symbol BTC
# Output: BTC (Bitcoin) $97,234.56 USD +2.34% (24h) | Vol: $28.5B | MCap: $1.92T


Watchlist scan:

python ${CLAUDE_SKILL_DIR}/scripts/price_tracker.py --watchlist top10


Historical export:

python ${CLAUDE_SKILL_DIR}/scripts/price_tracker.py --symbol ETH --period 90d --output csv
# Creates: ${CLAUDE_SKILL_DIR}/data/ETH_90d_[date].csv

Resources
${CLAUDE_SKILL_DIR}/references/implementation.md - Output formats, full config, integration guide, file map
CoinGecko API - Primary data source
yfinance - Fallback for historical data
Weekly Installs
281
Repository
jeremylongshore…s-skills
GitHub Stars
2.1K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn