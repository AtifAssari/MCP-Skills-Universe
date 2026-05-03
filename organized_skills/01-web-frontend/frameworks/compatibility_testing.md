---
rating: ⭐⭐⭐
title: compatibility-testing
url: https://skills.sh/proffesor-for-testing/agentic-qe/compatibility-testing
---

# compatibility-testing

skills/proffesor-for-testing/agentic-qe/compatibility-testing
compatibility-testing
Installation
$ npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill compatibility-testing
SKILL.md
Compatibility Testing
Browser engine

Browser-driven checks (viewport emulation, responsive validation, cross-browser screenshots) should go through the qe-browser fleet skill (.claude/skills/qe-browser/). Vibium is installed by aqe init. Quick reference:

# Viewport emulation per breakpoint
vibium viewport 375 667   # mobile
vibium viewport 768 1024  # tablet
vibium viewport 1920 1080 # desktop

# Full device emulation (user-agent, DPR, touch)
vibium emulate-device "iPhone 15"

# Visual diff per viewport
for vp in "375 667 mobile" "768 1024 tablet" "1920 1080 desktop"; do
  read w h name <<< "$vp"
  vibium viewport $w $h
  node .claude/skills/qe-browser/scripts/visual-diff.js --name "homepage-$name"
done


Cross-browser (Firefox/Safari) still requires Playwright or a cloud device farm today — Vibium's BiDi backend is Chrome-only at v26.3.x.

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

Cover 95%+ of your user base. Use analytics to identify actual browser/device usage. Don't waste time on browsers nobody uses.

With Agents: Agents orchestrate parallel cross-browser testing across cloud platforms. qe-visual-tester catches visual inconsistencies across platforms automatically.

Weekly Installs
351
Repository
proffesor-for-t…entic-qe
GitHub Stars
334
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn