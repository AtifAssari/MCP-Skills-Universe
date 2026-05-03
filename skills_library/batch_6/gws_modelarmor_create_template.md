---
title: gws-modelarmor-create-template
url: https://skills.sh/googleworkspace/cli/gws-modelarmor-create-template
---

# gws-modelarmor-create-template

skills/googleworkspace/cli/gws-modelarmor-create-template
gws-modelarmor-create-template
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-modelarmor-create-template
Summary

Create Google Model Armor templates to filter prompts and responses for safety.

Requires GCP project ID, location, and template ID; supports preset templates (jailbreak) or custom JSON configuration
Templates work with companion sanitize-prompt and sanitize-response commands for comprehensive content filtering
Write operation requiring user confirmation before execution
Defaults to jailbreak preset if no preset or JSON configuration is specified
SKILL.md
modelarmor +create-template

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Create a new Model Armor template

Usage
gws modelarmor +create-template --project <PROJECT> --location <LOCATION> --template-id <ID>

Flags
Flag	Required	Default	Description
--project	✓	—	GCP project ID
--location	✓	—	GCP location (e.g. us-central1)
--template-id	✓	—	Template ID to create
--preset	—	—	Use a preset template: jailbreak
--json	—	—	JSON body for the template configuration (overrides --preset)
Examples
gws modelarmor +create-template --project P --location us-central1 --template-id my-tmpl --preset jailbreak
gws modelarmor +create-template --project P --location us-central1 --template-id my-tmpl --json '{...}'

Tips
Defaults to the jailbreak preset if neither --preset nor --json is given.
Use the resulting template name with +sanitize-prompt and +sanitize-response.

[!CAUTION] This is a write command — confirm with the user before executing.

See Also
gws-shared — Global flags and auth
gws-modelarmor — All filter user-generated content for safety commands
Weekly Installs
10.9K
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