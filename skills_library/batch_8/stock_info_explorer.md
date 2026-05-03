---
title: stock-info-explorer
url: https://skills.sh/sundial-org/awesome-openclaw-skills/stock-info-explorer
---

# stock-info-explorer

skills/sundial-org/awesome-openclaw-skills/stock-info-explorer
stock-info-explorer
Installation
$ npx skills add https://github.com/sundial-org/awesome-openclaw-skills --skill stock-info-explorer
SKILL.md
Stock Information Explorer

This skill fetches OHLCV data from Yahoo Finance via yfinance and computes technical indicators locally (no API key required).

Commands
1) Real-time Quotes (price)
uv run --script scripts/yf.py price TSLA
# shorthand
uv run --script scripts/yf.py TSLA

2) Fundamental Summary (fundamentals)
uv run --script scripts/yf.py fundamentals NVDA

3) ASCII Trend (history)
uv run --script scripts/yf.py history AAPL 6mo

4) Professional Chart (pro)

Generates a high-resolution PNG chart. By default it includes Volume and Moving Averages (MA5/20/60).

# candle (default)
uv run --script scripts/yf.py pro 000660.KS 6mo

# line
uv run --script scripts/yf.py pro 000660.KS 6mo line

Indicators (optional)

Add flags to include indicator panels/overlays.

uv run --script scripts/yf.py pro TSLA 6mo --rsi --macd --bb
uv run --script scripts/yf.py pro TSLA 6mo --vwap --atr

--rsi : RSI(14)
--macd: MACD(12,26,9)
--bb : Bollinger Bands(20,2)
--vwap: VWAP (cumulative for the selected range)
--atr : ATR(14)
5) One-shot Report (report) ⭐

Prints a compact text summary (price + fundamentals + indicator signals) and automatically generates a Pro chart with BB + RSI + MACD.

uv run --script scripts/yf.py report 000660.KS 6mo
# output includes: CHART_PATH:/tmp/<...>.png

Ticker Examples
US stocks: AAPL, NVDA, TSLA
KR stocks: 005930.KS, 000660.KS
Crypto: BTC-USD, ETH-KRW
Forex: USDKRW=X
Notes / Limitations
Indicators are computed locally from price data (Yahoo does not reliably provide precomputed indicator series).
Data quality may vary by ticker/market (e.g., missing volume for some symbols).

Korean note: 실시간 시세 + 펀더멘털 + 기술지표(차트/요약)까지 한 번에 처리하는 종합 주식 분석 스킬입니다.

Weekly Installs
468
Repository
sundial-org/awe…w-skills
GitHub Stars
589
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass