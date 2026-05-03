---
rating: ⭐⭐
title: gws-drive-upload
url: https://skills.sh/googleworkspace/cli/gws-drive-upload
---

# gws-drive-upload

skills/googleworkspace/cli/gws-drive-upload
gws-drive-upload
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-drive-upload
Summary

Upload files to Google Drive with automatic MIME type detection and metadata.

Accepts a local file path and uploads it to Google Drive, with optional parent folder targeting and custom filename override
Automatically detects MIME type based on file extension; filename defaults to source filename unless specified with --name
Requires Google Workspace authentication via the shared gws module; treat as a write command and confirm with users before execution
SKILL.md
drive +upload

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Upload a file with automatic metadata

Usage
gws drive +upload <file>

Flags
Flag	Required	Default	Description
<file>	✓	—	Path to file to upload
--parent	—	—	Parent folder ID
--name	—	—	Target filename (defaults to source filename)
Examples
gws drive +upload ./report.pdf
gws drive +upload ./report.pdf --parent FOLDER_ID
gws drive +upload ./data.csv --name 'Sales Data.csv'

Tips
MIME type is detected automatically.
Filename is inferred from the local path unless --name is given.

[!CAUTION] This is a write command — confirm with the user before executing.

See Also
gws-shared — Global flags and auth
gws-drive — All manage files, folders, and shared drives commands
Weekly Installs
19.2K
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