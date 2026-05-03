---
title: distributing-tauri-for-android
url: https://skills.sh/dchuk/claude-code-tauri-skills/distributing-tauri-for-android
---

# distributing-tauri-for-android

skills/dchuk/claude-code-tauri-skills/distributing-tauri-for-android
distributing-tauri-for-android
Installation
$ npx skills add https://github.com/dchuk/claude-code-tauri-skills --skill distributing-tauri-for-android
SKILL.md
Distributing Tauri Apps for Android

This skill covers the complete workflow for preparing and distributing Tauri v2 applications on Android, including Google Play Store publication.

Prerequisites

Before distributing your Tauri app for Android:

Play Console Account: Create a developer account at https://play.google.com/console/developers
Android SDK: Ensure Android SDK is installed and configured
Code Signing: Set up Android code signing (keystore)
Tauri Android Initialized: Run tauri android init if not already done
App Icon Configuration

After initializing Android support, configure your app icon:

# npm
npm run tauri icon /path/to/app-icon.png

# yarn
yarn tauri icon /path/to/app-icon.png

# pnpm
pnpm tauri icon /path/to/app-icon.png

# cargo
cargo tauri icon /path/to/app-icon.png


This generates icons in all required sizes for Android.

Build Configuration
tauri.conf.json Android Settings

Configure Android-specific settings in your tauri.conf.json:

{
  "bundle": {
    "android": {
      "minSdkVersion": 24,
      "versionCode": 1
    }
  }
}

Configuration Options
Option	Default	Description
minSdkVersion	24	Minimum Android SDK version (Android 7.0)
versionCode	Auto-calculated	Integer version code for Play Store
Version Code Calculation

Tauri automatically calculates the version code from your app version:

versionCode = major * 1000000 + minor * 1000 + patch


Example: Version 1.2.3 becomes version code 1002003

Override this in tauri.conf.json if you need sequential numbering:

{
  "bundle": {
    "android": {
      "versionCode": 42
    }
  }
}

Minimum SDK Version

Default minimum is Android 7.0 (SDK 24). For higher requirements:

{
  "bundle": {
    "android": {
      "minSdkVersion": 28
    }
  }
}


Common SDK versions:

SDK 24: Android 7.0 (Nougat)
SDK 26: Android 8.0 (Oreo)
SDK 28: Android 9.0 (Pie)
SDK 29: Android 10
SDK 30: Android 11
SDK 31: Android 12
SDK 33: Android 13
SDK 34: Android 14
Building for Distribution
Android App Bundle (AAB) - Recommended

Google Play requires AAB format for new apps. Generate an AAB:

# npm
npm run tauri android build -- --aab

# yarn
yarn tauri android build --aab

# pnpm
pnpm tauri android build -- --aab

# cargo
cargo tauri android build --aab


Output location:

gen/android/app/build/outputs/bundle/universalRelease/app-universal-release.aab

APK Generation

For testing or alternative distribution channels:

# npm
npm run tauri android build -- --apk

# yarn
yarn tauri android build --apk

# pnpm
pnpm tauri android build -- --apk

# cargo
cargo tauri android build --apk

Architecture-Specific Builds

Build for specific CPU architectures:

# Single architecture
npm run tauri android build -- --target aarch64

# Multiple architectures
npm run tauri android build -- --target aarch64 --target armv7


Available targets:

aarch64 - ARM 64-bit (most modern devices)
armv7 - ARM 32-bit (older devices)
i686 - Intel 32-bit (emulators)
x86_64 - Intel 64-bit (emulators, some Chromebooks)
Split APKs by Architecture

Create separate APKs per architecture (useful for testing):

npm run tauri android build -- --apk --split-per-abi


Note: Not needed for Play Store submission. Google Play automatically serves the correct architecture from your AAB.

Code Signing
Generate a Keystore

Create a release keystore for signing:

keytool -genkey -v -keystore release-key.keystore \
  -alias my-app-alias \
  -keyalg RSA \
  -keysize 2048 \
  -validity 10000


Important: Store your keystore securely. Losing it means you cannot update your app.

Configure Signing in Gradle

Create or update gen/android/keystore.properties:

storePassword=your_store_password
keyPassword=your_key_password
keyAlias=my-app-alias
storeFile=/path/to/release-key.keystore


Update gen/android/app/build.gradle.kts to use the keystore:

import java.util.Properties
import java.io.FileInputStream

val keystorePropertiesFile = rootProject.file("keystore.properties")
val keystoreProperties = Properties()
if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(FileInputStream(keystorePropertiesFile))
}

android {
    signingConfigs {
        create("release") {
            keyAlias = keystoreProperties["keyAlias"] as String
            keyPassword = keystoreProperties["keyPassword"] as String
            storeFile = file(keystoreProperties["storeFile"] as String)
            storePassword = keystoreProperties["storePassword"] as String
        }
    }
    buildTypes {
        release {
            signingConfig = signingConfigs.getByName("release")
        }
    }
}

Environment Variables for CI/CD

For automated builds, use environment variables:

android {
    signingConfigs {
        create("release") {
            keyAlias = System.getenv("ANDROID_KEY_ALIAS")
            keyPassword = System.getenv("ANDROID_KEY_PASSWORD")
            storeFile = file(System.getenv("ANDROID_KEYSTORE_PATH"))
            storePassword = System.getenv("ANDROID_STORE_PASSWORD")
        }
    }
}

Google Play Store Submission
Pre-Submission Checklist
App signed with release keystore
Version code incremented from previous release
App icon configured in all required sizes
Screenshots prepared (required by Play Store)
Privacy policy URL ready (required for most apps)
Content rating questionnaire completed
Upload Process
Navigate to Play Console: https://play.google.com/console/developers
Create application or select existing app
Upload AAB file from:
gen/android/app/build/outputs/bundle/universalRelease/app-universal-release.aab

Complete store listing (title, description, screenshots)
Set content rating
Configure pricing and distribution
Submit for review
First Release Requirements

The initial submission requires manual upload through Play Console for signature verification. Google will manage your app signing key through Play App Signing.

Automation Note

Tauri currently does not offer built-in automation for creating Android releases. However, you can use the Google Play Developer API for automated submissions in CI/CD pipelines.

Troubleshooting
Build Fails with Signing Error

Ensure your keystore path is absolute or relative to the correct directory:

# Absolute path
storeFile=/Users/username/keys/release-key.keystore

# Relative to gen/android directory
storeFile=../../release-key.keystore

Version Code Not Incrementing

If using auto-calculation, ensure your package.json or Cargo.toml version is updated. For manual control:

{
  "bundle": {
    "android": {
      "versionCode": 2
    }
  }
}

APK Not Installing on Device

Check minimum SDK version compatibility:

# Check device Android version
adb shell getprop ro.build.version.sdk

AAB Too Large

Consider using --split-per-abi for testing, but for Play Store, Google handles this automatically. If still too large:

Optimize your frontend assets
Use dynamic feature modules
Enable ProGuard/R8 minification
Quick Reference
Common Build Commands
# Development build
npm run tauri android dev

# Release AAB for Play Store
npm run tauri android build -- --aab

# Release APK for testing
npm run tauri android build -- --apk

# Specific architecture
npm run tauri android build -- --aab --target aarch64

File Locations
File	Location
AAB output	gen/android/app/build/outputs/bundle/universalRelease/app-universal-release.aab
APK output	gen/android/app/build/outputs/apk/universal/release/app-universal-release-unsigned.apk
Gradle config	gen/android/app/build.gradle.kts
Keystore properties	gen/android/keystore.properties
Android manifest	gen/android/app/src/main/AndroidManifest.xml
Resources
Google Play Console
Tauri Android Documentation
Google Play Release Checklist
Play App Signing
Weekly Installs
59
Repository
dchuk/claude-co…i-skills
GitHub Stars
18
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass