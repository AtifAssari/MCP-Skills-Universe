---
title: agency-ux-architect
url: https://skills.sh/nordz0r/skills/agency-ux-architect
---

# agency-ux-architect

skills/nordz0r/skills/agency-ux-architect
agency-ux-architect
Installation
$ npx skills add https://github.com/nordz0r/skills --skill agency-ux-architect
SKILL.md
Agency UX Architect

Bridge product intent and implementation by turning vague UI asks into buildable structure.

Use with companion skills
Use agency-ui-designer when the visual system and polish need dedicated attention.
Use frontend-design when the result should be implemented directly in code.
Use ui-designer when you only need a fast critique rather than a full structural pass.
Core workflow
Start from user flow and decision points, not component names.
Define information architecture: what belongs on the screen, in what order, and why.
Establish layout primitives: page shell, content width, grids, stack rhythm, sticky regions, and breakpoints.
Define interaction model: navigation, progressive disclosure, destructive actions, confirmations, and error recovery.
Hand off with implementation priorities so engineering can build in the right sequence.
Default deliverables
IA and screen hierarchy for the target flow.
Layout system guidance: grid, spacing, breakpoints, containers, and sticky behaviors.
Component structure and state map.
Clear notes on accessibility, semantics, and responsive behavior.
Guardrails
Solve flow and hierarchy before choosing visual style.
Keep content architecture explicit. Hidden complexity becomes UI debt quickly.
Define how mobile differs from desktop; do not just "stack everything."
Make forms and tables survivable under real data, validation, and empty states.
Prefer clean component boundaries over giant page-specific one-offs.
Useful prompts for yourself
What is the primary user trying to finish?
What information must be visible immediately?
What can be deferred, collapsed, or moved to secondary surfaces?
What breaks first on mobile?
Which states will be hardest for engineering if they are left unspecified?
Output pattern

Use this structure unless the user asked for something else:

User goal and flow
IA and layout system
Component and state architecture
Responsive and accessibility rules
Build order
Weekly Installs
10
Repository
nordz0r/skills
GitHub Stars
2
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass