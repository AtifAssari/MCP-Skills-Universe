---
title: flutter-setting-up-on-macos
url: https://skills.sh/flutter/skills/flutter-setting-up-on-macos
---

# flutter-setting-up-on-macos

skills/flutter/skills/flutter-setting-up-on-macos
flutter-setting-up-on-macos
Installation
$ npx skills add https://github.com/flutter/skills --skill flutter-setting-up-on-macos
Summary

Automated macOS environment configuration for Flutter development with Xcode and CocoaPods setup.

Guides installation and linking of Xcode command-line tools, acceptance of developer licenses, and CocoaPods dependency management
Includes validation workflow using flutter doctor and flutter devices to confirm proper environment setup and macOS desktop recognition
Provides troubleshooting steps for common issues including missing command-line tools, CocoaPods path problems, and desktop support enablement
SKILL.md
Setting Up a macOS Environment for Flutter Development
Contents
Prerequisites
Tooling Configuration
Workflow: Configuring macOS Tooling
Workflow: Validating the Environment
Troubleshooting
Prerequisites

Ensure the following baseline requirements are met before configuring the macOS-specific toolchain:

macOS operating system.
Flutter SDK installed and added to the system PATH.
Active internet connection for downloading toolchains and dependencies.
Tooling Configuration

macOS desktop development requires specific Apple toolchains to compile and debug native Swift and Objective-C code.

Xcode: Required for compiling macOS desktop applications.
CocoaPods: Required for managing native dependencies used by Flutter plugins.
Workflow: Configuring macOS Tooling

Copy and follow this checklist to configure the macOS build environment.

 Install Xcode: Install the latest version of Xcode from the Mac App Store or the Apple Developer portal.
 Configure Command-Line Tools: Link the Xcode command-line tools to the installed Xcode version. Run the following command in the terminal:
sudo sh -c 'xcode-select -s /Applications/Xcode.app/Contents/Developer && xcodebuild -runFirstLaunch'

Conditional: If Xcode is installed in a custom directory, replace /Applications/Xcode.app with the correct absolute path.
 Accept Xcode Licenses: Accept the required developer licenses by running:
sudo xcodebuild -license

Read and agree to the prompts.
 Install CocoaPods: Install CocoaPods to handle native macOS plugin dependencies.
sudo gem install cocoapods

Conditional: If CocoaPods is already installed, ensure it is updated to the latest version (sudo gem update cocoapods).
Workflow: Validating the Environment

Execute this feedback loop to ensure the environment is correctly configured for macOS desktop development.

 Run Validator: Execute the Flutter diagnostic tool with verbose output:
flutter doctor -v

 Review Errors: Check the Xcode section in the output.
 Fix & Retry: If errors or missing components are reported under the Xcode section, resolve them according to the output instructions, then re-run flutter doctor -v until the Xcode section passes.
 Verify Device Availability: Confirm that Flutter recognizes the macOS desktop as a valid deployment target:
flutter devices

Success Criteria: The output must contain at least one entry with macos listed as the platform.
Troubleshooting

If the validation workflow fails, apply the following resolutions:

Missing Command-Line Tools: If flutter doctor reports missing tools, ensure the xcode-select command was run with sudo and points to the correct .app directory.
CocoaPods Not Found: If CocoaPods is installed but not detected, verify that your Ruby gem binary path is included in your shell's PATH environment variable.
Device Not Listed: If flutter devices does not list macos, ensure desktop support is enabled in your Flutter configuration:
flutter config --enable-macos-desktop

Weekly Installs
7.8K
Repository
flutter/skills
GitHub Stars
1.3K
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn