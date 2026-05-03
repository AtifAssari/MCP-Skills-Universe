---
rating: ⭐⭐
title: agent-capabilities
url: https://skills.sh/jgtolentino/insightpulse-odoo/agent-capabilities
---

# agent-capabilities

skills/jgtolentino/insightpulse-odoo/agent-capabilities
agent-capabilities
Installation
$ npx skills add https://github.com/jgtolentino/insightpulse-odoo --skill agent-capabilities
SKILL.md
Agent Capabilities - Visual Regression Testing

This document outlines Claude's comprehensive capabilities for implementing and managing visual regression testing infrastructure in web applications.

Core Competencies
1. Visual Regression Testing Infrastructure

Claude can set up complete visual regression testing infrastructure following industry best practices from Ant Design, Argos CI, and other leading organizations.

Capabilities:

✅ Configure Playwright for visual testing
✅ Implement jest-image-snapshot for pixel-perfect comparison
✅ Create baseline screenshot management system
✅ Generate visual diff reports with HTML/Markdown output
✅ Set up multi-viewport and multi-browser testing
✅ Configure threshold-based comparison with anti-aliasing detection

Implementation Reference:

Skill: .claude/skills/visual-regression-testing/SKILL.md
Test utilities: tests/shared/imageTest.tsx
Scripts: scripts/visual-regression/
2. CI/CD Integration

Claude can integrate visual regression testing into GitHub Actions workflows with automated PR checks, baseline updates, and artifact management.

Capabilities:

✅ Create PR check workflows that fail on visual regression
✅ Automate baseline updates on main branch merges
✅ Generate and upload visual diff artifacts
✅ Post PR comments with visual comparison previews
✅ Configure parallel test execution for performance
✅ Set up report generation and distribution

Implementation Reference:

PR workflow: .github/workflows/visual-regression-pr.yml
Baseline workflow: .github/workflows/visual-regression-baseline.yml
Report workflow: .github/workflows/visual-regression-report.yml
3. Screenshot Management

Claude can implement sophisticated screenshot capture and management systems with support for dynamic content masking, animation freezing, and viewport control.

Capabilities:

✅ Capture full-page and element-specific screenshots
✅ Auto-hide timestamps, dates, and other dynamic content
✅ Freeze animations and transitions for consistency
✅ Handle responsive design across multiple viewports
✅ Support theme variants (light/dark mode)
✅ Organize screenshots with semantic naming

Implementation Reference:

Baseline capture: scripts/visual-regression/capture-baselines.ts
Test utilities: tests/shared/imageTest.tsx:45-100
4. Comparison and Reporting

Claude can implement pixel-perfect comparison with configurable thresholds and generate comprehensive visual diff reports.

Capabilities:

✅ Pixel-by-pixel comparison using pixelmatch
✅ Configurable difference thresholds (0.01% to 5%)
✅ Anti-aliasing detection to reduce false positives
✅ Generate HTML reports with side-by-side comparisons
✅ Create Markdown reports for GitHub PR comments
✅ Track regression history and trends

Implementation Reference:

Comparison: scripts/visual-regression/compare-screenshots.ts
HTML report: scripts/visual-regression/generate-report.js
5. Cloud Storage Integration

Claude can integrate visual regression artifacts with cloud storage providers for long-term archival and sharing.

Capabilities:

✅ Upload to AWS S3, Azure Blob Storage, or Alibaba OSS
✅ Generate public URLs for artifact sharing
✅ Implement retention policies
✅ Configure CDN distribution
✅ Support local storage for development

Implementation Reference:

Upload utility: scripts/visual-regression/upload-to-storage.ts
Workflow Patterns
Pattern 1: Initial Setup

When a user requests visual regression testing setup, Claude will:

Create directory structure:

tests/shared/imageTest.tsx
scripts/visual-regression/
.github/workflows/visual-regression-*.yml
__image_snapshots__/baseline/


Install dependencies:

{
  "devDependencies": {
    "@playwright/test": "^1.40.0",
    "playwright": "^1.40.0",
    "jest-image-snapshot": "^6.2.0",
    "pixelmatch": "^5.3.0",
    "pngjs": "^7.0.0"
  }
}


Add npm scripts:

{
  "scripts": {
    "visual:test": "playwright test",
    "visual:baseline": "GENERATE_BASELINE=true playwright test --grep @baseline",
    "visual:update-baseline": "npm run visual:baseline",
    "visual:compare": "node scripts/visual-regression/compare-screenshots.ts",
    "visual:report": "node scripts/visual-regression/generate-report.js",
    "visual:upload": "node scripts/visual-regression/upload-to-storage.ts"
  }
}


Configure Playwright:

// playwright.config.ts
export default {
  testDir: './tests',
  use: {
    baseURL: 'http://localhost:5173',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
  ],
};

Pattern 2: Component Testing

When adding visual tests for a new component:

Create test file:

import { test } from '@playwright/test';
import { runVisualTest, VIEWPORTS } from '../shared/imageTest';

test('button component - all variants', async ({ page }) => {
  await runVisualTest(page, {
    identifier: 'button-variants',
    url: '/components/button',
    viewport: VIEWPORTS.desktop,
    threshold: 0.05,
  });
});


Generate baseline:

npm run visual:baseline


Run in CI:

Automatically runs on PR creation
Fails if visual differences detected
Posts diff images in PR comment
Pattern 3: Baseline Updates

When intentional visual changes are made:

Review diff report:

Check CI artifacts
Download visual-report.html
Verify changes are intentional

Update baselines:

npm run visual:update-baseline
git add __image_snapshots__/baseline/
git commit -m "chore: update visual baselines for button redesign"


Push and re-test:

CI re-runs tests
Passes with updated baselines
Pattern 4: Troubleshooting

When visual tests fail unexpectedly:

Check for environmental differences:

Font rendering (use Docker)
Browser version (pin in CI)
OS differences (test on same platform as CI)

Adjust thresholds if needed:

threshold: 0.1, // Increase from 0.05 to 0.1


Mask dynamic content:

hideSelectors: [
  '[data-testid="timestamp"]',
  '.loading-spinner',
],

Best Practices
1. What to Test

✅ Do test:

Critical user-facing components
Layout and responsive behavior
Theme variations (light/dark)
Multi-viewport rendering
Component state variants

❌ Don't test:

Frequently changing content (news feeds, timestamps)
Random/dynamic data displays
Third-party embedded content
Loading states with spinners
2. Threshold Configuration
// Critical UI - strict comparison
threshold: 0.01  // 0.01% = ~10 pixels in 100k

// Standard components
threshold: 0.1   // 0.1% = ~100 pixels in 100k

// Charts/graphs with anti-aliasing
threshold: 0.5   // 0.5% = ~500 pixels in 100k

3. Performance Optimization
Run tests in parallel across workers
Use headless mode in CI
Cache Playwright browsers
Selectively test affected components
Reuse unchanged baselines
4. False Positive Reduction
Freeze animations with CSS
Use consistent environment (Docker)
Pin browser versions
Mask timestamps and dynamic content
Enable anti-aliasing detection
Integration with Existing Tools

Visual regression testing integrates with:

Webapp Testing Skill
Uses webapp-testing skill for Playwright setup
Leverages scripts/with_server.py for server management
Follows reconnaissance-then-action pattern

Reference: .claude/skills/webapp-testing/SKILL.md

CI/CD Pipelines
Runs after unit/component tests pass
Blocks merges on visual regression
Uploads artifacts to GitHub Actions
Posts results in PR comments

Reference: .github/workflows/visual-regression-pr.yml:1

Odoo Development
Can test Odoo web interface components
Supports multi-theme testing
Validates responsive layouts
Tests module-specific UI changes
Real-World Examples
Example 1: Homepage Visual Test
import { test } from '@playwright/test';
import { runVisualTest, VIEWPORTS } from '../shared/imageTest';

test('homepage - responsive design', async ({ page }) => {
  for (const [name, viewport] of Object.entries(VIEWPORTS)) {
    await runVisualTest(page, {
      identifier: `homepage-${name}`,
      url: '/',
      viewport,
      fullPage: true,
      threshold: 0.1,
    });
  }
});

Example 2: Component Library Test
test('design system - all components', async ({ page }) => {
  const components = ['button', 'input', 'select', 'modal', 'table'];

  for (const component of components) {
    await runVisualTest(page, {
      identifier: `component-${component}`,
      url: `/components/${component}`,
      selector: `[data-testid="${component}-showcase"]`,
      threshold: 0.05,
    });
  }
});

Example 3: Theme Switching Test
test('dark mode - all pages', async ({ page }) => {
  const pages = ['/', '/about', '/contact'];

  for (const pagePath of pages) {
    // Test light mode
    await runVisualTest(page, {
      identifier: `${pagePath.replace(/\//g, '-')}-light`,
      url: pagePath,
      fullPage: true,
    });

    // Switch to dark mode
    await page.evaluate(() => {
      document.documentElement.setAttribute('data-theme', 'dark');
    });

    // Test dark mode
    await runVisualTest(page, {
      identifier: `${pagePath.replace(/\//g, '-')}-dark`,
      url: pagePath,
      fullPage: true,
    });
  }
});

Learning Resources
Official Documentation
Ant Design Visual Regression
Playwright Screenshots
jest-image-snapshot
Industry Tools
Argos CI - Visual testing platform
Percy - Visual review platform
Chromatic - Storybook visual testing
Implementation References

All code is available in this repository:

.claude/skills/visual-regression-testing/SKILL.md - Full skill documentation
.github/workflows/visual-regression-*.yml - CI/CD workflows
tests/shared/imageTest.tsx - Test utilities
scripts/visual-regression/ - Implementation scripts
When to Use This Capability

Claude should proactively offer visual regression testing when:

User mentions visual testing or regression

"I need to test UI changes"
"How can I prevent visual bugs?"
"Set up screenshot testing"

Component development context

Building design systems
Creating component libraries
Implementing responsive layouts

CI/CD enhancement requests

"Improve our testing pipeline"
"Add automated UI checks"
"Prevent visual bugs in PRs"

Debugging visual issues

"Something looks different but I can't tell what"
"UI broke on mobile but works on desktop"
"Theme switching has issues"
Agent Decision Tree
User request → Contains visual/UI/screenshot keywords?
  ├─ Yes → Offer visual regression testing setup
  │   ├─ Already has visual tests? → Enhance/extend
  │   └─ No visual tests? → Full setup
  │
  └─ No → Monitor for component development
      └─ Creating UI components? → Suggest visual testing

Summary

Claude has comprehensive capabilities for implementing production-grade visual regression testing infrastructure. This includes:

✅ Complete Playwright + jest-image-snapshot setup
✅ GitHub Actions CI/CD integration
✅ Automated baseline management
✅ Visual diff reporting with HTML/Markdown
✅ Multi-viewport and multi-browser support
✅ Cloud storage integration for artifacts
✅ Best practices from industry leaders (Ant Design, Argos)

All implementations follow proven patterns from leading design systems and are production-ready for immediate use.

Last Updated: 2025-11-13 Methodology Source: Ant Design Visual Regression Testing Implementation Status: ✅ Complete and production-ready

Weekly Installs
55
Repository
jgtolentino/ins…lse-odoo
GitHub Stars
20
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass