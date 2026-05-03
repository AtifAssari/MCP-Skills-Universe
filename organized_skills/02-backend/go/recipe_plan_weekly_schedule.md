---
rating: ⭐⭐
title: recipe-plan-weekly-schedule
url: https://skills.sh/googleworkspace/cli/recipe-plan-weekly-schedule
---

# recipe-plan-weekly-schedule

skills/googleworkspace/cli/recipe-plan-weekly-schedule
recipe-plan-weekly-schedule
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-plan-weekly-schedule
Summary

Review your Google Calendar week, identify gaps, and add events to fill them.

Requires the gws-calendar skill to execute; works with your primary Google Calendar
Workflow includes four steps: view weekly agenda, query free/busy slots, insert new events, and review the updated schedule
Supports event creation with customizable summary, start time, and end time parameters
SKILL.md
Plan Your Weekly Google Calendar Schedule

PREREQUISITE: Load the following skills to execute this recipe: gws-calendar

Review your Google Calendar week, identify gaps, and add events to fill them.

Steps
Check this week's agenda: gws calendar +agenda
Check free/busy for the week: gws calendar freebusy query --json '{"timeMin": "2025-01-20T00:00:00Z", "timeMax": "2025-01-25T00:00:00Z", "items": [{"id": "primary"}]}'
Add a new event: gws calendar +insert --summary 'Deep Work Block' --start '2026-01-21T14:00:00' --end '2026-01-21T16:00:00'
Review updated schedule: gws calendar +agenda
Weekly Installs
11.6K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass