---
rating: ⭐⭐⭐
title: frontend-planning
url: https://skills.sh/ywj3493/claude-skills/frontend-planning
---

# frontend-planning

skills/ywj3493/claude-skills/frontend-planning
frontend-planning
Installation
$ npx skills add https://github.com/ywj3493/claude-skills --skill frontend-planning
SKILL.md
frontend-planning

DEPRECATED: This skill has been superseded by dev-planning. Use dev-planning instead, which supports backend, frontend, and infrastructure domains in a unified pipeline with test traceability.

6-step planning document pipeline for frontend projects, organized by domain.

When to Use
User says "프론트엔드 기획", "frontend planning", "UI 설계", "화면 설계"
User says "프론트엔드 문서", "기획 문서 만들어줘", "plan frontend"
Starting a new frontend project that needs structured design documents
Adding a major frontend feature that requires multi-page planning
When NOT to Use
Backend-only projects (use the backend planning pipeline instead)
Fixing a single component or small UI tweak
Editing or updating existing specification documents
Non-UI work such as CI/CD, infrastructure, or tooling
Pipeline Overview
Step 0:   Tech stack detection
Step 0.5: Domain analysis & document discovery
Step 1:   Requirements          → <domain>/requirements/requirements.md
Step 2:   User Flows            → <domain>/requirements/user-flows.md
Step 3:   UI Spec               → <domain>/requirements/ui-spec.md
Step 4:   Use Cases             → <domain>/workflows/use-cases.md
Step 5:   Component Tree        → <domain>/workflows/component-tree.md
Step 6:   State & API Integration → <domain>/workflows/state-api-integration.md
Step 7:   README (table of contents)


Steps 1–3 are planning/design documents (what to build). Steps 4–6 are implementation documents (how to build).

For multi-domain projects, Steps 1–6 repeat per domain. Step 7 runs once.

Output Structure
docs/en/specifications/
├── architecture.md              # Project structure (Mermaid) — cross-cutting
├── infrastructure.md            # Deployment & infra (Mermaid) — cross-cutting
├── config.md                    # Environment variables
├── README.md                    # Index of all domains/documents (Step 7)
└── <domain>/
    ├── requirements/
    │   ├── requirements.md      # Step 1
    │   ├── user-flows.md        # Step 2
    │   └── ui-spec.md           # Step 3
    └── workflows/
        ├── use-cases.md         # Step 4
        ├── component-tree.md    # Step 5
        └── state-api-integration.md  # Step 6

Navigation

Every domain document includes two navigation blocks:

Top — sequential prev/next for linear reading:

> [← Requirements](requirements.md) | [UI Spec →](ui-spec.md)


First document omits "←", last document omits "→".

Bottom — full index to jump to any document:

---
> **All Documents**
> [Requirements](requirements.md) | ... | [State & API](state-api-integration.md)


The current document is shown in bold instead of a link.

Step-by-Step Instructions
Step 0: Detect Tech Stack
Read package.json — framework, dependencies
Read tsconfig.json — TypeScript usage
Scan directory structure — src/, app/, pages/, components/
Check styling and state management solutions

Summarize and confirm with the user before proceeding.

Step 0.5: Domain Analysis & Document Discovery

Domain Analysis

Ask the user to describe major feature areas
Propose domain groupings (e.g., auth, dashboard)
Always create at least one domain directory
Present proposed structure and wait for confirmation

Document Discovery

Scan README.md, CLAUDE.md, all .md files under docs/en/specifications/ and docs/en/policy/
Classify each by first 30 lines: requirements / user-stories / use-cases / api-spec / sequence-diagram / architecture / config / infrastructure / deployment / policy / other
Present discovered documents grouped by category using @-reference format
Carry confirmed document list to all subsequent steps

If no documents found, record "No project documents found" and proceed.

Step 1: Requirements

Output: <domain>/requirements/requirements.md

Load template: references/requirements-template.md
Load discovered docs classified as requirements, user-stories, or architecture
Ask user for: project purpose, target users, core features, non-functional requirements
Generate document and wait for review
Step 2: User Flows

Output: <domain>/requirements/user-flows.md

Load template: references/user-flows-template.md
Load Step 1 output
Load discovered docs classified as use-cases or sequence-diagram
For each major feature: Mermaid flowchart (happy path), alternative/exception paths
Generate document and wait for review
Step 3: UI Spec

Output: <domain>/requirements/ui-spec.md

Load template: references/ui-spec-template.md
Load Steps 1–2 outputs
Skim discovered docs classified as api-spec or architecture
For each view: URL/trigger, layout structure, key components, responsive behavior, SEO (if applicable)
Generate document and wait for review
Step 4: Use Cases

Output: <domain>/workflows/use-cases.md

Load template: references/use-cases-template.md
Load Steps 1–3 outputs
Load discovered docs classified as use-cases or architecture
For each use case: actor, preconditions/postconditions, main/alternative/exception flows
Generate document and wait for review
Step 5: Component Tree

Output: <domain>/workflows/component-tree.md

Load template: references/component-tree-template.md
Load Steps 1–4 outputs
Define: Mermaid graph of component hierarchy, shared vs page-specific components, TypeScript prop interfaces
Generate document and wait for review
Step 6: State & API Integration

Output: <domain>/workflows/state-api-integration.md

Load template: references/state-api-integration-template.md
Load Steps 1–5 outputs
Load discovered docs classified as api-spec — use as authoritative endpoint source
Define: state strategy, store interfaces, API endpoints table, DTOs, caching, error handling
Generate document and wait for review
Step 7: Generate README

Output: docs/en/specifications/README.md

After all domains complete Steps 1–6:

Single-domain: table of contents linking all 6 documents
Multi-domain: section per domain + optional per-domain README.md
If README exists, merge rather than overwrite
Include discovered documents in a Related Project Documents section

Report all generated file paths on completion.

Document Rules
Language: English
Meta block: Created, Last Modified, Status, Tech Stack, Prerequisites, Reference Documents
Mermaid: flowchart TD for user flows, graph TD for component trees
TypeScript: interface for props, stores, DTOs
References: Each step loads all previous outputs before generating
Review gate: Never proceed without user approval
Navigation: Every domain document has top (prev/next) and bottom (all documents) navigation
@-references: Use for discovered docs per @docs/en/policy/reference-convention.md; never @-prefix docs/reference/ files
Weekly Installs
10
Repository
ywj3493/claude-skills
GitHub Stars
2
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass