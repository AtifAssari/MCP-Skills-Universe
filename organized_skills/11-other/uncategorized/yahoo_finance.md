---
rating: ⭐⭐
title: yahoo-finance
url: https://skills.sh/0juano/agent-skills/yahoo-finance
---

# yahoo-finance

skills/0juano/agent-skills/yahoo-finance
yahoo-finance
Installation
$ npx skills add https://github.com/0juano/agent-skills --skill yahoo-finance
SKILL.md
Yahoo Finance CLI

Financial data terminal powered by Yahoo Finance. All commands via the yf script.

Setup

The script is at {baseDir}/scripts/yf. It uses uv run --script with inline PEP 723 metadata — dependencies install automatically on first run.

chmod +x {baseDir}/scripts/yf

Commands
Command	Purpose	Example
yf price TICKER	Quick price + change + volume	yf price YPF
yf quote TICKER	Detailed quote (52w, PE, yield)	yf quote AAPL
yf compare T1,T2,T3	Side-by-side comparison table	yf compare YPF,PAM,GGAL
yf credit TICKER	Credit analysis: leverage, coverage, debt maturity	yf credit YPF
yf macro	Morning macro dashboard (UST, DXY, VIX, oil, gold, BTC, ARS)	yf macro
yf fx [BASE]	LatAm FX rates (ARS, BRL, CLP, MXN, COP)	yf fx USD
yf flows ETF	ETF top holdings + fund data	yf flows EMB
yf history TICKER [PERIOD]	Price history (1d/5d/1mo/3mo/6mo/1y/ytd/max)	yf history YPF 3mo
yf fundamentals TICKER	Full financials (IS, BS, CF)	yf fundamentals YPF
yf news TICKER	Recent news headlines	yf news YPF
yf search QUERY	Find tickers	yf search "argentina bond"

All commands support --json for machine-readable output.

When to Use Which Command
Morning check: yf macro → get UST yields, DXY, VIX, commodities, BTC, ARS in one shot
Quick look: yf price TICKER → fast price/change/volume
Deep dive equity: yf quote → yf fundamentals → yf history
Credit analysis: yf credit TICKER → leverage ratios, interest coverage, debt breakdown
EM/LatAm FX: yf fx → all major LatAm pairs vs USD
ETF research: yf flows ETF → top holdings, AUM, expense ratio
Comparison: yf compare → side-by-side for relative value
Error Handling

The script handles bad tickers, missing data, and rate limits gracefully with clear error messages. If Yahoo Finance rate-limits, wait a moment and retry.

Output

By default, output uses Rich tables for clean terminal display. Add --json to any command for structured JSON output suitable for piping or further processing.

Weekly Installs
374
Repository
0juano/agent-skills
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn