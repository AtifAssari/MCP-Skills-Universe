---
title: distributing-tauri-for-ios
url: https://skills.sh/dchuk/claude-code-tauri-skills/distributing-tauri-for-ios
---

# distributing-tauri-for-ios

skills/dchuk/claude-code-tauri-skills/distributing-tauri-for-ios
distributing-tauri-for-ios
Installation
$ npx skills add https://github.com/dchuk/claude-code-tauri-skills --skill distributing-tauri-for-ios
SKILL.md
Distributing Tauri Apps for iOS

This skill covers the complete process of distributing Tauri v2 applications to Apple's iOS App Store.

Prerequisites

Before distributing a Tauri iOS app, ensure:

macOS development machine (required for iOS builds)
Xcode installed with iOS SDK
Apple Developer Program enrollment ($99/year)
Tauri project initialized for iOS (tauri ios init)
Apple Developer Program Enrollment

Enroll at developer.apple.com/programs:

Sign in with Apple ID
Accept the Apple Developer Agreement
Complete enrollment (individual or organization)
Wait for approval (typically 24-48 hours)
Bundle Identifier Configuration

The bundle identifier must be unique and match across all configurations.

tauri.conf.json
{
  "identifier": "com.yourcompany.yourapp",
  "version": "1.0.0",
  "bundle": {
    "iOS": {
      "bundleVersion": "1"
    }
  }
}


Configuration notes:

identifier: Reverse-domain format, must match App Store Connect
version: Becomes CFBundleShortVersionString (user-visible version)
bundleVersion: Becomes CFBundleVersion (build number, must increment for each upload)
Register Bundle ID in App Store Connect
Go to Certificates, Identifiers & Profiles
Click "+" to register a new identifier
Select "App IDs" then "App"
Enter description and explicit Bundle ID matching tauri.conf.json
Select required capabilities
Click "Register"
Code Signing Setup
Create Certificates

Distribution Certificate (required for App Store):

Open Keychain Access on macOS
Keychain Access > Certificate Assistant > Request a Certificate from a Certificate Authority
Enter email, select "Saved to disk"
Go to Certificates
Click "+" and select "Apple Distribution"
Upload the certificate signing request
Download and double-click to install
Create Provisioning Profile

App Store Distribution Profile:

Go to Profiles
Click "+" to create new profile
Select "App Store Connect" under Distribution
Select your App ID
Select your distribution certificate
Name and generate the profile
Download the .mobileprovision file
Install Provisioning Profile
# Copy to Xcode provisioning profiles directory
cp ~/Downloads/YourApp_AppStore.mobileprovision \
   ~/Library/MobileDevice/Provisioning\ Profiles/


Or double-click the file to install automatically.

Xcode Project Configuration

Open the Tauri iOS project in Xcode:

tauri ios build --open

Configure Signing in Xcode
Select the project in the navigator
Select your app target
Go to "Signing & Capabilities" tab
Uncheck "Automatically manage signing" for manual control
Select your Team
Select the App Store provisioning profile
Required Capabilities

Add capabilities based on app requirements:

Capability	When Required
Push Notifications	If using APNs
Background Modes	For background tasks
App Groups	For sharing data between extensions
Associated Domains	For universal links
Info.plist Configuration

Located at src-tauri/gen/apple/[AppName]_iOS/Info.plist:

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleDisplayName</key>
    <string>Your App Name</string>
    <key>CFBundleName</key>
    <string>YourApp</string>
    <key>CFBundleIdentifier</key>
    <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
    <key>CFBundleVersion</key>
    <string>$(CURRENT_PROJECT_VERSION)</string>
    <key>CFBundleShortVersionString</key>
    <string>$(MARKETING_VERSION)</string>
    <key>UILaunchStoryboardName</key>
    <string>LaunchScreen</string>
    <key>UISupportedInterfaceOrientations</key>
    <array>
        <string>UIInterfaceOrientationPortrait</string>
        <string>UIInterfaceOrientationLandscapeLeft</string>
        <string>UIInterfaceOrientationLandscapeRight</string>
    </array>
    <key>NSCameraUsageDescription</key>
    <string>This app requires camera access for...</string>
    <key>NSPhotoLibraryUsageDescription</key>
    <string>This app requires photo library access for...</string>
</dict>
</plist>


Required usage descriptions (add only if your app uses these features):

NSCameraUsageDescription: Camera access
NSPhotoLibraryUsageDescription: Photo library
NSLocationWhenInUseUsageDescription: Location services
NSMicrophoneUsageDescription: Microphone access
App Icons

Generate iOS app icons from a source image (1024x1024 recommended):

tauri icon /path/to/app-icon.png --ios-color '#ffffff'


This generates all required icon sizes in src-tauri/gen/apple/Assets.xcassets/AppIcon.appiconset/.

Building for App Store
Command Line Build
# Build IPA for App Store Connect
tauri ios build --export-method app-store-connect


The IPA is generated at:

src-tauri/gen/apple/build/arm64/[AppName].ipa

Build Options
# Build with specific target
tauri ios build --target aarch64-apple-ios --export-method app-store-connect

# Build in release mode (default for export-method)
tauri ios build --release --export-method app-store-connect

# Build and open in Xcode for manual archive
tauri ios build --open

Archive via Xcode (Alternative)
Open project: tauri ios build --open
Select "Any iOS Device" as destination
Product > Archive
Window > Organizer to view archives
Click "Distribute App"
Select "App Store Connect"
Follow the wizard
App Store Connect API Key Setup

Create an API key for automated uploads:

Go to App Store Connect > Users and Access
Select "Integrations" tab
Click "App Store Connect API" then "+"
Name the key and select "Admin" or "Developer" role
Click "Generate"
Download the .p8 file (only available once)
Note the Key ID and Issuer ID
Store the API Key
# Create directory
mkdir -p ~/.appstoreconnect/private_keys

# Move the key file (rename to include Key ID)
mv ~/Downloads/AuthKey_XXXXXXXXXX.p8 ~/.appstoreconnect/private_keys/

# Alternative location
mkdir -p ~/private_keys
mv ~/Downloads/AuthKey_XXXXXXXXXX.p8 ~/private_keys/

Environment Variables (Optional)
export APPLE_API_KEY_ID="XXXXXXXXXX"
export APPLE_API_ISSUER="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

Uploading to App Store Connect
Using altool
xcrun altool --upload-app \
  --type ios \
  --file "src-tauri/gen/apple/build/arm64/YourApp.ipa" \
  --apiKey "$APPLE_API_KEY_ID" \
  --apiIssuer "$APPLE_API_ISSUER"

Using Transporter App
Download Transporter from Mac App Store
Sign in with Apple ID
Drag and drop the IPA file
Click "Deliver"
Using Xcode Organizer
Window > Organizer
Select your archive
Click "Distribute App"
Select "App Store Connect"
Choose "Upload" or "Export"
Follow prompts
TestFlight Beta Testing

After upload processing (typically 15-30 minutes):

Internal Testing
App Store Connect > Your App > TestFlight
Add internal testers (up to 100, must be App Store Connect users)
Testers receive email invitation
External Testing
Create a test group
Add build to the group
Submit for Beta App Review (required for external testers)
Add external testers (up to 10,000)
Testers install via TestFlight app
App Store Submission
Create App in App Store Connect
Go to App Store Connect
My Apps > "+" > New App
Select iOS platform
Enter app name, primary language, bundle ID, SKU
Click "Create"
Prepare App Store Listing

Required assets:

Asset	Specification
Screenshots	6.7" (1290x2796), 6.5" (1284x2778), 5.5" (1242x2208)
App Icon	1024x1024 PNG (no alpha)
Description	Up to 4000 characters
Keywords	Up to 100 characters
Support URL	Required
Privacy Policy URL	Required
App Privacy

Complete the App Privacy questionnaire:

App Store Connect > Your App > App Privacy
Answer questions about data collection
Specify data types collected
Indicate data usage purposes
Submit for Review
Select your build in App Store Connect
Complete all required metadata
Answer export compliance questions
Click "Submit for Review"

Review typically takes 24-48 hours.

Common Issues and Solutions
Code Signing Errors

"No signing certificate found"

# List available certificates
security find-identity -v -p codesigning

# Verify certificate is valid
security find-certificate -c "Apple Distribution" -p


"Provisioning profile doesn't match"

Ensure bundle ID matches exactly in all locations
Regenerate provisioning profile if certificates changed
Build Failures

"Unsupported architecture"

# Ensure building for correct target
tauri ios build --target aarch64-apple-ios --export-method app-store-connect


"Missing entitlements"

Check capabilities in Xcode match App ID capabilities
Regenerate provisioning profile after capability changes
Upload Errors

"Invalid binary"

Ensure minimum iOS version is set correctly
Verify all required icons are present
Check Info.plist has required keys

"Missing compliance" Add to Info.plist if not using encryption:

<key>ITSAppUsesNonExemptEncryption</key>
<false/>

CI/CD Integration
GitHub Actions Example
name: iOS Release

on:
  push:
    tags:
      - 'v*'

jobs:
  build-ios:
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Rust
        uses: dtolnay/rust-action@stable
        with:
          targets: aarch64-apple-ios

      - name: Install dependencies
        run: npm ci

      - name: Install certificate
        env:
          CERTIFICATE_BASE64: ${{ secrets.APPLE_CERTIFICATE_BASE64 }}
          CERTIFICATE_PASSWORD: ${{ secrets.APPLE_CERTIFICATE_PASSWORD }}
        run: |
          CERTIFICATE_PATH=$RUNNER_TEMP/certificate.p12
          KEYCHAIN_PATH=$RUNNER_TEMP/app-signing.keychain-db

          echo -n "$CERTIFICATE_BASE64" | base64 --decode > $CERTIFICATE_PATH

          security create-keychain -p "" $KEYCHAIN_PATH
          security set-keychain-settings -lut 21600 $KEYCHAIN_PATH
          security unlock-keychain -p "" $KEYCHAIN_PATH

          security import $CERTIFICATE_PATH -P "$CERTIFICATE_PASSWORD" \
            -A -t cert -f pkcs12 -k $KEYCHAIN_PATH

          security list-keychain -d user -s $KEYCHAIN_PATH

      - name: Install provisioning profile
        env:
          PROVISIONING_PROFILE_BASE64: ${{ secrets.PROVISIONING_PROFILE_BASE64 }}
        run: |
          PP_PATH=$RUNNER_TEMP/profile.mobileprovision
          echo -n "$PROVISIONING_PROFILE_BASE64" | base64 --decode > $PP_PATH
          mkdir -p ~/Library/MobileDevice/Provisioning\ Profiles
          cp $PP_PATH ~/Library/MobileDevice/Provisioning\ Profiles/

      - name: Build iOS
        run: npm run tauri ios build -- --export-method app-store-connect

      - name: Upload to App Store Connect
        env:
          APPLE_API_KEY_ID: ${{ secrets.APPLE_API_KEY_ID }}
          APPLE_API_ISSUER: ${{ secrets.APPLE_API_ISSUER }}
          APPLE_API_KEY: ${{ secrets.APPLE_API_KEY }}
        run: |
          mkdir -p ~/.appstoreconnect/private_keys
          echo "$APPLE_API_KEY" > ~/.appstoreconnect/private_keys/AuthKey_$APPLE_API_KEY_ID.p8

          xcrun altool --upload-app --type ios \
            --file src-tauri/gen/apple/build/arm64/*.ipa \
            --apiKey $APPLE_API_KEY_ID \
            --apiIssuer $APPLE_API_ISSUER

Version Management
Incrementing Versions

For each App Store submission, increment appropriately:

{
  "version": "1.0.0",
  "bundle": {
    "iOS": {
      "bundleVersion": "1"
    }
  }
}

version: Increment for user-visible changes (1.0.0 -> 1.0.1 or 1.1.0)
bundleVersion: Must increment for every upload (1 -> 2 -> 3)
Version Script Example
#!/bin/bash
# increment-build.sh
CONFIG="src-tauri/tauri.conf.json"
CURRENT=$(jq -r '.bundle.iOS.bundleVersion' $CONFIG)
NEW=$((CURRENT + 1))
jq ".bundle.iOS.bundleVersion = \"$NEW\"" $CONFIG > tmp.json && mv tmp.json $CONFIG
echo "Bundle version incremented to $NEW"

Reference Links
Apple Developer Program
App Store Connect
App Store Review Guidelines
Tauri iOS Documentation
Tauri Distribution Guide
Weekly Installs
58
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