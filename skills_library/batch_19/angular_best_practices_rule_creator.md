---
title: angular-best-practices-rule-creator
url: https://skills.sh/alfredoperez/angular-best-practices/angular-best-practices-rule-creator
---

# angular-best-practices-rule-creator

skills/alfredoperez/angular-best-practices/angular-best-practices-rule-creator
angular-best-practices-rule-creator
Installation
$ npx skills add https://github.com/alfredoperez/angular-best-practices --skill angular-best-practices-rule-creator
SKILL.md
Rule Creator Agent

Creates new Angular best practice rules and optional library skills following the exact project conventions.

Capabilities
1. Create a New Rule

When asked to create a rule:

Determine the prefix from the rule filename (e.g., material-imports.md → prefix material)
Look up the section number in packages/angular-best-practices-build/src/config.ts → sectionMap
Place the file in the correct rules/ subdirectory based on the prefix:
test-* → rules/testing/
a11y-*, ui-*, loading-*, dialogs-*, theming-* → rules/ui/
http-*, mapper-* → rules/data/
ts-* → rules/typescript/
opt-*, bundle-*, async-* → rules/optimization/
arch-* → rules/core/
Everything else (signals, components, forms, rxjs, ngrx, material, primeng, spartan, transloco, etc.) → rules/angular/
Copy the template from rules/_template.md
Fill in the frontmatter and content following these rules:
Title: Verb + Subject (e.g., "Use Signal Inputs")
Description: 1 sentence max
Code blocks: 0-2 max (incorrect + correct, or just correct)
Code per block: 3-5 lines max
Total length: Under 50 lines (ideal 30-40)
No installation commands, configuration dumps, or folder structures
Validate with the angular-best-practices-rules-reviewer skill
2. Create a New Library Skill

When asked to create a new optional library skill:

Choose the next available section number (check SECTION_TITLES in config.ts)
Update packages/angular-best-practices-build/src/config.ts:
Add prefix → section number in sectionMap
Add section title in SECTION_TITLES
Add section impact in SECTION_IMPACTS
Add entry in OPTIONAL_SKILLS array
Add section definition in rules/_sections.md
Create skills/<skill-name>/SKILL.md with frontmatter (name, description, metadata, tags, globs). Read .claude/skills/angular-best-practices-rules-reviewer/references/skill-best-practices.md for SKILL.md quality standards.
Create initial rule files in rules/angular/ with the skill's prefix
Run npm run build to generate AGENTS.md files
Prefix → Section Mapping (Current)
Prefix	Section	Title
async, opt-async	1	Eliminating Waterfalls
bundle	2	Bundle Optimization
opt, performance	3	JavaScript Performance
ts	4	TypeScript Best Practices
signal	5	Signals & Reactivity
component	6	Component Patterns
rxjs	7	RxJS Patterns
cd	8	Change Detection
template	9	Template Optimization
ssr	10	SSR & Hydration
form	11	Forms
ngrx	12	NgRx State Management
signalstore	13	SignalStore
tanstack	14	TanStack Query
arch	15	Architecture
test	16	Testing
core, di, error-handling, observability, pattern, routing, security	17	Infrastructure
ui, a11y, loading, dialogs, theming	18	UI & Accessibility
http, mapper	19	Data Handling
material	20	Angular Material
primeng	21	PrimeNG
spartan	22	Spartan UI
transloco	23	Internationalization
File Placement
Subdirectory	Prefixes
rules/angular/	signal, component, rxjs, cd, template, ssr, form, ngrx, signalstore, tanstack, material, primeng, spartan, transloco
rules/testing/	test
rules/ui/	ui, a11y, loading, dialogs, theming
rules/typescript/	ts
rules/optimization/	opt, bundle, async, performance
rules/core/	arch, core, di, error-handling, observability, pattern, routing, security
rules/data/	http, mapper
Template Reference
---
title: Verb + Subject
impact: MEDIUM
impactDescription: Brief metric (e.g., "2-10x faster", "O(n) to O(1)")
tags: tag1, tag2
---

## Verb + Subject

One sentence explaining the rule.

**Incorrect:**

\`\`\`typescript
// 3-5 lines max
\`\`\`

**Correct:**

\`\`\`typescript
// 3-5 lines max
\`\`\`

Build Commands
npm run build                    # Regenerate all AGENTS.md files
npm run build:skip-validation    # Skip validation during development

Weekly Installs
109
Repository
alfredoperez/an…ractices
GitHub Stars
31
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass