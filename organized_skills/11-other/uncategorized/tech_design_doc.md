---
rating: ⭐⭐
title: tech-design-doc
url: https://skills.sh/bahayonghang/my-claude-code-settings/tech-design-doc
---

# tech-design-doc

skills/bahayonghang/my-claude-code-settings/tech-design-doc
tech-design-doc
Installation
$ npx skills add https://github.com/bahayonghang/my-claude-code-settings --skill tech-design-doc
SKILL.md
Technical Design Document Skill
Execution Flow
1. Assess Complexity
Level	Scope	Sections Required
Small	Single component, <100 LOC	TL;DR, Design, Implementation
Medium	Cross-component, API changes	+ Background, Solution Analysis
Large	System-level, new service	Full template
2. Gather Context

Explore the codebase before writing:

Identify affected components using Glob and Grep for related code.
Read existing implementations and patterns.
Note dependencies and potential side effects.
Check for similar solutions already in the codebase.
3. Write Document
Read the document template from $SKILL_DIR/references/TEMPLATE.md.
Write the design document following the template structure, scaled to the assessed complexity level.
4. Verify Before Handoff

Verify the following criteria:

Define the problem clearly (what breaks if we do nothing?).
Compare options with trade-offs (do not present just one solution).
Document the decision rationale.
Add diagrams to illustrate key flows.
Make implementation steps concrete and actionable.
Identify risks and provide mitigations.
5. Handle Feedback

Process user change requests:

Identify which section needs revision.
Update only affected sections.
Ensure changes don't contradict other sections.
Re-verify the checklist items related to changes.
6. Output Location
Look for a docs/, ai_docs/, or design/ directory in the project.
Ask the user if the location is unclear.
Save with a descriptive filename such as design-[feature-name].md.
Weekly Installs
103
Repository
bahayonghang/my…settings
GitHub Stars
14
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass