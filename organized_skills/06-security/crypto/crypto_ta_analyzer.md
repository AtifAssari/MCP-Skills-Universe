---
rating: ⭐⭐
title: crypto-ta-analyzer
url: https://skills.sh/dkyazzentwatwa/chatgpt-skills/crypto-ta-analyzer
---

# crypto-ta-analyzer

skills/dkyazzentwatwa/chatgpt-skills/crypto-ta-analyzer
crypto-ta-analyzer
Installation
$ npx skills add https://github.com/dkyazzentwatwa/chatgpt-skills --skill crypto-ta-analyzer
Summary

29+ technical indicators with 7-tier trading signals, divergence detection, and volume confirmation for crypto and stocks.

Combines 29 proven indicators (RSI, MACD, Bollinger Bands, Ichimoku, OBV, and 24 others) weighted by reliability to generate consensus-based buy/sell signals
Detects bullish and bearish divergences across RSI, MACD, and OBV; identifies Bollinger Band squeezes and volume confirmation levels
Supports multiple data sources including CoinGecko, exchange APIs, Yahoo Finance, and custom price data with automatic OHLCV normalization
Generates detailed output including 7-tier signal classification (STRONG_BUY to STRONG_SELL), confidence scores, individual indicator signals, and regime analysis (trending vs ranging)
SKILL.md
Crypto TA Analyzer

Use the bundled indicators when the user needs explicit technical analysis rather than a narrative market opinion.

Workflow
Get normalized OHLCV data first.
Use scripts/data_converter.py or scripts/coingecko_converter.py when source formats need reshaping.
Run scripts/ta_analyzer.py for the actual indicator stack and signal scoring.
Explain indicator agreement, conflicts, and regime sensitivity instead of presenting one number without context.
Guardrails
Do not present signals as guaranteed outcomes.
Keep the distinction clear between deterministic indicator output and discretionary interpretation.
Weekly Installs
1.3K
Repository
dkyazzentwatwa/…t-skills
GitHub Stars
53
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass