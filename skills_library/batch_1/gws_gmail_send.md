---
title: gws-gmail-send
url: https://skills.sh/googleworkspace/cli/gws-gmail-send
---

# gws-gmail-send

skills/googleworkspace/cli/gws-gmail-send
gws-gmail-send
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-gmail-send
Summary

Send emails via Gmail with support for attachments, HTML formatting, and send-as aliases.

Requires recipient email(s), subject, and body text; supports CC, BCC, and optional sender address for send-as aliases
Handles file attachments up to 25MB total, with multiple files supported via repeated --attach flags
Supports both plain text and HTML email bodies; HTML fragments do not require wrapper tags
Includes --dry-run flag to preview the request before sending, and automatic RFC 5322 formatting and MIME encoding
SKILL.md
gmail +send

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Send an email

Usage
gws gmail +send --to <EMAILS> --subject <SUBJECT> --body <TEXT>

Flags
Flag	Required	Default	Description
--to	✓	—	Recipient email address(es), comma-separated
--subject	✓	—	Email subject
--body	✓	—	Email body (plain text, or HTML with --html)
--from	—	—	Sender address (for send-as/alias; omit to use account default)
--attach	—	—	Attach a file (can be specified multiple times)
--cc	—	—	CC email address(es), comma-separated
--bcc	—	—	BCC email address(es), comma-separated
--html	—	—	Treat --body as HTML content (default is plain text)
--dry-run	—	—	Show the request that would be sent without executing it
--draft	—	—	Save as draft instead of sending
Examples
gws gmail +send --to alice@example.com --subject 'Hello' --body 'Hi Alice!'
gws gmail +send --to alice@example.com --subject 'Hello' --body 'Hi!' --cc bob@example.com
gws gmail +send --to alice@example.com --subject 'Hello' --body '<b>Bold</b> text' --html
gws gmail +send --to alice@example.com --subject 'Hello' --body 'Hi!' --from alias@example.com
gws gmail +send --to alice@example.com --subject 'Report' --body 'See attached' -a report.pdf
gws gmail +send --to alice@example.com --subject 'Files' --body 'Two files' -a a.pdf -a b.csv
gws gmail +send --to alice@example.com --subject 'Hello' --body 'Hi!' --draft

Tips
Handles RFC 5322 formatting, MIME encoding, and base64 automatically.
Use --from to send from a configured send-as alias instead of your primary address.
Use -a/--attach to add file attachments. Can be specified multiple times. Total size limit: 25MB.
With --html, use fragment tags (, , , , etc.) — no / wrapper needed.
Use --draft to save the message as a draft instead of sending it immediately.

[!CAUTION] This is a write command — confirm with the user before executing.

See Also
gws-shared — Global flags and auth
gws-gmail — All send, read, and manage email commands
Weekly Installs
18.1K
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