---
title: rss-aggregator
url: https://skills.sh/zephyrwang6/myskill/rss-aggregator
---

# rss-aggregator

skills/zephyrwang6/myskill/rss-aggregator
rss-aggregator
Installation
$ npx skills add https://github.com/zephyrwang6/myskill --skill rss-aggregator
SKILL.md
RSS Aggregator

This skill fetches and aggregates the latest updates from a curated list of RSS feeds defined in references/feeds.opml.

Usage

When the user asks for updates (e.g., "recent updates", "last 3 days", "what's new"), use the scripts/aggregate.py script.

Command
uv run --with feedparser scripts/aggregate.py --days <number_of_days>


If the user doesn't specify a timeframe, default to 3 days.

Output

The script outputs a list of updates in the following format:

Title
Author
Summary (~500 words, extracted from feed content)
Update Time
Link
Configuration

The list of feeds is stored in references/feeds.opml.

Weekly Installs
194
Repository
zephyrwang6/myskill
GitHub Stars
281
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn