---
rating: ⭐⭐⭐
title: freeunlimited-websearch
url: https://skills.sh/lngu/openclaw-skill-freeunlimited-websearch/freeunlimited-websearch
---

# freeunlimited-websearch

skills/lngu/openclaw-skill-freeunlimited-websearch/freeUnlimited-websearch
freeUnlimited-websearch
Installation
$ npx skills add https://github.com/lngu/openclaw-skill-freeunlimited-websearch --skill freeUnlimited-websearch
SKILL.md
Free Unlimited Web Search

Search the web for free using DuckDuckGo - no API key or rate limits.

Features
Free: No API key required
Unlimited: No rate limits or quotas
Private: Uses DuckDuckGo's privacy-focused search
Requirements
Python 3.8+
ddgs package (pip install ddgs)
Installation

Install the ddgs package in a Python environment:

pip install ddgs


Clone this skill to your openclaw skills directory:

git clone https://github.com/YOUR_USERNAME/openclaw-skill-freeUnlimited-websearch ~/.openclaw/skills/freeUnlimited-websearch


Update search.py shebang to point to your Python with ddgs installed:

# Edit the first line of search.py to your python path, e.g.:
#!/path/to/your/venv/bin/python


Enable the skill in ~/.openclaw/openclaw.json:

{
  "skills": {
    "entries": {
      "freeUnlimited-websearch": {
        "enabled": true
      }
    }
  }
}


Restart openclaw:

openclaw gateway restart

Usage

The skill is automatically invoked when OpenClaw needs to search the web for current information.

Output

Returns JSON array of search results with title, href, and body fields.

Weekly Installs
480
Repository
lngu/openclaw-s…ebsearch
GitHub Stars
2
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail