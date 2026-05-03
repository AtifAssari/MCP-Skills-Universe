---
title: gws-workflow-file-announce
url: https://skills.sh/googleworkspace/cli/gws-workflow-file-announce
---

# gws-workflow-file-announce

skills/googleworkspace/cli/gws-workflow-file-announce
gws-workflow-file-announce
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-workflow-file-announce
Summary

Post a Google Drive file announcement to a Google Chat space.

Requires a Drive file ID and Chat space name; optionally accepts a custom announcement message
Automatically fetches the file name from Drive to construct the announcement
Supports multiple output formats: JSON (default), table, YAML, and CSV
Pairs with gws drive +upload for a complete upload-and-announce workflow
SKILL.md
workflow +file-announce

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Announce a Drive file in a Chat space

Usage
gws workflow +file-announce --file-id <ID> --space <SPACE>

Flags
Flag	Required	Default	Description
--file-id	✓	—	Drive file ID to announce
--space	✓	—	Chat space name (e.g. spaces/SPACE_ID)
--message	—	—	Custom announcement message
--format	—	—	Output format: json (default), table, yaml, csv
Examples
gws workflow +file-announce --file-id FILE_ID --space spaces/ABC123
gws workflow +file-announce --file-id FILE_ID --space spaces/ABC123 --message 'Check this out!'

Tips
This is a write command — sends a Chat message.
Use gws drive +upload first to upload the file, then announce it here.
Fetches the file name from Drive to build the announcement.
See Also
gws-shared — Global flags and auth
gws-workflow — All cross-service productivity workflows commands
Weekly Installs
11.6K
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