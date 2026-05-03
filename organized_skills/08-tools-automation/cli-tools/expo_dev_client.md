---
rating: ⭐⭐⭐
title: expo-dev-client
url: https://skills.sh/expo/skills/expo-dev-client
---

# expo-dev-client

skills/expo/skills/expo-dev-client
expo-dev-client
Installation
$ npx skills add https://github.com/expo/skills --skill expo-dev-client
Summary

Build custom Expo development clients for testing native code on physical devices via EAS Build or locally.

Only needed when using custom native modules, Apple targets (widgets, app clips), or third-party native code not in Expo Go; try Expo Go first with npx expo start
Supports cloud builds with automatic TestFlight submission or local builds on your machine, outputting .ipa (iOS) or .apk/.aab (Android) files
Requires eas.json configuration with a development profile that sets developmentClient: true and autoIncrement: true
Once installed, the dev client launcher UI connects to your local Metro bundler via URL or QR code for live development and native code testing
SKILL.md

Use EAS Build to create development clients for testing native code changes on physical devices. Use this for creating custom Expo Go clients for testing branches of your app.

Important: When Development Clients Are Needed

Only create development clients when your app requires custom native code. Most apps work fine in Expo Go.

You need a dev client ONLY when using:

Local Expo modules (custom native code)
Apple targets (widgets, app clips, extensions)
Third-party native modules not in Expo Go

Try Expo Go first with npx expo start. If everything works, you don't need a dev client.

EAS Configuration

Ensure eas.json has a development profile:

{
  "cli": {
    "version": ">= 16.0.1",
    "appVersionSource": "remote"
  },
  "build": {
    "production": {
      "autoIncrement": true
    },
    "development": {
      "autoIncrement": true,
      "developmentClient": true
    }
  },
  "submit": {
    "production": {},
    "development": {}
  }
}


Key settings:

developmentClient: true - Bundles expo-dev-client for development builds
autoIncrement: true - Automatically increments build numbers
appVersionSource: "remote" - Uses EAS as the source of truth for version numbers
Building for TestFlight

Build iOS dev client and submit to TestFlight in one command:

eas build -p ios --profile development --submit


This will:

Build the development client in the cloud
Automatically submit to App Store Connect
Send you an email when the build is ready in TestFlight

After receiving the TestFlight email:

Download the build from TestFlight on your device
Launch the app to see the expo-dev-client UI
Connect to your local Metro bundler or scan a QR code
Building Locally

Build a development client on your machine:

# iOS (requires Xcode)
eas build -p ios --profile development --local

# Android
eas build -p android --profile development --local


Local builds output:

iOS: .ipa file
Android: .apk or .aab file
Installing Local Builds

Install iOS build on simulator:

# Find the .app in the .tar.gz output
tar -xzf build-*.tar.gz
xcrun simctl install booted ./path/to/App.app


Install iOS build on device (requires signing):

# Use Xcode Devices window or ideviceinstaller
ideviceinstaller -i build.ipa


Install Android build:

adb install build.apk

Building for Specific Platform
# iOS only
eas build -p ios --profile development

# Android only
eas build -p android --profile development

# Both platforms
eas build --profile development

Checking Build Status
# List recent builds
eas build:list

# View build details
eas build:view

Using the Dev Client

Once installed, the dev client provides:

Development server connection - Enter your Metro bundler URL or scan QR
Build information - View native build details
Launcher UI - Switch between development servers

Connect to local development:

# Start Metro bundler
npx expo start --dev-client

# Scan QR code with dev client or enter URL manually

Troubleshooting

Build fails with signing errors:

eas credentials


Clear build cache:

eas build -p ios --profile development --clear-cache


Check EAS CLI version:

eas --version
eas update

Weekly Installs
21.5K
Repository
expo/skills
GitHub Stars
1.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass