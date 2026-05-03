---
rating: ⭐⭐⭐
title: finance-news
url: https://skills.sh/sundial-org/awesome-openclaw-skills/finance-news
---

# finance-news

skills/sundial-org/awesome-openclaw-skills/finance-news
finance-news
Installation
$ npx skills add https://github.com/sundial-org/awesome-openclaw-skills --skill finance-news
Summary

AI-powered market briefings with multi-region coverage, portfolio tracking, and automated delivery.

Covers US, European, and Japanese markets with news from WSJ, Barron's, CNBC, Yahoo Finance, and Finnhub via RSS feeds and APIs
Generates morning and evening briefings with Gemini-powered summaries in English or German, delivered via WhatsApp or displayed on demand
Supports portfolio management (add/remove stocks, import CSV) with ticker-specific news and price alert configuration
Configurable cron scheduling for automated briefings at market open/close times, with optional approval gates via Lobster workflows
SKILL.md
Finance News Skill

AI-powered market news briefings with configurable language output and automated delivery.

First-Time Setup

Run the interactive setup wizard to configure your sources, delivery channels, and schedule:

finance-news setup


The wizard will guide you through:

📰 RSS Feeds: Enable/disable WSJ, Barron's, CNBC, Yahoo, etc.
📊 Markets: Choose regions (US, Europe, Japan, Asia)
📤 Delivery: Configure WhatsApp/Telegram group
🌐 Language: Set default language (English/German)
⏰ Schedule: Configure morning/evening cron times

You can also configure specific sections:

finance-news setup --section feeds     # Just RSS feeds
finance-news setup --section delivery  # Just delivery channels
finance-news setup --section schedule  # Just cron schedule
finance-news setup --reset             # Reset to defaults
finance-news config                    # Show current config

Quick Start
# Generate morning briefing
finance-news briefing --morning

# View market overview
finance-news market

# Get news for your portfolio
finance-news portfolio

# Get news for specific stock
finance-news news AAPL

Features
📊 Market Coverage
US Markets: S&P 500, Dow Jones, NASDAQ
Europe: DAX, STOXX 50, FTSE 100
Japan: Nikkei 225
📰 News Sources
Premium: WSJ, Barron's (RSS feeds)
Free: CNBC, Yahoo Finance, Finnhub
Portfolio: Ticker-specific news from Yahoo
🤖 AI Summaries
Gemini-powered analysis
Configurable language (English/German)
Briefing styles: summary, analysis, headlines
📅 Automated Briefings
Morning: 6:30 AM PT (US market open)
Evening: 1:00 PM PT (US market close)
Delivery: WhatsApp (configure group in cron scripts)
Commands
Briefing Generation
# Morning briefing (English is default)
finance-news briefing --morning

# Evening briefing with WhatsApp delivery
finance-news briefing --evening --send --group "Market Briefing"

# German language option
finance-news briefing --morning --lang de

# Analysis style (more detailed)
finance-news briefing --style analysis

Market Data
# Market overview (indices + top headlines)
finance-news market

# JSON output for processing
finance-news market --json

Portfolio Management
# List portfolio
finance-news portfolio-list

# Add stock
finance-news portfolio-add NVDA --name "NVIDIA Corporation" --category Tech

# Remove stock
finance-news portfolio-remove TSLA

# Import from CSV
finance-news portfolio-import ~/my_stocks.csv

# Interactive portfolio creation
finance-news portfolio-create

Ticker News
# News for specific stock
finance-news news AAPL
finance-news news TSLA

Configuration
Portfolio CSV Format

Location: ~/clawd/skills/finance-news/config/portfolio.csv

symbol,name,category,notes
AAPL,Apple Inc.,Tech,Core holding
NVDA,NVIDIA Corporation,Tech,AI play
MSFT,Microsoft Corporation,Tech,

Sources Configuration

Location: ~/clawd/skills/finance-news/config/config.json (legacy fallback: config/sources.json)

RSS feeds for WSJ, Barron's, CNBC, Yahoo
Market indices by region
Language settings
Cron Jobs
Setup via OpenClaw
# Add morning briefing cron job
openclaw cron add --schedule "30 6 * * 1-5" \
  --timezone "America/Los_Angeles" \
  --command "bash ~/clawd/skills/finance-news/cron/morning.sh"

# Add evening briefing cron job
openclaw cron add --schedule "0 13 * * 1-5" \
  --timezone "America/Los_Angeles" \
  --command "bash ~/clawd/skills/finance-news/cron/evening.sh"

Manual Cron (crontab)
# Morning briefing (6:30 AM PT, weekdays)
30 6 * * 1-5 bash ~/clawd/skills/finance-news/cron/morning.sh

# Evening briefing (1:00 PM PT, weekdays)
0 13 * * 1-5 bash ~/clawd/skills/finance-news/cron/evening.sh

Sample Output
🌅 **Börsen-Morgen-Briefing**
Dienstag, 21. Januar 2026 | 06:30 Uhr

📊 **Märkte**
• S&P 500: 5.234 (+0,3%)
• DAX: 16.890 (-0,1%)
• Nikkei: 35.678 (+0,5%)

📈 **Dein Portfolio**
• AAPL $256 (+1,2%) — iPhone-Verkäufe übertreffen Erwartungen
• NVDA $512 (+3,4%) — KI-Chip-Nachfrage steigt

🔥 **Top Stories**
• [WSJ] Fed signalisiert mögliche Zinssenkung im März
• [CNBC] Tech-Sektor führt Rally an

🤖 **Analyse**
Der S&P zeigt Stärke. Dein Portfolio profitiert von NVDA's 
Momentum. Fed-Kommentare könnten Volatilität auslösen.

Integration
With OpenBB (existing skill)
# Get detailed quote, then news
openbb-quote AAPL && finance-news news AAPL

With OpenClaw Agent

The agent will automatically use this skill when asked about:

"What's the market doing?"
"News for my portfolio"
"Generate morning briefing"
"What's happening with AAPL?"
With Lobster (Workflow Engine)

Run briefings via Lobster for approval gates and resumability:

# Run with approval before WhatsApp send
lobster "workflows.run --file workflows/briefing.yaml"

# With custom args
lobster "workflows.run --file workflows/briefing.yaml --args-json '{\"time\":\"evening\",\"lang\":\"en\"}'"


See workflows/README.md for full documentation.

Files
skills/finance-news/
├── SKILL.md              # This documentation
├── Dockerfile            # NixOS-compatible container
├── config/
│   ├── portfolio.csv     # Your watchlist
│   ├── config.json       # RSS/API/language configuration
│   ├── alerts.json       # Price target alerts
│   └── manual_earnings.json  # Earnings calendar overrides
├── scripts/
│   ├── finance-news      # Main CLI
│   ├── briefing.py       # Briefing generator
│   ├── fetch_news.py     # News aggregator
│   ├── portfolio.py      # Portfolio CRUD
│   ├── summarize.py      # AI summarization
│   ├── alerts.py         # Price alert management
│   ├── earnings.py       # Earnings calendar
│   ├── ranking.py        # Headline ranking
│   └── stocks.py         # Stock management
├── workflows/
│   ├── briefing.yaml     # Lobster workflow with approval gate
│   └── README.md         # Workflow documentation
├── cron/
│   ├── morning.sh        # Morning cron (Docker-based)
│   └── evening.sh        # Evening cron (Docker-based)
└── cache/                # 15-minute news cache

Dependencies
Python 3.10+
feedparser (pip install feedparser)
Gemini CLI (brew install gemini-cli)
OpenBB (existing openbb-quote wrapper)
OpenClaw message tool (for WhatsApp delivery)
Troubleshooting
Gemini not working
# Authenticate Gemini
gemini  # Follow login flow

RSS feeds timing out
Check network connectivity
WSJ/Barron's may require subscription cookies for some content
Free feeds (CNBC, Yahoo) should always work
WhatsApp delivery failing
Verify WhatsApp group exists and bot has access
Check openclaw doctor for WhatsApp status
Weekly Installs
1.9K
Repository
sundial-org/awe…w-skills
GitHub Stars
589
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn