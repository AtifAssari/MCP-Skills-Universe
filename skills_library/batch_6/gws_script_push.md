---
title: gws-script-push
url: https://skills.sh/googleworkspace/cli/gws-script-push
---

# gws-script-push

skills/googleworkspace/cli/gws-script-push
gws-script-push
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-script-push
SKILL.md
script +push

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Upload local files to an Apps Script project

Usage
gws script +push --script <ID>

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
gws-script — All manage google apps script projects commands
Weekly Installs
5.8K
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