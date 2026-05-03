---
rating: ⭐⭐⭐
title: apple-reminders
url: https://skills.sh/steipete/clawdis/apple-reminders
---

# apple-reminders

skills/steipete/clawdis/apple-reminders
apple-reminders
Installation
$ npx skills add https://github.com/steipete/clawdis --skill apple-reminders
Summary

Manage Apple Reminders from the terminal with list, date, and output filtering.

Create, view, complete, and delete reminders with support for custom lists, due dates, and time specifications
Filter reminders by today, tomorrow, this week, overdue, or specific dates in multiple formats (YYYY-MM-DD, ISO 8601, natural language)
Output results as JSON, plain text (TSV), or quiet mode for scripting and automation
macOS-only; requires remindctl CLI installed via Homebrew and Reminders app permission granted
SKILL.md
Apple Reminders CLI (remindctl)

Use remindctl to manage Apple Reminders directly from the terminal.

When to Use

✅ USE this skill when:

User explicitly mentions "reminder" or "Reminders app"
Creating personal to-dos with due dates that sync to iOS
Managing Apple Reminders lists
User wants tasks to appear in their iPhone/iPad Reminders app
When NOT to Use

❌ DON'T use this skill when:

Scheduling OpenClaw tasks or alerts → use cron tool with systemEvent instead
Calendar events or appointments → use Apple Calendar
Project/work task management → use Notion, GitHub Issues, or task queue
One-time notifications → use cron tool for timed alerts
User says "remind me" but means an OpenClaw alert → clarify first
Setup
Install: brew install steipete/tap/remindctl
macOS-only; grant Reminders permission when prompted
Check status: remindctl status
Request access: remindctl authorize
Common Commands
View Reminders
remindctl                    # Today's reminders
remindctl today              # Today
remindctl tomorrow           # Tomorrow
remindctl week               # This week
remindctl overdue            # Past due
remindctl all                # Everything
remindctl 2026-01-04         # Specific date

Manage Lists
remindctl list               # List all lists
remindctl list Work          # Show specific list
remindctl list Projects --create    # Create list
remindctl list Work --delete        # Delete list

Create Reminders
remindctl add "Buy milk"
remindctl add --title "Call mom" --list Personal --due tomorrow
remindctl add --title "Meeting prep" --due "2026-02-15 09:00"

Complete/Delete
remindctl complete 1 2 3     # Complete by ID
remindctl delete 4A83 --force  # Delete by ID

Output Formats
remindctl today --json       # JSON for scripting
remindctl today --plain      # TSV format
remindctl today --quiet      # Counts only

Date Formats

Accepted by --due and date filters:

today, tomorrow, yesterday
YYYY-MM-DD
YYYY-MM-DD HH:mm
ISO 8601 (2026-01-04T12:34:56Z)
Example: Clarifying User Intent

User: "Remind me to check on the deploy in 2 hours"

Ask: "Do you want this in Apple Reminders (syncs to your phone) or as an OpenClaw alert (I'll message you here)?"

Apple Reminders → use this skill
OpenClaw alert → use cron tool with systemEvent
Weekly Installs
1.5K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass