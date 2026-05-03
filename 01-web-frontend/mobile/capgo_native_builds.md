---
title: capgo-native-builds
url: https://skills.sh/cap-go/capgo-skills/capgo-native-builds
---

# capgo-native-builds

skills/cap-go/capgo-skills/capgo-native-builds
capgo-native-builds
Installation
$ npx skills add https://github.com/cap-go/capgo-skills --skill capgo-native-builds
SKILL.md
Capgo Native Builds

Use Capgo native builds for iOS and Android cloud build requests.

When to Use This Skill
User wants a hosted native iOS or Android build
User needs Capgo build credentials configured or updated
User needs signed build artifacts and temporary output download links
Procedures
Step 1: Prepare Credentials

Before requesting a build, save credentials locally with the Capgo CLI.

Use the credential workflow that matches the platform:

iOS -> certificate, provisioning profiles, App Store Connect credentials
Android -> keystore and Play config
Step 2: Request the Build

Prefer the Capgo build flow:

npx @capgo/cli@latest build request com.example.app --platform ios --path .


Use --platform android for Android builds.

Add --output-upload when the user needs a time-limited download link for the build output.

Step 3: Adjust Build Inputs

Handle platform-specific build inputs as needed:

iOS scheme, target, distribution mode, provisioning profile mapping
Android flavor, keystore alias, Play config

Only add flags that the project actually needs.

Step 4: Manage Credentials

Use the Capgo CLI credential commands for updates:

build credentials save
build credentials list
build credentials update
build credentials clear
build credentials migrate

Keep credentials local unless the user explicitly wants project-local storage.

Error Handling
For iOS signing failures, re-check certificate, provisioning mapping, and App Store Connect fields before retrying the build.
For Android signing failures, re-check the keystore path, alias, and passwords before changing build logic.
For missing output artifacts, verify --output-upload and retention settings first.
Weekly Installs
90
Repository
cap-go/capgo-skills
GitHub Stars
32
First Seen
Mar 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn