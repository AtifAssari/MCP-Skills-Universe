---
title: asc-build-lifecycle
url: https://skills.sh/rudrankriyam/app-store-connect-cli-skills/asc-build-lifecycle
---

# asc-build-lifecycle

skills/rudrankriyam/app-store-connect-cli-skills/asc-build-lifecycle
asc-build-lifecycle
Installation
$ npx skills add https://github.com/rudrankriyam/app-store-connect-cli-skills --skill asc-build-lifecycle
Summary

Query, monitor, and expire builds in App Store Connect with asc command-line tools.

Find builds by version, platform, or upload date; inspect processing state and build details with dedicated query commands
Manage build retention by previewing and applying expiration policies based on age thresholds, with dry-run support
Publish directly to TestFlight or App Store with end-to-end workflows including optional polling, submission, and confirmation flags
Distinguish between asc builds upload (preparation only) and asc publish (full distribution pipeline) for correct workflow selection
SKILL.md
asc build lifecycle

Use this skill to manage build state, processing, and retention.

Find the right build
Latest build:
asc builds info --app "APP_ID" --latest --version "1.2.3" --platform IOS
Next safe build number:
asc builds next-build-number --app "APP_ID" --version "1.2.3" --platform IOS
Recent builds:
asc builds list --app "APP_ID" --sort -uploadedDate --limit 10
Inspect processing state
asc builds info --build-id "BUILD_ID"
Distribution flows
Prefer end-to-end:
asc publish testflight --app "APP_ID" --ipa "./app.ipa" --group "GROUP_ID" --wait
asc publish appstore --app "APP_ID" --ipa "./app.ipa" --version "1.2.3" --wait --submit --confirm
Cleanup
Preview expiration:
asc builds expire-all --app "APP_ID" --older-than 90d --dry-run
Apply expiration:
asc builds expire-all --app "APP_ID" --older-than 90d --confirm
Single build:
asc builds expire --build-id "BUILD_ID" --confirm
Notes
asc builds upload prepares upload operations only; use asc publish for end-to-end flows.
For long processing times, use --wait, --poll-interval, and --timeout where supported.
Weekly Installs
1.9K
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