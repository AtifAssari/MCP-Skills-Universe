---
title: fusion-issue-author-feature
url: https://skills.sh/equinor/fusion-skills/fusion-issue-author-feature
---

# fusion-issue-author-feature

skills/equinor/fusion-skills/fusion-issue-author-feature
fusion-issue-author-feature
Installation
$ npx skills add https://github.com/equinor/fusion-skills --skill fusion-issue-author-feature
SKILL.md
Author Feature Issue
Dependency

Requires fusion-issue-authoring as the top-level orchestrator for classification, shared gates, and publish flow.

When to use

Use this skill when the request is for a new capability or enhancement.

When not to use

Do not use this skill for bugs, user stories centered on role narratives, or generic technical tasks.

Required inputs
Feature intent and value
Scope and non-goals
Success criteria
Instructions
Confirm routed type is Feature.
Draft locally in .tmp/FEATURE-<context>.md.
Structure draft with:
Story/problem statement
Scope (in/out)
Functional requirements
Acceptance criteria
Dependencies/risks
Check that scope boundaries and non-goals are explicit.
Return draft summary for orchestrator review/publish flow.

Template fallback:

skills/fusion-issue-author-feature/assets/issue-templates/feature.md
Expected output
Draft file path in .tmp/
Proposed title/body summary
Feature-specific scope and acceptance summary
Safety & constraints

Do not perform mutation directly; mutation stays in fusion-issue-authoring.

Weekly Installs
47
Repository
equinor/fusion-skills
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass