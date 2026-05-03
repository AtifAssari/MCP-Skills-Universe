---
title: gws-apps-script-push
url: https://skills.sh/googleworkspace/cli/gws-apps-script-push
---

# gws-apps-script-push

skills/googleworkspace/cli/gws-apps-script-push
gws-apps-script-push
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-apps-script-push
Summary

Upload local files to a Google Apps Script project, replacing all remote files.

Supports .gs, .js, .html, and appsscript.json files; automatically skips hidden files and node_modules
Requires a Script Project ID via the --script flag; optionally specify a source directory with --dir (defaults to current directory)
Destructive operation that replaces all files in the target project; requires user confirmation before execution
Depends on gws authentication and global flags documented in gws-shared
SKILL.md
apps-script +push

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Upload local files to an Apps Script project

Usage
gws apps-script +push --script <ID>

Flags
Flag	Required	Default	Description
--script	✓	—	Script Project ID
--dir	—	—	Directory containing script files (defaults to current dir)
Examples
gws script +push --script SCRIPT_ID
gws script +push --script SCRIPT_ID --dir ./src

Tips
Supports .gs, .js, .html, and appsscript.json files.
Skips hidden files and node_modules automatically.
This replaces ALL files in the project.

[!CAUTION] This is a write command — confirm with the user before executing.

See Also
gws-shared — Global flags and auth
gws-apps-script — All manage and execute apps script projects commands
Weekly Installs
632
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass