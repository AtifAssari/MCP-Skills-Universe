---
rating: ⭐⭐
title: hig-components-status
url: https://skills.sh/raintree-technology/apple-hig-skills/hig-components-status
---

# hig-components-status

skills/raintree-technology/apple-hig-skills/hig-components-status
hig-components-status
Installation
$ npx skills add https://github.com/raintree-technology/apple-hig-skills --skill hig-components-status
SKILL.md
Apple HIG: Status Components

Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered.

Key Principles

Show progress for operations longer than a second or two.

Determinate when duration/percentage is known. A filling progress bar gives users a clear sense of remaining work. Use for downloads, uploads, or any measurable process.

Indeterminate when duration is unknown. A spinner communicates work is happening without promising a timeframe. Use for unpredictable network requests.

Prefer progress bars over spinners. Determinate progress feels faster and more trustworthy.

Place indicators where content will appear. Inline progress near the content area, not modal or distant.

Don't stack multiple indicators. Aggregate simultaneous operations into one representation or show the most relevant.

Don't hide the status bar without good reason. Reserve hiding for immersive experiences (full-screen media, games, AR).

Match status bar style to your content. Light or dark for adequate contrast.

Respect safe areas. No interactive content behind the status bar.

Restore the status bar promptly when exiting immersive contexts.

Activity rings are for Move, Exercise, and Stand goals. Don't repurpose the ring metaphor for unrelated data.

Respect ring color conventions. Red (Move), green (Exercise), blue (Stand) are strongly associated with Apple Fitness.

Use HealthKit APIs for activity data rather than manual tracking.

Celebrate completions with animation and haptics when rings close.

Reference Index
Reference	Topic	Key content
progress-indicators.md	Progress bars and spinners	Determinate, indeterminate, inline placement, duration
status-bars.md	iOS/iPadOS status bar	System info, visibility, style, safe areas
activity-rings.md	watchOS activity rings	Move/Exercise/Stand, HealthKit, fitness tracking, color
Output Format
Indicator type recommendation with rationale (determinate vs indeterminate).
Timing and animation guidance -- duration thresholds, animation style, transitions.
Accessibility -- VoiceOver progress announcements, live region updates.
Platform-specific behavior across targeted platforms.
Questions to Ask
Is the duration known or unknown?
Which platforms?
How long does the operation typically take?
System-level or in-app indicator?
Related Skills
hig-components-system -- Widgets and complications displaying progress or status
hig-inputs -- Gestures triggering progress states (pull-to-refresh)
hig-technologies -- HealthKit for activity ring data; VoiceOver for progress announcements

Built by Raintree Technology · More developer tools

Weekly Installs
151
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