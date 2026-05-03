---
rating: ⭐⭐
title: cmk:system-design
url: https://skills.sh/commandosslabs/ai-devkit/cmk:system-design
---

# cmk:system-design

skills/commandosslabs/ai-devkit/cmk:system-design
cmk:system-design
Installation
$ npx skills add https://github.com/commandosslabs/ai-devkit --skill cmk:system-design
SKILL.md
System Design
Intents
Draft a system design for our payments service

Update the system design — we switched from PostgreSQL to DynamoDB

We're adding a message queue between the API and worker — update the architecture

How should we architect the notification system?

Use the scaling knowledge from our load tests to update the design

References

Read references/system-design-conventions.md for placement rules and references/system-design-template.md for section structure.

Scope

System design captures the technical "how" at architecture level. Product requirements belong in the PRD; implementation detail in feature specs. System-wide decisions should reference or create ADRs.

Input

Synthesize from whatever the user provides: conversation context, existing PRD (docs/PRD.md), local docs, external links, direct prompts, or docs/knowledge/ entries (when explicitly referenced).

Workflow: Create
Normalize input into architecture context: mission, design principles, tech stack, components, dependencies, cross-cutting concerns, constraints.
Map into template sections from references/system-design-template.md. Align to local convention if one exists.
Place at the repository's existing path, or fallback: docs/system-design.md.
Mark unknowns in Open Points — don't guess.
Link upstream PRD in Related Documents when one exists.
Set status to draft.
Workflow: Iterate
Read the existing system design in full.
Upstream check: If docs/PRD.md exists, scan its scope, success criteria, and status. Warn the user if the update conflicts with upstream PRD.
Identify what changed and why.
Update affected sections in place. Preserve unchanged content.
Update Last updated date.
Transition status when appropriate: draft → active → shipped, or any → deprecated.
Output
Create: complete system design at docs/system-design.md
Iterate: targeted updates to affected sections only
Unresolved decisions go in Open Points
Design principles are opinionated and system-specific
Architecture diagram matches component descriptions
Security section is always present — includes assumptions, gaps, and controls
No feature-level implementation detail
Weekly Installs
12
Repository
commandosslabs/ai-devkit
GitHub Stars
3
First Seen
Mar 9, 2026