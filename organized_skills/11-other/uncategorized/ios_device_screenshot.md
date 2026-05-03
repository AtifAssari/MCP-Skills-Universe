---
rating: ⭐⭐⭐
title: ios-device-screenshot
url: https://skills.sh/0xbigboss/claude-code/ios-device-screenshot
---

# ios-device-screenshot

skills/0xbigboss/claude-code/ios-device-screenshot
ios-device-screenshot
Installation
$ npx skills add https://github.com/0xbigboss/claude-code --skill ios-device-screenshot
SKILL.md
iOS Device Screenshot

Take screenshots from physical iOS devices connected via USB using pymobiledevice3.

Installation
# Install pymobiledevice3 using uv (recommended)
uv tool install pymobiledevice3

# Or with pipx
pipx install pymobiledevice3

Prerequisites
Physical iOS device connected via USB
Developer Mode enabled on the device (Settings > Privacy & Security > Developer Mode)
Device trusted - approve "Trust This Computer" prompt on device
Usage
For iOS 17+ (including iOS 26+)

iOS 17+ requires a tunneld daemon running with root privileges:

# Terminal 1: Start tunneld (requires sudo, runs continuously)
sudo pymobiledevice3 remote tunneld

# Terminal 2: Take screenshot via DVT (Developer Tools)
pymobiledevice3 developer dvt screenshot --tunnel "" /path/to/screenshot.png


The --tunnel "" flag tells it to use the tunneld for device communication.

For iOS 16 and earlier
pymobiledevice3 developer screenshot /path/to/screenshot.png

Quick Reference
# List connected devices
xcrun devicectl list devices

# Check iOS version
ideviceinfo -k ProductVersion

# Check if developer image is mounted
ideviceimagemounter list

# Auto-mount developer image if needed
pymobiledevice3 mounter auto-mount --tunnel ""

# Take screenshot (iOS 17+) - single device
pymobiledevice3 developer dvt screenshot --tunnel "" ~/Desktop/screenshot.png

# Take screenshot with specific device UDID (required for multiple devices)
# First get UDIDs from: xcrun devicectl list devices
# Pass UDID directly to --tunnel (NOT --udid flag which doesn't work with tunneld)
pymobiledevice3 developer dvt screenshot --tunnel "00008101-001E05A41144001E" ~/Desktop/screenshot.png


Important: When multiple devices are connected, pass the UDID directly to --tunnel (not --udid). The --tunnel "" syntax prompts for interactive selection which fails in non-interactive shells.

Troubleshooting
"InvalidServiceError" or "Failed to start service"
Ensure tunneld is running: ps aux | grep tunneld
If not running: sudo pymobiledevice3 remote tunneld
Use the DVT command instead of regular screenshot: developer dvt screenshot instead of developer screenshot
"DeveloperDiskImage not mounted"
pymobiledevice3 mounter auto-mount --tunnel ""

Multiple devices connected

Specify the target device with --udid:

# List devices first
xcrun devicectl list devices

# Use specific UDID
pymobiledevice3 developer dvt screenshot --tunnel "" --udid "40182233-00C8-51ED-8C68-174E14E4B4C9" /tmp/screenshot.png

Key Discovery

For iOS 17+, the regular pymobiledevice3 developer screenshot command often fails even with tunneld running. The solution is to use the DVT (Developer Tools) variant:

# This fails on iOS 17+:
pymobiledevice3 developer screenshot --tunnel "" /tmp/screenshot.png

# This works on iOS 17+:
pymobiledevice3 developer dvt screenshot --tunnel "" /tmp/screenshot.png

Integration Example
#!/bin/bash
# Take iOS device screenshot and open it

OUTPUT="/tmp/ios-screenshot-$(date +%Y%m%d-%H%M%S).png"

# Check if tunneld is running, start if not
if ! pgrep -f "pymobiledevice3 remote tunneld" > /dev/null; then
    echo "Starting tunneld (requires sudo)..."
    sudo pymobiledevice3 remote tunneld &
    sleep 3
fi

# Take screenshot
pymobiledevice3 developer dvt screenshot --tunnel "" "$OUTPUT"

if [ -f "$OUTPUT" ]; then
    echo "Screenshot saved to: $OUTPUT"
    open "$OUTPUT"  # macOS: open in Preview
else
    echo "Failed to capture screenshot"
    exit 1
fi

Weekly Installs
152
Repository
0xbigboss/claude-code
GitHub Stars
43
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn