---
title: resend-design-skills
url: https://skills.sh/resend/design-skills/resend-design-skills
---

# resend-design-skills

skills/resend/design-skills/resend-design-skills
resend-design-skills
Installation
$ npx skills add https://github.com/resend/design-skills --skill resend-design-skills
SKILL.md
Design Skills

A collection of design-related skills for Claude Code.

Available Skills
Skill	Description	Path
resend-brand	Applies Resend's brand colors, typography, and visual identity to marketing materials and artifacts	brand-guidelines/SKILL.md
resend-design-system	UI component APIs, design tokens, and composition patterns for building product UI in the Resend codebase	design-system/SKILL.md
marketing-pages	Page structure, component reuse rules, and public primitives for creating/editing marketing pages in src/app/(website)/	marketing-pages/SKILL.md
design-audit	Audits the Resend dashboard for design system alignment — missing docs, component substitution, token misuse, deprecated usage, and pattern candidates	design-audit/SKILL.md
When to use which skill
resend-brand — Marketing pages, social graphics, presentations, documents, and any external-facing visual content
resend-design-system — Product UI, src/ui/ components, design tokens, and code patterns inside the Resend codebase
marketing-pages — Creating, updating, or deleting marketing pages in src/app/(website)/, including page structure, public primitives, and SEO metadata
design-audit — "Audit design", "design alignment", "dashboard design audit", or the scheduled Monday routine
Structure

Each skill lives in its own folder with a SKILL.md file that defines:

Frontmatter with name and description
Guidelines, rules, and reference material
design-skills/
├── SKILL.md              # This index file
├── brand-guidelines/
│   └── SKILL.md          # Resend brand skill
├── design-system/
│   ├── SKILL.md          # Resend design system skill
│   └── references/
│       ├── components.md
│       ├── design-tokens.md
│       ├── patterns.md
│       └── patterns/
│           └── README.md # Documented UI composition patterns
├── design-audit/
│   ├── SKILL.md          # Design audit skill
│   └── references/
│       ├── rubric.md
│       ├── report-format.md
│       └── linear-delivery.md
├── marketing-pages/
│   ├── SKILL.md          # Marketing pages skill
│   └── references/
│       └── components.md
└── tests/
    └── TESTS.md          # Combined test suite

Weekly Installs
496
Repository
resend/design-skills
GitHub Stars
22
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass