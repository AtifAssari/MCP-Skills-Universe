---
title: project planner
url: https://skills.sh/eddiebe147/claude-settings/project-planner
---

# project planner

skills/eddiebe147/claude-settings/Project Planner
Project Planner
Installation
$ npx skills add https://github.com/eddiebe147/claude-settings --skill 'Project Planner'
SKILL.md
Project Planner

The Project Planner skill helps you create structured, comprehensive project plans with clear timelines, dependencies, deliverables, and resource requirements. It follows the ID8Pipeline methodology and ensures every project starts with proper scoping, architecture planning, and checkpoint definitions.

This skill creates actionable project plans that include work breakdown structures (WBS), critical path analysis, resource allocation, and risk mitigation strategies. It integrates with the ID8Pipeline 11-stage framework to ensure projects are built systematically from concept to launch.

The planner emphasizes vertical slicing, clear dependencies, and realistic timeline estimation based on team capacity and project complexity.

Core Workflows
Workflow 1: Create New Project Plan

Steps:

Discovery Phase

Gather project requirements and constraints
Identify stakeholders and team members
Define success criteria and business objectives
Clarify scope boundaries (what's in, what's out)

Scope Definition

Create one-liner problem statement (Stage 1: Concept Lock)
Define V1 feature set (max 5 core features)
Document "Not Yet" list (Stage 2: Scope Fence)
Establish quality gates and checkpoints

Work Breakdown Structure

Break project into major phases aligned with ID8Pipeline stages
Decompose features into vertical slices
Identify atomic tasks (4-8 hour chunks)
Map dependencies between tasks

Timeline Creation

Estimate task durations (consider complexity and team capacity)
Identify critical path and parallel work streams
Add buffer time (20% for uncertainty)
Set milestone dates with checkpoint criteria

Resource Planning

Assign tasks to team members or roles
Identify skill gaps or training needs
Plan for resource conflicts and availability
Allocate budget and tools

Documentation

Create PIPELINE_STATUS.md in project root
Generate PROJECT_PLAN.md with WBS and timeline
Set up tracking mechanisms (GitHub Projects, etc.)
Define communication cadence

Output: Complete project plan with timeline, dependencies, resource allocation, and checkpoint definitions.

Workflow 2: Update Existing Project Plan

Steps:

Read current PIPELINE_STATUS.md and PROJECT_PLAN.md
Assess actual progress vs. planned progress
Identify blockers, delays, or scope changes
Recalculate timeline based on new information
Update resource allocation if needed
Revise risk mitigation strategies
Document changes and communicate to stakeholders
Workflow 3: Quick Project Kickoff

For smaller projects or MVPs:

Define one-liner (Concept Lock)
List 3-5 core features (Scope Fence)
Choose tech stack (Architecture Sketch)
Create 2-week sprint plan with daily checkpoints
Set up basic project tracking
Quick Reference
Action	Command/Trigger
Create new project plan	"plan project [name]"
Update existing plan	"update project plan"
Quick MVP kickoff	"quick project kickoff for [idea]"
Review timeline	"review project timeline"
Check dependencies	"analyze project dependencies"
Estimate completion	"when will this project finish"
Add milestone	"add milestone [name]"
Adjust resources	"replan resources for [project]"
Best Practices
Start with the one-liner: Every project needs a clear, single-sentence definition of what problem it solves for whom
Enforce scope fence: Explicitly document what's NOT in V1 to prevent scope creep
Use vertical slicing: Build complete features end-to-end rather than horizontal layers
Build in checkpoints: Every stage has a clear exit criteria question that must be answered
Plan for 70% capacity: Team members are never 100% available due to meetings, interruptions, and context switching
Make dependencies visible: Use dependency mapping to identify critical path and parallelization opportunities
Time-box estimation sessions: Spend 30-60 minutes max on initial estimates; refine as you learn
Update weekly: Review and update project plan every week based on actual progress
Track assumptions: Document all assumptions made during planning and validate them early
Create feedback loops: Build in regular checkpoints for stakeholder review and course correction
Use the ID8Pipeline: Follow the 11 stages systematically - no skipping unless explicitly overridden with reason
Plan tests early: Include test coverage requirements in timeline (Stage 7 must be complete before polish)
Integration Points
ID8Pipeline: Automatically structures plans around 11-stage framework
GitHub Projects: Can generate project boards and issues from plan
PIPELINE_STATUS.md: Maintains current stage and checkpoint status
Task Manager skill: Hands off daily task management once plan is created
Sprint Planner skill: Breaks project plan into sprint-sized chunks
Risk Assessor skill: Identifies and tracks project risks during planning
Template Outputs
PROJECT_PLAN.md Structure
# [Project Name] - Project Plan

## Concept Lock (Stage 1)
**One-liner:** [Problem statement and target user]

## Scope Fence (Stage 2)
**V1 Features:**
1. Feature 1
2. Feature 2
3. Feature 3

**Not Yet List:**
- Future feature 1
- Future feature 2

## Timeline
[Gantt-style breakdown with dates and dependencies]

## Resources
[Team allocation and budget]

## Risks
[Top 5 risks and mitigation strategies]

## Success Criteria
[How we know we're done and it worked]

Estimation Guidelines
Project Size	Duration	Team Size	Complexity
Micro (POC)	1-2 weeks	1-2 people	Low
Small (MVP)	1-2 months	2-4 people	Medium
Medium (Product)	3-6 months	4-8 people	Medium-High
Large (Platform)	6-12 months	8+ people	High

Adjustment factors:

New tech stack: +30% time
Unclear requirements: +50% time
External dependencies: +20% time per dependency
Junior team: +40% time
Regulatory compliance: +25% time
Weekly Installs
–
Repository
eddiebe147/clau…settings
First Seen
–
Security Audits
Gen Agent Trust HubPass