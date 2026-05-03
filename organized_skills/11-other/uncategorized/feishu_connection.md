---
rating: ⭐⭐⭐
title: feishu-connection
url: https://skills.sh/xiaomingx/moltbot-connector-feishu-dingtalk/feishu-connection
---

# feishu-connection

skills/xiaomingx/moltbot-connector-feishu-dingtalk/feishu-connection
feishu-connection
Installation
$ npx skills add https://github.com/xiaomingx/moltbot-connector-feishu-dingtalk --skill feishu-connection
SKILL.md
Feishu Bridge

Bridge Feishu bot messages to Clawdbot Gateway over local WebSocket.

Architecture
Feishu user → Feishu cloud ←WS→ bridge.py (local) ←WS→ Clawdbot Gateway → AI agent

Feishu SDK connects outbound (no inbound port / public IP needed)
Bridge authenticates to Gateway using the existing gateway token
Each Feishu chat maps to a Clawdbot session (feishu:<chatId>)
Setup
1. Create Feishu bot
Go to open.feishu.cn/app → Create self-built app → Add Bot capability
Enable permissions: im:message, im:message.group_at_msg, im:message.p2p_msg
Events: add im.message.receive_v1, set delivery to WebSocket long-connection
Publish the app (create version → request approval)
Note the App ID and App Secret
2. Store secret
mkdir -p ~/.clawdbot/secrets
echo "YOUR_APP_SECRET" > ~/.clawdbot/secrets/feishu_app_secret
chmod 600 ~/.clawdbot/secrets/feishu_app_secret

3. Install & run
cd <skill-dir>/feishu-connection
uv sync
FEISHU_APP_ID=cli_xxx uv run python bridge.py

4. Auto-start (macOS)
FEISHU_APP_ID=cli_xxx uv run python setup_service.py
launchctl load ~/Library/LaunchAgents/com.clawdbot.feishu-bridge.plist

Diagnostics
# Check service
launchctl list | grep feishu

# Logs
tail -f ~/.clawdbot/logs/feishu-bridge.err.log

# Stop
launchctl unload ~/Library/LaunchAgents/com.clawdbot.feishu-bridge.plist

Group chat behavior

Bridge replies only when: user @-mentions the bot, message ends with ?/？, contains request verbs (帮/请/分析/总结…), or calls the bot by name. Customize the name list in bridge.py → should_respond_in_group().

Environment variables
Variable	Required	Default
FEISHU_APP_ID	✅	—
FEISHU_APP_SECRET_PATH	—	~/.clawdbot/secrets/feishu_app_secret
CLAWDBOT_CONFIG_PATH	—	~/.clawdbot/clawdbot.json
CLAWDBOT_AGENT_ID	—	main
FEISHU_THINKING_THRESHOLD_MS	—	2500
Weekly Installs
89
Repository
xiaomingx/moltb…dingtalk
GitHub Stars
7
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail