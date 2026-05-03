---
rating: ⭐⭐
title: busirocket-tailwindcss-v4
url: https://skills.sh/busirocket/agents-skills/busirocket-tailwindcss-v4
---

# busirocket-tailwindcss-v4

skills/busirocket/agents-skills/busirocket-tailwindcss-v4
busirocket-tailwindcss-v4
Installation
$ npx skills add https://github.com/busirocket/agents-skills --skill busirocket-tailwindcss-v4
SKILL.md
Tailwind CSS v4 Best Practices

Setup and styling patterns for Tailwind CSS v4 projects.

When to Use

Use this skill when:

Setting up Tailwind CSS v4 in a project
Writing component styles with Tailwind utilities
Deciding when to extract custom CSS vs using utilities
Avoiding style drift and maintaining consistency
Non-Negotiables (MUST)
Import Tailwind via a single global CSS entry: @import 'tailwindcss';
Keep that global CSS imported from the root layout.
Prefer Tailwind utilities in className for most styling.
Avoid large custom CSS files; keep custom CSS truly global (resets, tokens).
Avoid heavy use of arbitrary values unless necessary; prefer consistent tokens.
Class Strategy
If class strings become hard to read:
Extract a small presentational component.
Or extract a components/<area>/... wrapper rather than inventing large custom CSS.
Rules
Setup
tailwind-setup - Tailwind CSS v4 setup (single global CSS import)
Class Strategy
tailwind-class-strategy - Prefer utilities, extract components when needed
tailwind-avoid-drift - Avoid style drift (keep custom CSS global, prefer tokens)
Ordering
tailwind-css-ordering - CSS order depends on import order
Related Skills
busirocket-react - Component extraction patterns
How to Use

Read individual rule files for detailed explanations and code examples:

rules/tailwind-setup.md
rules/tailwind-class-strategy.md
rules/tailwind-avoid-drift.md


Each rule file contains:

Brief explanation of why it matters
Code examples (correct and incorrect patterns)
Additional context and best practices
Weekly Installs
60
Repository
busirocket/agents-skills
GitHub Stars
1
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass