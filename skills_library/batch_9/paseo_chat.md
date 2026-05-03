---
title: paseo-chat
url: https://skills.sh/getpaseo/paseo/paseo-chat
---

# paseo-chat

skills/getpaseo/paseo/paseo-chat
paseo-chat
Installation
$ npx skills add https://github.com/getpaseo/paseo --skill paseo-chat
SKILL.md
Paseo Chat Skill

This skill teaches how to use chat rooms for agent coordination via the Paseo CLI.

User's arguments: $ARGUMENTS

Prerequisites

Load the Paseo skill first if you need CLI guidance for launching or messaging agents.

Rules

When using chat:

create a room with paseo chat create if you need a new room
inspect available rooms with paseo chat ls and paseo chat inspect
post with paseo chat post
read with paseo chat read
keep reads bounded, usually --limit 10 or --limit 20
check chat often while working

Mentions are active:

write mentions inline in the message body as @<agent-id> to notify a specific agent immediately
use @everyone to notify all non-archived, non-internal agents
notifications are sent to the target agent without blocking the chat post
if a normal post is enough and no one needs to act right now, skip the mention
Command Surface
Create a room
paseo chat create issue-456 --purpose "Coordinate implementation and review"

List rooms
paseo chat ls

Inspect room details
paseo chat inspect issue-456

Post a message
paseo chat post issue-456 "I traced the failure to relay auth. Investigating config loading now."


With a reply:

paseo chat post issue-456 "I can take that next." --reply-to msg-001


With a direct mention:

paseo chat post issue-456 "@<agent-id> Can you verify the relay path next?"


With a room-wide mention:

paseo chat post issue-456 "@everyone Check the latest status update and reply with blockers."

Read recent messages
paseo chat read issue-456 --limit 10

Filter reads
paseo chat read issue-456 --agent <agent-id>
paseo chat read issue-456 --since 5m
paseo chat read issue-456 --since 2026-03-24T10:00:00Z

Wait for new messages
paseo chat wait issue-456 --timeout 60s

Defaults

When creating a room:

choose a short slug: issue-456, pr-143-review, relay-cleanup
give it a clear purpose

When using a room:

read only a bounded window before acting
post updates when they would help another agent or your future self
use --reply-to when responding to a specific message
use inline @<agent-id> mentions when you want to get a specific agent's attention
use @everyone when the whole active team needs to react now
check chat frequently enough that shared coordination actually works
your own agent ID is available via $PASEO_AGENT_ID

Typical things to post:

status updates
blockers
handoffs
review findings
important context another agent may need later
Your Job
Understand whether you should use an existing room or create a new one
Create the room with paseo chat create if needed
Read the room with bounded history
Post clearly
Use --reply-to when replying to a specific message
Use inline @<agent-id> mentions when you want to notify someone directly
Use @everyone when you need to notify all active non-archived agents
Weekly Installs
304
Repository
getpaseo/paseo
GitHub Stars
5.2K
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass