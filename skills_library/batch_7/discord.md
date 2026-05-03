---
title: discord
url: https://skills.sh/steipete/clawdis/discord
---

# discord

skills/steipete/clawdis/discord
discord
Installation
$ npx skills add https://github.com/steipete/clawdis --skill discord
SKILL.md
Discord (Via message)

Use the message tool. No provider-specific discord tool exposed to the agent.

Musts
Always: channel: "discord".
Respect gating: channels.discord.actions.* (some default off: roles, moderation, presence, channels).
Prefer explicit ids: guildId, channelId, messageId, userId.
Multi-account: optional accountId.
Guidelines
Avoid Markdown tables in outbound Discord messages.
Mention users as <@USER_ID>.
Prefer Discord components v2 (components) for rich UI; use legacy embeds only when you must.
Targets
Send-like actions: to: "channel:<id>" or to: "user:<id>".
Message-specific actions: channelId: "<id>" (or to) + messageId: "<id>".
Common Actions (Examples)

Send message:

{
  "action": "send",
  "channel": "discord",
  "to": "channel:123",
  "message": "hello",
  "silent": true
}


Send with media:

{
  "action": "send",
  "channel": "discord",
  "to": "channel:123",
  "message": "see attachment",
  "media": "file:///tmp/example.png"
}

Optional silent: true to suppress Discord notifications.

Send with components v2 (recommended for rich UI):

{
  "action": "send",
  "channel": "discord",
  "to": "channel:123",
  "message": "Status update",
  "components": "[Carbon v2 components]"
}

components expects Carbon component instances (Container, TextDisplay, etc.) from JS/TS integrations.
Do not combine components with embeds (Discord rejects v2 + embeds).

Legacy embeds (not recommended):

{
  "action": "send",
  "channel": "discord",
  "to": "channel:123",
  "message": "Status update",
  "embeds": [{ "title": "Legacy", "description": "Embeds are legacy." }]
}

embeds are ignored when components v2 are present.

React:

{
  "action": "react",
  "channel": "discord",
  "channelId": "123",
  "messageId": "456",
  "emoji": "✅"
}


Read:

{
  "action": "read",
  "channel": "discord",
  "to": "channel:123",
  "limit": 20
}


Edit / delete:

{
  "action": "edit",
  "channel": "discord",
  "channelId": "123",
  "messageId": "456",
  "message": "fixed typo"
}

{
  "action": "delete",
  "channel": "discord",
  "channelId": "123",
  "messageId": "456"
}


Poll:

{
  "action": "poll",
  "channel": "discord",
  "to": "channel:123",
  "pollQuestion": "Lunch?",
  "pollOption": ["Pizza", "Sushi", "Salad"],
  "pollMulti": false,
  "pollDurationHours": 24
}


Pins:

{
  "action": "pin",
  "channel": "discord",
  "channelId": "123",
  "messageId": "456"
}


Threads:

{
  "action": "thread-create",
  "channel": "discord",
  "channelId": "123",
  "messageId": "456",
  "threadName": "bug triage"
}


Search:

{
  "action": "search",
  "channel": "discord",
  "guildId": "999",
  "query": "release notes",
  "channelIds": ["123", "456"],
  "limit": 10
}


Presence (often gated):

{
  "action": "set-presence",
  "channel": "discord",
  "activityType": "playing",
  "activityName": "with fire",
  "status": "online"
}

Writing Style (Discord)
Short, conversational, low ceremony.
No markdown tables.
Mention users as <@USER_ID>.
Weekly Installs
1.1K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn