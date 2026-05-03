---
rating: ⭐⭐
title: team-lead
url: https://skills.sh/iankiku/forwward-teams/team-lead
---

# team-lead

skills/iankiku/forwward-teams/team-lead
team-lead
Installation
$ npx skills add https://github.com/iankiku/forwward-teams --skill team-lead
SKILL.md
Team Lead — Compose & Coordinate Agent Teams

Analyze a task, pick the right team shape, spawn agents, coordinate work.

Step 0: Project Config

Before spawning agents, ensure .claude/project.json exists:

${CLAUDE_PLUGIN_ROOT}/scripts/cli init


Agents read this file for all build commands — no re-detection needed.

Model Tiers
Tier	Model	Use for
Think	sonnet	Planning, architecture, debugging, review
Execute	haiku	Implementation, commands, edits, fixes

Default to haiku. Use sonnet only when reasoning depth matters.

Team Recipes
Feature Dev (2-3 agents)

Trigger: New features, UI + backend, E2E work.

Name	Model	Role
lead	sonnet	Integration, API contracts, shared types
backend	haiku	API routes, DB, server logic
frontend	haiku	Components, UI, client-side (blocked by backend)
Code Quality (2 agents)

Trigger: Reviews, tech debt, quality checks.

Name	Model	Role
reviewer	sonnet	Correctness, security, patterns (read-only)
debt	haiku	Duplicates, dead code, over-engineering (read-only)
Strategic Sprint (2-3 agents)

Trigger: Market research, competitive analysis, strategic planning, fundraising.

Name	Model	Role
researcher	sonnet	Market intelligence, competitor analysis
strategist	sonnet	Prioritization, roadmap (blocked by researcher)
ceo	sonnet	Decision synthesis, OKRs, resource calls (blocked by strategist)
Bug Hunt (2 agents)

Trigger: Bug fixes, debugging, incidents.

Name	Model	Role
investigator	sonnet	Root cause, reproduction steps
fixer	haiku	Implement fix (blocked by investigator)
Workflow
Analyze — Read task, pick closest recipe (or combine, cap at 4 agents)
Create team — TeamCreate, then TaskCreate for each work item
Spawn agents — Agent tool with model tier, permissions, team name
Coordinate — TaskUpdate to assign, SendMessage for blockers
Gate — Each agent runs /gate before declaring done
Ship — Run /ship to push and open PR
Rules
Smallest team possible. 2 agents over 3 when feasible.
Skip the team for single-focus tasks — do it yourself.
mode: "acceptEdits" for builders, mode: "default" for reviewers.
Never spawn duplicates — shut down stuck agents first.
Simple tasks don't need teams. Use judgment.
Weekly Installs
23
Repository
iankiku/forwward-teams
GitHub Stars
14
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass