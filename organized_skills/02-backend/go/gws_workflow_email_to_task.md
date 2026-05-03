---
rating: ⭐⭐
title: gws-workflow-email-to-task
url: https://skills.sh/googleworkspace/cli/gws-workflow-email-to-task
---

# gws-workflow-email-to-task

skills/googleworkspace/cli/gws-workflow-email-to-task
gws-workflow-email-to-task
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-workflow-email-to-task
Summary

Convert Gmail messages into Google Tasks entries with subject-to-title mapping.

Extracts email subject as task title and message snippet as task notes
Supports custom task list selection via --tasklist flag; defaults to @default list
Requires Gmail message ID as input; recommends user confirmation before task creation
Depends on gws-shared for authentication and global workflow flags
SKILL.md
workflow +email-to-task

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Convert a Gmail message into a Google Tasks entry

Usage
gws workflow +email-to-task --message-id <ID>

Flags
Flag	Required	Default	Description
--message-id	✓	—	Gmail message ID to convert
--tasklist	—	@default	Task list ID (default: @default)
Examples
gws workflow +email-to-task --message-id MSG_ID
gws workflow +email-to-task --message-id MSG_ID --tasklist LIST_ID

Tips
Reads the email subject as the task title and snippet as notes.
Creates a new task — confirm with the user before executing.
See Also
gws-shared — Global flags and auth
gws-workflow — All cross-service productivity workflows commands
Weekly Installs
12.4K
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