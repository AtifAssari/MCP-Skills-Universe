---
title: tailwind-best-practices
url: https://skills.sh/mastra-ai/mastra/tailwind-best-practices
---

# tailwind-best-practices

skills/mastra-ai/mastra/tailwind-best-practices
tailwind-best-practices
Installation
$ npx skills add https://github.com/mastra-ai/mastra --skill tailwind-best-practices
SKILL.md
Tailwind Best Practices
Overview

Styling guidelines for the Mastra Playground UI, containing 5 rules across 3 categories. Rules are prioritized by impact to guide automated refactoring and code generation. These rules ensure design system consistency, prevent token drift, and maintain component library integrity.

Scope
packages/playground-ui
packages/playground
When to Apply

Reference these guidelines when:

Writing new React components with Tailwind styles
Reviewing code for styling consistency
Refactoring existing styled components
Adding or modifying UI elements
Priority-Ordered Guidelines

Rules are prioritized by impact:

Priority	Category	Impact
1	Component Usage	CRITICAL
2	Design Tokens	CRITICAL
3	ClassName Usage	HIGH
Quick Reference
Critical Patterns (Apply First)

Component Usage:

Use existing components from @playground-ui/ds/components/ (component-use-existing)
Never create new components in the ds/ folder

Design Tokens:

Only use tokens from tailwind.config.ts in @playground-ui (tokens-use-existing)
Never modify design tokens or tailwind.config.ts (tokens-no-modification)
High-Impact Patterns

ClassName Usage:

No arbitrary Tailwind values except height and width (classname-no-arbitrary)
No className prop on DS components except h-/w- on DialogContent and Popover (classname-no-ds-override)
References

Full documentation with code examples is available in:

references/tailwind-best-practices-reference.md - Complete guide with all patterns
references/rules/ - Individual rule files organized by category

To look up a specific pattern, grep the rules directory:

grep -l "component" references/rules/
grep -l "token" references/rules/
grep -l "className" references/rules/

Rule Categories in references/rules/
component-* - Component usage rules (1 rule)
tokens-* - Design token rules (2 rules)
classname-* - ClassName usage rules (2 rules)
Weekly Installs
906
Repository
mastra-ai/mastra
GitHub Stars
23.5K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass