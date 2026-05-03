---
title: visual-regression-testing
url: https://skills.sh/aj-geddes/useful-ai-prompts/visual-regression-testing
---

# visual-regression-testing

skills/aj-geddes/useful-ai-prompts/visual-regression-testing
visual-regression-testing
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill visual-regression-testing
SKILL.md
Visual Regression Testing
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Visual regression testing captures screenshots of UI components and pages, then compares them across versions to detect unintended visual changes. This automated approach catches CSS bugs, layout issues, and design regressions that traditional functional tests miss.

When to Use
Detecting CSS regression bugs
Validating responsive design across viewports
Testing across different browsers
Verifying component visual consistency
Catching layout shifts and overlaps
Testing theme changes
Validating design system components
Reviewing visual changes in PRs
Quick Start

Minimal working example:

// tests/visual/homepage.spec.ts
import { test, expect } from "@playwright/test";

test.describe("Homepage Visual Tests", () => {
  test("homepage matches baseline", async ({ page }) => {
    await page.goto("/");

    // Wait for images to load
    await page.waitForLoadState("networkidle");

    // Full page screenshot
    await expect(page).toHaveScreenshot("homepage-full.png", {
      fullPage: true,
      maxDiffPixels: 100, // Allow small differences
    });
  });

  test("responsive design - mobile", async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 667 }); // iPhone SE
    await page.goto("/");

    await expect(page).toHaveScreenshot("homepage-mobile.png");
  });

  test("responsive design - tablet", async ({ page }) => {
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Playwright Visual Testing	Playwright Visual Testing
Percy Visual Testing	Percy Visual Testing
Chromatic for Storybook	Chromatic for Storybook
Cypress Visual Testing	Cypress Visual Testing
BackstopJS Configuration	BackstopJS Configuration
Handling Dynamic Content	Handling Dynamic Content
Testing Responsive Components	Testing Responsive Components
Best Practices
✅ DO
Hide or mock dynamic content (timestamps, ads)
Test across multiple viewports
Wait for animations and images to load
Use consistent viewport sizes
Disable animations during capture
Test interactive states (hover, focus)
Review diffs carefully before approving
Store baselines in version control
❌ DON'T
Test pages with constantly changing content
Ignore small legitimate differences
Skip responsive testing
Forget to update baselines after design changes
Test pages with random data
Use overly strict thresholds (0% diff)
Skip browser/device variations
Commit unapproved diffs
Weekly Installs
354
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass