---
title: standup-meeting
url: https://skills.sh/supercent-io/skills-template/standup-meeting
---

# standup-meeting

skills/supercent-io/skills-template/standup-meeting
standup-meeting
Installation
$ npx skills add https://github.com/supercent-io/skills-template --skill standup-meeting
Summary

Structured daily standup facilitation with three formats: 3-question updates, board-walking, and async remote standups.

Provides three standup formats (3 Questions, Walking the Board, and Slack-based async) adaptable to in-person, hybrid, and fully remote teams
Includes time-boxed 15-minute structure with built-in templates for tracking yesterday's work, today's plans, and blockers
Enforces core constraints: consistent daily timing, full team participation, and separation of problem-solving from the standup itself
Generates standup minutes with sprint progress summary, action items, and blocker tracking for accountability
SKILL.md
Standup Meeting
When to use this skill
Daily: same time, same place
During a sprint: when team sync is needed
Remote teams: async standup
Instructions
Step 1: 3 Questions Format
## Daily Standup Template

**Date**: 2025-01-15
**Time**: 9:30 AM
**Duration**: 15 minutes

### Team Member A
- **Yesterday**:
  - Completed user authentication API (#123)
  - 2 code reviews
- **Today**:
  - Implement JWT refresh token (#124)
  - Write unit tests
- **Blockers**:
  - Need Redis setup docs (ask Team Member B for help)

### Team Member B
- **Yesterday**:
  - Frontend form validation (#125)
- **Today**:
  - Implement profile page UI (#126)
- **Blockers**: None

### Team Member C
- **Yesterday**:
  - Database migration (#127)
  - Performance testing
- **Today**:
  - Index optimization (#128)
- **Blockers**:
  - Need production DB access (urgent)

### Action Items
1. [ ] Team Member B shares Redis docs with Team Member A (Today 10:00)
2. [ ] Team lead requests DB access for Team Member C (Today)

Step 2: Walking the Board (Board-Based)
## Standup: Walking the Board

**Sprint Goal**: Complete user authentication system

### In Progress
- #123: User Login API (Team Member A, 80% done)
- #124: Refresh Token (Team Member A, planned)
- #125: Form Validation (Team Member B, 90% done)

### Blocked
- #127: DB Migration (Team Member C)
  - **Blocker**: Access needed
  - **Owner**: Team Lead
  - **ETA**: This afternoon

### Ready for Review
- #122: Password Reset (Team Member D)
  - Need reviewer

### Done
- #120: Email Service Integration
- #121: User Registration

### Sprint Progress
- **Completed**: 12 points
- **Remaining**: 13 points
- **On Track**: Yes ✅

Step 3: Async Standup (Remote Teams)

Slack template:

[Daily Update - 2025-01-15]

**Yesterday**
- Completed user authentication flow
- Fixed bug in password validation

**Today**
- Implementing JWT refresh tokens
- Writing unit tests

**Blockers**
- None

**Sprint Progress**
- 8/13 story points completed

Output format
Standup Minutes
# Daily Standup - 2025-01-15

**Attendees**: 5/5
**Duration**: 12 minutes
**Sprint**: Sprint 10 (Day 3/10)

## Summary
- Stories Completed: 2 (5 points)
- Stories In Progress: 3 (8 points)
- Blockers: 1 (DB access permission)

## Individual Updates
[Refer to the 3 Questions format above]

## Action Items
1. Team lead: Request DB access (High priority)
2. Team Member B: Share Redis docs
3. Team Member D: Assign reviewer for PR #122

## Notes
- Sprint goal on track
- Team morale: High

Constraints
Required Rules (MUST)
Time-boxed: within 15 minutes
Same time: consistent time every day
Everyone participates: every team member gives an update
Prohibited (MUST NOT)
Problem Solving: Do not solve problems in the standup
Status Report: Not a status report to management
Late Start: Start on time
Best practices
Stand Up: Actually stand up (keep it short)
Parking Lot: Deep discussion goes to a separate time
Visualize: Run it while looking at the board
References
Scrum Guide - Daily Scrum
15 Minute Stand-up
Metadata
Version
Current version: 1.0.0
Last updated: 2025-01-01
Supported platforms: Claude, ChatGPT, Gemini
Tags

#standup #daily-scrum #agile #team-sync #project-management

Examples
Example 1: Basic usage
Example 2: Advanced usage
Weekly Installs
10.5K
Repository
supercent-io/sk…template
GitHub Stars
88
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass