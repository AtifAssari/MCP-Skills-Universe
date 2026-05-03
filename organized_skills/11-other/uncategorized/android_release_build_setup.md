---
rating: ⭐⭐⭐
title: android-release-build-setup
url: https://skills.sh/hitoshura25/claude-devtools/android-release-build-setup
---

# android-release-build-setup

skills/hitoshura25/claude-devtools/android-release-build-setup
android-release-build-setup
Installation
$ npx skills add https://github.com/hitoshura25/claude-devtools --skill android-release-build-setup
SKILL.md
Android Release Build Setup

This skill orchestrates complete Android release build configuration by running three atomic skills in sequence.

What This Does

Sets up everything needed for Android release builds:

Keystore Generation - Production and local dev keystores
ProGuard/R8 Configuration - Code minification and optimization
Signing Configuration - Dual-source signing (CI/CD + local dev)
Prerequisites
Android project with Gradle
JDK installed (for keytool command)
Project uses Kotlin DSL (build.gradle.kts)
Process

This skill runs three sub-skills in order:

Step 1: Generate Keystores

Follow the skill at: ~/claude-devtools/skills/android-keystore-generation/SKILL.md

What it does:

Creates production keystore (for CI/CD only)
Creates local development keystore
Generates KEYSTORE_INFO.txt with credentials
Updates .gitignore

Verify before continuing:

ls keystores/*.jks
cat keystores/KEYSTORE_INFO.txt

Step 2: Configure ProGuard/R8

Follow the skill at: ~/claude-devtools/skills/android-proguard-setup/SKILL.md

What it does:

Creates proguard-rules.pro with safe defaults
Enables minification in build.gradle.kts
Enables resource shrinking

Verify before continuing:

test -f app/proguard-rules.pro
grep "isMinifyEnabled = true" app/build.gradle.kts

Step 3: Configure Signing

Follow the skill at: ~/claude-devtools/skills/android-signing-config/SKILL.md

What it does:

Adds signingConfigs to build.gradle.kts
Creates gradle.properties.template
Configures ~/.gradle/gradle.properties (with permission)
Adds validation for missing signing config

Verify before continuing:

./gradlew assembleRelease
jarsigner -verify app/build/outputs/apk/release/app-release.apk

Final Verification (MANDATORY)

After all three skills complete, verify the complete setup:

# 1. Clean build
./gradlew clean

# 2. Build release APK
./gradlew assembleRelease

# 3. Verify APK exists
ls -lh app/build/outputs/apk/release/app-release.apk

# 4. Verify ProGuard mapping generated
ls -lh app/build/outputs/mapping/release/mapping.txt

# 5. Verify signing
jarsigner -verify -verbose -certs app/build/outputs/apk/release/app-release.apk


All checks must pass before marking this skill as complete.

Completion Criteria

Do NOT mark complete unless ALL are verified:

✅ Keystores generated and secured

 production-release.jks exists in keystores/
 local-dev-release.jks exists in keystores/
 KEYSTORE_INFO.txt created with passwords
 keystores/ added to .gitignore

✅ ProGuard configured

 proguard-rules.pro exists with safe defaults
 isMinifyEnabled = true in build.gradle.kts
 isShrinkResources = true in build.gradle.kts

✅ Signing configured

 signingConfigs.release exists in build.gradle.kts
 Release buildType uses signingConfig
 gradle.properties configured (local) OR environment variables set (CI)

✅ MANDATORY: Build verification

 ./gradlew assembleDebug succeeds
 ./gradlew assembleRelease succeeds
 app/build/outputs/apk/release/app-release.apk exists
 app/build/outputs/mapping/release/mapping.txt exists
 jarsigner -verify confirms APK is signed correctly
Summary Report

After completion, provide this summary:

✅ Android Release Build Setup Complete!

📦 Keystores Generated:
  Production: keystores/production-release.jks (CI/CD only)
  Local Dev: keystores/local-dev-release.jks (local testing)
  Credentials: keystores/KEYSTORE_INFO.txt

🔒 ProGuard/R8 Configuration:
  ✓ Minification enabled
  ✓ Resource shrinking enabled
  ✓ Safe default rules: app/proguard-rules.pro

⚙️  Build Configuration:
  ✓ Signing config added to app/build.gradle.kts
  ✓ Dual-source strategy (env vars + gradle.properties)
  ✓ Validation on release builds

📋 Next Steps:

  For Local Development:
    ./gradlew assembleRelease
    ./gradlew installRelease

  For CI/CD (GitHub Actions):
    Add GitHub Secrets (see KEYSTORE_INFO.txt):
      - SIGNING_KEY_STORE_BASE64
      - SIGNING_KEY_ALIAS
      - SIGNING_STORE_PASSWORD
      - SIGNING_KEY_PASSWORD

⚠️  CRITICAL REMINDERS:
  - NEVER commit keystores to git
  - NEVER use production keystore locally
  - ALWAYS back up production keystore securely
  - Loss of production keystore = cannot update app!

Integration with Other Skills

This skill is prerequisite for:

android-e2e-testing-setup - Tests release builds
android-release-validation - Validates signed APK/AAB
android-playstore-publishing - Uses keystore for CI/CD workflow
android-playstore-pipeline - Orchestrates full setup
Troubleshooting

If any skill fails:

Fix the specific issue in that skill
Re-run that skill until it completes
Continue with remaining skills
Run final verification

Common issues:

Keystore generation fails → Install JDK
ProGuard breaks build → Add keep rules
Signing fails → Check gradle.properties paths
Weekly Installs
11
Repository
hitoshura25/cla…devtools
GitHub Stars
3
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail