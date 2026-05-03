---
title: asc-signing-setup
url: https://skills.sh/rudrankriyam/app-store-connect-cli-skills/asc-signing-setup
---

# asc-signing-setup

skills/rudrankriyam/app-store-connect-cli-skills/asc-signing-setup
asc-signing-setup
Installation
$ npx skills add https://github.com/rudrankriyam/app-store-connect-cli-skills --skill asc-signing-setup
Summary

iOS/macOS signing asset setup and rotation via Apple's asc CLI.

Manage bundle IDs, capabilities, signing certificates, and provisioning profiles through command-line workflows
Supports multiple certificate types (distribution, development) and profile types (App Store, ad-hoc, development) with device assignment
Includes rotation and cleanup commands to revoke old certificates and delete expired profiles
Requires prior authentication via asc auth login or environment variables, plus a CSR file for certificate creation
SKILL.md
asc signing setup

Use this skill when you need to create or renew signing assets for iOS/macOS apps.

Preconditions
Auth is configured (asc auth login or ASC_* env vars).
You know the bundle identifier and target platform.
You have a CSR file for certificate creation.
Workflow
Create or find the bundle ID:
asc bundle-ids list --paginate
asc bundle-ids create --identifier "com.example.app" --name "Example" --platform IOS
Configure bundle ID capabilities:
asc bundle-ids capabilities list --bundle "BUNDLE_ID"
asc bundle-ids capabilities add --bundle "BUNDLE_ID" --capability ICLOUD
Add capability settings when required:
--settings '[{"key":"ICLOUD_VERSION","options":[{"key":"XCODE_13","enabled":true}]}]'
Create a signing certificate:
asc certificates list --certificate-type IOS_DISTRIBUTION
asc certificates create --certificate-type IOS_DISTRIBUTION --csr "./cert.csr"
Create a provisioning profile:
asc profiles create --name "AppStore Profile" --profile-type IOS_APP_STORE --bundle "BUNDLE_ID" --certificate "CERT_ID"
Include devices for development/ad-hoc:
asc profiles create --name "Dev Profile" --profile-type IOS_APP_DEVELOPMENT --bundle "BUNDLE_ID" --certificate "CERT_ID" --device "DEVICE_ID"
Download the profile:
asc profiles download --id "PROFILE_ID" --output "./profiles/AppStore.mobileprovision"
Rotation and cleanup
Revoke old certificates:
asc certificates revoke --id "CERT_ID" --confirm
Delete old profiles:
asc profiles delete --id "PROFILE_ID" --confirm
Shared team storage with asc signing sync

Use this when you want a lightweight, non-interactive alternative to fastlane match for encrypted git-backed certificate/profile storage.

# Push current ASC signing assets into an encrypted git repo
asc signing sync push \
  --bundle-id "com.example.app" \
  --profile-type IOS_APP_STORE \
  --repo "git@github.com:team/certs.git" \
  --password "$MATCH_PASSWORD"

# Pull and decrypt them into a local directory
asc signing sync pull \
  --repo "git@github.com:team/certs.git" \
  --password "$MATCH_PASSWORD" \
  --output-dir "./signing"


Notes:

--password falls back to ASC_MATCH_PASSWORD.
The encrypted repo follows a familiar match-style git layout for certs and profiles.
pull writes files to disk; keychain import or profile installation is a separate step.
Notes
Always check --help for the exact enum values (certificate types, profile types).
Use --paginate for large accounts.
--certificate accepts comma-separated IDs when multiple certificates are required.
Device management uses asc devices commands (UDID required).
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