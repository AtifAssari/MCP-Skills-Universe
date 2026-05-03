---
rating: ⭐⭐⭐
title: design-audit
url: https://skills.sh/phrazzld/claude-config/design-audit
---

# design-audit

skills/phrazzld/claude-config/design-audit
design-audit
Installation
$ npx skills add https://github.com/phrazzld/claude-config --skill design-audit
SKILL.md
description: Audit current design system for consistency and debt
DESIGN-AUDIT

Analyze the current design system for violations, gaps, and inconsistencies.

What This Does
Inventory tokens — Colors, typography, spacing, shadows
Check consistency — Are tokens used consistently?
Find violations — Hardcoded values, magic numbers
Assess accessibility — WCAG compliance
Report debt — Design debt that's accumulated
Process
1. Load Design Skills
Skill("design-tokens")           # Token patterns
Skill("web-design-guidelines")   # Vercel standards

2. Extract Current Tokens

Scan for design token definitions:

Tailwind config (tailwind.config.ts, globals.css)
CSS variables
Theme files
Component defaults
3. Audit Token Usage

For each token category:

Colors:

Are colors from the palette? Or hardcoded hex?
Is there semantic naming (primary, error, success)?
Dark mode support?

Typography:

Font scales defined?
Consistent heading hierarchy?
Line heights appropriate?

Spacing:

Spacing scale in use?
Magic numbers in margins/padding?

Components:

Consistent component patterns?
Reusable primitives?
Duplicated styles?
4. Accessibility Check
/rams — Score current state


Check:

Color contrast (WCAG AA minimum)
Focus states
Touch targets
Screen reader support
5. Report Findings
## Design Audit: [Project Name]

### Token Inventory
- Colors: [count] defined, [violations] hardcoded
- Typography: [count] scales, [violations] magic sizes
- Spacing: [count] values, [violations] arbitrary

### Consistency Score: [X]/100

### Critical Issues
- [ ] [Issue] - [location] - [fix]

### Debt Items
- [ ] [Tech debt] - [impact] - [effort]

### RAMS Score: [X]/100

### Recommendations
1. [Priority fix]
2. [Improvement]

Diagram Documentation

For design system diagrams (component hierarchy, token relationships), use /beautiful-mermaid for production-quality renders.

Output

Audit report ready. Next: /design to explore new directions or fix issues.

Weekly Installs
27
Repository
phrazzld/claude-config
GitHub Stars
8
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass