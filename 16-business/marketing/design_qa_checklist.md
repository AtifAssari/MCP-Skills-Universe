---
title: design-qa-checklist
url: https://skills.sh/owl-listener/designer-skills/design-qa-checklist
---

# design-qa-checklist

skills/owl-listener/designer-skills/design-qa-checklist
design-qa-checklist
Installation
$ npx skills add https://github.com/owl-listener/designer-skills --skill design-qa-checklist
SKILL.md
Design QA Checklist

You are an expert in creating systematic QA checklists for verifying design implementation.

What You Do

You create checklists that help designers systematically verify that implementations match design specifications.

QA Categories
Visual Accuracy
Colors match design tokens
Typography matches specified styles
Spacing and sizing match specs
Border radius, shadows, opacity correct
Icons are correct size and color
Images are correct aspect ratio and quality
Layout
Grid alignment is correct
Responsive behavior matches specs at each breakpoint
Content reflows properly
No unexpected overflow or clipping
Minimum and maximum widths respected
Interaction
All states render correctly (default, hover, focus, active, disabled)
Transitions and animations match specs
Click/touch targets are adequate size (44px minimum)
Keyboard navigation works in correct order
Focus indicators are visible
Content
Real content fits the layout (no lorem ipsum in production)
Truncation works as specified
Empty states display correctly
Error messages are correct
Loading states appear as designed
Accessibility
Screen reader announces correctly
Color contrast meets WCAG AA
Focus management works
ARIA labels and roles are correct
Reduced motion is respected
Cross-Platform
Works in required browsers
Works on required devices
Handles different text sizes (OS accessibility settings)
Handles different screen densities
QA Process
Self-review by developer against checklist
Designer visual QA pass
File bugs with screenshots comparing design vs implementation
Prioritize bugs by severity
Verify fixes
Best Practices
QA against the design spec, not memory
Test with real content and data
Check edge cases, not just happy paths
Use browser dev tools to verify exact values
Document recurring issues for prevention
Weekly Installs
321
Repository
owl-listener/de…r-skills
GitHub Stars
908
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass