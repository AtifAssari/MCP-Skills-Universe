---
title: stock-market-pro
url: https://skills.sh/sundial-org/awesome-openclaw-skills/stock-market-pro
---

# stock-market-pro

skills/sundial-org/awesome-openclaw-skills/stock-market-pro
stock-market-pro
Installation
$ npx skills add https://github.com/sundial-org/awesome-openclaw-skills --skill stock-market-pro
Summary

Real-time stock quotes, fundamental analysis, and professional charts across global markets and crypto.

Covers five command categories: real-time price quotes, candlestick and line charts with moving averages, fundamental metrics (PE, EPS, ROE, profit margins), earnings dates with consensus estimates, and 10-day historical trends
Supports US stocks, Korean exchange tickers, cryptocurrency pairs, and forex with no API key required
Generates high-resolution PNG charts with volume indicators and configurable periods from 1 month to max historical data
Built on Python 3.11+ with automatic dependency management via uv
SKILL.md
Stock Market Pro

A professional-grade financial analysis tool powered by Yahoo Finance data.

Core Features
1. Real-time Quotes (price)

Get instant price updates and day ranges.

uv run --script scripts/yf price [TICKER]

2. Professional Charts (pro)

Generate high-resolution PNG charts with Volume and Moving Averages.

Candlestick: uv run --script scripts/yf pro [TICKER] [PERIOD]
Line Chart: uv run --script scripts/yf pro [TICKER] [PERIOD] line
Periods: 1mo, 3mo, 6mo, 1y, 5y, max, etc.
3. Fundamental Analysis (fundamentals)

Deep dive into valuation: Market Cap, PE, EPS, ROE, and Profit Margins.

uv run --script scripts/yf fundamentals [TICKER]

4. Earnings & Estimates (earnings)

Check upcoming earnings dates and market consensus (Expected Revenue/EPS).

5. Historical Trends (history)

View recent 10-day trends with terminal-friendly ASCII charts.

Ticker Examples
US Stocks: AAPL, NVDA, TSLA
Korean Stocks: 005930.KS (Samsung), 000660.KS (SK Hynix)
Crypto: BTC-USD, ETH-KRW
Technical Notes
Engine: Python 3.11+, yfinance, mplfinance, rich
Key Benefit: No API key required. Automatically handles dependencies via uv.

한국어 설명: 실시간 주가 조회, 재무 지표 분석 및 전문 봉차트 생성이 가능한 종합 주식 분석 스킬입니다.

Weekly Installs
3.0K
Repository
sundial-org/awe…w-skills
GitHub Stars
589
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn