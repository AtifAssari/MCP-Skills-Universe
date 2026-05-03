---
title: asc-cli-usage
url: https://skills.sh/rudrankriyam/app-store-connect-cli-skills/asc-cli-usage
---

# asc-cli-usage

skills/rudrankriyam/app-store-connect-cli-skills/asc-cli-usage
asc-cli-usage
Installation
$ npx skills add https://github.com/rudrankriyam/app-store-connect-cli-skills --skill asc-cli-usage
Summary

App Store Connect CLI reference for command discovery, flags, output formats, and authentication.

Use --help at any level (asc --help, asc builds --help, asc builds list --help) to discover available commands and flags
Output adapts to context: defaults to table in interactive terminals and json when piped; use --output table or --output markdown for explicit human-readable formatting
Destructive operations require --confirm flag; use --paginate to retrieve all pages of results
Authenticate via keychain with asc auth login, or set environment variables (ASC_KEY_ID, ASC_ISSUER_ID, ASC_PRIVATE_KEY_PATH, etc.); ASC_APP_ID provides a default app
Control request and upload timeouts with ASC_TIMEOUT and ASC_UPLOAD_TIMEOUT environment variables
SKILL.md
asc cli usage

Use this skill when you need to run or design asc commands for App Store Connect.

Command discovery
Always use --help to discover commands and flags.
asc --help
asc builds --help
asc builds list --help
Canonical verbs (current asc)
Prefer view over legacy get aliases for read-only commands in docs and automation.
asc apps view --id "APP_ID"
asc versions view --version-id "VERSION_ID"
asc pricing availability view --app "APP_ID"
Prefer edit for update-only availability surfaces and other canonical edit flows.
asc pricing availability edit --app "APP_ID" --territory "USA,GBR" --available true
asc app-setup availability edit --app "APP_ID" --territory "USA,GBR" --available true
asc xcode version edit --build-number "42"
Keep set where the CLI intentionally models a higher-level replacement/configuration flow and --help still shows set as the canonical verb.
Flag conventions
Use explicit long flags (e.g., --app, --output).
Prefer explicit flags in automation; some newer commands can prompt for missing fields when run interactively.
Destructive operations require --confirm.
Use --paginate when the user wants all pages.
Output formats
Output defaults are TTY-aware: table in interactive terminals, json when piped or non-interactive.
Use --output table or --output markdown only for human-readable output.
--pretty is only valid with JSON output.
Authentication and defaults
Prefer keychain auth via asc auth login.
Fallback env vars: ASC_KEY_ID, ASC_ISSUER_ID, ASC_PRIVATE_KEY_PATH, ASC_PRIVATE_KEY, ASC_PRIVATE_KEY_B64.
ASC_APP_ID can provide a default app ID.
When permissions are unclear, inspect exact API key role coverage with asc web auth capabilities.
This lives under the experimental web auth surface.
It can resolve the current local auth by default, or inspect a specific key with --key-id.
Timeouts
ASC_TIMEOUT / ASC_TIMEOUT_SECONDS control request timeouts.
ASC_UPLOAD_TIMEOUT / ASC_UPLOAD_TIMEOUT_SECONDS control upload timeouts.
Weekly Installs
2.2K
Repository
rudrankriyam/ap…i-skills
GitHub Stars
776
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass