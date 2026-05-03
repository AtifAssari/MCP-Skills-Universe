---
rating: ⭐⭐
title: gws-chat-send
url: https://skills.sh/googleworkspace/cli/gws-chat-send
---

# gws-chat-send

skills/googleworkspace/cli/gws-chat-send
gws-chat-send
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-chat-send
Summary

Send plain-text messages to Google Chat spaces.

Requires space name (e.g. spaces/AAAA...) and message text as command arguments
Supports only plain text messages; use the raw API for cards or threaded replies
Write operation that should be confirmed with the user before execution
Depends on gws-shared for authentication and global flags
SKILL.md
chat +send

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Send a message to a space

Usage
gws chat +send --space <NAME> --text <TEXT>

Flags
Flag	Required	Default	Description
--space	✓	—	Space name (e.g. spaces/AAAA...)
--text	✓	—	Message text (plain text)
Examples
gws chat +send --space spaces/AAAAxxxx --text 'Hello team!'

Tips
Use 'gws chat spaces list' to find space names.
For cards or threaded replies, use the raw API instead.

[!CAUTION] This is a write command — confirm with the user before executing.

See Also
gws-shared — Global flags and auth
gws-chat — All manage chat spaces and messages commands
Weekly Installs
11.7K
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