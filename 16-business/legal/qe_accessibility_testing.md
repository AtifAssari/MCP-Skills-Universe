---
rating: ⭐⭐⭐
title: qe-accessibility-testing
url: https://skills.sh/proffesor-for-testing/agentic-qe/qe-accessibility-testing
---

# qe-accessibility-testing

skills/proffesor-for-testing/agentic-qe/qe-accessibility-testing
qe-accessibility-testing
Installation
$ npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill qe-accessibility-testing
SKILL.md
Accessibility Testing

<default_to_action> When testing accessibility or ensuring compliance:

APPLY POUR principles: Perceivable, Operable, Understandable, Robust
TEST with keyboard-only navigation (Tab, Enter, Escape)
VALIDATE with screen readers (VoiceOver, NVDA, JAWS)
CHECK color contrast (4.5:1 for text, 3:1 for large text)
AUTOMATE with axe-core, integrate in CI/CD pipeline

Quick A11y Checklist:

All images have alt text (or alt="" for decorative)
All form fields have labels
Color is never the only indicator
Focus visible on all interactive elements
Keyboard navigation works throughout

Critical Success Factors:

Automated testing catches 30-50% of issues
Manual testing with real assistive tech required
Include users with disabilities in testing </default_to_action>
Quick Reference Card
When to Use
Legal compliance (ADA, Section 508, EU Directive)
New feature development
Before release validation
Accessibility audits
WCAG 2.2 Levels
Level	Requirement	Target
A	Basic accessibility	Minimum legal
AA	Standard (most orgs)	Industry standard
AAA	Enhanced	Specialized sites
POUR Principles
Principle	Meaning	Key Tests
Perceivable	Can perceive content	Alt text, contrast, captions
Operable	Can operate UI	Keyboard, no seizures, navigation
Understandable	Can understand	Clear labels, predictable, errors
Robust	Works with assistive tech	Valid HTML, ARIA
Color Contrast Requirements
Content	AA Ratio	AAA Ratio
Normal text	4.5:1	7:1
Large text (18pt+)	3:1	4.5:1
UI components	3:1	-
Keyboard Navigation Testing
// Test all interactive elements reachable via keyboard
test('all interactive elements keyboard accessible', async ({ page }) => {
  await page.goto('/');

  const focusableElements = await page.$$('button, a, input, select, textarea, [tabindex]');

  for (const element of focusableElements) {
    await element.focus();
    const isFocused = await element.evaluate(el => document.activeElement === el);
    expect(isFocused).toBe(true);
  }
});

// Verify visible focus indicator
test('focus indicator visible', async ({ page }) => {
  await page.goto('/');
  await page.keyboard.press('Tab');

  const focusedElement = await page.locator(':focus');
  const outline = await focusedElement.evaluate(el =>
    getComputedStyle(el).outline
  );

  expect(outline).not.toBe('none');
});

Automated Testing with axe-core
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('page has no accessibility violations', async ({ page }) => {
  await page.goto('/');

  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag22aa'])
    .analyze();

  expect(results.violations).toEqual([]);
});

// CI/CD integration
test('checkout flow accessible', async ({ page }) => {
  await page.goto('/checkout');

  const results = await new AxeBuilder({ page })
    .include('#checkout-form')
    .disableRules(['color-contrast']) // Fix in next sprint
    .analyze();

  expect(results.violations.filter(v =>
    v.impact === 'critical' || v.impact === 'serious'
  )).toHaveLength(0);
});

Screen Reader Testing Checklist
## VoiceOver (macOS) Testing
- [ ] Page title announced on load
- [ ] Headings hierarchy correct (h1 → h2 → h3)
- [ ] Landmarks present (nav, main, footer)
- [ ] Images have descriptive alt text
- [ ] Form labels read correctly
- [ ] Error messages announced
- [ ] Dynamic content updates announced (aria-live)

Agent-Driven Accessibility
// Comprehensive a11y validation
await Task("Accessibility Validation", {
  url: 'https://example.com/checkout',
  standard: 'WCAG2.2',
  level: 'AA',
  checks: ['keyboard', 'screen-reader', 'color-contrast'],
  includeScreenReaderSimulation: true
}, "qe-visual-tester");

// Fleet coordination for comprehensive testing
const a11yFleet = await FleetManager.coordinate({
  strategy: 'comprehensive-accessibility',
  agents: [
    'qe-visual-tester',     // Visual & keyboard checks
    'qe-test-generator',    // Generate a11y tests
    'qe-quality-gate'       // Enforce compliance
  ],
  topology: 'parallel'
});

Agent Coordination Hints
Memory Namespace
aqe/accessibility/
├── wcag-results/*       - WCAG audit results
├── screen-reader/*      - Screen reader test logs
├── remediation/*        - Fix recommendations
└── compliance/*         - Compliance reports

Fleet Coordination
const a11yFleet = await FleetManager.coordinate({
  strategy: 'accessibility-testing',
  agents: [
    'qe-visual-tester',   // axe-core, keyboard, focus
    'qe-test-generator',  // Generate a11y test cases
    'qe-quality-gate'     // Block non-compliant builds
  ],
  topology: 'parallel'
});

Related Skills
visual-testing-advanced - Visual a11y checks
mobile-testing - Mobile a11y (VoiceOver, TalkBack)
compliance-testing - Legal compliance
Remember

1 billion people have disabilities. Inaccessible software excludes 15% of humanity. Legal requirements: ADA, Section 508, EU Directive 2016/2102. $13T purchasing power. 250%+ increase in lawsuits.

Automated testing catches only 30-50% of issues. Combine with manual keyboard testing, screen reader testing, and real user testing with people with disabilities.

With Agents: Agents automate WCAG 2.2 compliance checking, screen reader simulation, and focus management validation. Use agents to enforce accessibility standards in CI/CD and catch violations before production.

Weekly Installs
43
Repository
proffesor-for-t…entic-qe
GitHub Stars
334
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn