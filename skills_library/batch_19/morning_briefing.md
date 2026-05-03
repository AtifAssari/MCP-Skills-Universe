---
title: morning-briefing
url: https://skills.sh/alphamoemoe/foci/morning-briefing
---

# morning-briefing

skills/alphamoemoe/foci/morning-briefing
morning-briefing
Installation
$ npx skills add https://github.com/alphamoemoe/foci --skill morning-briefing
SKILL.md
Morning Briefing

Generate a structured daily market briefing based on YouTuber sentiment.

Triggers
"今日晨报"
"早上好"
"morning briefing"
"daily briefing"
"今天市场怎么样"
/morning-briefing
Instructions

When the user wants a morning briefing, follow these steps:

Get Daily Summary Call get_daily_summary for today (and yesterday for comparison).

Get Hot Tickers Call list_tickers to identify the most discussed stocks.

Get Top 5 Stock Details Call get_ticker_sentiment for the top 5 most mentioned stocks to get detailed sentiment.

Compile Briefing Create a structured morning report with:

Market mood overview
Top bullish picks
Top bearish concerns
Notable viewpoints
What to watch today

Present Results Format the output as:

# 📰 每日晨报 | YYYY-MM-DD

## 市场情绪温度计 🌡️

**整体情绪**: 🟢 偏多 / 🟡 中性 / 🔴 偏空

- 看涨观点: XX 条
- 看跌观点: XX 条
- 中性观点: XX 条

---

## 今日最看涨 📈

| 排名 | 股票 | 看涨博主数 | 关键理由 |
|------|------|------------|----------|
| 1 | NVDA | 8 | AI需求强劲 |
| 2 | AAPL | 5 | 新品发布预期 |
| 3 | ... | ... | ... |

## 今日最看跌 📉

| 排名 | 股票 | 看跌博主数 | 主要担忧 |
|------|------|------------|----------|
| 1 | XXX | 4 | 估值过高 |
| 2 | ... | ... | ... |

---

## 重点股票速览

### NVDA
- **情绪**: 🟢 强烈看涨
- **看涨/看跌**: 8/1
- **热点**: AI芯片需求、数据中心增长
- **代表观点**: "[观点]" — 博主A

### TSLA
- **情绪**: 🟡 分歧较大
- **看涨/看跌**: 4/3
- **热点**: FSD进展、交付数据
- **代表观点**: "[观点]" — 博主B

[重复 Top 5]

---

## 值得关注的观点 💡

1. **[博主A]**: "[独到观点摘要]"
2. **[博主B]**: "[独到观点摘要]"
3. **[博主C]**: "[独到观点摘要]"

---

## 今日关注 👀

- [ ] NVDA: 关注AI相关消息
- [ ] TSLA: 关注交付数据
- [ ] 宏观: 关注Fed讲话

---

*数据来源: 60+ 财经 YouTuber | 更新时间: HH:MM*

Tool Sequence
get_daily_summary(date=today) + get_daily_summary(date=yesterday) → In parallel
list_tickers → Get hot stocks
get_ticker_sentiment(top_ticker_1) + ... + get_ticker_sentiment(top_ticker_5) → Top 5 in parallel
Compile morning briefing
Notes
Keep it scannable and actionable
Highlight what changed from yesterday
Include a mix of consensus and contrarian views
Format for easy reading on mobile
Add timestamps for context
Weekly Installs
95
Repository
alphamoemoe/foci
GitHub Stars
6
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn