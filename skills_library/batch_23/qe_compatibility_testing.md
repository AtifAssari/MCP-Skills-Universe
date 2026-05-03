---
title: qe-compatibility-testing
url: https://skills.sh/proffesor-for-testing/agentic-qe/qe-compatibility-testing
---

# qe-compatibility-testing

skills/proffesor-for-testing/agentic-qe/qe-compatibility-testing
qe-compatibility-testing
Installation
$ npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill qe-compatibility-testing
SKILL.md
Compatibility Testing

<default_to_action> When validating cross-browser/platform compatibility:

DEFINE browser matrix (cover 95%+ of users)
TEST responsive breakpoints (mobile, tablet, desktop)
RUN in parallel across browsers/devices
USE cloud services for device coverage (BrowserStack, Sauce Labs)
COMPARE visual screenshots across platforms

Quick Compatibility Checklist:

Chrome, Firefox, Safari, Edge (latest + N-1)
Mobile Safari (iOS), Mobile Chrome (Android)
Screen sizes: 320px, 768px, 1920px
Test on actual target devices for critical flows

Critical Success Factors:

Users access from 100+ browser/device combinations
Test where users are, not where you develop
Cloud testing reduces 10 hours to 15 minutes </default_to_action>
Quick Reference Card
When to Use
Before release
After CSS/layout changes
Launching in new markets
Responsive design validation
Browser Matrix
Browser	Versions	Priority
Chrome	Latest, N-1	High
Firefox	Latest, N-1	High
Safari	Latest, N-1	High
Edge	Latest	Medium
Mobile Safari	iOS latest	High
Mobile Chrome	Android latest	High
Screen Breakpoints
Category	Width Range
Mobile	320px - 480px
Tablet	481px - 768px
Desktop	769px - 1920px+
Responsive Design Testing
import { test, expect } from '@playwright/test';

const devices = [
  { name: 'iPhone 12', width: 390, height: 844 },
  { name: 'iPad', width: 768, height: 1024 },
  { name: 'Desktop', width: 1920, height: 1080 }
];

for (const device of devices) {
  test(`layout on ${device.name}`, async ({ page }) => {
    await page.setViewportSize({
      width: device.width,
      height: device.height
    });

    await page.goto('https://example.com');

    const nav = await page.locator('nav');
    if (device.width < 768) {
      // Mobile: hamburger menu
      expect(await nav.locator('.hamburger')).toBeVisible();
    } else {
      // Desktop: full menu
      expect(await nav.locator('.menu-items')).toBeVisible();
    }
  });
}

Cross-Browser with Playwright
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
    { name: 'webkit', use: { ...devices['Desktop Safari'] } },
    { name: 'mobile-chrome', use: { ...devices['Pixel 5'] } },
    { name: 'mobile-safari', use: { ...devices['iPhone 12'] } }
  ]
});

// Run: npx playwright test --project=chromium --project=firefox

Cloud Testing Integration
// BrowserStack configuration
const capabilities = {
  'browserName': 'Chrome',
  'browser_version': '118.0',
  'os': 'Windows',
  'os_version': '11',
  'browserstack.user': process.env.BROWSERSTACK_USER,
  'browserstack.key': process.env.BROWSERSTACK_KEY
};

// Parallel execution across devices
const deviceMatrix = [
  { os: 'Windows', browser: 'Chrome' },
  { os: 'OS X', browser: 'Safari' },
  { os: 'Android', device: 'Samsung Galaxy S24' },
  { os: 'iOS', device: 'iPhone 15' }
];

Agent-Driven Compatibility Testing
// Cross-platform visual comparison
await Task("Compatibility Testing", {
  url: 'https://example.com',
  browsers: ['chrome', 'firefox', 'safari', 'edge'],
  devices: ['desktop', 'tablet', 'mobile'],
  platform: 'browserstack',
  parallel: true
}, "qe-visual-tester");

// Returns:
// {
//   combinations: 12,  // 4 browsers × 3 devices
//   passed: 11,
//   differences: [{ browser: 'safari', device: 'mobile', diff: 0.02 }]
// }

Agent Coordination Hints
Memory Namespace
aqe/compatibility-testing/
├── browser-matrix/*     - Browser/version configurations
├── device-matrix/*      - Device configurations
├── visual-diffs/*       - Cross-browser visual differences
└── reports/*            - Compatibility reports

Fleet Coordination
const compatFleet = await FleetManager.coordinate({
  strategy: 'compatibility-testing',
  agents: [
    'qe-visual-tester',       // Visual comparison
    'qe-test-executor',       // Cross-browser execution
    'qe-performance-tester'   // Performance by platform
  ],
  topology: 'parallel'
});

Related Skills
mobile-testing - Mobile-specific testing
visual-testing-advanced - Visual regression
accessibility-testing - Cross-platform a11y
Remember

Test where users are, not where you develop. Developers use latest Chrome on high-end machines. Users access from older browsers, low-end devices, and slow networks.

Cover 95%+ of your user base. Use analytics to identify actual browser/device usage. Don't waste time on browsers nobody uses.

With Agents: Agents orchestrate parallel cross-browser testing across cloud platforms, reducing 10 hours of manual testing to 15 minutes. qe-visual-tester catches visual inconsistencies across platforms automatically.

Weekly Installs
45
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