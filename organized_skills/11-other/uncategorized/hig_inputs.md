---
rating: ⭐⭐
title: hig-inputs
url: https://skills.sh/raintree-technology/apple-hig-skills/hig-inputs
---

# hig-inputs

skills/raintree-technology/apple-hig-skills/hig-inputs
hig-inputs
Installation
$ npx skills add https://github.com/raintree-technology/apple-hig-skills --skill hig-inputs
SKILL.md
Apple HIG: Inputs

Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered.

Key Principles

Support multiple input methods. Touch, pointer, keyboard, pencil, voice, eyes, hands, controllers. Design for the inputs available on each platform. On iPadOS, support both touch and pointer; on macOS, both pointer and keyboard.

Consistent feedback for every input action. Visible, audible, or haptic response.

Standard gestures must behave consistently. Tap to activate, swipe to scroll/navigate, pinch to zoom, long press for context menus, drag to move. Don't override system gestures (edge swipes for back, Home, notifications).

Use standard recognizers; keep custom gestures discoverable. Apple's built-in recognizers handle edge cases and accessibility. If you add non-standard gestures, provide hints or coaching to teach them.

Apple Pencil: precision drawing, markup, and selection. Support pressure, tilt, and hover. Distinguish finger from Pencil when appropriate (finger pans, Pencil draws).

Support Scribble in text fields. Users expect to write with Pencil in any text input.

Keyboard shortcuts and full navigation. Standard shortcuts (Cmd+C/V/Z) plus custom ones visible in the iPadOS Command key overlay. Logical tab order.

Respect the software keyboard. Adjust layout when keyboard appears. Use keyboard-avoidance APIs.

Game controllers: MFi controllers with on-screen fallbacks. Map to extended gamepad profile, sensible defaults, remappable. Always offer touch or keyboard alternatives.

Pointer and trackpad: native feel. Hover effects, pointer shape adaptation, standard cursor behaviors. Two-finger scroll, pinch to zoom, swipe to navigate.

Digital Crown: primary scrolling and value-adjustment input on watchOS. Scrolling lists, adjusting values, navigating views. Haptic feedback at detents.

Eyes and spatial (visionOS): look and pinch. Generous hit targets (eye tracking is less precise than touch). Avoid sustained gaze for activation. Direct hand manipulation in immersive experiences.

Focus system: critical for tvOS and visionOS. Predictable focus movement. Every interactive element focusable. Clear visual indicators (scale, highlight, elevation). Logical focus groups.

Siri Remote: limited surface. Touch area for swiping, clickpad for selection, few physical buttons. Keep interactions simple.

Gyroscope, accelerometer, UWB: use judiciously. Suits gaming, fitness, AR. Not for essential tasks. Provide calibration and reset. For UWB, communicate distance and direction with visual or haptic cues.

Reference Index
Reference	Topic	Key content
gestures.md	Touch gestures	Tap, swipe, pinch, long press, drag, system gestures
apple-pencil-and-scribble.md	Apple Pencil	Precision, pressure, tilt, hover, handwriting
keyboards.md	Keyboards	Shortcuts, navigation, software keyboard, Command key
game-controls.md	Game controllers	MFi, extended gamepad, remapping, fallbacks
pointing-devices.md	Pointer/trackpad	Hover, cursor morphing, trackpad gestures
digital-crown.md	Digital Crown	Scrolling, value adjustment, haptic detents
eyes.md	Eye tracking	Look and tap, gaze targeting, hit target sizing
spatial-interactions.md	Spatial input	Hand gestures, direct manipulation, immersive input
focus-and-selection.md	Focus system	tvOS/visionOS navigation, focus indicators, groups
remotes.md	Remotes	Touch surface, clickpad, simple interactions
gyro-and-accelerometer.md	Motion sensors	Gyroscope, accelerometer, calibration, gaming
nearby-interactions.md	Nearby interactions	U1 chip, directional finding, proximity triggers
camera-control.md	Camera Control	iPhone camera hardware button, quick launch
Output Format
Input method recommendations by platform and how they interact.
Gesture specification table -- standard and custom gestures with expected behaviors.
Keyboard shortcut recommendations following system conventions.
Accessibility input alternatives for VoiceOver, Switch Control, etc.
Questions to Ask
Which platforms and input devices?
Productivity or casual app?
Custom gestures in the design?
Game controller support needed?
Related Skills
hig-components-status -- Progress indicators responding to input (pull-to-refresh)
hig-components-system -- System experiences with unique input constraints
hig-technologies -- VoiceOver, Siri voice input, ARKit spatial gesture context

Built by Raintree Technology · More developer tools

Weekly Installs
154
Repository
raintree-techno…g-skills
GitHub Stars
45
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass