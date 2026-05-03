---
title: technical-deslop
url: https://skills.sh/vincentkoc/dotskills/technical-deslop
---

# technical-deslop

skills/vincentkoc/dotskills/technical-deslop
technical-deslop
Installation
$ npx skills add https://github.com/vincentkoc/dotskills --skill technical-deslop
SKILL.md
Technical Deslop
Purpose

Clean branch/staged diffs by removing AI-style slop and restoring repo-consistent style without changing behavior.

When to use
A diff feels over-explained, overly defensive, or inconsistent with surrounding code.
You need a final cleanup pass before review/PR.
You want to normalize style after automated generation.
Workflow
Capture scope with git diff --cached and git diff $(git merge-base origin/main HEAD)..HEAD.
Focus only on changed hunks (or user-scoped files).
Apply the cleanup sequence in references/playbook.md.
Remove slop patterns: redundant comments, unnecessary defensive branches, non-idiomatic casts, and style drift.
Re-check behavior boundaries: no logic changes unless the user explicitly requested them.
Report a short 1-3 sentence summary of cleanup performed.

Read references/slop-patterns.md for detection rules and references/playbook.md for execution order.

Inputs
Optional file scope (FILES) or explicit user file targets.
Current branch diff and staged diff.
Repository conventions from local instructions/config.
Outputs
Behavior-preserving cleanup in touched files.
Minimal summary of what was normalized and where.
Weekly Installs
65
Repository
vincentkoc/dotskills
GitHub Stars
44
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass