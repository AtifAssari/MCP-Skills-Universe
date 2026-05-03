---
title: slack
url: https://skills.sh/linuxhsj/openclaw-zero-token/slack
---

# slack

skills/linuxhsj/openclaw-zero-token/slack
slack
Installation
$ npx skills add https://github.com/linuxhsj/openclaw-zero-token --skill slack
SKILL.md
Slack Actions
Overview

Use slack to react, manage pins, send/edit/delete messages, and fetch member info. The tool uses the bot token configured for OpenClaw.

Inputs to collect
channelId and messageId (Slack message timestamp, e.g. 1712023032.1234).
For reactions, an emoji (Unicode or :name:).
For message sends, a to target (channel:<id> or user:<id>) and content.

Message context lines include slack message id and channel fields you can reuse directly.

Actions
Action groups
Action group	Default	Notes
reactions	enabled	React + list reactions
messages	enabled	Read/send/edit/delete
pins	enabled	Pin/unpin/list
memberInfo	enabled	Member info
emojiList	enabled	Custom emoji list
React to a message
{
  "action": "react",
  "channelId": "C123",
  "messageId": "1712023032.1234",
  "emoji": "✅"
}

List reactions
{
  "action": "reactions",
  "channelId": "C123",
  "messageId": "1712023032.1234"
}

Send a message
{
  "action": "sendMessage",
  "to": "channel:C123",
  "content": "Hello from OpenClaw"
}

Edit a message
{
  "action": "editMessage",
  "channelId": "C123",
  "messageId": "1712023032.1234",
  "content": "Updated text"
}

Delete a message
{
  "action": "deleteMessage",
  "channelId": "C123",
  "messageId": "1712023032.1234"
}

Read recent messages
{
  "action": "readMessages",
  "channelId": "C123",
  "limit": 20
}

Pin a message
{
  "action": "pinMessage",
  "channelId": "C123",
  "messageId": "1712023032.1234"
}

Unpin a message
{
  "action": "unpinMessage",
  "channelId": "C123",
  "messageId": "1712023032.1234"
}

List pinned items
{
  "action": "listPins",
  "channelId": "C123"
}

Member info
{
  "action": "memberInfo",
  "userId": "U123"
}

Emoji list
{
  "action": "emojiList"
}

Ideas to try
React with ✅ to mark completed tasks.
Pin key decisions or weekly status updates.
Weekly Installs
16
Repository
linuxhsj/opencl…ro-token
GitHub Stars
4.7K
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn