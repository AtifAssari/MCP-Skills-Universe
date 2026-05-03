---
title: asc-metadata-sync
url: https://skills.sh/rudrankriyam/app-store-connect-cli-skills/asc-metadata-sync
---

# asc-metadata-sync

skills/rudrankriyam/app-store-connect-cli-skills/asc-metadata-sync
asc-metadata-sync
Installation
$ npx skills add https://github.com/rudrankriyam/app-store-connect-cli-skills --skill asc-metadata-sync
Summary

Sync App Store Connect metadata and localizations with validation and legacy format migration support.

Manage two localization types: version-specific fields (description, keywords, what's new, support/marketing URLs) and app-level fields (name, subtitle, privacy policy)
Download, validate, and upload .strings files in bulk for multi-language workflows with built-in character limit enforcement
Export current metadata state, validate against App Store requirements, and import updates using the legacy migration workflow
Quick field editing commands for individual metadata updates (what's new, description, keywords, copyright, release type) without file manipulation
SKILL.md
asc metadata sync

Use this skill to keep local metadata in sync with App Store Connect.

Two Types of Localizations
1. Version Localizations (per-release)

Fields: description, keywords, whatsNew, supportUrl, marketingUrl, promotionalText

# List version localizations
asc localizations list --version "VERSION_ID"

# Download
asc localizations download --version "VERSION_ID" --path "./localizations"

# Upload from .strings files
asc localizations upload --version "VERSION_ID" --path "./localizations"

2. App Info Localizations (app-level)

Fields: name, subtitle, privacyPolicyUrl, privacyChoicesUrl, privacyPolicyText

# First, find the app info ID
asc apps info list --app "APP_ID"

# List app info localizations
asc localizations list --app "APP_ID" --type app-info --app-info "APP_INFO_ID"

# Upload app info localizations
asc localizations upload --app "APP_ID" --type app-info --app-info "APP_INFO_ID" --path "./app-info-localizations"


Note: If you get "multiple app infos found", you must specify --app-info with the correct ID.

Legacy Fastlane Metadata Workflow
Export current state
asc migrate export --app "APP_ID" --version-id "VERSION_ID" --output-dir "./fastlane"

Validate local files
asc migrate validate --fastlane-dir "./fastlane"


This checks character limits and required fields.

Import updates
asc migrate import --app "APP_ID" --version-id "VERSION_ID" --fastlane-dir "./fastlane" --dry-run
asc migrate import --app "APP_ID" --version-id "VERSION_ID" --fastlane-dir "./fastlane"

Quick Field Updates
Version-specific fields
# What's New
asc apps info edit --app "APP_ID" --locale "en-US" --whats-new "Bug fixes and improvements"

# Description
asc apps info edit --app "APP_ID" --locale "en-US" --description "Your app description here"

# Keywords
asc apps info edit --app "APP_ID" --locale "en-US" --keywords "keyword1,keyword2,keyword3"

# Support URL
asc apps info edit --app "APP_ID" --locale "en-US" --support-url "https://support.example.com"

Version metadata
# Copyright
asc versions update --version-id "VERSION_ID" --copyright "2026 Your Company"

# Release type
asc versions update --version-id "VERSION_ID" --release-type AFTER_APPROVAL

TestFlight notes
asc build-localizations create --build "BUILD_ID" --locale "en-US" --whats-new "TestFlight notes here"

.strings File Format

For bulk updates, use .strings files:

// en-US.strings
"description" = "Your app description";
"keywords" = "keyword1,keyword2,keyword3";
"whatsNew" = "What's new in this version";
"supportUrl" = "https://support.example.com";


For app-info type:

// en-US.strings (app-info type)
"privacyPolicyUrl" = "https://example.com/privacy";
"name" = "Your App Name";
"subtitle" = "Your subtitle";

Multi-Language Workflow
Export all localizations:
asc localizations download --version "VERSION_ID" --path "./localizations"


Translate the .strings files (or use translation service)

Upload all at once:

asc localizations upload --version "VERSION_ID" --path "./localizations"

Verify:
asc localizations list --version "VERSION_ID" --output table

Character Limits
Field	Limit
Name	30
Subtitle	30
Keywords	100 (comma-separated)
Description	4000
What's New	4000
Promotional Text	170

Use asc metadata validate --dir "./metadata" for canonical metadata trees. Use asc migrate validate --fastlane-dir "./fastlane" for legacy fastlane-format metadata.

Notes
Version localizations and app info localizations are different; use the right command and --type flag.
Use asc localizations list to confirm available locales and IDs.
Privacy Policy URL is in app info localizations, not version localizations.
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