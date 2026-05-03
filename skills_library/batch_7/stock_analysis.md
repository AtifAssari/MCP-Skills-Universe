---
title: stock-analysis
url: https://skills.sh/alphamoemoe/foci/stock-analysis
---

# stock-analysis

skills/alphamoemoe/foci/stock-analysis
stock-analysis
Installation
$ npx skills add https://github.com/alphamoemoe/foci --skill stock-analysis
Summary

Comprehensive sentiment analysis report for individual stocks with bull and bear breakdowns.

Aggregates sentiment scores and viewpoint counts across multiple bloggers for a single ticker
Retrieves detailed arguments from both bullish and bearish perspectives with direct quotes and attribution
Identifies blogger positions and conviction levels (heavy/light holdings) to gauge skin-in-the-game confidence
Compiles risk factors and presents findings in a structured report format without buy/sell recommendations
Supports both English and Chinese ticker queries with localized output formatting
SKILL.md
Comprehensive Stock Analysis

Generate a complete sentiment analysis report for a single stock.

Triggers
"分析 NVDA"
"NVDA 怎么样"
"analyze TSLA"
"what about AAPL"
"帮我看看 AMD"
/stock-analysis NVDA
/stock-analysis {ticker}
Arguments
ticker - Stock ticker to analyze (required)
Instructions

When the user wants a comprehensive analysis of a stock, follow these steps:

Get Sentiment Data Call get_ticker_sentiment(ticker) to get overall sentiment and breakdown by blogger.

Search Related Viewpoints Call search_viewpoints(ticker) to find all detailed opinions.

Find Who Holds It Call get_blogger_positions for bloggers who mentioned the stock to understand their conviction level.

Compile Analysis Create a comprehensive report covering:

Overall sentiment score
Bull vs bear breakdown
Key arguments from both sides
Notable bloggers with positions
Risk factors mentioned

Present Results Format the output as:

## TICKER 综合分析报告

### 情绪概览

| 指标 | 数值 |
|------|------|
| 整体情绪 | 🟢 看涨 (X/10) |
| 看涨博主 | X 位 |
| 看跌博主 | X 位 |
| 中性/观望 | X 位 |
| 总提及次数 | XX |

### 多方观点 🐂

**核心论点:**
1. [论点1] — 博主A (XX万粉丝)
2. [论点2] — 博主B
3. [论点3] — 博主C

**代表观点:**
> "[详细观点引用]"
> — 博主A, 2025-01-20

### 空方观点 🐻

**核心论点:**
1. [论点1] — 博主D
2. [论点2] — 博主E

**代表观点:**
> "[详细观点引用]"
> — 博主D, 2025-01-19

### 持仓博主

| 博主 | 态度 | 持仓情况 |
|------|------|----------|
| 博主A | 看涨 | 重仓 |
| 博主B | 观望 | 轻仓 |

### 风险提示 ⚠️

- [风险1]: [描述]
- [风险2]: [描述]

### 总结
[客观总结各方观点，不做买卖建议]

Tool Sequence
get_ticker_sentiment(ticker) → Get sentiment breakdown
search_viewpoints(ticker) → Get detailed viewpoints
list_bloggers → Get blogger info (if needed for context)
get_blogger_positions(blogger) → For key bloggers mentioning the stock
Compile comprehensive report
Notes
Present all viewpoints fairly, both bull and bear
Include specific quotes when available
Do NOT give buy/sell recommendations
Highlight consensus and divergence
Note the recency of viewpoints
Weekly Installs
941
Repository
alphamoemoe/foci
GitHub Stars
6
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn