---
rating: ⭐⭐
title: normalize
url: https://skills.sh/pbakaus/impeccable/normalize
---

# normalize

skills/pbakaus/impeccable/normalize
normalize
Installation
$ npx skills add https://github.com/pbakaus/impeccable --skill normalize
Summary

Analyze and redesign features to match your design system standards and ensure consistency.

Requires upfront design system discovery—searches for documentation, UI guidelines, and design tokens before making changes; asks clarifying questions rather than guessing at principles
Systematically normalizes typography, color, spacing, components, motion, responsive behavior, and accessibility across eight key dimensions
Prioritizes UX consistency and usability over visual polish; replaces custom implementations with design system equivalents and removes hard-coded values in favor of design tokens
Includes cleanup phase to consolidate reusable components, remove orphaned code, and verify quality against repository standards
SKILL.md

Analyze and redesign the feature to perfectly match our design system standards, aesthetics, and established patterns.

MANDATORY PREPARATION

Invoke /impeccable — it contains design principles, anti-patterns, and the Context Gathering Protocol. Follow the protocol before proceeding — if no design context exists yet, you MUST run /impeccable teach first.

Plan

Before making changes, deeply understand the context:

Discover the design system: Search for design system documentation, UI guidelines, component libraries, or style guides (grep for "design system", "ui guide", "style guide", etc.). Study it thoroughly until you understand:

Core design principles and aesthetic direction
Target audience and personas
Component patterns and conventions
Design tokens (colors, typography, spacing)

CRITICAL: If something isn't clear, ask. Don't guess at design system principles.

Analyze the current feature: Assess what works and what doesn't:

Where does it deviate from design system patterns?
Which inconsistencies are cosmetic vs. functional?
What's the root cause—missing tokens, one-off implementations, or conceptual misalignment?

Create a normalization plan: Define specific changes that will align the feature with the design system:

Which components can be replaced with design system equivalents?
Which styles need to use design tokens instead of hard-coded values?
How can UX patterns match established user flows?

IMPORTANT: Great design is effective design. Prioritize UX consistency and usability over visual polish alone. Think through the best possible experience for your use case and personas first.

Execute

Systematically address all inconsistencies across these dimensions:

Typography: Use design system fonts, sizes, weights, and line heights. Replace hard-coded values with typographic tokens or classes.
Color & Theme: Apply design system color tokens. Remove one-off color choices that break the palette.
Spacing & Layout: Use spacing tokens (margins, padding, gaps). Align with grid systems and layout patterns used elsewhere.
Components: Replace custom implementations with design system components. Ensure props and variants match established patterns.
Motion & Interaction: Match animation timing, easing, and interaction patterns to other features.
Responsive Behavior: Ensure breakpoints and responsive patterns align with design system standards.
Accessibility: Verify contrast ratios, focus states, ARIA labels match design system requirements.
Progressive Disclosure: Match information hierarchy and complexity management to established patterns.

NEVER:

Create new one-off components when design system equivalents exist
Hard-code values that should use design tokens
Introduce new patterns that diverge from the design system
Compromise accessibility for visual consistency

This is not an exhaustive list—apply judgment to identify all areas needing normalization.

Clean Up

After normalization, ensure code quality:

Consolidate reusable components: If you created new components that should be shared, move them to the design system or shared UI component path.
Remove orphaned code: Delete unused implementations, styles, or files made obsolete by normalization.
Verify quality: Lint, type-check, and test according to repository guidelines. Ensure normalization didn't introduce regressions.
Ensure DRYness: Look for duplication introduced during refactoring and consolidate.

Remember: You are a brilliant frontend designer with impeccable taste, equally strong in UX and UI. Your attention to detail and eye for end-to-end user experience is world class. Execute with precision and thoroughness.

Weekly Installs
54.6K
Repository
pbakaus/impeccable
GitHub Stars
24.2K
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass