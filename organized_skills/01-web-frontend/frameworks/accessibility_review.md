---
rating: ⭐⭐⭐
title: accessibility-review
url: https://skills.sh/anthropics/knowledge-work-plugins/accessibility-review
---

# accessibility-review

skills/anthropics/knowledge-work-plugins/accessibility-review
accessibility-review
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill accessibility-review
SKILL.md
/accessibility-review

If you see unfamiliar placeholders or need to check which tools are connected, see CONNECTORS.md.

Audit a design or page for WCAG 2.1 AA accessibility compliance.

Usage
/accessibility-review $ARGUMENTS


Audit for accessibility: @$1

WCAG 2.1 AA Quick Reference
Perceivable
1.1.1 Non-text content has alt text
1.3.1 Info and structure conveyed semantically
1.4.3 Contrast ratio >= 4.5:1 (normal text), >= 3:1 (large text)
1.4.11 Non-text contrast >= 3:1 (UI components, graphics)
Operable
2.1.1 All functionality available via keyboard
2.4.3 Logical focus order
2.4.7 Visible focus indicator
2.5.5 Touch target >= 44x44 CSS pixels
Understandable
3.2.1 Predictable on focus (no unexpected changes)
3.3.1 Error identification (describe the error)
3.3.2 Labels or instructions for inputs
Robust
4.1.2 Name, role, value for all UI components
Common Issues
Insufficient color contrast
Missing form labels
No keyboard access to interactive elements
Missing alt text on meaningful images
Focus traps in modals
Missing ARIA landmarks
Auto-playing media without controls
Time limits without extension options
Testing Approach
Automated scan (catches ~30% of issues)
Keyboard-only navigation
Screen reader testing (VoiceOver, NVDA)
Color contrast verification
Zoom to 200% — does layout break?
Output
## Accessibility Audit: [Design/Page Name]
**Standard:** WCAG 2.1 AA | **Date:** [Date]

### Summary
**Issues found:** [X] | **Critical:** [X] | **Major:** [X] | **Minor:** [X]

### Findings

#### Perceivable
| # | Issue | WCAG Criterion | Severity | Recommendation |
|---|-------|---------------|----------|----------------|
| 1 | [Issue] | [1.4.3 Contrast] | 🔴 Critical | [Fix] |

#### Operable
| # | Issue | WCAG Criterion | Severity | Recommendation |
|---|-------|---------------|----------|----------------|
| 1 | [Issue] | [2.1.1 Keyboard] | 🟡 Major | [Fix] |

#### Understandable
| # | Issue | WCAG Criterion | Severity | Recommendation |
|---|-------|---------------|----------|----------------|
| 1 | [Issue] | [3.3.2 Labels] | 🟢 Minor | [Fix] |

#### Robust
| # | Issue | WCAG Criterion | Severity | Recommendation |
|---|-------|---------------|----------|----------------|
| 1 | [Issue] | [4.1.2 Name, Role, Value] | 🟡 Major | [Fix] |

### Color Contrast Check
| Element | Foreground | Background | Ratio | Required | Pass? |
|---------|-----------|------------|-------|----------|-------|
| [Body text] | [color] | [color] | [X]:1 | 4.5:1 | ✅/❌ |

### Keyboard Navigation
| Element | Tab Order | Enter/Space | Escape | Arrow Keys |
|---------|-----------|-------------|--------|------------|
| [Element] | [Order] | [Behavior] | [Behavior] | [Behavior] |

### Screen Reader
| Element | Announced As | Issue |
|---------|-------------|-------|
| [Element] | [What SR says] | [Problem if any] |

### Priority Fixes
1. **[Critical fix]** — Affects [who] and blocks [what]
2. **[Major fix]** — Improves [what] for [who]
3. **[Minor fix]** — Nice to have

If Connectors Available

If ~~design tool is connected:

Inspect color values, font sizes, and touch targets directly from Figma
Check component ARIA roles and keyboard behavior in the design spec

If ~~project tracker is connected:

Create tickets for each accessibility finding with severity and WCAG criterion
Link findings to existing accessibility remediation epics
Tips
Start with contrast and keyboard — These catch the most common and impactful issues.
Test with real assistive technology — My audit is a great start, but manual testing with VoiceOver/NVDA catches things I can't.
Prioritize by impact — Fix issues that block users first, polish later.
Weekly Installs
1.1K
Repository
anthropics/know…-plugins
GitHub Stars
11.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass