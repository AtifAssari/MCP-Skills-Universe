---
title: ue-cli
url: https://skills.sh/banab4/ue-cli/ue-cli
---

# ue-cli

skills/banab4/ue-cli/ue-cli
ue-cli
Installation
$ npx skills add https://github.com/banab4/ue-cli --skill ue-cli
SKILL.md
ue-cli

CLI for controlling Unreal Engine Editor via Remote Control API (HTTP :30010).

Prerequisites
UE Editor running with Web Remote Control plugin enabled (HTTP :30010)
Python Editor Script Plugin enabled (for script commands)
ue-cli installed: npm install -g @banaba/ue-cli
Workflow (IMPORTANT — MUST follow this order)

NEVER skip to raw API calls. Always resolve through scripts or discovery first.

Step 1. Check scripts
ue-cli script --list


Scan the output for a script that covers your task. Scripts run inside UE Python and bypass Remote Control API serialization limits — always preferred.

Step 2. Use script if matched
ue-cli call <scriptName> --params '{...}' --force


ue-cli call auto-detects: if the first argument matches a script name, it runs as a Python script. No objectPath needed.

# Example — script mode (1 arg)
ue-cli call asset_open --params '{"asset_path":"/Game/SM/BP_Top"}' --force

Step 3. Discover (fallback)

If no script matches, search the discovery catalog:

ue-cli discover                              # browse all objects/functions
ue-cli discover <keyword>                    # search by keyword
ue-cli discover --object <keyword>           # filter by class name
ue-cli discover --detail <objectPath>        # show function signatures


Then call the discovered function:

ue-cli call <objectPath> <functionName> --params '{...}' --force

Step 4. Raw API (last resort)

Only when discovery also fails to find what you need:

Command	Description
ue-cli call <objectPath> <functionName> [--params '{}']	Call a function
ue-cli get <objectPath> <propertyName>	Read a property
ue-cli set <objectPath> <propertyName> --value '{}'	Write a property
ue-cli describe <objectPath>	Inspect full object schema (online)
ue-cli search --query '{}'	Search assets (online)
ue-cli info	List all API routes (online)
ue-cli batch --requests '[...]'	Execute multiple requests
Global flags
Flag	Description
--host <url>	UE host (default: http://localhost:30010)
--dry-run	Preview request without sending
--force	Skip confirmation (always use this flag)
--timeout <ms>	HTTP timeout (default: 5000)
--verbose	Print request/response headers
--transaction	Generate undo transaction (call, set)
Git Bash

On Git Bash (MSYS), /Script/... paths get converted. Always prefix with:

MSYS_NO_PATHCONV=1 ue-cli call ...

Weekly Installs
20
Repository
banab4/ue-cli
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass