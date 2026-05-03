---
title: fin-guru-research
url: https://skills.sh/aojdevstudio/finance-guru/fin-guru-research
---

# fin-guru-research

skills/aojdevstudio/finance-guru/fin-guru-research
fin-guru-research
Installation
$ npx skills add https://github.com/aojdevstudio/finance-guru --skill fin-guru-research
SKILL.md
Research Workflow Skill

Execute structured market research with source validation and temporal awareness.

Workflow Steps
Scope Definition — Clarify research objectives, timeframe, and deliverable format
Data Collection — Gather intelligence from multiple sources with temporal qualifiers
Source Validation — Flag market data older than same-day, economic data older than 30 days
Analysis — Apply analytical frameworks to collected data
Synthesis — Produce research summary with confidence levels and data gaps
Handoff — Package findings for downstream analysis (quant, strategy)
Tools Integration
screener_cli.py — Multi-pattern technical screening (8 patterns)
moving_averages_cli.py — Trend identification (SMA/EMA/WMA/HMA)
momentum_cli.py — Confluence analysis (RSI, MACD, Stochastic, Williams %R, ROC)
volatility_cli.py — Regime analysis and opportunity assessment
data_validator_cli.py — Data integrity verification (100% quality required)
itc_risk_cli.py — Market-implied risk scores for supported tickers
Requirements
ALL web searches MUST include temporal qualifiers using current date context
Separate verified data from assumptions with confidence levels
Cite all sources with START/END tags and precise timestamps
Flag data gaps relevant to downstream analysis
Weekly Installs
11
Repository
aojdevstudio/fi…nce-guru
GitHub Stars
303
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn