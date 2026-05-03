---
rating: ⭐⭐⭐
title: imsg
url: https://skills.sh/steipete/clawdis/imsg
---

# imsg

skills/steipete/clawdis/imsg
imsg
Installation
$ npx skills add https://github.com/steipete/clawdis --skill imsg
SKILL.md
imsg

Use imsg to read and send iMessage/SMS via macOS Messages.app.

When to Use

✅ USE this skill when:

User explicitly asks to send iMessage or SMS
Reading iMessage conversation history
Checking recent Messages.app chats
Sending to phone numbers or Apple IDs
When NOT to Use

❌ DON'T use this skill when:

Telegram messages → use message tool with channel:telegram
Signal messages → use Signal channel if configured
WhatsApp messages → use WhatsApp channel if configured
Discord messages → use message tool with channel:discord
Slack messages → use slack skill
Group chat management (adding/removing members) → not supported
Bulk/mass messaging → always confirm with user first
Replying in current conversation → just reply normally (OpenClaw routes automatically)
Requirements
macOS with Messages.app signed in
Full Disk Access for terminal
Automation permission for Messages.app (for sending)
Common Commands
List Chats
imsg chats --limit 10 --json

View History
# By chat ID
imsg history --chat-id 1 --limit 20 --json

# With attachments info
imsg history --chat-id 1 --limit 20 --attachments --json

Watch for New Messages
imsg watch --chat-id 1 --attachments

Send Messages
# Text only
imsg send --to "+14155551212" --text "Hello!"

# With attachment
imsg send --to "+14155551212" --text "Check this out" --file /path/to/image.jpg

# Specify service
imsg send --to "+14155551212" --text "Hi" --service imessage
imsg send --to "+14155551212" --text "Hi" --service sms

Service Options
--service imessage — Force iMessage (requires recipient has iMessage)
--service sms — Force SMS (green bubble)
--service auto — Let Messages.app decide (default)
Safety Rules
Always confirm recipient and message content before sending
Never send to unknown numbers without explicit user approval
Be careful with attachments — confirm file path exists
Rate limit yourself — don't spam
Example Workflow

User: "Text mom that I'll be late"

# 1. Find mom's chat
imsg chats --limit 20 --json | jq '.[] | select(.displayName | contains("Mom"))'

# 2. Confirm with user
# "Found Mom at +1555123456. Send 'I'll be late' via iMessage?"

# 3. Send after confirmation
imsg send --to "+1555123456" --text "I'll be late"

Weekly Installs
1.0K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass