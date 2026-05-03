---
title: project-management
url: https://skills.sh/miles990/claude-software-skills/project-management
---

# project-management

skills/miles990/claude-software-skills/project-management
project-management
Installation
$ npx skills add https://github.com/miles990/claude-software-skills --skill project-management
SKILL.md
Project Management
Overview

Software project management methodologies, issue tracking systems, and team collaboration practices.

Agile Methodologies
Scrum Framework
┌─────────────────────────────────────────────────────────────────┐
│                        Scrum Framework                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Product      Sprint         Sprint          Sprint             │
│  Backlog   →  Planning   →   Execution   →   Review/Retro      │
│                   │              │                              │
│                   ▼              ▼                              │
│              Sprint         Daily Standup                       │
│              Backlog        (15 min)                           │
│                                                                 │
│  Roles:                                                         │
│  • Product Owner: Backlog priority, stakeholder voice           │
│  • Scrum Master: Process facilitation, impediment removal       │
│  • Development Team: Self-organizing, cross-functional          │
│                                                                 │
│  Artifacts:                                                     │
│  • Product Backlog: Prioritized feature list                    │
│  • Sprint Backlog: Committed sprint work                        │
│  • Increment: Potentially shippable product                     │
│                                                                 │
│  Events:                                                        │
│  • Sprint Planning: What & How for sprint                       │
│  • Daily Standup: Sync & impediments                           │
│  • Sprint Review: Demo to stakeholders                          │
│  • Sprint Retrospective: Process improvement                    │
└─────────────────────────────────────────────────────────────────┘

Kanban Board
┌──────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
│   Backlog    │   To Do      │ In Progress  │   Review     │    Done      │
│              │   (WIP: 5)   │   (WIP: 3)   │   (WIP: 2)   │              │
├──────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│ ┌──────────┐ │ ┌──────────┐ │ ┌──────────┐ │ ┌──────────┐ │ ┌──────────┐ │
│ │ Feature  │ │ │ Bug fix  │ │ │ API      │ │ │ Login    │ │ │ Auth     │ │
│ │ Request  │ │ │ #123     │ │ │ endpoint │ │ │ page     │ │ │ module   │ │
│ └──────────┘ │ └──────────┘ │ │ @alice   │ │ │ @bob     │ │ └──────────┘ │
│ ┌──────────┐ │ ┌──────────┐ │ └──────────┘ │ └──────────┘ │ ┌──────────┐ │
│ │ Tech     │ │ │ Refactor │ │ ┌──────────┐ │              │ │ Database │ │
│ │ Debt     │ │ │ auth     │ │ │ Tests    │ │              │ │ migration│ │
│ └──────────┘ │ └──────────┘ │ │ @charlie │ │              │ └──────────┘ │
│              │              │ └──────────┘ │              │              │
└──────────────┴──────────────┴──────────────┴──────────────┴──────────────┘

Key Principles:
• Visualize work
• Limit Work In Progress (WIP)
• Manage flow
• Make policies explicit
• Implement feedback loops
• Improve collaboratively

User Stories
# User Story Format
As a [type of user]
I want [goal/desire]
So that [benefit/value]

# Example
As a registered user
I want to reset my password via email
So that I can regain access to my account if I forget my password

# Acceptance Criteria (Given-When-Then)
Given I am on the login page
When I click "Forgot Password"
And I enter my registered email
And I click "Send Reset Link"
Then I should receive an email with a password reset link
And the link should expire after 24 hours

# INVEST Criteria
□ Independent - Can be developed separately
□ Negotiable - Details can be discussed
□ Valuable - Delivers user/business value
□ Estimable - Can be sized
□ Small - Fits in a sprint
□ Testable - Has clear acceptance criteria

Story Points & Estimation
# Fibonacci Scale
1  - Trivial (< 1 hour)
2  - Simple (few hours)
3  - Straightforward (half day)
5  - Medium complexity (1-2 days)
8  - Complex (3-5 days)
13 - Very complex (1+ week)
21 - Epic (break it down!)

# Planning Poker
1. Product Owner presents story
2. Team discusses & asks questions
3. Each member secretly selects estimate
4. All reveal simultaneously
5. Discuss outliers
6. Re-vote if needed
7. Reach consensus

# Velocity Calculation
Sprint 1: 32 points completed
Sprint 2: 28 points completed
Sprint 3: 35 points completed
Average Velocity: 31.7 points/sprint

Issue Tracking
GitHub Issues
# Issue Template: Bug Report
---
name: Bug Report
about: Report a bug to help us improve
labels: bug, needs-triage
---

## Description
A clear description of the bug.

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

## Expected Behavior
What should happen.

## Actual Behavior
What actually happens.

## Environment
- OS: [e.g., macOS 14.0]
- Browser: [e.g., Chrome 120]
- Version: [e.g., 2.1.0]

## Screenshots
If applicable, add screenshots.

## Additional Context
Any other relevant information.

# Issue Template: Feature Request
---
name: Feature Request
about: Suggest a new feature
labels: enhancement
---

## Problem Statement
What problem does this solve?

## Proposed Solution
How should this work?

## Alternatives Considered
Other approaches you've thought about.

## Additional Context
Mockups, examples, or references.

GitHub Projects (v2)
# Project configuration
fields:
  - name: Status
    type: single_select
    options:
      - Backlog
      - Ready
      - In Progress
      - In Review
      - Done

  - name: Priority
    type: single_select
    options:
      - 🔴 High
      - 🟡 Medium
      - 🟢 Low

  - name: Sprint
    type: iteration
    duration: 2 weeks

  - name: Estimate
    type: number

  - name: Team
    type: single_select
    options:
      - Frontend
      - Backend
      - DevOps

views:
  - name: Kanban Board
    type: board
    group_by: Status

  - name: Sprint Backlog
    type: table
    filter: Sprint = @current
    sort: Priority

  - name: Roadmap
    type: roadmap
    date_field: Target Date

Linear Workflow
# Linear project structure
teams:
  - name: Engineering
    key: ENG
    workflows:
      - Backlog → Todo → In Progress → In Review → Done

cycles:
  - duration: 2 weeks
  - auto_archive: true

labels:
  - bug
  - feature
  - improvement
  - tech-debt

priorities:
  - Urgent
  - High
  - Medium
  - Low
  - No Priority

# Linear CLI usage
linear issue create --title "Add OAuth support" --team ENG --priority high
linear issue list --team ENG --state "In Progress"
linear cycle current

Sprint Planning
Sprint Planning Meeting
## Sprint Planning Agenda (2-4 hours)

### Part 1: What (1-2 hours)
1. Review sprint goal
2. Product Owner presents prioritized backlog
3. Team asks clarifying questions
4. Select stories for sprint commitment

### Part 2: How (1-2 hours)
1. Break stories into tasks
2. Identify dependencies
3. Assign initial owners
4. Validate capacity vs commitment

## Sprint Goal Template
"By the end of this sprint, users will be able to [specific capability],
enabling [business value]."

## Capacity Planning
Team Size: 5 developers
Sprint Length: 2 weeks (10 working days)
Meetings/Ceremonies: 1 day equivalent
PTO/Holidays: 2 days
Buffer (bugs, support): 10%

Available Capacity: (5 × 10 - 5 - 2) × 0.9 = 38.7 person-days
Historical Velocity: ~35 story points

Definition of Done
## Definition of Done (DoD)

### Code Complete
- [ ] Feature implemented per acceptance criteria
- [ ] Unit tests written (>80% coverage)
- [ ] Integration tests passing
- [ ] No linting errors or warnings
- [ ] Self-reviewed code

### Review Complete
- [ ] Code review approved by 2+ team members
- [ ] No blocking comments unresolved
- [ ] Security considerations reviewed

### Testing Complete
- [ ] QA testing passed
- [ ] Edge cases tested
- [ ] Performance acceptable
- [ ] Cross-browser testing (if applicable)

### Documentation Complete
- [ ] Code documented (JSDoc/comments)
- [ ] API documentation updated
- [ ] README updated if needed
- [ ] Changelog entry added

### Deployment Ready
- [ ] Feature flag configured (if needed)
- [ ] Database migrations tested
- [ ] Monitoring/alerts configured
- [ ] Merged to main branch

Retrospectives
Retrospective Formats
## Mad/Sad/Glad
┌─────────────────┬─────────────────┬─────────────────┐
│      Mad 😠     │     Sad 😢      │    Glad 😊      │
├─────────────────┼─────────────────┼─────────────────┤
│ Constant scope  │ Missed sprint   │ Great team      │
│ changes         │ goal            │ collaboration   │
│                 │                 │                 │
│ Unclear         │ Technical debt  │ Shipped major   │
│ requirements    │ growing         │ feature         │
└─────────────────┴─────────────────┴─────────────────┘

## Start/Stop/Continue
┌─────────────────┬─────────────────┬─────────────────┐
│     Start 🟢    │     Stop 🔴     │  Continue 🔵    │
├─────────────────┼─────────────────┼─────────────────┤
│ Pair programming│ Long meetings   │ Daily standups  │
│                 │                 │                 │
│ Sprint demos    │ Scope creep     │ Code reviews    │
│                 │                 │                 │
│ Documentation   │ Last-minute     │ Knowledge       │
│                 │ changes         │ sharing         │
└─────────────────┴─────────────────┴─────────────────┘

## 4 Ls: Liked, Learned, Lacked, Longed For
## Sailboat: Wind (helps), Anchors (slows), Rocks (risks)

Action Items Template
## Sprint 23 Retrospective Action Items

| Action | Owner | Due | Status |
|--------|-------|-----|--------|
| Set up automated E2E tests | @alice | Sprint 24 | 🟡 In Progress |
| Document API endpoints | @bob | Sprint 24 | ⬜ Not Started |
| Schedule architecture review | @carol | Next week | ✅ Done |

## Metrics to Track
- Sprint burndown consistency
- Bug escape rate
- Deployment frequency
- Lead time for changes

Metrics & Reporting
Key Metrics
## DORA Metrics
1. Deployment Frequency: How often code deploys to production
2. Lead Time for Changes: Commit to production time
3. Change Failure Rate: % of deployments causing failures
4. Time to Restore: How long to recover from failures

## Sprint Metrics
- Velocity: Story points completed per sprint
- Sprint Burndown: Work remaining over time
- Escaped Defects: Bugs found after release
- Planned vs Delivered: Commitment accuracy

## Team Health
- Team satisfaction surveys
- Turnover rate
- Knowledge sharing sessions
- Technical debt ratio

Related Skills
[[git-workflows]] - Version control
[[devops-cicd]] - Deployment practices
[[code-quality]] - Quality standards
Weekly Installs
208
Repository
miles990/claude…e-skills
GitHub Stars
12
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass