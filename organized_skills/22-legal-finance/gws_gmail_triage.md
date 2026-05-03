---
rating: ⭐⭐
title: gws-gmail-triage
url: https://skills.sh/googleworkspace/cli/gws-gmail-triage
---

# gws-gmail-triage

skills/googleworkspace/cli/gws-gmail-triage
gws-gmail-triage
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-gmail-triage
Summary

Quickly summarize unread Gmail inbox messages with sender, subject, and date.

Displays up to 20 unread messages by default; customize with --max flag
Supports Gmail search queries via --query flag to filter beyond unread (e.g., from:boss)
Read-only operation; never modifies your mailbox
Optional --labels flag includes label names in output; supports JSON format for scripting
SKILL.md
gmail +triage

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Show unread inbox summary (sender, subject, date)

Usage
gws gmail +triage

Flags
Flag	Required	Default	Description
--max	—	20	Maximum messages to show (default: 20)
--query	—	—	Gmail search query (default: is:unread)
--labels	—	—	Include label names in output
Examples
gws gmail +triage
gws gmail +triage --max 5 --query 'from:boss'
gws gmail +triage --format json | jq '.[].subject'
gws gmail +triage --labels

Tips
Read-only — never modifies your mailbox.
Defaults to table output format.
See Also
gws-shared — Global flags and auth
gws-gmail — All send, read, and manage email commands
Weekly Installs
17.7K
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