---
rating: ⭐⭐
title: data912-market-data
url: https://skills.sh/ferminrp/agent-skills/data912-market-data
---

# data912-market-data

skills/ferminrp/agent-skills/data912-market-data
data912-market-data
Installation
$ npx skills add https://github.com/ferminrp/agent-skills --skill data912-market-data
SKILL.md
Data912 Market Data

Query Data912's public market API for Argentina and USA market data snapshots, historical bars, and EOD derivatives analytics.

API Overview
Base URL: https://data912.com
Auth: None required (public API)
Format: JSON responses
Source note: Data912 describes this API as educational/hobby data and explicitly not real-time.
Caching note: Server metadata indicates roughly 2-hour Cloudflare caching.
Endpoint Groups
1. Live Market Panels
/live/mep (USD MEP)
/live/ccl (USD CCL)
/live/arg_stocks
/live/arg_options
/live/arg_cedears
/live/arg_notes
/live/arg_corp
/live/arg_bonds
/live/usa_adrs
/live/usa_stocks

Example:

curl -s "https://data912.com/live/arg_stocks" | jq '.[0:5]'

2. Historical OHLC
/historical/stocks/{ticker}
/historical/cedears/{ticker}
/historical/bonds/{ticker}

Example:

curl -s "https://data912.com/historical/stocks/GGAL" | jq '.[0:10]'

3. EOD Derivatives Analytics
/eod/volatilities/{ticker}
/eod/option_chain/{ticker}

Examples:

curl -s "https://data912.com/eod/volatilities/AAPL" | jq '.'
curl -s "https://data912.com/eod/option_chain/AAPL" | jq '.[0:10]'

Out of Scope for This Skill
Do not use /contact in this skill. Keep this skill focused on market data retrieval and interpretation.
Key Fields
Panel Fields (/live/*)
symbol: instrument ticker/symbol
px_bid, q_bid: bid price and bid size
px_ask, q_ask: ask price and ask size
c: last/close-like traded value
pct_change: percentage variation
v: volume
q_op: operations count (when provided)
Historical Fields (/historical/*/{ticker})
date: date string
o, h, l, c: OHLC values
v: volume
dr: daily return
sa: additional numeric metric provided by source
Volatility Metrics (/eod/volatilities/{ticker})
IV term structure: iv_s_term, iv_m_term, iv_l_term
IV percentiles: iv_*_percentile
HV term structure: hv_s_term, hv_m_term, hv_l_term
HV percentiles: hv_*_percentile
Relative-value ratios: iv_hv_*_ratio, iv_fair_iv_ratio
Fair value reference: fair_iv, fair_iv_percentile
Option Chain Fields (/eod/option_chain/{ticker})
Contract context: opex, s_symbol, type, k
Market data: bid, ask, c, oi
Greeks: delta, gamma, theta, vega, rho
Valuation/probabilities: fair_value, fair_iv, itm_prob, intrinsic, otm
Horizon context: r_days, r_tdays, hv_2m, hv_1yr
Workflow
Identify intent and select endpoint group:
FX/panel snapshot -> /live/*
Time series/evolution -> /historical/*/{ticker}
Options/risk analytics -> /eod/*/{ticker}
Validate required input:
For historical/EOD endpoints, require a ticker symbol.
If ticker is missing, ask for it before querying.
Fetch data with curl -s and parse with jq.
Handle empty arrays:
If response is [], report: "No data currently available for this endpoint/ticker."
Present an actionable summary:
Start with a short snapshot.
Then include relevant detail fields requested by the user.
Keep context clear:
Remind users this is educational/non-real-time data.
Avoid turning output into trading advice.
Error Handling
429 Too Many Requests:
Most market endpoints publish 120 req/min.
Back off and retry after a short delay; avoid burst loops.
422 Validation Error:
Usually invalid/missing path input such as ticker formatting.
Re-check symbol and endpoint before retrying.
Network/timeout failures:
Retry a small number of times (for example, 2 retries with delay).
If still failing, return a clear failure message and the endpoint attempted.
Presenting Results

When returning results to the user:

Lead with a concise snapshot (what moved, where, and magnitude).
For panel requests, compare bid/ask/last and % change.
For historical requests, summarize trend windows and notable jumps.
For vol/options requests, highlight percentiles and IV/HV relationships.
Explicitly mention the data is educational/non-real-time.
Do not provide financial recommendations.
OpenAPI Spec

For the full schema and endpoint definitions, see references/openapi-spec.json.

Weekly Installs
35
Repository
ferminrp/agent-skills
GitHub Stars
35
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass