---
title: design-system
url: https://skills.sh/jwilger/agent-skills/design-system
---

# design-system

skills/jwilger/agent-skills/design-system
design-system
Installation
$ npx skills add https://github.com/jwilger/agent-skills --skill design-system
SKILL.md
Design System

Value: Communication -- a documented design system creates shared vocabulary for every visual decision. When philosophy is explicit and tokens are named, contributors extend the system consistently without guessing at intent.

Purpose

Facilitates collaborative creation of a design system specification. Produces an artifact at docs/design-system.pen (if Pencil MCP is available) or docs/design-system.html (single-file fallback) that documents philosophy, tokens, and the full component hierarchy from atoms through templates.

Practices
Detect Artifact Format

Check whether the mcp__pencil__get_editor_state tool is available.

Present: Use .pen format. Follow references/pencil-workflow.md.
Absent: Use HTML format. Follow references/html-artifact.md.

Decide the format before starting any design work. Do not switch formats mid-process.

Follow the Seven-Phase Collaborative Process

You MUST follow references/design-phases.md for the full methodology. Each phase completes before the next begins.

Phases at a glance:

Philosophy & Constraints -- Brand, principles, accessibility, responsive strategy, constraints. Every subsequent decision traces here.
Design Tokens -- Color, typography, spacing, radii, elevation, motion, breakpoints, opacity. Each token cites a philosophy principle.
Atoms -- Indivisible elements (buttons, inputs, labels, icons). Each documents states and references only tokens.
Molecules -- Functional units composed of atoms (form fields, search bars). Documents composition and interaction.
Organisms -- Distinct UI sections composed of molecules and atoms (headers, forms, data tables). Documents layout behavior.
Templates -- Page layouts arranging organisms. Defines structure, content slots, and breakpoint behavior.
Artifact Assembly -- Compile into the chosen format with philosophy as the first section.
Facilitate, Do Not Assume

You are a facilitator, not a stenographer. Ask probing questions at each phase. Challenge choices that conflict with stated philosophy. Use references/facilitation-questions.md for question banks.

Do not assume visual preferences -- ask
Do not skip ahead when the user gives a partial answer -- probe deeper
If event model wireframes exist in docs/event_model/, use them to identify required components, but still confirm with the user
Present token proposals informed by the philosophy and ask for adjustments
Enforce Philosophy Traceability

Every design decision traces back to the philosophy.

Tokens cite which philosophy principle they serve (e.g., P1)
Atoms reference which tokens they use
Molecules document which atoms they compose
Organisms document which molecules and atoms they compose
Templates document which organisms they arrange

If a token cannot cite a principle, either the token is unnecessary or the philosophy is incomplete. Resolve before proceeding.

Do:

Define philosophy before any visual decisions
Use only token references in components -- never raw values
Complete each phase before starting the next
Verify traceability at every level
Refer to references/token-categories.md for comprehensive token guidance

Do not:

Make technology decisions (CSS framework, component library) -- those belong in architecture-decisions
Skip the philosophy phase or treat it as optional
Use raw color codes, pixel values, or font names in components
Design multiple phases simultaneously
Proceed with gaps -- if something is undefined, ask
Enforcement Note

Advisory in all modes. Phase gates are self-enforced: the agent must complete each phase's outputs and get user confirmation before proceeding. Token traceability is self-enforced: the agent must verify every component references tokens, not raw values.

Hard constraints:

Phase ordering (complete each phase before starting the next): [RP]
Constraints
"No raw values in components": This means no literal color codes, pixel values, font sizes, or spacing values anywhere in component definitions. "I defined a token for it" is not sufficient if the component file contains the raw value instead of the token reference. Defining many single-use tokens to technically satisfy this rule while defeating reusability is also a violation.
Philosophy phase: Philosophy means named principles with enough specificity to guide decisions. "Modern and clean" is not a philosophy -- it constrains nothing. Each principle should be testable: given a design decision, the principle should help you choose between options. If it doesn't eliminate any option, it's not specific enough.
Verification

After completing work guided by this skill, verify:

 Philosophy documented with named principles before any components
 Tokens defined for all visual categories (color, typography, spacing, radii, elevation, motion, breakpoints, opacity)
 Every token cites a philosophy principle
 Atoms reference only tokens (no raw values)
 Molecules compose only atoms from the catalog
 Organisms compose only molecules and atoms from the catalog
 Templates arrange only organisms from the catalog
 All component states documented (default, hover, focus, disabled, error as applicable)
 Wireframe fields mapped to components if event model exists
 Artifact exists at docs/design-system.pen or docs/design-system.html
 Philosophy is the first section in the artifact

If any criterion is not met, revisit the relevant phase before proceeding.

Dependencies

This skill works standalone. For enhanced workflows, it integrates with:

event-modeling: Wireframes from event modeling sessions identify which components the design system must include. Run event-modeling first for best results.
architecture-decisions: The design system specification informs technology decisions for UI implementation (CSS framework, component library, build tooling). Run design-system before architecture-decisions.
atomic-design: The design system specification provides the token definitions, component catalog, and hierarchy that atomic-design implements in code.
tdd: Token values and component specifications become testable contracts -- visual regression tests verify token compliance.

Missing a dependency? Install with:

npx skills add jwilger/agent-skills --skill event-modeling

Weekly Installs
63
Repository
jwilger/agent-skills
GitHub Stars
2
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass