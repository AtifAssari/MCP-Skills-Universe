---
title: x-monitor
url: https://skills.sh/ythx-101/x-monitor/x-monitor
---

# x-monitor

skills/ythx-101/x-monitor/x-monitor
x-monitor
Installation
$ npx skills add https://github.com/ythx-101/x-monitor --skill x-monitor
SKILL.md
X Monitor

Monitor tweet replies and detect questions for AI-assisted answering.

When to Use
User says "monitor this tweet", "watch replies", "check comments"
User shares a tweet link and wants to track responses
User needs help answering technical questions in their tweet replies
When NOT to Use
Just fetching a single tweet's content → use x-tweet-fetcher
Posting or replying on X → not supported (read-only)
Searching X for topics → use x-research
Usage
# Fetch all replies on a tweet
python3 scripts/monitor.py --url "https://x.com/user/status/123"

# Check for new replies since last check
python3 scripts/monitor.py --url "https://x.com/user/status/123" --watch

# Pretty output
python3 scripts/monitor.py --url "https://x.com/user/status/123" --pretty

Requirements
Camofox browser running on localhost:9377
Working Nitter instance (default: nitter.net)
File Structure
x-monitor/
├── README.md
├── SKILL.md          (this file)
├── scripts/
│   └── monitor.py    (main script)
└── data/
    └── state.json    (tracks last check per tweet)

Weekly Installs
76
Repository
ythx-101/x-monitor
GitHub Stars
4
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn