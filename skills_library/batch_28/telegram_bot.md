---
title: telegram-bot
url: https://skills.sh/delexw/claude-code-misc/telegram-bot
---

# telegram-bot

skills/delexw/claude-code-misc/telegram-bot
telegram-bot
Installation
$ npx skills add https://github.com/delexw/claude-code-misc --skill telegram-bot
SKILL.md
Telegram Bot

Two scripts for Telegram bot interaction:

1. Fetch latest channel message

Reads the most recent post from your Telegram channel.

python3 <skill-dir>/scripts/fetch_dm.py


Requires: TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID

2. Send message to channel

Posts a message to your Telegram channel.

python3 <skill-dir>/scripts/send_channel.py "Your message here"


Supports HTML formatting (<b>, <i>, <code>, <a href="...">).

Requires: TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID

Weekly Installs
8
Repository
delexw/claude-code-misc
GitHub Stars
1
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn