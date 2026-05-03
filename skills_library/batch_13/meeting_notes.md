---
title: meeting-notes
url: https://skills.sh/beshkenadze/claude-skills-marketplace/meeting-notes
---

# meeting-notes

skills/beshkenadze/claude-skills-marketplace/meeting-notes
meeting-notes
Installation
$ npx skills add https://github.com/beshkenadze/claude-skills-marketplace --skill meeting-notes
SKILL.md
Meeting Notes
Overview

Transforms raw meeting transcripts or recordings into structured, actionable meeting notes.

Instructions

When processing meeting content:

Extract metadata: Date, attendees, meeting type
Identify key discussions: Main topics covered
Capture decisions: What was decided and by whom
List action items: Task, owner, deadline
Note follow-ups: Items for future meetings
Output Format
# Meeting Notes: [Topic]

**Date:** YYYY-MM-DD
**Attendees:** Names
**Duration:** X minutes

## Summary
Brief 2-3 sentence overview of the meeting.

## Key Discussion Points
- Topic 1: Summary of discussion
- Topic 2: Summary of discussion

## Decisions Made
1. [Decision] - Decided by [Person]
2. [Decision] - Decided by [Person]

## Action Items
| Task | Owner | Due Date | Status |
|------|-------|----------|--------|
| Task description | Name | Date | Pending |

## Follow-up Items
- Items to discuss in next meeting

## Next Meeting
Date/time if scheduled

Examples
Example: Process Transcript

Input: Raw meeting transcript with multiple speakers

Output: Structured notes following the format above with clear attribution

Guidelines
Do
Keep summaries concise (2-3 sentences max)
Attribute decisions to specific people
Include owners and deadlines for all action items
Flag unclear items for clarification
Use consistent formatting throughout
Don't
Include verbatim transcript in notes
Leave action items without owners
Skip the summary section
Omit attendee names from notes
Weekly Installs
9
Repository
beshkenadze/cla…ketplace
GitHub Stars
2
First Seen
Feb 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass