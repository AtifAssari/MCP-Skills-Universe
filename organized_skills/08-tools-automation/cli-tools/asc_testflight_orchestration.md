---
rating: ⭐⭐
title: asc-testflight-orchestration
url: https://skills.sh/rudrankriyam/app-store-connect-cli-skills/asc-testflight-orchestration
---

# asc-testflight-orchestration

skills/rudrankriyam/app-store-connect-cli-skills/asc-testflight-orchestration
asc-testflight-orchestration
Installation
$ npx skills add https://github.com/rudrankriyam/app-store-connect-cli-skills --skill asc-testflight-orchestration
Summary

Orchestrate TestFlight distribution, tester groups, and release notes via the App Store Connect CLI.

Manage testers and groups with list, create, add, and invite commands; supports pagination for large datasets
Distribute builds to groups and remove them with confirmation; export and import full TestFlight configuration as YAML
Create and update "What to Test" notes per build and locale for release communication
Use IDs for deterministic operations; integrates with the ID resolver skill for name-to-ID lookups
SKILL.md
asc TestFlight orchestration

Use this skill when managing TestFlight testers, groups, and build distribution.

Export current config
asc testflight config export --app "APP_ID" --output "./testflight.yaml"
Include builds/testers:
asc testflight config export --app "APP_ID" --output "./testflight.yaml" --include-builds --include-testers
Manage groups and testers
Groups:
asc testflight groups list --app "APP_ID" --paginate
asc testflight groups create --app "APP_ID" --name "Beta Testers"
Testers:
asc testflight testers list --app "APP_ID" --paginate
asc testflight testers add --app "APP_ID" --email "tester@example.com" --group "Beta Testers"
asc testflight testers invite --app "APP_ID" --email "tester@example.com"
Distribute builds
asc builds add-groups --build-id "BUILD_ID" --group "GROUP_ID"
Remove from group:
asc builds remove-groups --build-id "BUILD_ID" --group "GROUP_ID" --confirm
What to Test notes
asc builds test-notes create --build-id "BUILD_ID" --locale "en-US" --whats-new "Test instructions"
asc builds test-notes update --localization-id "LOCALIZATION_ID" --whats-new "Updated notes"
Notes
Use --paginate on large groups/tester lists.
Prefer IDs for deterministic operations; use the ID resolver skill when needed.
Weekly Installs
2.0K
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