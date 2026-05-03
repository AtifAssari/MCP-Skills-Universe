---
rating: ⭐⭐
title: ui-a11y
url: https://skills.sh/sickn33/antigravity-awesome-skills/ui-a11y
---

# ui-a11y

skills/sickn33/antigravity-awesome-skills/ui-a11y
ui-a11y
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill ui-a11y
SKILL.md
UI Accessibility Audit
Overview

Part of StyleSeed, this skill audits components and pages for accessibility issues with an emphasis on the Toss seed's mobile UI patterns. It combines WCAG 2.2 AA checks with practical code fixes for touch targets, focus states, contrast, labels, and reduced motion.

When to Use
Use when reviewing a page or component for accessibility regressions
Use when a StyleSeed UI looks polished but has uncertain keyboard or contrast behavior
Use when adding new interactive controls to a mobile-first screen
Use when you want a prioritized list of issues and fixable items
Audit Areas
Perceivable
text contrast
non-text contrast for controls and graphics
alt text for images
labels for meaningful icons
no information conveyed by color alone
Operable
touch targets at least 44x44px
keyboard reachability for all interactive controls
logical tab order
visible focus indicators
reduced-motion support for nonessential animation
Understandable
visible labels or aria-label on inputs
error text associated with the correct field
clear wording for errors and validation
document language set appropriately
Robust
semantic HTML where possible
correct use of ARIA when semantics alone are insufficient
no faux buttons or links without the right roles and behavior
Output

Return:

Issues found, grouped by severity
Safe autofixes that can be applied directly
Items that need manual review or product judgment
A short summary of the accessibility risk level
Best Practices
Fix semantics before layering on ARIA
Use the design system tokens only if they still meet contrast requirements
Treat touch target failures as real usability defects, not polish issues
Prefer partial, verified fixes over speculative accessibility changes
Additional Resources
StyleSeed repository
Source skill
Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
10
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass