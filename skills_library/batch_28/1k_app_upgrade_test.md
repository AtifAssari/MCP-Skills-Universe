---
title: 1k-app-upgrade-test
url: https://skills.sh/onekeyhq/app-monorepo/1k-app-upgrade-test
---

# 1k-app-upgrade-test

skills/onekeyhq/app-monorepo/1k-app-upgrade-test
1k-app-upgrade-test
Installation
$ npx skills add https://github.com/onekeyhq/app-monorepo --skill 1k-app-upgrade-test
SKILL.md
Test Version Creation

Automates creation of test version branches with hardcoded build configurations for testing app upgrade functionality and version migration flows.

Quick Reference
Version Pattern

Test versions follow the pattern: 9XXX.YY.Z

9XXX - Test version indicator (e.g., 9005)
YY.Z - Matches production version being tested

Example: 9005.20.0 for testing production 5.20.0

Build Number Formula

Build number is calculated as:

DATE=$(date +%Y%m%d)
BUILD_NUMBER=$((${DATE}00 + 30))


Format: 10 digits = YYYYMMDD00 + 30

Example: If today is 20260130, build number is 2026013030

Workflow
Step 1: Get Version Information

Ask user for test version number:

Format: 9XXX.YY.Z
Example: 9005.20.0
Step 2: Calculate Build Number
DATE=$(date +%Y%m%d)
BUILD_NUMBER=$((${DATE}00 + 30))
echo "Build number: $BUILD_NUMBER"

Step 3: Create Branch
git checkout -b <test_version>
# Example: git checkout -b 9005.20.0

Step 4: Modify Configuration Files

Update these files in order:

.env.version

Set VERSION to test version

.github/actions/shared-env/action.yml

Update version in outputs section

.github/workflows/release-android.yml

Hardcode BUILD_NUMBER in "Write .env.version" step

.github/workflows/release-ios.yml

Hardcode BUILD_NUMBER in "Write .env.version" step

.github/workflows/daily-build.yml

Hardcode BUILD_NUMBER in "Setup ENV" step

apps/mobile/android/app/build.gradle

Update versionCode
Update versionName
Step 5: Commit and Push
git add .
git commit -m "chore: create test version <version>"
git push origin <test_version>

Files to Modify
File	What to Update
.env.version	VERSION
.github/actions/shared-env/action.yml	Hardcode BUILD_NUMBER, remove conditionals
.github/workflows/release-android.yml	Hardcode BUILD_NUMBER in .env.version write
.github/workflows/release-ios.yml	Hardcode BUILD_NUMBER in .env.version write
.github/workflows/daily-build.yml	Hardcode BUILD_NUMBER in Setup ENV step
apps/mobile/android/app/build.gradle	versionCode, versionName
Detailed Guide

For comprehensive test version creation workflow with examples, see upgrade-test-version.md.

Topics covered:

Version number format and conventions
Build number calculation formula
Step-by-step file modification instructions
Configuration file examples
Git workflow for test versions
QA testing considerations
When to Use This Skill
Creating test builds for QA upgrade testing
Testing version migration flows
Verifying app upgrade functionality
Creating release candidates with specific build numbers
Testing version-specific features or fixes
Related Skills
/1k-git-workflow - Git branching conventions
/1k-dev-commands - Build and release commands
Weekly Installs
49
Repository
onekeyhq/app-monorepo
GitHub Stars
2.4K
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass