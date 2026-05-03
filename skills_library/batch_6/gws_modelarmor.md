---
title: gws-modelarmor
url: https://skills.sh/googleworkspace/cli/gws-modelarmor
---

# gws-modelarmor

skills/googleworkspace/cli/gws-modelarmor
gws-modelarmor
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-modelarmor
Summary

Google Model Armor: Filter user-generated content for safety.

Provides three core helper commands: sanitize prompts, sanitize responses, and create custom filtering templates
Integrates with Google Workspace services via the gws CLI tool with shared authentication and security rules
Requires schema inspection via gws schema to discover available resources, methods, and parameter requirements before executing API calls
SKILL.md
modelarmor (v1)

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

gws modelarmor <resource> <method> [flags]

Helper Commands
Command	Description
+sanitize-prompt	Sanitize a user prompt through a Model Armor template
+sanitize-response	Sanitize a model response through a Model Armor template
+create-template	Create a new Model Armor template
Discovering Commands

Before calling any API method, inspect it:

# Browse resources and methods
gws modelarmor --help

# Inspect a method's required params, types, and defaults
gws schema modelarmor.<resource>.<method>


Use gws schema output to build your --params and --json flags.

Weekly Installs
11.0K
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