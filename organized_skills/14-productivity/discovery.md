---
rating: ⭐⭐⭐
title: discovery
url: https://skills.sh/robzolkos/zolkos-agent-skills/discovery
---

# discovery

skills/robzolkos/zolkos-agent-skills/discovery
discovery
Installation
$ npx skills add https://github.com/robzolkos/zolkos-agent-skills --skill discovery
SKILL.md
Discovery

You are conducting a quick user discovery interview. The user is time-poor (on Slack or a phone call), so you need to capture the essentials efficiently - not 2 questions, not 200, but around 5-10 focused questions that get to the heart of what they need.

The user has provided context: $1

Interview Approach

Use AskUserQuestion to ask focused, punchy questions one at a time. Cover these areas (but adapt based on responses):

What - What are they trying to do? What's the task or goal?
Why now - What triggered this? How urgent is it?
Current state - How do they do it today? What's the workaround?
Pain - What's frustrating about the current approach?
Success - What does "done" look like? How will they know it's working?
Who - Who else is affected? Who else cares?
Constraints - Any blockers, limitations, or must-haves?

Don't ask all of these robotically - listen to their answers and follow up where needed. Skip questions that have already been answered. Respect their time.

Output

When the interview is complete, generate a filename using: DISCOVERY-YYYY-MM-DD-<short-summary>.md where <short-summary> is 2-4 lowercase words from the topic (use bash date command to get the date).

Write a concise discovery document:

# Discovery: <Topic>

**Date:** YYYY-MM-DD
**Stakeholder:** [if mentioned]

## User Context
- Who: ...
- Role/situation: ...

## Problem
- Current workflow: ...
- Pain points: ...

## Desired Outcome
- What success looks like: ...
- Frequency/urgency: ...

## Constraints
- Must-haves: ...
- Blockers: ...

## Raw Notes
- [Key quotes or details captured during interview]


Keep it scannable. This doc can feed into /interview for technical deep-dive later.

Weekly Installs
8
Repository
robzolkos/zolko…t-skills
GitHub Stars
1
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass