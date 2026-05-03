---
rating: ⭐⭐
title: recipe-review-meet-participants
url: https://skills.sh/googleworkspace/cli/recipe-review-meet-participants
---

# recipe-review-meet-participants

skills/googleworkspace/cli/recipe-review-meet-participants
recipe-review-meet-participants
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-review-meet-participants
Summary

Review Google Meet attendance records and participant session durations.

Requires the gws-meet skill to access Google Meet conference data
Three-step workflow: list recent conferences, retrieve participant details, and view individual session timestamps and durations
Returns tabular output for easy review of who attended and how long they stayed
SKILL.md
Review Google Meet Attendance

PREREQUISITE: Load the following skills to execute this recipe: gws-meet

Review who attended a Google Meet conference and for how long.

Steps
List recent conferences: gws meet conferenceRecords list --format table
List participants: gws meet conferenceRecords participants list --params '{"parent": "conferenceRecords/CONFERENCE_ID"}' --format table
Get session details: gws meet conferenceRecords participants participantSessions list --params '{"parent": "conferenceRecords/CONFERENCE_ID/participants/PARTICIPANT_ID"}' --format table
Weekly Installs
11.1K
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