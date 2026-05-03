---
title: akshare
url: https://skills.sh/succ985/openclaw-akshare-skill/akshare
---

# akshare

skills/succ985/openclaw-akshare-skill/akshare
akshare
Installation
$ npx skills add https://github.com/succ985/openclaw-akshare-skill --skill akshare
Summary

Real-time and historical financial data for Chinese and Asian markets via AkShare library.

Covers A-shares, Hong Kong stocks, US stocks, futures, funds, and macroeconomic indicators with real-time quotes and historical daily/weekly/monthly data
Supports multiple adjustment modes (forward, backward, or unadjusted) and returns pandas DataFrames for easy processing
Includes macroeconomic data such as GDP, CPI, and PMI for market analysis
Requires implementing custom caching and retry logic due to lack of built-in caching and potential rate limiting
SKILL.md
AkShare - Chinese Financial Data
Overview

AkShare is a free, open-source Python library for accessing Chinese financial market data. This skill provides guidance for fetching data from Chinese exchanges including Shanghai Stock Exchange, Shenzhen Stock Exchange, Hong Kong Exchange, and more.

Quick Start

Install AkShare:

pip install akshare


Basic stock quote:

import akshare as ak
df = ak.stock_zh_a_spot_em()  # Real-time A-share data

Stock Data
A-Shares (A股)

Real-time quotes:

# All A-shares real-time data
df = ak.stock_zh_a_spot_em()

# Single stock real-time quote
df = ak.stock_zh_a_spot()


Historical data:

# Historical daily data
df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20240101", end_date="20241231", adjust="qfq")


Stock list:

# Get all A-share stock list
df = ak.stock_info_a_code_name()

Hong Kong Stocks (港股)

Real-time quotes:

df = ak.stock_hk_spot_em()


Historical data:

df = ak.stock_hk_hist(symbol="00700", period="daily", adjust="qfq")

US Stocks (美股)

Real-time data:

df = ak.stock_us_spot_em()

Futures Data (期货)

Real-time futures:

# Commodity futures
df = ak.futures_zh_spot()


Historical futures:

df = ak.futures_zh_hist_sina(symbol="IF0")

Fund Data (基金)

Fund list:

df = ak.fund_open_fund_info_em()


Fund historical data:

df = ak.fund_open_fund_info_em(fund="000001", indicator="单位净值走势")

Macroeconomic Indicators (宏观)

GDP data:

df = ak.macro_china_gdp()


CPI data:

df = ak.macro_china_cpi()


PMI data:

df = ak.macro_china_pmi()

Common Parameters

Period (周期):

daily - 日线
weekly - 周线
monthly - 月线

Adjustment (复权):

qfq - 前复权
hfq - 后复权
"" - 不复权
Tips
Data caching: AkShare doesn't cache data, implement your own caching if needed
Rate limiting: Be mindful of request frequency to avoid being blocked
Data format: Returns pandas DataFrame, can be easily processed
Error handling: Network errors may occur, implement retry logic
References

For complete API documentation and advanced usage, see:

references/akshare_api.md - Detailed API reference
references/common_functions.md - Commonly used functions
https://akshare.akfamily.xyz/ - Official documentation
Weekly Installs
1.1K
Repository
succ985/opencla…re-skill
GitHub Stars
6
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass