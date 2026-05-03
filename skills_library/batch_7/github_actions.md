---
title: github-actions
url: https://skills.sh/callstackincubator/agent-skills/github-actions
---

# github-actions

skills/callstackincubator/agent-skills/github-actions
github-actions
Installation
$ npx skills add https://github.com/callstackincubator/agent-skills --skill github-actions
SKILL.md
GitHub Actions Build Artifacts
Overview

Reusable GitHub Actions patterns to build React Native apps for iOS simulators and Android emulators in the cloud, then publish artifacts retrievable via gh CLI or GitHub API.

When to Apply

Use this skill when:

Creating CI workflows that build React Native simulator/emulator artifacts.
Uploading iOS simulator and Android emulator installables from PRs or manual dispatch runs.
Replacing local-only mobile builds with downloadable CI artifacts.
Needing stable artifact IDs/names for scripted retrieval with gh or REST API.
Quick Reference
Add composite actions from gha-ios-composite-action.md and gha-android-composite-action.md.
Wire them into .github/workflows/mobile-build.yml from gha-workflow-and-downloads.md.
Upload with actions/upload-artifact@v4 and capture artifact-id output.
Download with gh run download or GET /repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format}.
References
File	Description
gha-ios-composite-action.md	Composite action.yml for iOS simulator .app.tar.gz builds and artifact upload
gha-android-composite-action.md	Composite action.yml for Android emulator .apk builds and artifact upload
gha-workflow-and-downloads.md	End-to-end workflow wiring plus gh and REST download commands
Problem -> Skill Mapping
Problem	Start With
Need CI iOS simulator .app.tar.gz artifact	gha-ios-composite-action.md
Need CI Android emulator .apk artifact	gha-android-composite-action.md
Need one workflow to trigger both platform jobs	gha-workflow-and-downloads.md
Need scripted artifact download	gha-workflow-and-downloads.md
Source Inspiration
callstackincubator/ios/action.yml
callstackincubator/android/action.yml
Weekly Installs
1.3K
Repository
callstackincuba…t-skills
GitHub Stars
1.3K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn