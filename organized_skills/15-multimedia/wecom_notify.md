---
rating: ⭐⭐⭐
title: wecom-notify
url: https://skills.sh/xueheng-li/openclaw-wechat/wecom-notify
---

# wecom-notify

skills/xueheng-li/openclaw-wechat/wecom-notify
wecom-notify
Installation
$ npx skills add https://github.com/xueheng-li/openclaw-wechat --skill wecom-notify
SKILL.md
WeCom Notify

Send text, image, or file messages to WeCom (企业微信) using scripts/send_wecom.py.

Usage
# Text message
python3 scripts/send_wecom.py "消息内容"
python3 scripts/send_wecom.py "消息内容" --to LiXueHeng

# Image message
python3 scripts/send_wecom.py --image /path/to/photo.png
python3 scripts/send_wecom.py --image /path/to/chart.jpg --to @all

# File message
python3 scripts/send_wecom.py --file /path/to/report.pdf
python3 scripts/send_wecom.py --file /path/to/data.xlsx --to LiXueHeng


Default recipient: LiXueHeng. Config is read from ~/.openclaw/openclaw.json (env.vars section).

Notes
Requires proxy (WECOM_PROXY in config) — API calls route through Guangzhou VPS tinyproxy at 10.147.17.105:8888 via ZeroTier
WeCom text messages have a 2048-byte limit (~680 Chinese characters). For longer messages, split into multiple sends
Image upload supports: jpg, png, gif (max 2MB for image type)
File upload supports: any format (max 20MB)
Uploaded media is temporary (3 days validity on WeCom servers)
The script uses only Python stdlib (urllib.request, json, mimetypes, uuid) — no pip dependencies
Weekly Installs
413
Repository
xueheng-li/open…w-wechat
GitHub Stars
157
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass