---
title: start-implementation
url: https://skills.sh/sones3/skills/start-implementation
---

# start-implementation

skills/sones3/skills/start-implementation
start-implementation
Installation
$ npx skills add https://github.com/sones3/skills --skill start-implementation
SKILL.md
Start Implementation

This skill ensures an issue is fully implemented without interruption, then documents the work, provides recommendations, commits changes, and closes the issue. Confirmation is required only if the issue is not already in the context.

Process
1. Check issue context
Determine if the issue to implement is already confirmed in the conversation context.
If it is not confirmed, present the issue to the user for confirmation:
Title
Issue number
Type (backend / frontend)
Blocked by / Dependencies
If it is already confirmed, skip this step.
2. Begin implementation
Implement all functionality required by the issue without pausing or switching tasks.
Follow the pre-discussed plan for implementation.
Include necessary coding, documentation, and integration work as part of the flow.
3. Document work upon completion

Once the implementation is complete:

Write a detailed summary in the GitHub issue:
What was implemented: step-by-step explanation of completed work.
Recommendations for other issues: insights, dependencies, or best practices discovered.
4. Commit and close the issue
Commit all changes with a clear commit message referencing the issue number.
Close the GitHub issue after committing.
5. Notes
The implementation must continue uninterrupted until fully completed.
Recommendations should be actionable and relevant for the remaining PRD issues.
Weekly Installs
8
Repository
sones3/skills
GitHub Stars
3
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass