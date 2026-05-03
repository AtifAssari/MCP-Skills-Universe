---
title: flutter-environment-setup-windows
url: https://skills.sh/flutter/skills/flutter-environment-setup-windows
---

# flutter-environment-setup-windows

skills/flutter/skills/flutter-environment-setup-windows
flutter-environment-setup-windows
Installation
$ npx skills add https://github.com/flutter/skills --skill flutter-environment-setup-windows
Summary

Automated Windows Flutter development environment setup with platform-specific toolchain configuration.

Configures Flutter SDK paths, Visual Studio C++ toolchain installation, and platform-specific settings via interactive prompts for Windows Desktop, Android, or both targets
Handles Android Studio setup, device/emulator configuration, and USB driver installation when Android is selected
Generates self-signed MSIX certificates using OpenSSL for local Windows app packaging and deployment
Includes automated validation via flutter doctor with conditional fixes for missing SDK tools, Visual Studio workload issues, and PATH configuration problems
SKILL.md
Goal

Configures a Windows development environment for building Flutter applications targeting Windows Desktop and Android. Analyzes system requirements, modifies environment variables, installs necessary C++ toolchains, manages platform-specific configurations, and generates self-signed certificates for local Windows application deployment. Assumes the host machine is running Windows 10 or 11 with administrative privileges available for system modifications.

Instructions

Configure Flutter SDK and Environment Variables Extract the Flutter SDK to a secure, user-writable directory (e.g., C:\develop\flutter). Do not place it in C:\Program Files\. Execute the following PowerShell command to append the Flutter bin directory to the user's PATH:

$flutterBinPath = "C:\develop\flutter\bin"
$currentUserPath = [Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::User)
if ($currentUserPath -notmatch [regex]::Escape($flutterBinPath)) {
    [Environment]::SetEnvironmentVariable("Path", "$currentUserPath;$flutterBinPath", [EnvironmentVariableTarget]::User)
}


Install Windows Tooling To compile Windows desktop applications, Visual Studio (not VS Code) is strictly required. Install Visual Studio with the "Desktop development with C++" workload. If automating via command line, use the following workload ID:

vs_setup.exe --add Microsoft.VisualStudio.Workload.NativeDesktop --includeRecommended


Decision Logic: Target Platform Configuration STOP AND ASK THE USER: "Which target platforms are you configuring for this environment? (A) Windows Desktop, (B) Android, or (C) Both?"

If (A) Windows Desktop: Proceed to Step 5. Disable Android and Web if unnecessary:
flutter config --no-enable-android
flutter config --no-enable-web
flutter config --enable-windows-desktop

If (B) Android: Proceed to Step 4. Disable Windows desktop if unnecessary:
flutter config --no-enable-windows-desktop

If (C) Both: Execute Steps 4 and 5. Ensure both platforms are enabled.

Configure Android Tooling on Windows

Install Android Studio and the Android SDK Command-line Tools via the SDK Manager.
For physical devices: Enable "Developer options" and "USB debugging" on the device. Install the OEM USB drivers for Windows.
For emulators: Enable hardware acceleration in the AVD Manager by selecting a "Hardware" graphics acceleration option under "Emulated Performance".

Build and Package Windows Desktop Applications To compile the Windows application, execute:

flutter build windows


To package the application manually, gather the following files from build\windows\runner\Release\:

The executable (<project_name>.exe)
All .dll files (e.g., flutter_windows.dll)
The data directory
Visual C++ redistributables (msvcp140.dll, vcruntime140.dll, vcruntime140_1.dll) placed adjacent to the .exe.

Optional: To rename the generated executable, modify the BINARY_NAME in windows/CMakeLists.txt:

# Change this to change the on-disk name of your application.
set(BINARY_NAME "CustomAppName")


Generate Self-Signed Certificates for MSIX Packaging (OpenSSL) If the user requires local testing of an MSIX package, generate a .pfx certificate. Ensure OpenSSL is in the PATH, then execute:

openssl genrsa -out mykeyname.key 2048
openssl req -new -key mykeyname.key -out mycsrname.csr
openssl x509 -in mycsrname.csr -out mycrtname.crt -req -signkey mykeyname.key -days 10000
openssl pkcs12 -export -out CERTIFICATE.pfx -inkey mykeyname.key -in mycrtname.crt


Instruct the user to install CERTIFICATE.pfx into the local machine's Certificate Store under "Trusted Root Certification Authorities".

Validate-and-Fix Feedback Loop Execute the Flutter diagnostic tool to verify the environment:

flutter doctor -v

Condition: If cmdline-tools component is missing is reported, instruct the user to open Android Studio -> Tools -> SDK Manager -> SDK Tools, and check "Android SDK Command-line Tools".
Condition: If Visual Studio toolchain issues are reported, verify the Microsoft.VisualStudio.Workload.NativeDesktop workload is fully installed.
Condition: If flutter is not recognized, verify the PowerShell PATH injection succeeded and restart the terminal process.
Constraints
Do not include external URLs or hyperlinks in any output.
Do not recommend placing the Flutter SDK in directories requiring elevated privileges (e.g., C:\Program Files\).
Do not confuse Visual Studio Code with Visual Studio; the latter is strictly required for the C++ toolchain on Windows.
Always assume the user is operating within a standard Windows command prompt or PowerShell environment unless otherwise specified.
Never skip the flutter doctor validation step; it is mandatory for confirming environment integrity.
Weekly Installs
813
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