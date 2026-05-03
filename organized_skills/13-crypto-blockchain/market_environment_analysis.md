---
rating: ⭐⭐⭐
title: market-environment-analysis
url: https://skills.sh/tradermonty/claude-trading-skills/market-environment-analysis
---

# market-environment-analysis

skills/tradermonty/claude-trading-skills/market-environment-analysis
market-environment-analysis
Installation
$ npx skills add https://github.com/tradermonty/claude-trading-skills --skill market-environment-analysis
Summary

Global market analysis with real-time data collection, risk sentiment assessment, and professional reporting.

Analyzes US, European, and Asian stock indices, forex pairs, commodities, and Treasury yields to assess market conditions and risk-on/risk-off sentiment
Requires WebSearch access for real-time data; no API keys needed
Generates structured reports covering executive summary, sector rotation, key economic events, and investment strategy implications
Includes utility functions for formatting reports, interpreting VIX levels, and checking trading hours across timezones
SKILL.md
Market Environment Analysis

Comprehensive analysis tool for understanding market conditions and creating professional market reports anytime.

When to Use
When you need a comprehensive overview of global market conditions
Before making trading or investment decisions
For daily/weekly market briefings
When assessing risk-on/risk-off sentiment
For understanding inter-market correlations and sector rotation
When preparing market reports for clients or personal records
Prerequisites
WebSearch access: Required for fetching real-time market data
No API keys required: This skill uses web search for data collection
Optional: Economic calendar data for event-driven analysis
Core Workflow
1. Initial Data Collection

Collect latest market data using web_search tool:

Major stock indices (S&P 500, NASDAQ, Dow, Nikkei 225, Shanghai Composite, Hang Seng)
Forex rates (USD/JPY, EUR/USD, major currency pairs)
Commodity prices (WTI crude, Gold, Silver)
US Treasury yields (2-year, 10-year, 30-year)
VIX index (Fear gauge)
Market trading status (open/close/current values)
2. Market Environment Assessment

Evaluate the following from collected data:

Trend Direction: Uptrend/Downtrend/Range-bound
Risk Sentiment: Risk-on/Risk-off
Volatility Status: Market anxiety level from VIX
Sector Rotation: Where capital is flowing
3. Report Structure
Standard Report Format:
1. Executive Summary (3-5 key points)
2. Global Market Overview
   - US Markets
   - Asian Markets
   - European Markets
3. Forex & Commodities Trends
4. Key Events & Economic Indicators
5. Risk Factor Analysis
6. Investment Strategy Implications

Script Usage
market_utils.py

Provides common functions for report creation:

# Generate report header
python scripts/market_utils.py

# Available functions:
- format_market_report_header(): Create header
- get_market_session_times(): Check trading hours
- categorize_volatility(vix): Interpret VIX levels
- format_percentage_change(value): Format price changes

Reference Documentation
Key Indicators Interpretation

Load references/indicators.md when you need:

Important levels for each index
Technical analysis key points
Sector-specific focus areas
Analysis Patterns

Load references/analysis_patterns.md when analyzing:

Risk-on/Risk-off criteria
Economic indicator interpretation
Inter-market correlations
Seasonality and market anomalies
Output Examples
Quick Summary Version
📊 Market Summary [2025/01/15 14:00]
━━━━━━━━━━━━━━━━━━━━━
【US】S&P 500: 5,123.45 (+0.45%)
【JP】Nikkei 225: 38,456.78 (-0.23%)
【FX】USD/JPY: 149.85 (↑0.15)
【VIX】16.2 (Normal range)

⚡ Key Events
- Japan GDP Flash
- US Employment Report

📈 Environment: Risk-On Continues

Detailed Analysis Version

Start with executive summary, then analyze each section in detail. Key clarifications:

Current market phase (Bullish/Bearish/Neutral)
Short-term direction (1-5 days outlook)
Risk events to monitor
Recommended position adjustments
Important Considerations
Timezone Awareness
Consider all major market timezones
US markets: Evening to early morning (Asian time)
European markets: Afternoon to evening (Asian time)
Asian markets: Morning to afternoon (Local time)
Economic Calendar Priority

Categorize by importance:

⭐⭐⭐ Critical (FOMC, NFP, CPI, etc.)
⭐⭐ Important (GDP, Retail Sales, etc.)
⭐ Reference level
Data Source Priority
Official releases (Central banks, Government statistics)
Major financial media (Bloomberg, Reuters)
Broker reports
Analyst consensus estimates
Troubleshooting
Data Collection Notes
Check market holidays (holiday calendars)
Be aware of daylight saving time changes
Distinguish between flash and final data
Market Volatility Response
First organize the facts
Reference historical similar events
Verify with multiple sources
Maintain objective analysis
Customization Options

Adjust based on user's investment style:

Day Traders: Intraday charts, order flow focus
Swing Traders: Daily/weekly technicals emphasis
Long-term Investors: Fundamentals, macro economics focus
Forex Traders: Currency correlations, interest rate differentials
Options Traders: Volatility analysis, Greeks monitoring
Resources
references/indicators.md - Key market indicators and interpretation guides
references/analysis_patterns.md - Risk-on/risk-off criteria and inter-market correlations
scripts/market_utils.py - Utility functions for report formatting and market status
Weekly Installs
704
Repository
tradermonty/cla…g-skills
GitHub Stars
1.2K
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn