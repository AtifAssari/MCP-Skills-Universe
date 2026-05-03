---
title: hig-platforms
url: https://skills.sh/raintree-technology/apple-hig-skills/hig-platforms
---

# hig-platforms

skills/raintree-technology/apple-hig-skills/hig-platforms
hig-platforms
Installation
$ npx skills add https://github.com/raintree-technology/apple-hig-skills --skill hig-platforms
SKILL.md
Apple HIG: Platform Design

Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered.

Key Principles

Each platform has a distinct identity. Do not port designs between platforms. Respect each platform's conventions, interaction models, and user expectations.

iOS: touch-first. Direct manipulation on a handheld screen. Optimize for one-handed use. Navigation uses tab bars and push/pop stacks.

iPadOS: expanded canvas. Support Split View, Slide Over, and Stage Manager. Use sidebars and multi-column layouts. Support pointer and keyboard alongside touch.

macOS: pointer and keyboard. Dense information display is acceptable. Use menu bars, toolbars, and keyboard shortcuts extensively. Windows are resizable with precise control.

tvOS: remote and focus. Viewed from a distance. Design for the Siri Remote with focus-based navigation. Large text, simple layouts, linear navigation.

visionOS: spatial interaction. 3D environment using windows, volumes, and spaces. Eye tracking for targeting, indirect gestures for interaction. Respect ergonomic comfort zones.

watchOS: glanceable and brief. Information consumable at a glance. Brief interactions. Digital Crown, haptics, and complications for timely content.

Games: own paradigm. Free to define in-game interaction models, but still respect platform conventions for system interactions (notifications, accessibility, controllers).

Reference Index
Reference	Topic	Key content
designing-for-ios.md	iOS	Touch, tab bars, navigation stacks, gestures, screen sizes, safe areas
designing-for-ipados.md	iPadOS	Multitasking, sidebars, pointer, keyboard, Apple Pencil, Stage Manager
designing-for-macos.md	macOS	Menu bars, toolbars, window management, keyboard shortcuts, dense layouts, Dock
designing-for-tvos.md	tvOS	Focus engine, Siri Remote, lean-back experience, content-forward, parallax
designing-for-visionos.md	visionOS	Spatial computing, windows/volumes/spaces, eye tracking, hand gestures, depth
designing-for-watchos.md	watchOS	Glanceable UI, Digital Crown, complications, notifications, haptics
designing-for-games.md	Games	Controllers, immersive experiences, platform-specific conventions, accessibility
Decision Framework

Identify the primary use context. On the go (iOS/watchOS), at a desk (macOS), on the couch (tvOS), spatial environment (visionOS)?

Match input to interaction. Touch for direct manipulation, pointer for precision, gaze+gesture for spatial, Digital Crown for quick scrolling, remote for focus navigation.

Adapt, don't replicate. A macOS sidebar becomes a tab bar on iPhone. A visionOS volume has no equivalent on watchOS. Translate intent, not implementation.

Leverage platform strengths. Live Activities on iOS, Desktop Widgets on macOS, complications on watchOS, immersive spaces on visionOS.

Maintain brand consistency while respecting each platform's visual language and interaction patterns.

Output Format
Platform-specific recommendations citing relevant HIG sections.
Platform differences table comparing navigation, input, layout, and conventions.
Implementation notes per platform including recommended APIs and adaptation strategies.
Questions to Ask
Which platforms are you targeting?
New app or adapting an existing one? If existing, which platform is the base?
SwiftUI or UIKit/AppKit?
Need to support older OS versions?
Primary use context? (On the go, desk, couch, spatial, glanceable?)
Related Skills
hig-foundations -- Shared principles (color, typography, accessibility, layout) across platforms
hig-patterns -- Interaction patterns that manifest differently per platform
hig-components-layout -- Navigation structures (tab bars, sidebars, split views) that vary by platform
hig-components-content -- Content display that adapts across platforms

Built by Raintree Technology · More developer tools

Weekly Installs
168
Repository
raintree-techno…g-skills
GitHub Stars
45
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass