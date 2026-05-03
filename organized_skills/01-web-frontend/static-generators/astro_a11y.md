---
rating: ⭐⭐
title: astro-a11y
url: https://skills.sh/soborbo/claudeskills/astro-a11y
---

# astro-a11y

skills/soborbo/claudeskills/astro-a11y
astro-a11y
Installation
$ npx skills add https://github.com/soborbo/claudeskills --skill astro-a11y
SKILL.md
Astro Accessibility Skill
Purpose

Ensures WCAG 2.1 AA compliance for lead generation websites. Legal requirement under UK Equality Act 2010. Provides essential patterns for keyboard navigation, screen readers, focus management, and ARIA implementation.

Core Rules
Keyboard navigable — All interactive elements reachable via Tab
Screen reader friendly — Semantic HTML, proper ARIA
Visible focus — Clear focus indicators on all elements
Sufficient contrast — 4.5:1 text, 3:1 UI components
No motion harm — Respect prefers-reduced-motion
Semantic HTML first — Use native elements before ARIA
Labels required — Every form input must have a label
Alternative text — All images need appropriate alt text
Buttons vs Links
Element	Use For
<button>	Actions (submit, toggle, open modal)
<a href>	Navigation (go to page, section)
Color Contrast Requirements
Element	Minimum Ratio
Body text	4.5:1
Large text (18px+ or 14px bold)	3:1
UI components	3:1
Disabled elements	No requirement
Testing Tools
Chrome DevTools → Rendering → Emulate vision deficiencies
axe DevTools extension
WAVE extension
Screen readers: NVDA (Windows), VoiceOver (Mac), JAWS
References
Semantic HTML Patterns
Focus Management — Skip links, focus traps, focus visible styles
ARIA Patterns — Live regions, mobile menus
Form Accessibility — Labels, error messages, required fields
Image Accessibility — Alt text patterns
Motion & Animation — Reduced motion support
Screen Reader Only Utility — SR-only CSS class
Testing Checklist
Keyboard
 Tab through entire page — logical order?
 All interactive elements reachable?
 Focus visible on every element?
 Can escape modals with Escape key?
 Skip link works?
Screen Reader
 Page title announced?
 Headings hierarchy correct?
 Images have alt text?
 Form labels announced?
 Errors announced (aria-live)?
Visual
 Contrast passes (4.5:1)?
 Text resizes to 200% without breaking?
 Works without color alone?
 Reduced motion respected?
Forbidden
❌ <div> or <span> for interactive elements
❌ outline: none without replacement focus style
❌ tabindex greater than 0
❌ Missing form labels
❌ Color as only indicator
❌ Auto-playing video/audio
❌ CAPTCHA without alternative
Definition of Done
 Skip link present on page
 All forms have proper labels
 Contrast ratios pass WCAG AA
 Keyboard navigation works completely
 axe DevTools shows 0 errors
 Screen reader test passed
 Reduced motion media query implemented
 All images have appropriate alt text
Weekly Installs
14
Repository
soborbo/claudeskills
GitHub Stars
2
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass