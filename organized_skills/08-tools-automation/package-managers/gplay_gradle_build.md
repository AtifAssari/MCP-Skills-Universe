---
rating: ⭐⭐⭐
title: gplay-gradle-build
url: https://skills.sh/tamtom/gplay-cli-skills/gplay-gradle-build
---

# gplay-gradle-build

skills/tamtom/gplay-cli-skills/gplay-gradle-build
gplay-gradle-build
Installation
$ npx skills add https://github.com/tamtom/gplay-cli-skills --skill gplay-gradle-build
SKILL.md
Gradle Build for Google Play

Use this skill when you need to build an Android app before uploading to Play Store.

Build Types
App Bundle (AAB) - Recommended

App Bundles are required for new apps on Google Play:

./gradlew bundleRelease


Output: app/build/outputs/bundle/release/app-release.aab

APK - Legacy

For apps not using bundles:

./gradlew assembleRelease


Output: app/build/outputs/apk/release/app-release.apk

Signing Configuration
build.gradle (app level)
android {
    signingConfigs {
        release {
            storeFile file(System.getenv("KEYSTORE_FILE") ?: "release.keystore")
            storePassword System.getenv("KEYSTORE_PASSWORD")
            keyAlias System.getenv("KEY_ALIAS")
            keyPassword System.getenv("KEY_PASSWORD")
        }
    }

    buildTypes {
        release {
            signingConfig signingConfigs.release
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}

Environment Variables
export KEYSTORE_FILE=/path/to/release.keystore
export KEYSTORE_PASSWORD=your_keystore_password
export KEY_ALIAS=your_key_alias
export KEY_PASSWORD=your_key_password

./gradlew bundleRelease

Version Management
gradle.properties
VERSION_NAME=1.2.3
VERSION_CODE=123

build.gradle
android {
    defaultConfig {
        versionCode project.property('VERSION_CODE').toInteger()
        versionName project.property('VERSION_NAME')
    }
}

Increment version
# Read current version
CURRENT_VERSION=$(grep VERSION_CODE gradle.properties | cut -d'=' -f2)
NEW_VERSION=$((CURRENT_VERSION + 1))

# Update gradle.properties
sed -i "" "s/VERSION_CODE=$CURRENT_VERSION/VERSION_CODE=$NEW_VERSION/" gradle.properties

# Build
./gradlew bundleRelease

ProGuard/R8 Configuration
Enable R8 (default in AGP 3.4+)
buildTypes {
    release {
        minifyEnabled true
        shrinkResources true
        proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
    }
}

Generate mapping file

Mapping file location: app/build/outputs/mapping/release/mapping.txt

Upload to Play Console for crash symbolication:

gplay deobfuscation upload \
  --package com.example.app \
  --edit $EDIT_ID \
  --apk-version 123 \
  --type proguard \
  --file app/build/outputs/mapping/release/mapping.txt

Build Variants
Product Flavors
android {
    flavorDimensions "version"
    productFlavors {
        free {
            dimension "version"
            applicationIdSuffix ".free"
        }
        paid {
            dimension "version"
        }
    }
}

Build specific flavor
./gradlew bundleFreeRelease
./gradlew bundlePaidRelease

CI/CD Build
GitHub Actions Example
- name: Build Release AAB
  run: |
    echo "${{ secrets.KEYSTORE_BASE64 }}" | base64 -d > release.keystore
    export KEYSTORE_FILE=release.keystore
    export KEYSTORE_PASSWORD="${{ secrets.KEYSTORE_PASSWORD }}"
    export KEY_ALIAS="${{ secrets.KEY_ALIAS }}"
    export KEY_PASSWORD="${{ secrets.KEY_PASSWORD }}"
    ./gradlew bundleRelease

- name: Upload to Play Store
  env:
    GPLAY_SERVICE_ACCOUNT: ${{ secrets.PLAY_SERVICE_ACCOUNT }}
  run: |
    gplay release \
      --package com.example.app \
      --track internal \
      --bundle app/build/outputs/bundle/release/app-release.aab

Common Build Tasks
Clean build
./gradlew clean bundleRelease

Build with specific SDK versions
./gradlew bundleRelease -PminSdkVersion=21 -PtargetSdkVersion=34

Build without tests
./gradlew bundleRelease -x test -x lint

Build multiple variants
./gradlew bundle  # Builds all variants

Troubleshooting
Build fails with signing errors
# Verify keystore
keytool -list -v -keystore release.keystore

Check AAB contents
bundletool build-apks \
  --bundle=app-release.aab \
  --output=output.apks \
  --mode=universal

unzip output.apks

Verify version codes
./gradlew tasks --all | grep Version

Best Practices
Never commit keystores - Store in secure location
Use environment variables for credentials
Enable ProGuard/R8 for release builds
Upload mapping files after each release
Increment version code for every build
Test release builds before uploading
Use App Bundles (AAB) instead of APKs when possible
Weekly Installs
89
Repository
tamtom/gplay-cli-skills
GitHub Stars
33
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass