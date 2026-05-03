---
rating: ⭐⭐⭐
title: android
url: https://skills.sh/hyperb1iss/hyperdroid-skill/android
---

# android

skills/hyperb1iss/hyperdroid-skill/android
android
Installation
$ npx skills add https://github.com/hyperb1iss/hyperdroid-skill --skill android
SKILL.md
Android Device Mastery

This skill covers everything about interacting with Android devices via ADB and shell commands.

Device Connection
Check Connected Devices
adb devices -l


Output shows serial, status, and device info. Common statuses:

device - Connected and authorized
unauthorized - Accept USB debugging prompt on device
offline - Connection issues, try adb kill-server && adb start-server
Wireless Debugging

Android 11+ (Recommended):

Enable Wireless debugging in Developer Options
Tap "Pair device with pairing code"
Run: adb pair <ip>:<pairing_port> and enter the code
Then: adb connect <ip>:<connection_port>

Legacy (requires USB first):

adb tcpip 5555
adb connect <device_ip>:5555

Multiple Devices

Always specify device with -s:

adb -s <serial> shell
adb -s emulator-5554 install app.apk

Shell Commands
Interactive Shell
adb shell                    # Enter shell
adb shell <command>          # Run single command
adb shell "cmd1 && cmd2"     # Chain commands

Essential Commands
# Device info
getprop ro.product.model              # Device model
getprop ro.build.version.release      # Android version
getprop ro.build.version.sdk          # SDK level

# File operations
ls -la /sdcard/
cat /path/to/file
cp /source /dest
rm /path/to/file

# Process info
ps -A | grep <name>
pidof <package_name>
top -n 1 -m 10

Safe Output Limiting

For commands with potentially large output:

adb shell "logcat -d | head -500"
adb shell "dumpsys activity | head -200"

App Management
Install/Uninstall
adb install app.apk                   # Basic install
adb install -r app.apk                # Replace existing
adb install -g app.apk                # Grant all permissions
adb install -r -g app.apk             # Both

adb uninstall com.example.app         # Full uninstall
adb uninstall -k com.example.app      # Keep data

Start/Stop Apps
# Start main activity
adb shell monkey -p com.example.app -c android.intent.category.LAUNCHER 1

# Start specific activity
adb shell am start -n com.example.app/.MainActivity

# Start with intent extras
adb shell am start -n com.example.app/.Activity \
    -a android.intent.action.VIEW \
    -d "myapp://page/123" \
    --es "key" "value"

# Force stop
adb shell am force-stop com.example.app

# Clear app data
adb shell pm clear com.example.app

List Packages
adb shell pm list packages              # All packages
adb shell pm list packages -3           # Third-party only
adb shell pm list packages | grep term  # Filter

adb shell pm path com.example.app       # APK location
adb shell dumpsys package com.example.app  # Full package info

Permissions
adb shell pm grant com.example.app android.permission.CAMERA
adb shell pm revoke com.example.app android.permission.CAMERA
adb shell dumpsys package com.example.app | grep permission

File Operations
Push/Pull Files
adb push local_file.txt /sdcard/
adb pull /sdcard/remote_file.txt ./

# Recursive
adb push local_dir/ /sdcard/target/
adb pull /sdcard/dir/ ./local/

Access App Data (Debuggable Apps)
adb shell run-as com.example.app ls files/
adb shell run-as com.example.app cat shared_prefs/prefs.xml
adb shell run-as com.example.app sqlite3 databases/app.db ".tables"

UI Automation
Input Commands
# Tap at coordinates
adb shell input tap 500 800

# Swipe (x1 y1 x2 y2 [duration_ms])
adb shell input swipe 500 1500 500 500 300

# Text input (needs focused field)
adb shell input text "hello"

# Key events
adb shell input keyevent KEYCODE_HOME      # Home
adb shell input keyevent KEYCODE_BACK      # Back
adb shell input keyevent KEYCODE_ENTER     # Enter
adb shell input keyevent KEYCODE_POWER     # Power
adb shell input keyevent KEYCODE_VOLUME_UP # Volume up

Common Keycodes
Code	Key	Code	Key
3	HOME	4	BACK
24	VOL_UP	25	VOL_DOWN
26	POWER	66	ENTER
67	DEL	82	MENU
Screenshots & Recording
# Screenshot
adb shell screencap -p /sdcard/screen.png
adb pull /sdcard/screen.png

# One-liner (binary-safe)
adb exec-out screencap -p > screen.png

# Screen recording (max 3 min)
adb shell screenrecord /sdcard/video.mp4
adb shell screenrecord --time-limit 10 /sdcard/video.mp4

UI Hierarchy
adb shell uiautomator dump /sdcard/ui.xml
adb pull /sdcard/ui.xml

Debugging & Logs
Logcat Essentials
# Dump and exit
adb logcat -d

# Last N lines
adb logcat -t 100

# Filter by tag:priority
adb logcat ActivityManager:I *:S

# Filter by package (get PID first)
adb logcat --pid=$(adb shell pidof -s com.example.app)

# Crash buffer
adb logcat -b crash


Priority levels: V(erbose), D(ebug), I(nfo), W(arn), E(rror), F(atal), S(ilent)

Common Debug Patterns
# Find crashes
adb logcat *:E | grep -E "(Exception|Error|FATAL)"

# Activity lifecycle
adb logcat ActivityManager:I ActivityTaskManager:I *:S

# Memory issues
adb logcat art:D dalvikvm:D *:S | grep -i "gc"

Memory Analysis
adb shell dumpsys meminfo com.example.app


Key metrics:

PSS: Proportional memory use (compare apps with this)
Private Dirty: Memory exclusive to process
Heap: Java/Native heap usage
Crash Analysis
# ANR traces
adb shell cat /data/anr/traces.txt

# Tombstones (native crashes, needs root)
adb shell ls /data/tombstones/

# Recent crashes via logcat
adb logcat -b crash -d

System Inspection
dumpsys Services
adb shell dumpsys -l                    # List all services

# Common services
adb shell dumpsys activity              # Activities, processes
adb shell dumpsys package <pkg>         # Package details
adb shell dumpsys battery               # Battery status
adb shell dumpsys meminfo               # System memory
adb shell dumpsys cpuinfo               # CPU usage
adb shell dumpsys window displays       # Display info
adb shell dumpsys connectivity          # Network state

System Properties
adb shell getprop                       # All properties
adb shell getprop | grep <filter>       # Filter properties

# Useful properties
getprop ro.product.model                # Model
getprop ro.build.fingerprint            # Build fingerprint
getprop ro.serialno                     # Serial number
getprop sys.boot_completed              # Boot status (1 = done)

Settings
# Namespaces: system, secure, global
adb shell settings get global airplane_mode_on
adb shell settings put system screen_brightness 128
adb shell settings list global

Reboot Commands
adb reboot                   # Normal reboot
adb reboot recovery          # Recovery mode
adb reboot bootloader        # Fastboot mode
adb reboot sideload          # Sideload mode
adb reboot-bootloader        # Alias for bootloader

Troubleshooting

Device not found:

adb kill-server && adb start-server


Unauthorized:

Check USB debugging is enabled
Revoke USB debugging authorizations in Developer Options, reconnect

Multiple devices error:

Use -s <serial> to specify device

Command not found (on device):

Some commands require root or are version-specific
Try /system/bin/<cmd> or check if command exists
Quick Reference
Task	Command
List devices	adb devices -l
Install app	adb install -r -g app.apk
Start app	adb shell monkey -p pkg -c android.intent.category.LAUNCHER 1
Stop app	adb shell am force-stop pkg
Screenshot	adb exec-out screencap -p > screen.png
Logs	adb logcat -d -t 100
Shell	adb shell
Push file	adb push local /sdcard/
Pull file	adb pull /sdcard/file ./
Tap	adb shell input tap X Y
Back	adb shell input keyevent 4
Home	adb shell input keyevent 3

For deep dives into specific topics, see references/deep-dive.md.

Weekly Installs
58
Repository
hyperb1iss/hype…id-skill
GitHub Stars
15
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass