---
rating: ⭐⭐
title: gccli
url: https://skills.sh/badlogic/pi-skills/gccli
---

# gccli

skills/badlogic/pi-skills/gccli
gccli
Installation
$ npx skills add https://github.com/badlogic/pi-skills --skill gccli
SKILL.md
Google Calendar CLI

Command-line interface for Google Calendar operations.

Installation
npm install -g @mariozechner/gccli

Setup
Google Cloud Console (one-time)
Create a new project (or select existing)
Enable the Google Calendar API
Set app name in OAuth branding
Add test users (all Gmail addresses you want to use)
Create OAuth client:
Click "Create Client"
Application type: "Desktop app"
Download the JSON file
Configure gccli

First check if already configured:

gccli accounts list


If no accounts, guide the user through setup:

Ask if they have a Google Cloud project with Calendar API enabled
If not, walk them through the Google Cloud Console steps above
Have them download the OAuth credentials JSON
Run: gccli accounts credentials ~/path/to/credentials.json
Run: gccli accounts add <email> (use --manual for browserless OAuth)
Usage

Run gccli --help for full command reference.

Common operations:

gccli <email> calendars - List all calendars
gccli <email> events <calendarId> [--from <dt>] [--to <dt>] - List events
gccli <email> event <calendarId> <eventId> - Get event details
gccli <email> create <calendarId> --summary <s> --start <dt> --end <dt> - Create event
gccli <email> freebusy <calendarIds> --from <dt> --to <dt> - Check availability

Use primary as calendarId for the main calendar.

Date/Time Format
Timed events: YYYY-MM-DDTHH:MM:SSZ (UTC) or YYYY-MM-DDTHH:MM:SS (local)
All-day events: YYYY-MM-DD with --all-day flag
Data Storage
~/.gccli/credentials.json - OAuth client credentials
~/.gccli/accounts.json - Account tokens
Weekly Installs
64
Repository
badlogic/pi-skills
GitHub Stars
1.5K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass