---
title: gws-gmail-reply
url: https://skills.sh/googleworkspace/cli/gws-gmail-reply
---

# gws-gmail-reply

skills/googleworkspace/cli/gws-gmail-reply
gws-gmail-reply
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-gmail-reply
Summary

Automatically reply to Gmail messages with full threading and recipient management.

Handles message threading automatically by setting In-Reply-To, References, and threadId headers; quotes the original message in the reply
Supports plain text and HTML reply bodies, with optional file attachments (multiple files via repeated --attach flags)
Allows adding extra recipients via --to, --cc, and --bcc flags, or sending from an alias with --from
Includes --dry-run mode to preview the request before sending, and --html flag for formatted replies with CSS styling
SKILL.md
gmail +reply

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Reply to a message (handles threading automatically)

Usage
gws gmail +reply --message-id <ID> --body <TEXT>

Flags
Flag	Required	Default	Description
--message-id	✓	—	Gmail message ID to reply to
--body	✓	—	Reply body (plain text, or HTML with --html)
--from	—	—	Sender address (for send-as/alias; omit to use account default)
--to	—	—	Additional To email address(es), comma-separated
--attach	—	—	Attach a file (can be specified multiple times)
--cc	—	—	CC email address(es), comma-separated
--bcc	—	—	BCC email address(es), comma-separated
--html	—	—	Treat --body as HTML content (default is plain text)
--dry-run	—	—	Show the request that would be sent without executing it
--draft	—	—	Save as draft instead of sending
Examples
gws gmail +reply --message-id 18f1a2b3c4d --body 'Thanks, got it!'
gws gmail +reply --message-id 18f1a2b3c4d --body 'Looping in Carol' --cc carol@example.com
gws gmail +reply --message-id 18f1a2b3c4d --body 'Adding Dave' --to dave@example.com
gws gmail +reply --message-id 18f1a2b3c4d --body '<b>Bold reply</b>' --html
gws gmail +reply --message-id 18f1a2b3c4d --body 'Updated version' -a updated.docx
gws gmail +reply --message-id 18f1a2b3c4d --body 'Draft reply' --draft

Tips
Automatically sets In-Reply-To, References, and threadId headers.
Quotes the original message in the reply body.
--to adds extra recipients to the To field.
Use -a/--attach to add file attachments. Can be specified multiple times.
With --html, the quoted block uses Gmail's gmail_quote CSS classes and preserves HTML formatting. Use fragment tags (, , , etc.) — no / wrapper needed.
With --html, inline images in the quoted message are preserved via cid: references.
Use --draft to save the reply as a draft instead of sending it immediately.
For reply-all, use +reply-all instead.
See Also
gws-shared — Global flags and auth
gws-gmail — All send, read, and manage email commands
Weekly Installs
12.6K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass