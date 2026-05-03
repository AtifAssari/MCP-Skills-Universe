---
title: slack-usage
url: https://skills.sh/fcakyon/claude-codex-settings/slack-usage
---

# slack-usage

skills/fcakyon/claude-codex-settings/slack-usage
slack-usage
Installation
$ npx skills add https://github.com/fcakyon/claude-codex-settings --skill slack-usage
SKILL.md
Slack Usage Best Practices
Critical Search Rule

ALWAYS use mcp__slack__slack_search_messages first for message searches. Only use mcp__slack__slack_get_channel_history when explicitly asked for recent channel history.

Search is more efficient and finds messages across all channels. Channel history only shows recent messages in one channel.

Slack API Best Practices
Rate Limiting

Slack APIs have rate limits (typically 1 request per second for most methods). When making multiple requests:

Space out bulk operations
Handle rate limit errors gracefully
Cache results when possible
Channel Types
Public channels - Visible to all workspace members
Private channels - Invite-only, prefix with lock icon
DMs - Direct messages between users
Group DMs - Multi-person direct conversations
Message Formatting

Format mentions and links properly:

User mention: <@USER_ID>
Channel link: <#CHANNEL_ID>
URL with text: <https://example.com|link text>
Bold: *text*
Code: backticks for inline, triple backticks for blocks
Threading Best Practices
Use threads for discussions to keep channels clean
Reply in thread when responding to specific messages
Use "Also send to channel" sparingly (only for important updates)
Thread replies don't trigger channel notifications by default
Bot vs User Tokens
Bot tokens (xoxb-): Actions appear as the bot, limited to channels bot is in
User tokens (xoxp-): Actions appear as user, access to all user's channels
Search typically requires user token for full workspace access
Posting messages works with either token type
Common Workflows

Finding past discussions:

Search with relevant keywords
Filter by channel, user, or date if needed
Get thread replies for full context

Monitoring channels:

Get channel history for recent activity
Note message timestamps for threading
React or reply as appropriate
MCP Limitations

This MCP provides read and write access to Slack. Consider:

Rate limits apply to all operations
Some admin operations not available
File uploads have size limits
Weekly Installs
34
Repository
fcakyon/claude-…settings
GitHub Stars
657
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass