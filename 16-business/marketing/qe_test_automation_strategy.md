---
title: qe-test-automation-strategy
url: https://skills.sh/proffesor-for-testing/agentic-qe/qe-test-automation-strategy
---

# qe-test-automation-strategy

skills/proffesor-for-testing/agentic-qe/qe-test-automation-strategy
qe-test-automation-strategy
Installation
$ npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill qe-test-automation-strategy
SKILL.md
Test Automation Strategy

<default_to_action> When designing or improving test automation:

FOLLOW test pyramid: 70% unit, 20% integration, 10% E2E
APPLY F.I.R.S.T. principles: Fast, Isolated, Repeatable, Self-validating, Timely
USE patterns: Page Object Model, Builder pattern, Factory pattern
INTEGRATE in CI/CD: Every commit runs tests, fail fast, clear feedback
MANAGE flaky tests: Quarantine, fix, or delete - never ignore

Quick Anti-Pattern Detection:

Ice cream cone (many E2E, few unit) → Invert to pyramid
Slow tests (> 10 min suite) → Parallelize, mock external deps
Flaky tests → Fix timing, isolate data, or quarantine
Test duplication → Share fixtures, use page objects
Brittle selectors → Use data-testid, semantic locators

Critical Success Factors:

Fast feedback is the goal (< 10 min full suite)
Automation supports testing, doesn't replace judgment
Invest in test infrastructure like production code </default_to_action>
Quick Reference Card
When to Use
Building new automation framework
Improving existing test efficiency
Reducing flaky test burden
Optimizing CI/CD pipeline speed
Test Pyramid
Layer	%	Speed	Isolation	Examples
Unit	70%	< 1ms	Complete	Pure functions, logic
Integration	20%	< 1s	Partial	API, database
E2E	10%	< 30s	None	User journeys
F.I.R.S.T. Principles
Principle	Meaning	How
Fast	Quick execution	Mock external deps
Isolated	No shared state	Fresh fixtures per test
Repeatable	Same result every time	No random data
Self-validating	Clear pass/fail	Assert, don't print
Timely	Written with code	TDD, not after
Anti-Patterns
Problem	Symptom	Fix
Ice cream cone	80% E2E, 10% unit	Invert pyramid
Slow suite	30+ min CI	Parallelize, prune
Flaky tests	Random failures	Quarantine, fix timing
Coupled tests	Order-dependent	Isolate data
Brittle selectors	Break on CSS change	Use data-testid
Page Object Model
// pages/LoginPage.js
class LoginPage {
  constructor(page) {
    this.page = page;
    this.emailInput = '[data-testid="email"]';
    this.passwordInput = '[data-testid="password"]';
    this.submitButton = '[data-testid="submit"]';
    this.errorMessage = '[data-testid="error"]';
  }

  async login(email, password) {
    await this.page.fill(this.emailInput, email);
    await this.page.fill(this.passwordInput, password);
    await this.page.click(this.submitButton);
  }

  async getError() {
    return this.page.textContent(this.errorMessage);
  }
}

// Test uses page object
test('shows error for invalid credentials', async ({ page }) => {
  const loginPage = new LoginPage(page);
  await loginPage.login('bad@email.com', 'wrong');
  expect(await loginPage.getError()).toBe('Invalid credentials');
});

CI/CD Integration
name: Test Pipeline
on: [push, pull_request]

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run test:unit -- --coverage
        timeout-minutes: 5
      - uses: codecov/codecov-action@v3

  integration-tests:
    needs: unit-tests
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
    steps:
      - run: npm run test:integration
        timeout-minutes: 10

  e2e-tests:
    needs: integration-tests
    runs-on: ubuntu-latest
    steps:
      - run: npx playwright test
        timeout-minutes: 15

Flaky Test Management
// Quarantine flaky tests
describe.skip('Quarantined - INC-123', () => {
  test('flaky test awaiting fix', () => { /* ... */ });
});

// Agent-assisted stabilization
await Task("Fix Flaky Tests", {
  tests: quarantinedTests,
  analysis: ['timing-issues', 'data-isolation', 'race-conditions'],
  strategies: ['add-waits', 'isolate-fixtures', 'mock-externals']
}, "qe-flaky-test-hunter");

Agent-Assisted Automation
// Generate tests following pyramid
await Task("Generate Test Suite", {
  sourceCode: 'src/',
  pyramid: { unit: 70, integration: 20, e2e: 10 },
  patterns: ['page-object', 'builder', 'factory'],
  framework: 'jest'
}, "qe-test-generator");

// Optimize test execution
await Task("Optimize Suite", {
  algorithm: 'johnson-lindenstrauss',
  targetReduction: 0.3,
  maintainCoverage: 0.95
}, "qe-regression-risk-analyzer");

// Analyze flaky patterns
await Task("Flaky Analysis", {
  testHistory: 'last-30-days',
  detectPatterns: ['timing', 'data', 'environment'],
  recommend: 'stabilization-strategy'
}, "qe-flaky-test-hunter");

Agent Coordination Hints
Memory Namespace
aqe/automation/
├── test-pyramid/*        - Coverage by layer
├── page-objects/*        - Shared page objects
├── flaky-registry/*      - Quarantined tests
└── execution-metrics/*   - Suite performance data

Fleet Coordination
const automationFleet = await FleetManager.coordinate({
  strategy: 'test-automation',
  agents: [
    'qe-test-generator',         // Generate pyramid-compliant tests
    'qe-test-executor',          // Parallel execution
    'qe-coverage-analyzer',      // Coverage gaps
    'qe-flaky-test-hunter',      // Flaky detection
    'qe-regression-risk-analyzer' // Smart selection
  ],
  topology: 'hierarchical'
});

Related Skills
tdd-london-chicago - TDD for unit tests
api-testing-patterns - Integration patterns
cicd-pipeline-qe-orchestrator - Pipeline integration
shift-left-testing - Early automation
Remember

Pyramid: 70% unit, 20% integration, 10% E2E. F.I.R.S.T. principles for every test. Page Object Model for E2E. Parallelize for speed. Quarantine flaky tests - never ignore them. Treat test code like production code.

With Agents: Agents generate pyramid-compliant tests, detect flaky patterns, optimize execution time, and maintain test infrastructure. Use agents to scale automation quality.

Weekly Installs
42
Repository
proffesor-for-t…entic-qe
GitHub Stars
334
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass