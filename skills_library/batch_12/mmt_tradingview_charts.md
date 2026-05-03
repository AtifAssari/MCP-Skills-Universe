---
title: mmt-tradingview-charts
url: https://skills.sh/emeraldls/mmt-agent-skills/mmt-tradingview-charts
---

# mmt-tradingview-charts

skills/emeraldls/mmt-agent-skills/mmt-tradingview-charts
mmt-tradingview-charts
Installation
$ npx skills add https://github.com/emeraldls/mmt-agent-skills --skill mmt-tradingview-charts
SKILL.md
MMT + TradingView Lightweight Charts

Rules for building charting applications that render MMT market data using TradingView Lightweight Charts (v5.x).

Chart Setup
Chart Initialization: createChart config, container setup, autoSize, dark/light themes
Data Mapping: transform MMT types (OHLCVTPublic, etc.) to Lightweight Charts format
Real-Time Updates
Live Candlestick Updates: WS candle stream to series.update(), handling candle close vs in-progress
Live Trade Ticker: WS trade stream to line/marker overlays, trade volume histogram
Multi-Chart Patterns
Multi-Pane Layout: price + volume + indicator panes, synchronized time scales
Multi-Symbol Comparison: overlay multiple symbols, normalize price scales
Indicators & Overlays
Volume Histogram: buy/sell volume from MMT candles as colored histogram
Funding Rate Overlay: stats channel funding rate as line/baseline series
Open Interest Overlay: OI candles as area/line on separate pane
Data Management
Historical Data Loading: REST fetch to setData, pagination for long ranges, loading states
Timeframe & Symbol Switching: clear stores, flush timers, reload on tf/symbol/exchange change
Interaction
Crosshair & Tooltips: subscribeCrosshairMove, custom tooltip with MMT data fields
Chart Lifecycle: React/framework integration, cleanup, resize, memory management
Framework Integration
React Integration Patterns: hooks, refs, lifecycle, state management, performance patterns
Weekly Installs
141
Repository
emeraldls/mmt-a…t-skills
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass