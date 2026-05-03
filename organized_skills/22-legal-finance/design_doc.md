---
rating: ⭐⭐
title: design-doc
url: https://skills.sh/diskd-ai/design-doc/design-doc
---

# design-doc

skills/diskd-ai/design-doc/design-doc
design-doc
Installation
$ npx skills add https://github.com/diskd-ai/design-doc --skill design-doc
SKILL.md
Technical Design Document Skill

Create structured technical design documents that communicate system behavior, implementation approach, and acceptance criteria.

Workflow
Gather context: Understand the feature/system scope, constraints, and goals
Draft structure: Use template from references/template.md
Fill sections: Work through each section, asking clarifying questions as needed
Review: Ensure acceptance criteria are testable and implementation outline is actionable
Template

See references/template.md for the full template structure and section guidelines.

Core sections:

Context and motivation: Problem statement, goals, non-goals
Implementation considerations: Constraints and design principles
High-level behavior: End-to-end system behavior
Domain-specific sections: Adapt to feature type (discovery, validation, API, state, rendering)
Error handling and UX: Error surfacing and recovery
Future-proofing: Design for extensibility
Implementation outline: Step-by-step approach
Testing approach: Unit, integration, manual tests
Acceptance criteria: Testable conditions for "done"
Writing Guidelines
Use --- underlines for section headers (Setext style)
Write in present tense for behavior ("loads", "validates", "returns")
Be specific: "max 100 chars" not "reasonable length"
Include concrete examples where behavior varies
Non-goals are as important as goals - prevent scope creep
Acceptance criteria must be verifiable, not subjective
Weekly Installs
142
Repository
diskd-ai/design-doc
GitHub Stars
1
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass