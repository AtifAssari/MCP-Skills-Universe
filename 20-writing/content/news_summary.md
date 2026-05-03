---
title: news-summary
url: https://skills.sh/sundial-org/awesome-openclaw-skills/news-summary
---

# news-summary

skills/sundial-org/awesome-openclaw-skills/news-summary
news-summary
Installation
$ npx skills add https://github.com/sundial-org/awesome-openclaw-skills --skill news-summary
SKILL.md
News Summary
Overview

Fetch and summarize news from trusted international sources via RSS feeds.

RSS Feeds
BBC (Primary)
# World news
curl -s "https://feeds.bbci.co.uk/news/world/rss.xml"

# Top stories
curl -s "https://feeds.bbci.co.uk/news/rss.xml"

# Business
curl -s "https://feeds.bbci.co.uk/news/business/rss.xml"

# Technology
curl -s "https://feeds.bbci.co.uk/news/technology/rss.xml"

Reuters
# World news
curl -s "https://www.reutersagency.com/feed/?best-regions=world&post_type=best"

NPR (US perspective)
curl -s "https://feeds.npr.org/1001/rss.xml"

Al Jazeera (Global South perspective)
curl -s "https://www.aljazeera.com/xml/rss/all.xml"

Parse RSS

Extract titles and descriptions:

curl -s "https://feeds.bbci.co.uk/news/world/rss.xml" | \
  grep -E "<title>|<description>" | \
  sed 's/<[^>]*>//g' | \
  sed 's/^[ \t]*//' | \
  head -30

Workflow
Text summary
Fetch BBC world headlines
Optionally supplement with Reuters/NPR
Summarize key stories
Group by region or topic
Voice summary
Create text summary
Generate voice with OpenAI TTS
Send as audio message
curl -s https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-1-hd",
    "input": "<news summary text>",
    "voice": "onyx",
    "speed": 0.95
  }' \
  --output /tmp/news.mp3

Example Output Format
📰 News Summary [date]

🌍 WORLD
- [headline 1]
- [headline 2]

💼 BUSINESS
- [headline 1]

💻 TECH
- [headline 1]

Best Practices
Keep summaries concise (5-8 top stories)
Prioritize breaking news and major events
For voice: ~2 minutes max
Balance perspectives (Western + Global South)
Cite source if asked
Weekly Installs
813
Repository
sundial-org/awe…w-skills
GitHub Stars
589
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass