---
title: gws-modelarmor-sanitize-prompt
url: https://skills.sh/googleworkspace/cli/gws-modelarmor-sanitize-prompt
---

# gws-modelarmor-sanitize-prompt

skills/googleworkspace/cli/gws-modelarmor-sanitize-prompt
gws-modelarmor-sanitize-prompt
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-modelarmor-sanitize-prompt
Summary

Sanitize user prompts through Google Model Armor safety templates.

Requires a Model Armor template resource name and accepts text input via flag, stdin, or full JSON request body
Designed for inbound prompt safety; use the companion +sanitize-response command for outbound response filtering
Integrates with Google Cloud authentication and global flags defined in gws-shared
SKILL.md
modelarmor +sanitize-prompt

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Sanitize a user prompt through a Model Armor template

Usage
gws modelarmor +sanitize-prompt --template <NAME>

Flags
Flag	Required	Default	Description
--template	✓	—	Full template resource name (projects/PROJECT/locations/LOCATION/templates/TEMPLATE)
--text	—	—	Text content to sanitize
--json	—	—	Full JSON request body (overrides --text)
Examples
gws modelarmor +sanitize-prompt --template projects/P/locations/L/templates/T --text 'user input'
echo 'prompt' | gws modelarmor +sanitize-prompt --template ...

Tips
If neither --text nor --json is given, reads from stdin.
For outbound safety, use +sanitize-response instead.
See Also
gws-shared — Global flags and auth
gws-modelarmor — All filter user-generated content for safety commands
Weekly Installs
10.7K
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