---
rating: ⭐⭐
title: asc-wall-submit
url: https://skills.sh/rudrankriyam/app-store-connect-cli-skills/asc-wall-submit
---

# asc-wall-submit

skills/rudrankriyam/app-store-connect-cli-skills/asc-wall-submit
asc-wall-submit
Installation
$ npx skills add https://github.com/rudrankriyam/app-store-connect-cli-skills --skill asc-wall-submit
Summary

Submit or update Wall of Apps entries via App-Store-Connect-CLI with dry-run preview and confirmation flow.

Supports two submission paths: standard App Store flow using app ID, or manual flow using TestFlight link and app name
Includes dry-run mode to preview changes before applying with --confirm flag
Generates PR-based submissions that modify docs/wall-of-apps.json with built-in guardrails against unrelated entry changes
Run commands from the App-Store-Connect-CLI repository root; fix invalid inputs and rerun if submission fails
SKILL.md
asc wall submit

Use this skill to add or update a Wall of Apps entry with the built-in CLI flow.

When to use
User wants to submit an app to the Wall of Apps
User wants to update an existing Wall of Apps entry
User asks for the exact Wall submission flow
Required inputs

Use one of these input paths:

Standard App Store flow: app ID
Manual/pre-release flow: link plus name
Submission workflow
Run commands from the App-Store-Connect-CLI repository root.
Preview first:
asc apps wall submit --app "1234567890" --dry-run
or asc apps wall submit --link "https://testflight.apple.com/join/ABCDEFG" --name "My Beta App" --dry-run
Apply with confirmation:
asc apps wall submit --app "1234567890" --confirm
or asc apps wall submit --link "https://testflight.apple.com/join/ABCDEFG" --name "My Beta App" --confirm
Review the generated PR plan and resulting change to docs/wall-of-apps.json.
Guardrails
Do not modify unrelated entries in docs/wall-of-apps.json.
If submission fails due to invalid input, fix the inputs and rerun the CLI command.
Keep submission path PR-based unless maintainers define an issue-based intake flow.
Examples

Add new app:

asc apps wall submit --app "1234567890" --confirm

Submit a non-App-Store/TestFlight entry:

asc apps wall submit --link "https://testflight.apple.com/join/ABCDEFG" --name "My Beta App" --confirm

Weekly Installs
1.2K
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