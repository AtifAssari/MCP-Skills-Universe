---
title: asc-id-resolver
url: https://skills.sh/rudrankriyam/app-store-connect-cli-skills/asc-id-resolver
---

# asc-id-resolver

skills/rudrankriyam/app-store-connect-cli-skills/asc-id-resolver
asc-id-resolver
Installation
$ npx skills add https://github.com/rudrankriyam/app-store-connect-cli-skills --skill asc-id-resolver
Summary

Resolve App Store Connect IDs from human-friendly names for use in other asc commands.

Maps bundle IDs, app names, and version strings to their corresponding ASC identifiers across apps, builds, versions, TestFlight groups, testers, and review submissions
Supports filtering by bundle ID, app name, version, and platform; includes pagination and sorting options to ensure complete and deterministic results
Outputs JSON by default with --pretty, --table, and --markdown formatting options for debugging and readability
Allows setting a default app ID via ASC_APP_ID environment variable to reduce repetition across sequential commands
SKILL.md
asc id resolver

Use this skill to map names to IDs needed by other commands.

App ID
By bundle ID or name:
asc apps list --bundle-id "com.example.app"
asc apps list --name "My App"
Fetch everything:
asc apps --paginate
Set default:
ASC_APP_ID=...
Build ID
Latest build:
asc builds info --app "APP_ID" --latest --version "1.2.3" --platform IOS
Recent builds:
asc builds list --app "APP_ID" --sort -uploadedDate --limit 5
Version ID
asc versions list --app "APP_ID" --paginate
TestFlight IDs
Groups:
asc testflight groups list --app "APP_ID" --paginate
Testers:
asc testflight testers list --app "APP_ID" --paginate
Pre-release version IDs
asc testflight pre-release list --app "APP_ID" --platform IOS --paginate
Review submission IDs
asc review submissions-list --app "APP_ID" --paginate
Output tips
JSON is default; use --pretty for debug.
For human viewing, use --output table or --output markdown.
Guardrails
Prefer --paginate on list commands to avoid missing IDs.
Use --sort where available to make results deterministic.
Weekly Installs
1.9K
Repository
rudrankriyam/ap…i-skills
GitHub Stars
776
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass