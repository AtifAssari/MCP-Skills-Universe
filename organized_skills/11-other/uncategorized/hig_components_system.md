---
rating: ⭐⭐
title: hig-components-system
url: https://skills.sh/raintree-technology/apple-hig-skills/hig-components-system
---

# hig-components-system

skills/raintree-technology/apple-hig-skills/hig-components-system
hig-components-system
Installation
$ npx skills add https://github.com/raintree-technology/apple-hig-skills --skill hig-components-system
SKILL.md
Apple HIG: System Experiences

Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered.

Key Principles

Glanceable, immediate value. System experiences bring your app's most important content to surfaces the user sees without launching your app. Design for seconds of attention.

Respect platform context. A Lock Screen widget has different constraints than a Home Screen widget. A complication is far smaller than a top shelf item.

Widgets: show relevant information, not everything. Display the most useful subset, updated appropriately.

Support multiple widget sizes with distinct layouts. Each size should be a thoughtful design, not a scaled version of another.

Deep-link on tap. Take users to the relevant content, not the app's root screen.

Live Activities: track events with a clear start and end. Deliveries, scores, timers, rides. Design for both Dynamic Island and Lock Screen.

Stay updated and timely. Stale data undermines trust. End promptly when the event concludes.

Respect user attention with notifications. Only send notifications for information users genuinely care about. No promotional or low-value notifications.

Notifications: actionable and self-contained. Include enough context to understand and act without opening the app. Support notification actions. Use threading and grouping.

Complications: focused data on the watch face. Design for the smallest useful representation. Support multiple families. Budget updates wisely.

Home Screen quick actions: 3-4 most common tasks. Short titles, optional subtitles, relevant SF Symbol icons.

Top Shelf: tvOS showcase. Feature content that entices: new episodes, featured items, recent content.

App Clips: instant, focused functionality within a strict size budget. Load quickly without App Store download. Only what's needed for the immediate task, then offer full app install.

App Shortcuts: surface key actions to Siri and Spotlight. Define shortcuts for frequent tasks. Use natural, conversational trigger phrases.

Reference Index
Reference	Topic	Key content
widgets.md	Widgets	Glanceable info, sizes, deep linking, timeline
live-activities.md	Live Activities	Real-time tracking, Dynamic Island, Lock Screen
notifications.md	Notifications	Attention, actions, grouping, content
complications.md	Complications	Watch face data, families, budgeted updates
home-screen-quick-actions.md	Quick actions	Haptic Touch, common tasks, SF Symbols
top-shelf.md	Top shelf	Featured content, showcase
app-clips.md	App Clips	Instant use, lightweight, focused task, NFC/QR
watch-faces.md	Watch faces	Custom complications, face sharing
app-shortcuts.md	App Shortcuts	Siri, Spotlight, voice triggers
Output Format
System experience recommendation -- which surface best fits the use case.
Content strategy -- what to display, priority, what to omit.
Update frequency -- refresh rate including system budget constraints.
Size/family variants -- which to support and how layout adapts.
Deep link behavior -- where tapping takes the user.
Questions to Ask
What information needs to surface outside the app?
Which platform?
How frequently does the data update?
What is the primary glanceable need?
Related Skills
hig-components-status -- Progress indicators in widgets or Live Activities
hig-inputs -- Interaction patterns for system experiences (Digital Crown for complications)
hig-technologies -- Siri for App Shortcuts, HealthKit for complications, NFC for App Clips

Built by Raintree Technology · More developer tools

Weekly Installs
154
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