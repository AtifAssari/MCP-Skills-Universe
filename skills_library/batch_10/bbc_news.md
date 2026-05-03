---
title: bbc-news
url: https://skills.sh/sundial-org/awesome-openclaw-skills/bbc-news
---

# bbc-news

skills/sundial-org/awesome-openclaw-skills/bbc-news
bbc-news
Installation
$ npx skills add https://github.com/sundial-org/awesome-openclaw-skills --skill bbc-news
SKILL.md
BBC News

Fetch top stories from BBC News across different sections and regions.

Quick Start

Fetch top stories:

python3 scripts/bbc_news.py


Fetch from specific section:

python3 scripts/bbc_news.py uk
python3 scripts/bbc_news.py world
python3 scripts/bbc_news.py technology


List all available sections:

python3 scripts/bbc_news.py --list

Available Sections
Main Sections
top - Top stories (default)
uk - UK news
world - World news
business - Business news
politics - Politics
health - Health news
education - Education
science - Science & Environment
technology - Technology news
entertainment - Entertainment & Arts
UK Regional
england - England news
scotland - Scotland news
wales - Wales news
northern-ireland - Northern Ireland news
World Regions
africa - Africa news
asia - Asia news
australia - Australia news
europe - Europe news
latin-america - Latin America news
middle-east - Middle East news
us-canada - US & Canada news
Options

Limit number of stories:

python3 scripts/bbc_news.py world --limit 5


JSON output:

python3 scripts/bbc_news.py technology --json

Examples

Get top 5 UK stories:

python3 scripts/bbc_news.py uk --limit 5


Get Scotland news in JSON:

python3 scripts/bbc_news.py scotland --json


Get latest technology headlines:

python3 scripts/bbc_news.py technology --limit 3

Dependencies

Requires feedparser:

pip3 install feedparser

Resources
scripts/bbc_news.py

Python CLI that fetches and displays BBC News stories from RSS feeds. Supports all major BBC sections and regions, with text and JSON output formats.

references/feeds.md

Complete list of BBC News RSS feed URLs organized by section and region.

Weekly Installs
65
Repository
sundial-org/awe…w-skills
GitHub Stars
589
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass