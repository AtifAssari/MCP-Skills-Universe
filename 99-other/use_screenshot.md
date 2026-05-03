---
title: use-screenshot
url: https://skills.sh/gjkeller/use-screenshot/use-screenshot
---

# use-screenshot

skills/gjkeller/use-screenshot/use-screenshot
use-screenshot
Installation
$ npx skills add https://github.com/gjkeller/use-screenshot --skill use-screenshot
SKILL.md
Use Screenshot
Trigger

When the user asks to check the latest screenshot, clipboard image, or a recent downloaded image.

Usage
Repo: node skills/use-screenshot/scripts/screenshot-agent.js
Downloads: node skills/use-screenshot/scripts/screenshot-agent.js --downloads
Clipboard only: node skills/use-screenshot/scripts/screenshot-agent.js --clipboard-only
Output is two lines:
source (clipboard or original file path)
temp file path (PNG/JPG/JPEG)
Agent pattern
out="$(node skills/use-screenshot/scripts/screenshot-agent.js)"
tmp="$(printf "%s\n" "$out" | sed -n '2p')"


If tmp is empty, treat as not found.

Notes
Desktop files are copied to temp then trashed.
Downloads files are moved to temp (not trashed).
Clipboard has no copy timestamp; the tool prefers a file modified within ~30s, otherwise clipboard.
Linux: requires wl-clipboard or xclip for clipboard images.
Weekly Installs
43
Repository
gjkeller/use-screenshot
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass