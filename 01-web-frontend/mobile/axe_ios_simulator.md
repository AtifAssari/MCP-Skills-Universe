---
title: axe-ios-simulator
url: https://skills.sh/0xbigboss/claude-code/axe-ios-simulator
---

# axe-ios-simulator

skills/0xbigboss/claude-code/axe-ios-simulator
axe-ios-simulator
Installation
$ npx skills add https://github.com/0xbigboss/claude-code --skill axe-ios-simulator
SKILL.md
AXe iOS Simulator Automation

AXe is a single-binary CLI for iOS Simulator automation via Apple's Accessibility APIs and HID.

Installation
brew install cameroncooke/axe/axe

Quick Start
# Get simulator UDID
axe list-simulators
UDID="<simulator-udid>"

# Basic interactions
axe tap -x 100 -y 200 --udid $UDID
axe tap --label "Safari" --udid $UDID
axe type 'Hello World!' --udid $UDID
axe gesture scroll-down --udid $UDID
axe button home --udid $UDID
axe screenshot --udid $UDID

Touch & Gestures
# Tap at coordinates
axe tap -x 100 -y 200 --udid $UDID

# Tap by accessibility identifier or label
axe tap --id "myButton" --udid $UDID
axe tap --label "Submit" --udid $UDID

# With timing controls
axe tap -x 100 -y 200 --pre-delay 1.0 --post-delay 0.5 --udid $UDID

# Swipe
axe swipe --start-x 100 --start-y 300 --end-x 300 --end-y 100 --udid $UDID
axe swipe --start-x 50 --start-y 500 --end-x 350 --end-y 500 --duration 2.0 --delta 25 --udid $UDID

# Low-level touch control
axe touch -x 150 -y 250 --down --udid $UDID
axe touch -x 150 -y 250 --up --udid $UDID
axe touch -x 150 -y 250 --down --up --delay 1.0 --udid $UDID

Gesture Presets
Preset	Use Case
scroll-up	Content navigation
scroll-down	Content navigation
scroll-left	Horizontal scrolling
scroll-right	Horizontal scrolling
swipe-from-left-edge	Back navigation
swipe-from-right-edge	Forward navigation
swipe-from-top-edge	Dismiss/close
swipe-from-bottom-edge	Open/reveal
axe gesture scroll-down --udid $UDID
axe gesture swipe-from-left-edge --udid $UDID
axe gesture scroll-up --screen-width 430 --screen-height 932 --udid $UDID
axe gesture scroll-down --pre-delay 1.0 --post-delay 0.5 --udid $UDID

Text Input
# Direct text (use single quotes for special characters)
axe type 'Hello World!' --udid $UDID

# From stdin (best for automation)
echo "Complex text" | axe type --stdin --udid $UDID

# From file
axe type --file input.txt --udid $UDID

# Individual key press by HID keycode
axe key 40 --udid $UDID  # Enter key
axe key 42 --duration 1.0 --udid $UDID  # Hold Backspace

# Key sequence
axe key-sequence --keycodes 11,8,15,15,18 --udid $UDID  # "hello"

Hardware Buttons
axe button home --udid $UDID
axe button lock --duration 2.0 --udid $UDID
axe button side-button --udid $UDID
axe button siri --udid $UDID
axe button apple-pay --udid $UDID

Screenshot & Video
# Screenshot (auto-generates filename)
axe screenshot --udid $UDID

# Screenshot to specific path
axe screenshot --output ~/Desktop/screenshot.png --udid $UDID

# Video recording to MP4
axe record-video --udid $UDID --fps 15 --output recording.mp4
axe record-video --udid $UDID --fps 10 --quality 60 --scale 0.5 --output low-bandwidth.mp4

# Stream MJPEG
axe stream-video --udid $UDID --fps 10 --format mjpeg > stream.mjpeg

# Pipe to ffmpeg
axe stream-video --udid $UDID --fps 30 --format ffmpeg | \
  ffmpeg -f image2pipe -framerate 30 -i - -c:v libx264 -preset ultrafast output.mp4


Press Ctrl+C to stop recording. AXe finalizes MP4 and prints path to stdout.

Accessibility Inspection
# Full screen accessibility tree
axe describe-ui --udid $UDID

# Accessibility info at specific point
axe describe-ui --point 100,200 --udid $UDID

Automation Patterns
Wait-then-tap pattern
axe tap --label "Continue" --pre-delay 2.0 --udid $UDID

Scroll to find element
for i in {1..5}; do
  axe describe-ui --udid $UDID | grep -q "targetElement" && break
  axe gesture scroll-down --udid $UDID
done
axe tap --label "targetElement" --udid $UDID

Form filling
axe tap --label "Email" --udid $UDID
axe type 'user@example.com' --udid $UDID
axe tap --label "Password" --udid $UDID
axe type 'secret123' --udid $UDID
axe tap --label "Sign In" --udid $UDID

Screenshot after action
axe tap --label "Submit" --post-delay 1.0 --udid $UDID
axe screenshot --output result.png --udid $UDID

Weekly Installs
200
Repository
0xbigboss/claude-code
GitHub Stars
43
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail