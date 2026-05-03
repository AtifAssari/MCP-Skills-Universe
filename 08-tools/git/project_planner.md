---
title: project-planner
url: https://skills.sh/0xdarkmatter/claude-mods/project-planner
---

# project-planner

skills/0xdarkmatter/claude-mods/project-planner
project-planner
Installation
$ npx skills add https://github.com/0xdarkmatter/claude-mods --skill project-planner
SKILL.md
Project Planner Skill

Lightweight awareness layer for docs/PLAN.md. Detects when plans need attention and points to /save and /sync commands.

Purpose

This skill does NOT manage plans directly. It:

Detects when docs/PLAN.md exists or is missing
Identifies stale plans (no recent updates vs git activity)
Suggests appropriate session commands

All plan operations go through /save (persist) and /sync (restore/status).

Detection Logic
Plan Missing
No docs/PLAN.md found
-> Suggest: /save to create initial plan from conversation

Plan Stale
docs/PLAN.md last modified: 5 days ago
git log shows: 12 commits since then
-> Suggest: /sync --git to update from commits

Uncommitted Work
git status shows: 5 modified files
docs/PLAN.md "In Progress" section outdated
-> Suggest: /sync --status to review

Session Start
Resuming work on project with docs/PLAN.md
-> Suggest: /sync to restore state

Quick Reference
Situation	Suggestion
No plan exists	/save after discussing goals
Plan is stale	/sync --git
Need to see plan	/sync --status
Update progress	/save "notes"
Start fresh	/save --archive
Staleness Heuristics

A plan is considered stale when:

Last modified > 3 days ago AND
Git shows commits since last modification AND
Commits relate to plan topics (feat:, fix:, refactor:)

A plan needs review when:

Session just started
Significant uncommitted changes exist
User mentions progress or completion
Notes
This skill only suggests, never modifies
/sync reads state, /save writes state
Single source of truth: docs/PLAN.md
Weekly Installs
28
Repository
0xdarkmatter/claude-mods
GitHub Stars
17
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass