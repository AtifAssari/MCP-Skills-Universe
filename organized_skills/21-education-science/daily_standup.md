---
rating: ⭐⭐⭐
title: daily-standup
url: https://skills.sh/knoopx/pi/daily-standup
---

# daily-standup

skills/knoopx/pi/daily-standup
daily-standup
Installation
$ npx skills add https://github.com/knoopx/pi --skill daily-standup
SKILL.md
Daily Standup

Generate standup updates for SLNG projects from Pi sessions and jj commits.

Usage
# Default: yesterday's activity
nu ~/.pi/agent/skills/daily-standup/slng-activity.nu

# Custom date range
nu ~/.pi/agent/skills/daily-standup/slng-activity.nu --since "3 days ago"
nu ~/.pi/agent/skills/daily-standup/slng-activity.nu --since "2026-02-20"

# JSON output
nu ~/.pi/agent/skills/daily-standup/slng-activity.nu --format json

Scope

SLNG projects only (~/Projects/slng/*). Do NOT include activity from other projects.

Output Format
## Standup: [Today's Date]

### Yesterday

- [Action verb + outcome] - be specific and concise

### Today

- [Concrete next action] - what you'll actually work on

### Blockers

- None _(or list specific blockers)_

Guidelines
Rule	Example
Action verbs	Built, Fixed, Added, Refactored, Implemented
Be specific	"Added Soniox STT support" not "Worked on features"
Max 5 items	Focus on highlights per section
No jargon	Readable by teammates unfamiliar with details
Real blockers	Only actual blockers, not minor friction
Related Skills
jujutsu: Commit history and revsets
self-reflect: Session reflection and learnings
Weekly Installs
11
Repository
knoopx/pi
GitHub Stars
45
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass