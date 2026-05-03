---
rating: ⭐⭐
title: flutter-environment-setup-linux
url: https://skills.sh/flutter/skills/flutter-environment-setup-linux
---

# flutter-environment-setup-linux

skills/flutter/skills/flutter-environment-setup-linux
flutter-environment-setup-linux
Installation
$ npx skills add https://github.com/flutter/skills --skill flutter-environment-setup-linux
Summary

Linux environment setup for Flutter desktop development with OS detection and toolchain validation.

Automatically detects Debian/Ubuntu or ChromeOS and halts with instructions for non-apt systems
Installs core dependencies (curl, git, unzip, libglu1-mesa) and Linux desktop toolchain (clang, cmake, ninja-build, GTK libraries)
Prompts for optional IDE setup (VS Code or Android Studio via snap)
Runs flutter doctor -v and flutter devices to validate the environment, automatically installing missing packages if detected
SKILL.md
flutter-linux-setup
Goal

Configures a Linux environment (Debian/Ubuntu or ChromeOS) for Flutter desktop application development by installing required system prerequisites, managing OS-specific configurations, and validating the toolchain.

Decision Logic
If OS is ChromeOS: Require manual enablement of Linux support before proceeding to package installation.
If OS is Debian/Ubuntu: Proceed directly to apt-get package updates and installations.
If OS is non-Debian (e.g., Fedora, Arch): Halt and inform the user that this skill specifically targets apt-get package managers.
Instructions

Determine the Host Operating System: STOP AND ASK THE USER: "Are you setting up this Flutter environment on a standard Debian/Ubuntu Linux distribution, or on a Chromebook (ChromeOS)?"

Handle ChromeOS Prerequisites (Conditional): If the user indicates they are on a Chromebook: Instruct the user to navigate to their ChromeOS Settings, turn on "Linux development environment", and ensure it is fully updated. STOP AND ASK THE USER: "Please confirm once Linux support is enabled and updated so we can proceed with the package installation."

Update System Packages: Execute the following command to refresh the package lists and upgrade existing packages:

sudo apt-get update -y && sudo apt-get upgrade -y


Install Core Prerequisites: Install the base dependencies required for Flutter to operate and build on Linux:

sudo apt-get install -y curl git unzip xz-utils zip libglu1-mesa


Install Linux Desktop Toolchain: Install the specific C/C++ toolchain and GTK libraries required to compile Linux desktop applications:

sudo apt-get install -y clang cmake ninja-build pkg-config libgtk-3-dev libstdc++-12-dev


IDE Configuration Prompt: STOP AND ASK THE USER: "For the best experience, an IDE with Flutter support is recommended. Would you like me to provide the installation commands for Visual Studio Code or Android Studio?"

If VS Code: Provide the snap installation command: sudo snap install --classic code
If Android Studio: Provide the snap installation command: sudo snap install android-studio --classic

Validate the Environment: Run the Flutter diagnostic tool to verify the Linux toolchain and device availability:

flutter doctor -v
flutter devices


Validate-and-Fix: Analyze the output of flutter doctor -v.

If the "Linux toolchain" section reports missing dependencies, parse the missing package names, construct a new sudo apt-get install -y <packages> command, and execute it.
If flutter devices does not list a linux platform device, verify that the libgtk-3-dev package was successfully installed and re-run the validation.
Constraints
Do not include any external URLs, hyperlinks, or references to external documentation.
Assume the user has sudo privileges and do not explain basic privilege escalation concepts.
Do not explain what individual packages (e.g., curl, cmake) do; assume the user understands standard Linux development tools.
Strictly use apt-get for package management to ensure non-interactive compatibility (-y flags must be present).
All terminal commands must be enclosed in bash code blocks.
Weekly Installs
781
Repository
flutter/skills
GitHub Stars
1.3K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn