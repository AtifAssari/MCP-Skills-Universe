---
rating: ⭐⭐⭐
title: ios-simulator-pwa-testing
url: https://skills.sh/sebastiaanwouters/dotagents/ios-simulator-pwa-testing
---

# ios-simulator-pwa-testing

skills/sebastiaanwouters/dotagents/ios-simulator-pwa-testing
ios-simulator-pwa-testing
Installation
$ npx skills add https://github.com/sebastiaanwouters/dotagents --skill ios-simulator-pwa-testing
SKILL.md
iOS Simulator PWA Testing

Test and debug Progressive Web Apps using iOS Simulator on macOS for a real iOS Safari experience.

Prerequisites
Xcode installed from App Store
Xcode Command Line Tools: xcode-select --install
Safari with Developer menu enabled
Quick Start
1. Launch Simulator
# Open Simulator app
open -a Simulator

# Or boot a specific device
xcrun simctl boot "iPhone 15 Pro"
open -a Simulator

2. Open Your PWA
# Open localhost URL (Mac's localhost is accessible from Simulator)
xcrun simctl openurl booted "http://localhost:3000"

# Or any URL
xcrun simctl openurl booted "https://your-pwa.com"

3. Debug with Safari Web Inspector
Enable Safari Develop Menu: Safari → Settings → Advanced → "Show features for web developers"
Open Safari on Mac
Go to Develop menu → Simulator → Select your webpage
Full Web Inspector opens with Console, Elements, Network, etc.
simctl Commands Reference
Device Management
# List all available simulators
xcrun simctl list devices

# List only booted simulators
xcrun simctl list devices | grep Booted

# Boot a simulator
xcrun simctl boot "iPhone 15 Pro"
xcrun simctl boot <DEVICE-UUID>

# Shutdown simulator
xcrun simctl shutdown booted
xcrun simctl shutdown all

# Erase simulator (factory reset)
xcrun simctl erase booted

# Delete unavailable/old simulators
xcrun simctl delete unavailable

Opening URLs
# Open URL in booted simulator
xcrun simctl openurl booted "http://localhost:3000"

# Open URL in specific simulator
xcrun simctl openurl "iPhone 15 Pro" "https://example.com"

Screenshots & Recording
# Take screenshot
xcrun simctl io booted screenshot ~/Desktop/ios-screenshot.png

# Record video (Ctrl+C to stop)
xcrun simctl io booted recordVideo ~/Desktop/ios-recording.mp4

# With specific format
xcrun simctl io booted recordVideo --type=mp4 ~/Desktop/recording.mp4

Media & Files
# Add photos/videos to simulator
xcrun simctl addmedia booted ~/Desktop/test-image.png
xcrun simctl addmedia booted ~/Desktop/test-video.mp4

Safari Web Inspector Features

When connected via Develop menu:

Console: View JS logs, errors, service worker logs
Elements: Inspect DOM, modify CSS in real-time
Network: Monitor requests, check service worker caching
Sources: Debug JavaScript, set breakpoints
Storage: Inspect localStorage, IndexedDB, Cache Storage
Service Workers: Debug service worker (visible in Develop menu as separate context)
Debugging Service Workers

PWA Service Workers appear in Safari's Develop menu:

Open Simulator with your PWA
Safari → Develop → Simulator → Look for "Service Worker" entries
Opens inspector with Console, Sources, Network tabs

Note: Service Worker debugging works BETTER in Simulator than on physical devices.

Accessibility Testing
Using Accessibility Inspector
Open Xcode
Xcode → Open Developer Tool → Accessibility Inspector
Select Simulator from the device dropdown
Hover over elements to see accessibility info
Run Audit to find accessibility issues
Command Line Accessibility Snapshot
# Get accessibility hierarchy (requires running app)
xcrun simctl ui booted accessibility

PWA-Specific Testing
Add to Home Screen (Manual)
Open your PWA URL in Safari on Simulator
Tap Share button (bottom bar)
Select "Add to Home Screen"
PWA installs as standalone app
Testing Installed PWA
Installed PWAs run in Web.app engine (same as real device)
Access via Develop menu as separate web context
Test display-mode: standalone media queries
Verify splash screens, icons, theme colors
Manifest Validation

Check your manifest is loaded correctly:

Open Web Inspector → Application tab (if available) or Network tab
Look for manifest.json request
Verify all icons, theme_color, display mode
Multi-Device Testing Script

Run scripts/multi-device-test.sh to test across multiple device sizes:

./scripts/multi-device-test.sh "http://localhost:3000"

Useful Keyboard Shortcuts (Simulator)
Shortcut	Action
⌘ + Shift + H	Go to Home Screen
⌘ + Shift + H (x2)	App Switcher
⌘ + → / ⌘ + ←	Rotate device
⌘ + S	Take screenshot
⌘ + R	Record video
⌘ + K	Toggle keyboard
Troubleshooting
"No Inspectable Applications" in Safari Develop menu
Ensure a webpage is open in Safari on Simulator
Restart Safari on Mac
Restart Simulator
Simulator not appearing in Develop menu
Quit Safari and Simulator
Reopen Simulator first, then Safari
localhost not working
Use http://localhost:PORT (Simulator shares Mac's network stack)
Try http://127.0.0.1:PORT as alternative
Service Worker not updating
Clear Safari cache in Simulator: Settings → Safari → Clear History and Website Data
Or erase simulator: xcrun simctl erase booted
Weekly Installs
20
Repository
sebastiaanwoute…otagents
GitHub Stars
1
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn