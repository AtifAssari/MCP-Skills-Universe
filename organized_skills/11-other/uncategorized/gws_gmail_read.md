---
rating: ⭐⭐
title: gws-gmail-read
url: https://skills.sh/googleworkspace/cli/gws-gmail-read
---

# gws-gmail-read

skills/googleworkspace/cli/gws-gmail-read
gws-gmail-read
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-gmail-read
Summary

Extract message body and headers from Gmail using message IDs.

Reads individual Gmail messages by ID and returns body content in plain text or HTML format
Optionally includes message headers (From, To, Subject, Date) in output
Supports multiple output formats (text, json) and automatically converts HTML-only messages to plain text
Handles multipart messages and base64 decoding; includes dry-run mode for testing requests
SKILL.md
gmail +read

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Read a message and extract its body or headers

Usage
gws gmail +read --id <ID>

Flags
Flag	Required	Default	Description
--id	✓	—	The Gmail message ID to read
--headers	—	—	Include headers (From, To, Subject, Date) in the output
--format	—	text	Output format (text, json)
--html	—	—	Return HTML body instead of plain text
--dry-run	—	—	Show the request that would be sent without executing it
Examples
gws gmail +read --id 18f1a2b3c4d
gws gmail +read --id 18f1a2b3c4d --headers
gws gmail +read --id 18f1a2b3c4d --format json | jq '.body'

Tips
Converts HTML-only messages to plain text automatically.
Handles multipart/alternative and base64 decoding.
See Also
gws-shared — Global flags and auth
gws-gmail — All send, read, and manage email commands
Weekly Installs
10.6K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn