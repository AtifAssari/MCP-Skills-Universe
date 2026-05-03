---
title: gws-modelarmor-sanitize-response
url: https://skills.sh/googleworkspace/cli/gws-modelarmor-sanitize-response
---

# gws-modelarmor-sanitize-response

skills/googleworkspace/cli/gws-modelarmor-sanitize-response
gws-modelarmor-sanitize-response
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-modelarmor-sanitize-response
Summary

Sanitize model responses through Google Model Armor templates for outbound safety.

Applies Model Armor templates to filter model outputs before delivery to users
Accepts text input via --text flag or piped stdin, with optional full JSON request body override
Requires template resource name in format projects/PROJECT/locations/LOCATION/templates/TEMPLATE
Complements the +sanitize-prompt command for inbound user input safety
SKILL.md
modelarmor +sanitize-response

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Sanitize a model response through a Model Armor template

Usage
gws modelarmor +sanitize-response --template <NAME>

Flags
Flag	Required	Default	Description
--template	✓	—	Full template resource name (projects/PROJECT/locations/LOCATION/templates/TEMPLATE)
--text	—	—	Text content to sanitize
--json	—	—	Full JSON request body (overrides --text)
Examples
gws modelarmor +sanitize-response --template projects/P/locations/L/templates/T --text 'model output'
model_cmd | gws modelarmor +sanitize-response --template ...

Tips
Use for outbound safety (model -> user).
For inbound safety (user -> model), use +sanitize-prompt.
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