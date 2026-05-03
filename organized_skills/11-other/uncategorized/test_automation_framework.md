---
rating: ⭐⭐
title: test-automation-framework
url: https://skills.sh/aj-geddes/useful-ai-prompts/test-automation-framework
---

# test-automation-framework

skills/aj-geddes/useful-ai-prompts/test-automation-framework
test-automation-framework
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill test-automation-framework
SKILL.md
Test Automation Framework
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

A test automation framework provides structure, reusability, and maintainability for automated tests. It defines patterns for organizing tests, managing test data, handling dependencies, and generating reports. A well-designed framework reduces duplication, improves reliability, and accelerates test development.

When to Use
Setting up new test automation
Scaling existing test suites
Standardizing test practices across teams
Reducing test maintenance burden
Improving test reliability and speed
Organizing large test codebases
Implementing reusable test utilities
Creating consistent reporting
Quick Start

Minimal working example:

// framework/pages/BasePage.ts
import { Page, Locator } from "@playwright/test";

export abstract class BasePage {
  constructor(protected page: Page) {}

  async goto(path: string) {
    await this.page.goto(path);
  }

  async waitForPageLoad() {
    await this.page.waitForLoadState("networkidle");
  }

  async takeScreenshot(name: string) {
    await this.page.screenshot({ path: `screenshots/${name}.png` });
  }

  protected async clickAndWait(locator: Locator) {
    await Promise.all([
      this.page.waitForResponse((resp) => resp.status() === 200),
      locator.click(),
    ]);
  }
}
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Page Object Model (Playwright/TypeScript)	Page Object Model (Playwright/TypeScript)
Test Fixtures and Factories	Test Fixtures and Factories
Custom Test Utilities	Custom Test Utilities
Configuration Management	Configuration Management
Custom Reporter	Custom Reporter
pytest Framework (Python)	pytest Framework (Python)
Test Organization	Test Organization
Best Practices
✅ DO
Use Page Object Model for UI tests
Create reusable test utilities
Implement proper wait strategies
Use fixtures for test data
Configure for multiple environments
Generate readable test reports
Organize tests by feature/type
Version control test framework
❌ DON'T
Put test logic in page objects
Use hard-coded waits (sleep)
Duplicate test setup code
Mix test data with test logic
Skip error handling
Ignore test flakiness
Create overly complex abstractions
Hardcode environment URLs
Weekly Installs
300
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