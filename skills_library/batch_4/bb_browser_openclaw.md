---
title: bb-browser-openclaw
url: https://skills.sh/epiral/bb-browser/bb-browser-openclaw
---

# bb-browser-openclaw

skills/epiral/bb-browser/bb-browser-openclaw
bb-browser-openclaw
Installation
$ npx skills add https://github.com/epiral/bb-browser --skill bb-browser-openclaw
SKILL.md
bb-browser sites — The web as CLI

36 platforms, 103 commands. One-liner structured data from any website using your login state.

All commands use --openclaw to run through OpenClaw's browser. No Chrome extension or daemon needed.

Quick Start
# First time: pull community adapters
bb-browser site update

# See what's available
bb-browser site list

# See which adapters match your browsing habits
bb-browser site recommend

# Run any adapter via OpenClaw's browser
bb-browser site reddit/hot --openclaw
bb-browser site hackernews/top 5 --openclaw
bb-browser site v2ex/hot --openclaw

IMPORTANT: Always use --openclaw

Every bb-browser site command MUST include --openclaw to use OpenClaw's browser:

# Correct
bb-browser site twitter/search "AI agent" --openclaw
bb-browser site zhihu/hot 10 --openclaw --json
bb-browser site xueqiu/hot-stock 5 --openclaw --jq '.items[] | {name, changePercent}'

# Wrong (requires separate Chrome extension)
bb-browser site twitter/search "AI agent"

Data Extraction (most common use)
# Social media
bb-browser site twitter/search "OpenClaw" --openclaw
bb-browser site twitter/thread <tweet-url> --openclaw
bb-browser site reddit/thread <post-url> --openclaw
bb-browser site weibo/hot --openclaw
bb-browser site xiaohongshu/search "query" --openclaw

# Developer
bb-browser site github/repo owner/repo --openclaw
bb-browser site github/issues owner/repo --openclaw
bb-browser site hackernews/top 10 --openclaw
bb-browser site stackoverflow/search "async await" --openclaw
bb-browser site arxiv/search "transformer" --openclaw

# Finance
bb-browser site xueqiu/stock SH600519 --openclaw
bb-browser site xueqiu/hot-stock 5 --openclaw
bb-browser site eastmoney/stock "茅台" --openclaw

# News & Knowledge
bb-browser site zhihu/hot --openclaw
bb-browser site 36kr/newsflash --openclaw
bb-browser site wikipedia/summary "Python" --openclaw

# Video
bb-browser site youtube/transcript VIDEO_ID --openclaw
bb-browser site bilibili/search "query" --openclaw

Filtering with --jq

Use --jq to extract specific fields (no need for --json, it's implied):

# Just stock names
bb-browser site xueqiu/hot-stock 5 --openclaw --jq '.items[].name'

# Specific fields as objects
bb-browser site xueqiu/hot-stock 5 --openclaw --jq '.items[] | {name, changePercent, heat}'

# Filter results
bb-browser site reddit/hot --openclaw --jq '.posts[] | {title, score}'

View adapter details
# Check what args an adapter takes
bb-browser site info xueqiu/stock

# Search adapters by keyword
bb-browser site search reddit

Login State

Adapters run inside OpenClaw's browser tabs. If a site requires login:

The adapter will return an error like {"error": "HTTP 401", "hint": "Not logged in?"}
Log in to the site in OpenClaw's browser:
openclaw browser open https://twitter.com

Complete login manually in the browser window
Retry the command
Creating New Adapters

Turn any website into a CLI command:

# Read the guide
bb-browser guide

# Or just tell me: "turn notion.so into a bb-browser adapter"
# I'll reverse-engineer the API, write the adapter, test it, and submit a PR.

All 36 Platforms
Category	Platforms
Search	Google, Baidu, Bing, DuckDuckGo, Sogou WeChat
Social	Twitter/X, Reddit, Weibo, Xiaohongshu, Jike, LinkedIn, Hupu
News	BBC, Reuters, 36kr, Toutiao, Eastmoney
Dev	GitHub, StackOverflow, HackerNews, CSDN, cnblogs, V2EX, Dev.to, npm, PyPI, arXiv
Video	YouTube, Bilibili
Entertainment	Douban, IMDb, Genius, Qidian
Finance	Xueqiu, Eastmoney, Yahoo Finance
Jobs	BOSS Zhipin, LinkedIn
Knowledge	Wikipedia, Zhihu, Open Library
Shopping	SMZDM
Tools	Youdao, GSMArena, Product Hunt, Ctrip
Weekly Installs
400
Repository
epiral/bb-browser
GitHub Stars
4.9K
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn