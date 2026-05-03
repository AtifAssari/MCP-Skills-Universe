---
rating: ⭐⭐⭐
title: concise-planning
url: https://skills.sh/sickn33/antigravity-awesome-skills/concise-planning
---

# concise-planning

skills/sickn33/antigravity-awesome-skills/concise-planning
concise-planning
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill concise-planning
Summary

Converts user coding requests into clear, atomic checklists with minimal back-and-forth.

Scans existing code, docs, and constraints before generating a plan to avoid unnecessary questions
Produces structured plans with approach, scope boundaries, 6–10 ordered action items, and validation steps
Uses verb-first, concrete task language (e.g., "Add X to file Y") to keep steps logically independent and actionable
Asks at most 1–2 blocking questions; makes reasonable assumptions for non-blocking unknowns to keep planning efficient
SKILL.md
Concise Planning
Goal

Turn a user request into a single, actionable plan with atomic steps.

Workflow
1. Scan Context
Read README.md, docs, and relevant code files.
Identify constraints (language, frameworks, tests).
2. Minimal Interaction
Ask at most 1–2 questions and only if truly blocking.
Make reasonable assumptions for non-blocking unknowns.
3. Generate Plan

Use the following structure:

Approach: 1-3 sentences on what and why.
Scope: Bullet points for "In" and "Out".
Action Items: A list of 6-10 atomic, ordered tasks (Verb-first).
Validation: At least one item for testing.
Plan Template
# Plan

<High-level approach>

## Scope

- In:
- Out:

## Action Items

[ ] <Step 1: Discovery>
[ ] <Step 2: Implementation>
[ ] <Step 3: Implementation>
[ ] <Step 4: Validation/Testing>
[ ] <Step 5: Rollout/Commit>

## Open Questions

- <Question 1 (max 3)>

Checklist Guidelines
Atomic: Each step should be a single logical unit of work.
Verb-first: "Add...", "Refactor...", "Verify...".
Concrete: Name specific files or modules when possible.
When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
625
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass