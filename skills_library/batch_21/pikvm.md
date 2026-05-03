---
title: pikvm
url: https://skills.sh/vm0-ai/vm0-skills/pikvm
---

# pikvm

skills/vm0-ai/vm0-skills/pikvm
pikvm
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill pikvm
SKILL.md
Coordinate System

Mouse coordinates use screen center as origin (0,0):

Negative X = left, Positive X = right
Negative Y = up, Positive Y = down

For 1920x1080 screen:

Top-left: (-960, -540)
Center: (0, 0)
Bottom-right: (960, 540)
Usage
Take Screenshot
curl -k -s -o /tmp/screenshot.jpg -u "$PIKVM_AUTH" "$PIKVM_URL/api/streamer/snapshot"

Type Text

Text must be sent as raw body with Content-Type: text/plain:

curl -k -s -X POST \
  -H "Content-Type: text/plain" \
  -u "$PIKVM_AUTH" \
  -d "Hello World" \
  "$PIKVM_URL/api/hid/print?limit=0"

Move Mouse

Move to absolute position (0,0 = screen center):

curl -k -s -X POST \
  -u "$PIKVM_AUTH" \
  "$PIKVM_URL/api/hid/events/send_mouse_move?to_x=-500&to_y=-300"

Mouse Click
# Press
curl -k -s -X POST \
  -u "$PIKVM_AUTH" \
  "$PIKVM_URL/api/hid/events/send_mouse_button?button=left&state=true"

# Release
curl -k -s -X POST \
  -u "$PIKVM_AUTH" \
  "$PIKVM_URL/api/hid/events/send_mouse_button?button=left&state=false"

Press Key

Press and release with state=true then state=false:

# Press Enter
curl -k -s -X POST \
  -u "$PIKVM_AUTH" \
  "$PIKVM_URL/api/hid/events/send_key?key=Enter&state=true"

curl -k -s -X POST \
  -u "$PIKVM_AUTH" \
  "$PIKVM_URL/api/hid/events/send_key?key=Enter&state=false"

Key Combo (e.g., Cmd+Space for Spotlight)

Press all keys in order, then release in reverse:

# Press Cmd
curl -k -s -X POST -u "$PIKVM_AUTH" "$PIKVM_URL/api/hid/events/send_key?key=MetaLeft&state=true"

# Press Space
curl -k -s -X POST -u "$PIKVM_AUTH" "$PIKVM_URL/api/hid/events/send_key?key=Space&state=true"

# Release Space
curl -k -s -X POST -u "$PIKVM_AUTH" "$PIKVM_URL/api/hid/events/send_key?key=Space&state=false"

# Release Cmd
curl -k -s -X POST -u "$PIKVM_AUTH" "$PIKVM_URL/api/hid/events/send_key?key=MetaLeft&state=false"

Mouse Scroll
curl -k -s -X POST \
  -u "$PIKVM_AUTH" \
  "$PIKVM_URL/api/hid/events/send_mouse_wheel?delta_x=0&delta_y=-50"

Get Device Info
curl -k -s \
  -u "$PIKVM_AUTH" \
  "$PIKVM_URL/api/info" | jq .

ATX Power Control
# Power on
curl -k -s -X POST \
  -u "$PIKVM_AUTH" \
  "$PIKVM_URL/api/atx/power?action=on"

# Power off
curl -k -s -X POST -u "$PIKVM_AUTH" "$PIKVM_URL/api/atx/power?action=off"

# Hard reset
curl -k -s -X POST -u "$PIKVM_AUTH" "$PIKVM_URL/api/atx/power?action=reset_hard"

Common Key Names
MetaLeft (Cmd), ControlLeft, AltLeft, ShiftLeft
Enter, Space, Escape, Tab, Backspace, Delete
ArrowUp, ArrowDown, ArrowLeft, ArrowRight
KeyA-KeyZ, Digit0-Digit9, F1-F12
PageUp, PageDown, Home, End
Equal (+), Minus (-)

API Endpoints Reference
Endpoint	Method	Description
/api/streamer/snapshot	GET	Screenshot (JPEG)
/api/hid/print	POST	Type text (body: raw text)
/api/hid/events/send_mouse_move	POST	Move mouse (to_x, to_y)
/api/hid/events/send_mouse_button	POST	Click (button, state)
/api/hid/events/send_mouse_wheel	POST	Scroll (delta_x, delta_y)
/api/hid/events/send_key	POST	Key press (key, state)
/api/atx/power	POST	Power control (action)
/api/info	GET	Device info
/api/atx	GET	ATX status
API Reference
Official docs: https://docs.pikvm.org/api/
Weekly Installs
84
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass