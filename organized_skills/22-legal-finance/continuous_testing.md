---
rating: ⭐⭐⭐
title: continuous-testing
url: https://skills.sh/aj-geddes/useful-ai-prompts/continuous-testing
---

# continuous-testing

skills/aj-geddes/useful-ai-prompts/continuous-testing
continuous-testing
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill continuous-testing
SKILL.md
Continuous Testing
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Continuous testing integrates automated testing throughout the software development lifecycle, providing rapid feedback on quality at every stage. It shifts testing left in the development process and ensures that code changes are validated automatically before reaching production.

When to Use
Setting up CI/CD pipelines
Automating test execution on commits
Implementing shift-left testing
Running tests in parallel
Creating test gates for deployments
Monitoring test health
Optimizing test execution time
Establishing quality gates
Quick Start

Minimal working example:

# .github/workflows/ci.yml
name: Continuous Testing

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

env:
  NODE_VERSION: "18"

jobs:
  # Unit tests - Fast feedback
  unit-tests:
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: ${{ env.NODE_VERSION }}
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
GitHub Actions CI Pipeline	GitHub Actions CI Pipeline
GitLab CI Pipeline	GitLab CI Pipeline
Jenkins Pipeline	Jenkins Pipeline
Test Selection Strategy	Test Selection Strategy
Flaky Test Detection	Flaky Test Detection
Test Metrics Dashboard	Test Metrics Dashboard
Best Practices
✅ DO
Run fast tests first (unit → integration → E2E)
Parallelize test execution
Cache dependencies
Set appropriate timeouts
Monitor test health and flakiness
Implement quality gates
Use test selection strategies
Generate comprehensive reports
❌ DON'T
Run all tests sequentially
Ignore flaky tests
Skip test maintenance
Allow tests to depend on each other
Run slow tests on every commit
Deploy with failing tests
Ignore test execution time
Skip security scanning
Weekly Installs
272
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail