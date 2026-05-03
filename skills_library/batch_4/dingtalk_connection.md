---
title: dingtalk-connection
url: https://skills.sh/xiaomingx/moltbot-connector-feishu-dingtalk/dingtalk-connection
---

# dingtalk-connection

skills/xiaomingx/moltbot-connector-feishu-dingtalk/dingtalk-connection
dingtalk-connection
Installation
$ npx skills add https://github.com/xiaomingx/moltbot-connector-feishu-dingtalk --skill dingtalk-connection
Summary

Bridge DingTalk outgoing webhooks to Clawdbot Gateway via local WebSocket connection.

Receives DingTalk bot messages through webhook callbacks and forwards them to Clawdbot Gateway for AI agent processing
Configurable port, path, and signing secret for webhook security and routing flexibility
Includes optional macOS launchd service setup for persistent bridge operation
Supports thinking time thresholds (default 2500ms) to control response streaming behavior in DingTalk sessions
SKILL.md
DingTalk Bridge

Bridge DingTalk bot messages to Clawdbot Gateway over a local WebSocket connection.

Architecture
DingTalk user -> DingTalk cloud -> webhook (bridge.py) -> Clawdbot Gateway -> AI agent

Setup
1. Create DingTalk bot

Create a bot that can send outgoing webhooks and set the callback URL to your public endpoint.

2. Run bridge
cd <skill-dir>/dingtalk-connection
uv sync
DINGTALK_SIGNING_SECRET=your_secret uv run python bridge.py

3. Auto-start (macOS)
uv run python setup_service.py
launchctl load ~/Library/LaunchAgents/com.clawdbot.dingtalk-bridge.plist

Environment variables
Variable	Required	Default
DINGTALK_PORT	—	3210
DINGTALK_PATH	—	/dingtalk
DINGTALK_SIGNING_SECRET	—	—
DINGTALK_BOT_ID	—	—
DINGTALK_BOT_NAME	—	—
CLAWDBOT_CONFIG_PATH	—	~/.clawdbot/clawdbot.json
CLAWDBOT_AGENT_ID	—	main
DINGTALK_THINKING_THRESHOLD_MS	—	2500
Weekly Installs
441
Repository
xiaomingx/moltb…dingtalk
GitHub Stars
7
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn