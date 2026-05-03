---
title: gpd-cli-usage
url: https://skills.sh/rudrankriyam/app-store-connect-cli-skills/gpd-cli-usage
---

# gpd-cli-usage

skills/rudrankriyam/app-store-connect-cli-skills/gpd-cli-usage
gpd-cli-usage
Installation
$ npx skills add https://github.com/rudrankriyam/app-store-connect-cli-skills --skill gpd-cli-usage
SKILL.md
GPD CLI usage

Use this skill when you need to run or design gpd commands for Google Play Developer Console.

Command discovery
Always use --help to confirm commands and flags.
gpd --help
gpd publish --help
gpd monetization --help
Flag conventions
Use explicit long flags (for example: --package, --track, --status).
No interactive prompts; destructive operations require --confirm.
Use --all when the user wants all pages.
Output formats
Default output is minified JSON.
Use --pretty for readable JSON during debugging.
Authentication and defaults
Service account auth via GPD_SERVICE_ACCOUNT_KEY is required.
Validate access for a package:
gpd auth check --package com.example.app
Safety
Use --dry-run when available before destructive operations.
Prefer edit lifecycle (gpd publish edit create) for multi-step publishing.
Weekly Installs
222
Repository
rudrankriyam/ap…i-skills
GitHub Stars
776
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass