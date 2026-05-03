---
rating: ⭐⭐
title: feishu-reaction
url: https://skills.sh/m1heng/clawdbot-feishu/feishu-reaction
---

# feishu-reaction

skills/m1heng/clawdbot-feishu/feishu-reaction
feishu-reaction
Installation
$ npx skills add https://github.com/m1heng/clawdbot-feishu --skill feishu-reaction
SKILL.md
Feishu Reaction Tool

Single tool feishu_reaction for adding, removing, and listing emoji reactions on Feishu messages.

Workflow: Reacting to Previous Messages

To react to a message other than the current one, first use feishu_message with action: "list" to fetch recent messages and find the target message_id, then use feishu_reaction with that message_id.

Actions
Add Reaction
{
  "action": "add",
  "message_id": "om_xxx",
  "emoji_type": "THUMBSUP"
}


Returns:

{
  "ok": true,
  "action": "add",
  "message_id": "om_xxx",
  "emoji_type": "THUMBSUP",
  "reaction_id": "ZCaCIjUBVVWSrm5L-3ZTw"
}

Remove Reaction
{
  "action": "remove",
  "message_id": "om_xxx",
  "reaction_id": "ZCaCIjUBVVWSrm5L-3ZTw"
}

List Reactions

List all reactions on a message:

{
  "action": "list",
  "message_id": "om_xxx"
}


Filter by emoji type:

{
  "action": "list",
  "message_id": "om_xxx",
  "emoji_type": "THUMBSUP"
}


Returns:

{
  "ok": true,
  "action": "list",
  "message_id": "om_xxx",
  "emoji_type_filter": "THUMBSUP",
  "total": 2,
  "reactions": [
    {
      "reaction_id": "ZCaCIjUBVVWSrm5L-3ZTw",
      "emoji_type": "THUMBSUP",
      "operator_type": "user",
      "operator_id": "ou_xxx"
    }
  ]
}

Parameters
Parameter	Required	Description
action	Yes	add, remove, or list
message_id	Yes	Feishu message ID (e.g., om_xxx)
emoji_type	add: Yes, list: Optional	Emoji type (e.g., THUMBSUP, HEART, SMILE)
reaction_id	remove: Yes	Reaction ID from add or list results
Common Emoji Types
Emoji	Type
THUMBSUP	THUMBSDOWN
FIRE	CLAP
PARTY	PRAY
SURPRISED	LAUGHING
Configuration
channels:
  feishu:
    tools:
      reaction: true  # default: true

Permissions
im:message.reactions:write_only — add and remove reactions
im:message.reactions:read — list reactions on messages
Weekly Installs
60
Repository
m1heng/clawdbot-feishu
GitHub Stars
4.3K
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass