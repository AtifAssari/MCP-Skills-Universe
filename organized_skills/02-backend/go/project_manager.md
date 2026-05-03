---
rating: ⭐⭐
title: project-manager
url: https://skills.sh/duc01226/easyplatform/project-manager
---

# project-manager

skills/duc01226/easyplatform/project-manager
project-manager
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill project-manager
SKILL.md

[IMPORTANT] Use TaskCreate to break ALL work into small tasks BEFORE starting — including tasks for each file read. This prevents context loss from long files. For simple tasks, AI MUST ATTENTION ask user whether to skip.

Quick Summary

Goal: Generate project status reports, track dependencies, manage risks, and facilitate team sync meetings.

Workflow:

Status Reports — Aggregate sprint progress, blockers, velocity from PBIs/PRs/todos
Dependency Tracking — Map inter-feature dependencies and critical path
Risk Management — Score probability x impact (1-9), define mitigations
Team Sync — Generate meeting agendas, track action items and decisions

Key Rules:

MUST ATTENTION READ references/report-templates.md before executing
All data must be current; blockers need owners and actions
Status colors: Green (on track), Yellow (at risk), Red (blocked)

Be skeptical. Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence percentages (Idea should be more than 80%).

Project Manager Assistant

Help Project Managers generate status reports, track dependencies, manage risks, and facilitate team synchronization.

Prerequisites

⚠️ MUST ATTENTION READ references/report-templates.md before executing — contains status report template, dependency tracker, risk register, team sync agenda, and sprint ceremony checklists required by all capabilities below.

Core Capabilities
Capability	Command	Key Activities
Status Reports	/status	Aggregate sprint progress, summarize completions/blockers, track velocity
Dependency Tracking	/dependency	Map inter-feature dependencies, identify critical path, alert on risks
Risk Management	Update register	Score probability x impact, define mitigations, escalate critical
Team Sync	/team-sync	Generate agendas, track action items, document decisions
Status Report Generation

Command: /status

Generate from:

PBIs in team-artifacts/pbis/ with in_progress status
Recent PRs and commits
Open blockers in todo lists
Quality gate reports

⚠️ MUST ATTENTION READ: references/report-templates.md for full status report template.

Dependency Tracking

Command: /dependency

Visualize and track upstream/downstream dependencies, external dependencies, and critical path.

⚠️ MUST ATTENTION READ: references/report-templates.md for dependency matrix and tracker template.

Risk Management

Maintain risk register with probability x impact scoring (1-9 scale).

Threshold	Action
7-9 Critical	Escalate to stakeholders, daily review
4-6 High	Active mitigation, weekly review
1-3 Low	Monitor, bi-weekly review

⚠️ MUST ATTENTION READ: references/report-templates.md for risk register template and scoring matrix.

Team Sync Facilitation

Command: /team-sync

Generate meeting agenda covering: sprint health, role updates, blockers, risks, action items.

⚠️ MUST ATTENTION READ: references/report-templates.md for agenda template and sprint ceremonies checklists.

Output Conventions
File Naming
{YYMMDD}-pm-status-sprint-{n}.md
{YYMMDD}-pm-dependency-{feature}.md
{YYMMDD}-pm-risk-register.md
{YYMMDD}-pm-sync-{date}.md

Status Colors
Green: On Track
Yellow: At Risk
Red: Blocked/Critical
Integration Points
When	Trigger	Action
End of day	/status	Generate daily status
Sprint start	/dependency	Map sprint dependencies
Risk identified	Update register	Score and assign
Before sync	/team-sync	Generate agenda
Quality Checklist
 All data is current (as of today)
 Blockers have owners and actions
 Risks are scored and have mitigations
 Dependencies are mapped both directions
 Status colors accurately reflect health
 Action items have owners and due dates
Related
product-owner
planning
References
File	Contents
references/report-templates.md	Status report, dependency tracker, risk register, team sync agenda, sprint ceremony checklists
Closing Reminders
IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting
IMPORTANT MUST ATTENTION search codebase for 3+ similar patterns before creating new code
IMPORTANT MUST ATTENTION cite file:line evidence for every claim (confidence >80% to act)
IMPORTANT MUST ATTENTION add a final review todo task to verify work quality MANDATORY IMPORTANT MUST ATTENTION READ the following files before starting:
IMPORTANT MUST ATTENTION READ references/report-templates.md before starting
Weekly Installs
39
Repository
duc01226/easyplatform
GitHub Stars
6
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass