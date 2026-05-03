---
rating: ⭐⭐
title: flutter-environment-setup-macos
url: https://skills.sh/flutter/skills/flutter-environment-setup-macos
---

# flutter-environment-setup-macos

skills/flutter/skills/flutter-environment-setup-macos
flutter-environment-setup-macos
Installation
$ npx skills add https://github.com/flutter/skills --skill flutter-environment-setup-macos
Summary

Automated macOS Flutter development environment setup with dependency validation and diagnostic fixes.

Verifies Flutter installation, Xcode availability, and CocoaPods presence; stops with clear instructions if any prerequisite is missing
Guides users through Xcode command-line tool configuration and license acceptance with required sudo commands
Runs iterative flutter doctor validation loops to identify and resolve remaining toolchain issues until the Xcode section passes completely
Confirms macOS desktop is enabled as a deployment target and detectable via flutter devices
SKILL.md
flutter-macos-setup
Goal

Configures a macOS development environment for building, running, and deploying Flutter applications. Validates tooling dependencies including Xcode and CocoaPods, and ensures the environment passes Flutter's diagnostic checks for macOS desktop development. Assumes the host operating system is macOS and the user has administrative privileges.

Instructions

Verify Flutter Installation Check if Flutter is installed and accessible in the current environment.

flutter --version


Decision Logic:

If the command fails, STOP AND ASK THE USER: "Flutter is not installed or not in your PATH. Please install Flutter and add it to your PATH before continuing."
If the command succeeds, proceed to step 2.

Verify Xcode Installation Ensure Xcode is installed on the macOS system.

xcodebuild -version


Decision Logic:

If Xcode is not installed, STOP AND ASK THE USER: "Xcode is required for macOS Flutter development. Please install the latest version of Xcode from the Mac App Store and notify me when complete."
If Xcode is installed, proceed to step 3.

Configure Xcode Command-Line Tools Link the Xcode command-line tools to the installed version of Xcode and run the first-launch setup. STOP AND ASK THE USER: "I need to configure Xcode command-line tools. This requires administrative privileges. Please run the following command in your terminal and confirm when done:"

sudo sh -c 'xcode-select -s /Applications/Xcode.app/Contents/Developer && xcodebuild -runFirstLaunch'


(Note: If the user installed Xcode in a non-standard directory, instruct them to replace /Applications/Xcode.app with their custom path).

Accept Xcode Licenses The Xcode license agreements must be accepted before compilation can occur. STOP AND ASK THE USER: "Please run the following command to review and accept the Xcode license agreements:"

sudo xcodebuild -license


Install CocoaPods CocoaPods is required for Flutter plugins that utilize native macOS code. Check if CocoaPods is installed:

pod --version


Decision Logic:

If installed, proceed to step 6.
If not installed, instruct the user to install it (e.g., via Homebrew or RubyGems) and verify the installation.
sudo gem install cocoapods


Validate Setup (Validate-and-Fix Loop) Run the Flutter diagnostic tool to check for any remaining macOS toolchain issues.

flutter doctor -v


Decision Logic:

Analyze the output under the Xcode section.
If there are errors or missing components, identify the specific missing dependency, provide the user with the exact command to fix it, and re-run flutter doctor -v.
Repeat this loop until the Xcode section reports no issues.

Verify Device Availability Ensure Flutter can detect the macOS desktop as a valid deployment target.

flutter devices


Verify that at least one entry in the output has "macos" listed as the platform. If it is missing, instruct the user to enable macOS desktop support:

flutter config --enable-macos-desktop

Constraints
Do NOT include any external URLs or links in the output or prompts.
Do NOT attempt to run sudo commands automatically; always pause and provide the exact command for the user to execute.
Do NOT explain basic terminal usage or general macOS concepts.
MUST ensure the flutter doctor Xcode section is completely clear of errors before considering the skill complete.
MUST assume the user is operating on a macOS environment; do not provide Windows or Linux alternatives.
Weekly Installs
879
Repository
flutter/skills
GitHub Stars
1.3K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn