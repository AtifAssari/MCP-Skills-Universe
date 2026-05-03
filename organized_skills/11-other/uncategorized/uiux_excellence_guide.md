---
rating: ⭐⭐
title: uiux-excellence-guide
url: https://skills.sh/jpkovas/uiux-excellence-guide/uiux-excellence-guide
---

# uiux-excellence-guide

skills/jpkovas/uiux-excellence-guide/uiux-excellence-guide
uiux-excellence-guide
Installation
$ npx skills add https://github.com/jpkovas/uiux-excellence-guide --skill uiux-excellence-guide
SKILL.md
UI UX Excellence Guide
Overview

Turn vague UI requests into production-ready decisions and implementation guidance. Prioritize beauty, clarity, usability, accessibility, and responsiveness as one system.

Workflow Selection

Choose exactly one primary workflow before proposing changes:

Use Greenfield Workflow when creating a new screen, feature, or app surface.
Use Refactor Workflow when improving existing UI without breaking product behavior.
Use Audit Workflow when the user asks for critique, diagnosis, or prioritized fixes.
Shared Rules

Apply these rules in every workflow:

Define UX goals before styling details.
Decide layout rhythm early: spacing ramp, grid, and density mode.
Use semantic tokens for spacing, typography, color, radius, elevation, and motion.
Treat microcopy as interaction design, not garnish.
Respect accessibility constraints as non-negotiable.
Validate quality with metrics and checks before delivery.

Read references/uiux-baseline-2026.md for numeric thresholds and defaults.

Greenfield Workflow
Frame the problem:
Identify audience, platform, key journeys, and success criteria.
Confirm if there is an existing design system; if none, create a minimal token contract.
Establish structural system:
Define spacing ramp on base 4.
Define grid, margins, and gutters by viewport/window class.
Define density tier (standard or compact) for data-heavy views.
Define readability and hierarchy:
Define type scale tokens with line-height.
Enforce contrast and non-text contrast.
Keep labels concise and state-first.
Define motion and state communication:
Use short, purposeful transitions for state change and spatial continuity.
Provide reduced-motion fallback behavior.
Plan validation:
Set UX and performance acceptance criteria before implementation.
Include accessibility and interaction checks in the done definition.
Refactor Workflow
Audit the current surface:
Map friction points: confusion, misclicks, unreadable content, poor hierarchy.
Identify inconsistencies in tokens, spacing rhythm, and interaction patterns.
Prioritize changes:
Rank by impact on task success, error reduction, and accessibility risk.
Prefer low-risk structural improvements before visual polish.
Refactor with guardrails:
Preserve working behavior unless regression is explicitly accepted.
Normalize onto semantic tokens and remove one-off values.
Improve copy and feedback loops where users get stuck.
Validate and report:
Document before/after effects and remaining risks.
Include exact files touched and expected user-visible improvements.
Audit Workflow
Produce findings first, ordered by severity.
Attach concrete evidence (component, flow, file, line when applicable).
Provide actionable fixes, not vague recommendations.
Separate hard blockers from enhancement opportunities.
State testing gaps explicitly if validation cannot be completed.
Output Contract

Return outcomes in this order:

Direction: concise visual and UX direction statement.
Decisions: spacing, typography, density, motion, accessibility, and performance choices.
Implementation: exact edits or code-level plan.
Validation: checklist and measured/proxy results.
Risks: what is still unknown or untested.

Use references/uiux-delivery-template.md when a complete delivery structure is needed.

References
references/uiux-baseline-2026.md: implementation defaults and thresholds.
references/uiux-delivery-template.md: reusable response format for design and implementation tasks.
Weekly Installs
45
Repository
jpkovas/uiux-ex…ce-guide
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass