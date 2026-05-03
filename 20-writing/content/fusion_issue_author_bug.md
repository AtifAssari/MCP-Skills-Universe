---
title: fusion-issue-author-bug
url: https://skills.sh/equinor/fusion-skills/fusion-issue-author-bug
---

# fusion-issue-author-bug

skills/equinor/fusion-skills/fusion-issue-author-bug
fusion-issue-author-bug
Installation
$ npx skills add https://github.com/equinor/fusion-skills --skill fusion-issue-author-bug
SKILL.md
Author Bug Issue
Dependency

Requires fusion-issue-authoring as the top-level orchestrator for classification, shared gates, and publish flow.

When to use

Use this skill when the request is about broken behavior, regressions, crashes, or unexpected results.

When not to use

Do not use this skill for feature requests, user stories, or generic enablement tasks.

Required inputs
Bug context (observed behavior, expected behavior, impact)
Reproduction information (if available)
Environment context
Instructions
Confirm routed type is Bug.
Draft locally in .tmp/BUG-<context>.md.
Structure draft with:
Description
Steps to reproduce
Expected behavior
Actual behavior
Environment
Impact
Validate the draft has enough reproduction detail for triage.
Return the draft summary for orchestrator review/publish flow.

Template fallback:

skills/fusion-issue-author-bug/assets/issue-templates/bug.md
Expected output
Draft file path in .tmp/
Proposed title/body summary
Bug-specific triage notes (repro clarity + impact)
Safety & constraints

Do not perform mutation directly; mutation stays in fusion-issue-authoring.

Weekly Installs
49
Repository
equinor/fusion-skills
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass