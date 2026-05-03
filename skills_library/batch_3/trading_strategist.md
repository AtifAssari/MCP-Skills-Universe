---
title: trading-strategist
url: https://skills.sh/kukapay/crypto-skills/trading-strategist
---

# trading-strategist

skills/kukapay/crypto-skills/trading-strategist
trading-strategist
Installation
$ npx skills add https://github.com/kukapay/crypto-skills --skill trading-strategist
Summary

Data-driven cryptocurrency trading strategies combining Binance market data, technical indicators, and sentiment analysis.

Integrates real-time and historical price/volume data from Binance with calculated TA indicators (SMA, RSI, MACD, Bollinger Bands, Stochastic)
Aggregates market sentiment from crypto RSS feeds to inform buy/sell/hold signals and entry/exit recommendations
Generates risk management guidance including stop-loss levels, position sizing (1-5% of capital), and volatility warnings
Supports multiple timeframes and analysis depths, from quick ticker snapshots to extended 50-100 day historical analysis for swing trading
SKILL.md
Trading Strategies Skill

This skill generates data-driven trading strategies for cryptocurrencies by integrating multiple data sources and analytical tools.

Core Components
Binance Market Data: Real-time price, volume, and historical klines from Binance API
Technical Analysis (TA): Calculated indicators including SMA, RSI, MACD, Bollinger Bands, Stochastic, and more
Market Sentiment: Aggregated sentiment scores from popular crypto RSS feeds
Workflow
Step 1: Data Collection
Fetch current ticker data from Binance API (/api/v3/ticker/price and /api/v3/ticker/24hr)
Retrieve historical klines (/api/v3/klines with 30-100 days of data)
Aggregate sentiment using the market-sentiment skill
Step 2: TA Calculation

Use the scripts/calculate_ta.py script to compute indicators from historical data.

Step 3: Strategy Generation

Combine TA signals, price action, and sentiment score to recommend:

Buy/Sell/Hold signals
Entry/exit points
Risk management (stop-loss, position sizing)
Timeframes (swing, day trading)
Usage Examples
Basic Strategy Request
For ETH, generate a trading strategy based on current market data.


→ Fetch ETH data, calculate TA, get sentiment, output strategy.

Advanced Analysis
Analyze BTC with 50-day history, include sentiment, recommend swing trade.


→ Use longer history, focus on swing signals.

Risk Management
Always include stop-loss recommendations
Suggest position sizes (1-5% of capital)
Warn about volatility and leverage risks
Note: Not financial advice
References
TA formulas: See references/ta_formulas.md
Sentiment interpretation: See references/sentiment_guide.md
Scripts
scripts/calculate_ta.py: Python script for TA indicator calculations
scripts/fetch_binance.py: Helper for Binance API calls ./skills/trading-strategies/SKILL.md
Weekly Installs
592
Repository
kukapay/crypto-skills
GitHub Stars
17
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn