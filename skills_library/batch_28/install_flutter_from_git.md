---
title: install-flutter-from-git
url: https://skills.sh/rodydavis/skills/install-flutter-from-git
---

# install-flutter-from-git

skills/rodydavis/skills/install-flutter-from-git
install-flutter-from-git
Installation
$ npx skills add https://github.com/rodydavis/skills --skill install-flutter-from-git
SKILL.md
Install Flutter from Git

This skill guides you through installing the Flutter SDK using git clone and setting up the environment for Web, Mobile, and Desktop development.

1. Prerequisites (All Platforms)

Ensure you have the following installed:

Git: Install Git
Curl/Unzip (macOS/Linux usually have these; Windows usually needs Git Bash or similar)
2. Install Flutter SDK
macOS / Linux

Open your terminal and run the following commands to clone the stable branch of the Flutter SDK.

# Create a directory for development (e.g., ~/development)
mkdir -p ~/development
cd ~/development

# Clone the Flutter SDK
git clone https://github.com/flutter/flutter.git -b stable

Windows

Open PowerShell or Command Prompt.

# Create a directory for development (e.g., C:\src)
mkdir C:\src
cd C:\src

# Clone the Flutter SDK
git clone https://github.com/flutter/flutter.git -b stable

3. Add Flutter to PATH

To run flutter commands from any terminal, you must add the SDK's bin directory to your PATH.

macOS (Zsh) / Linux (Bash/Zsh)

Open your shell configuration file (e.g., ~/.zshrc, ~/.bashrc, or ~/.zshenv).

Add the following line (replace ~/development/flutter with your actual path):

export PATH="$PATH:$HOME/development/flutter/bin"


Refresh your current terminal:

source ~/.zshrc  # or ~/.bashrc

Windows
Press Win + S, type "env", and select Edit the system environment variables.
Click Environment Variables.
Under User variables, select Path and click Edit.
Click New and add the full path to flutter\bin (e.g., C:\src\flutter\bin).
Click OK on all windows.
Restart your terminal/PowerShell.
4. Verify Installation

Run the following command to check for missing dependencies:

flutter doctor

5. Platform Setup
Web (Chrome)
Install Chrome: Ensure Google Chrome is installed.
Enable Web Support (usually enabled by default):
flutter config --enable-web

Verify: Run flutter devices to see "Chrome" listed.
Mobile (iOS & Android)
iOS (macOS only)
Install Xcode: Download from the Mac App Store.
Configure Command Line Tools:
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
sudo xcodebuild -runFirstLaunch

Install CocoaPods (for dependency management):
sudo gem install cocoapods

Simulator: Open via open -a Simulator.
Android (All Operating Systems)
Install Android Studio: Download here.
Install SDK Components:
Open Android Studio -> SDK Manager.
Install Android SDK Platform-Tools.
Install Android SDK Command-line Tools (latest).
Accept Licenses:
flutter doctor --android-licenses

(Press y to accept all licences).
Emulator: Create a device in AVD Manager.
Desktop (macOS, Windows, Linux)
macOS Desktop
Install Xcode: (Same as iOS steps above).
Enable macOS:
flutter config --enable-macos-desktop

Windows Desktop
Install Visual Studio (not VS Code): Download VS Community.
Workloads: When installing, select Desktop development with C++.
Enable Windows:
flutter config --enable-windows-desktop

Linux Desktop
Install Dependencies (Ubuntu/Debian example):
sudo apt-get update
sudo apt-get install clang cmake ninja-build pkg-config libgtk-3-dev liblzma-dev

Enable Linux:
flutter config --enable-linux-desktop

6. Final Check

Run flutter doctor again to ensure all desired platforms have checkmarks.

flutter doctor -v

Weekly Installs
55
Repository
rodydavis/skills
GitHub Stars
40
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn