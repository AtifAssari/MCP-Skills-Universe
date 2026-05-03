---
rating: ⭐⭐⭐
title: wework
url: https://skills.sh/dvcrn/skills/wework
---

# wework

skills/dvcrn/skills/wework
wework
Installation
$ npx skills add https://github.com/dvcrn/skills --skill wework
SKILL.md
WeWork
Overview

Use this skill to run wework safely and produce exact commands for location lookup, desk availability checks, booking, and calendar export. Prefer read-only commands first and only run booking once location and date are validated.

Read references/commands.md when you need full command and flag coverage. Read references/example-output.md when you need concrete output shapes for desks, locations, and bookings.

Runbook
Confirm installation and command availability.
Confirm authentication source (env vars or flags).
Resolve location candidates (locations).
Check availability for the target date (desks).
Run booking (book).
Verify final state (bookings) and optionally export calendar (calendar).
Installation And Auth

Install the CLI:

npm install -g wework-cli


Use environment variables by default:

export WEWORK_USERNAME="your_username"
export WEWORK_PASSWORD="your_password"


For installed CLI usage with env credentials:

wework bookings


Use --username and --password only when explicitly requested.

Common Tasks

Use these as canonical examples:

# list locations in Tokyo
wework locations --city "tokyo"

# list available desks in Bangkok for a date
wework desks --city "Bangkok" --date 2025-12-09

# list available desks for one location UUID
wework desks --location-uuid YOUR_LOCATION_UUID --date 2026-03-01

# create booking range with city + space name
wework book --city "Tokyo" --name "Shibuya Scramble Square" --date 2026-02-18~2026-02-20

# list upcoming bookings
wework bookings

# write ICS file for calendar import
wework calendar --calendar-path ./wework_bookings.ics


For single-day bookings, keep --date in YYYY-MM-DD. For multi-day booking ranges, use YYYY-MM-DD~YYYY-MM-DD.

Output Strategy

Use default CLI output for interactive use. This CLI does not currently expose a JSON output flag in --help, so for automation treat output as text and parse conservatively.

Safety Checks

Before book operations:

Confirm the target location exists (locations).
Confirm desk availability for the same date (desks).
Use explicit --date in YYYY-MM-DD format.
Verify result with bookings after booking.

If authentication fails, re-check WEWORK_USERNAME and WEWORK_PASSWORD values, or explicitly pass --username / --password.

Version Notes

/Users/david/src/wework-cli/README.md includes older examples that use positional date arguments and a me command. Current live CLI help (checked via wework --help and subcommand --help) uses --date flags for book/desks and does not expose me. Prefer live command help when the README and binary behavior differ.

Weekly Installs
12
Repository
dvcrn/skills
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass