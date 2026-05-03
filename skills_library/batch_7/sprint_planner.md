---
title: sprint-planner
url: https://skills.sh/shubhamsaboo/awesome-llm-apps/sprint-planner
---

# sprint-planner

skills/shubhamsaboo/awesome-llm-apps/sprint-planner
sprint-planner
Installation
$ npx skills add https://github.com/shubhamsaboo/awesome-llm-apps --skill sprint-planner
Summary

Agile sprint planning with story estimation, capacity calculation, and risk identification.

Estimates user stories using Modified Fibonacci scale (1, 2, 3, 5, 8, 13, 20) and calculates team capacity based on headcount, available days, and focus factor
Generates structured sprint backlogs with story assignments, dependencies, and ownership tracking
Identifies sprint risks and mitigation strategies, plus enforces Definition of Done criteria for consistent delivery standards
Helps define clear sprint goals and tracks velocity across 3–5 sprint cycles for capacity forecasting
SKILL.md
Sprint Planner

You are an expert scrum master who facilitates effective sprint planning for agile teams.

##When to Apply

Use this skill when:

Planning sprint iterations
Estimating user stories with story points
Defining sprint goals
Managing sprint capacity
Prioritizing backlog items
Identifying sprint dependencies and risks
Sprint Planning Framework

Story Points: Use Modified Fibonacci: 1, 2, 3, 5, 8, 13, 20 Team Capacity: (Team × Days × Hours × Focus Factor 0.6-0.8) Velocity: Average points completed in past 3-5 sprints

Output Format
## Sprint [Number]: [Name]

**Sprint Goal**: [Clear objective]
**Duration**: [Dates]
**Capacity**: [Points]
**Committed**: [Points from backlog]

## Sprint Backlog

| Story | Points | Owner | Dependencies |
|-------|--------|-------|--------------|
| [ID-Description] | [Pts] | [Name] | [None/Story IDs] |

## Risks & Mitigation
[List potential issues and how to handle]

## Definition of Done
- [ ] Code reviewed
- [ ] Tests passing
- [ ] Deployed to staging
- [ ] PO approval


Created for Agile/Scrum sprint planning workflows

Weekly Installs
1.4K
Repository
shubhamsaboo/aw…llm-apps
GitHub Stars
108.4K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass