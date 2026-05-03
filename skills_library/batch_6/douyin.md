---
title: douyin
url: https://skills.sh/xiaoyiv/douyin-skill/douyin
---

# douyin

skills/xiaoyiv/douyin-skill/douyin
douyin
Installation
$ npx skills add https://github.com/xiaoyiv/douyin-skill --skill douyin
Summary

Download Douyin videos and extract metadata using browser automation.

Supports both short links (v.douyin.com) and full Douyin URLs for video retrieval
Extracts video metadata including title, author, and engagement statistics
Offers flexible output modes: full video download or metadata-only extraction with custom output directories
Requires one-time interactive login setup to establish authenticated browser session
SKILL.md
Douyin Skill

Download videos from Douyin using browser automation.

Setup (One-Time)
python -m nodriver_kit.tools.login_interactive --url https://www.douyin.com --profile douyin

Download Video
python scripts/download.py "https://v.douyin.com/xxx"
python scripts/download.py "https://v.douyin.com/xxx" --info-only
python scripts/download.py "https://v.douyin.com/xxx" --output ./videos

Weekly Installs
3.2K
Repository
xiaoyiv/douyin-skill
GitHub Stars
2
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn