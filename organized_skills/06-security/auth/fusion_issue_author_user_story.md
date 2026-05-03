---
rating: ⭐⭐
title: fusion-issue-author-user-story
url: https://skills.sh/equinor/fusion-skills/fusion-issue-author-user-story
---

# fusion-issue-author-user-story

skills/equinor/fusion-skills/fusion-issue-author-user-story
fusion-issue-author-user-story
Installation
$ npx skills add https://github.com/equinor/fusion-skills --skill fusion-issue-author-user-story
SKILL.md
Author User Story Issue
Dependency

Requires fusion-issue-authoring as the top-level orchestrator for classification, shared gates, and publish flow.

When to use

Use this skill when the request is primarily about user workflow and behavior from a specific role perspective.

When not to use

Do not use this skill for pure bug reports, generic feature specs without user narrative, or technical enablement tasks.

Required inputs
User role and workflow context
Story goal (As a... I want... so that...)
Key scenarios and success criteria
Instructions
Confirm routed type is User Story.
Draft locally in .tmp/USER-STORY-<context>.md.
Structure draft with:
Story statement
Context/pain points
Functional requirements
Scenarios (Given/When/Then)
Validation approach
Ensure scenarios are testable and role-centered.
Return draft summary for orchestrator review/publish flow.

Template fallback:

skills/fusion-issue-author-user-story/assets/issue-templates/user-story.md
Expected output
Draft file path in .tmp/
Proposed title/body summary
Story-specific scenario and validation summary
Safety & constraints

Do not perform mutation directly; mutation stays in fusion-issue-authoring.

Weekly Installs
46
Repository
equinor/fusion-skills
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass