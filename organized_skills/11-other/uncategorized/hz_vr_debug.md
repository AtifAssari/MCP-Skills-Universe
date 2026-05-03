---
rating: ⭐⭐⭐
title: hz-vr-debug
url: https://skills.sh/meta-quest/agentic-tools/hz-vr-debug
---

# hz-vr-debug

skills/meta-quest/agentic-tools/hz-vr-debug
hz-vr-debug
Installation
$ npx skills add https://github.com/meta-quest/agentic-tools --skill hz-vr-debug
SKILL.md
VR Debug Skill

Debug Meta Quest VR and MR applications using the hzdb command-line interface. This skill covers viewing application logs, capturing device state, diagnosing crashes, and resolving common issues encountered during Quest development.

When to Use This Skill

Use this skill when you need to:

Debug an application running on a connected Meta Quest device
View real-time or historical application logs (logcat)
Capture screenshots of the VR/MR view
Diagnose application crashes, rendering glitches, or performance problems
Investigate tracking, controller, audio, or permission issues
Pull diagnostic files from the device for offline analysis

This skill is relevant for any Meta Quest headset (Quest 2, Quest 3, Quest 3S, Quest Pro) running Horizon OS.

Prerequisites

Before using this skill, ensure the following are in place:

hzdb CLI installed -- Install the hzdb CLI:
npm install -g @meta-quest/hzdb

Verify with hzdb --version. hzdb wraps ADB and adds Quest-specific device management, log viewing, screenshot capture, and file management.
Meta Quest device connected via USB -- Use a USB-C cable that supports data transfer (not charge-only).
Developer mode enabled -- Developer mode must be turned on in the Meta Horizon app on your phone, under your headset's settings.
ADB authorization accepted -- The first time you connect, you must put on the headset and accept the "Allow USB debugging" prompt.
Quick Start Workflow

The fastest way to begin debugging a Quest application:

# 1. Verify the device is connected and recognized
hzdb device list

# 2. List applications currently installed
hzdb app list

# 3. View live logs (most recent 100 lines)
hzdb log

# 4. Capture a screenshot of the current VR view
hzdb capture screenshot


If hzdb device list returns no devices, check the USB cable, developer mode, and ADB authorization.

Key Debugging Commands
Device Commands
Command	Description
hzdb device list	List all connected Quest devices
hzdb device info <id>	Show device model, OS version, and more
hzdb device battery	Show battery level and charging status
hzdb device wake	Wake the device from sleep
hzdb device reboot	Reboot the device
hzdb device connect <ip>	Connect to a device over WiFi
Log Commands
Command	Description
hzdb log	View the last 100 log lines
hzdb log -n 500	View the last 500 log lines
hzdb log --tag Unity	Filter logs by tag
hzdb log --level E	Filter by severity (V, D, I, W, E, F)
hzdb adb logcat	Full logcat with advanced filtering options
hzdb adb logcat --follow	Stream logs continuously
Application Commands
Command	Description
hzdb app list	List installed applications
hzdb app info <package>	Show detailed info about an app
hzdb app launch <package>	Launch an application by package name
hzdb app stop <package>	Force-stop a running application
hzdb app clear <package>	Clear application data and cache
hzdb app install <apk>	Install an APK to the device
hzdb app uninstall <package>	Uninstall an application
Capture Commands
Command	Description
hzdb capture screenshot	Capture a screenshot of the current VR/MR view
hzdb capture screenshot -o file.png	Save screenshot to a specific file
File Commands
Command	Description
hzdb files ls /sdcard/	List files on the device
hzdb files pull /sdcard/path/file ./local/	Pull a file from the device
hzdb files push ./local/file /sdcard/path/	Push a file to the device
hzdb files rm /sdcard/path/file	Delete a file on the device
hzdb files mkdir /sdcard/path/dir	Create a directory on the device
Common Debugging Workflow

A typical debugging session follows this pattern:

1. Connect and Verify
hzdb device list
hzdb device info <device_id>


Confirm the device is recognized, check the OS version, and note the battery level. A low battery can cause thermal throttling that affects performance tests.

2. Identify the Application
hzdb app list


Find the package name for the application you want to debug. Package names typically follow the pattern com.company.appname.

3. Reproduce and Capture Logs
# Start logging before reproducing the issue
hzdb adb logcat --follow


Put on the headset and reproduce the issue. The logs stream in real time to your terminal. Press Ctrl+C to stop.

4. Capture Visual State
# Take a screenshot at the moment of the issue
hzdb capture screenshot

5. Analyze and Diagnose

Review the captured logs for errors, warnings, and crash signatures. Look for:

FATAL EXCEPTION -- Unhandled Java/Kotlin exceptions
native crash or SIGABRT / SIGSEGV -- Native code crashes
ANR -- Application Not Responding (frozen UI thread)
OOM or OutOfMemoryError -- Memory exhaustion
6. Iterate

Make code changes, rebuild, deploy, and test again:

hzdb app stop com.example.myapp
hzdb app launch com.example.myapp
hzdb log --tag Unity --level W

Tips and Best Practices
Filtering Logs Effectively

Use severity filters to cut through noise:

# Show only errors
hzdb log --level E

# Show warnings and above
hzdb log --level W


Filter by tag to focus on specific subsystems:

hzdb adb logcat --tag VrApi
hzdb adb logcat --tag Unity


Use advanced filters with hzdb adb logcat:

# Complex filter expressions
hzdb adb logcat --filter "Unity:W ActivityManager:I"

# Regex pattern matching
hzdb adb logcat --regex "error|exception"

# Specific log buffer
hzdb adb logcat --buffer crash


See logcat-filtering.md for a full guide on log filtering techniques.

Searching for Crash Signatures

When investigating crashes, search the log output for known patterns:

hzdb log | grep -i "fatal\|crash\|exception\|anr"


Common crash-related tags include AndroidRuntime, DEBUG, and libc.

Checking Permissions

Many Horizon OS features require specific manifest permissions. If a feature silently fails, check that the application manifest includes the required permissions. Common ones:

com.oculus.permission.HAND_TRACKING -- Hand tracking access
com.oculus.permission.USE_SCENE -- Scene API spatial data access
android.permission.RECORD_AUDIO -- Microphone access
android.permission.CAMERA -- Camera access (for mixed reality)
Performance Debugging

If the application stutters or drops frames:

# Check device battery and thermal state
hzdb device battery

# Watch for thermal throttling messages in logs
hzdb adb logcat --tag ThermalService --level W

# Check VrApi frame timing
hzdb adb logcat --tag VrApi | grep FPS


See common-issues.md for a catalog of known issues and their solutions.

References
Skill References
Logcat Filtering Guide -- Detailed guide to filtering and interpreting device logs
Screenshots and Video Capture -- Capturing visual state from the device
Common Issues and Diagnostics -- Catalog of common Quest development issues and solutions
Weekly Installs
11
Repository
meta-quest/agentic-tools
GitHub Stars
31
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykPass