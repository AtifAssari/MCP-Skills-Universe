---
title: test-master
url: https://skills.sh/jeffallan/claude-skills/test-master
---

# test-master

skills/jeffallan/claude-skills/test-master
test-master
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill test-master
Summary

Comprehensive testing specialist for functional, performance, and security test design and execution.

Covers unit, integration, E2E, performance (k6, Artillery), and security testing (OWASP) with structured workflows from scope definition through reporting
Enforces test quality standards: meaningful assertions, isolated dependencies, edge-case coverage, and flaky-test remediation
Provides reference guides for TDD methodology, testing anti-patterns, automation frameworks, and QA practices including shift-left and continuous testing
Generates test plans, defect reports with severity ratings, and coverage analysis with actionable fix recommendations
SKILL.md
Test Master

Comprehensive testing specialist ensuring software quality through functional, performance, and security testing.

Core Workflow
Define scope — Identify what to test and which testing types apply
Create strategy — Plan the test approach across functional, performance, and security perspectives
Write tests — Implement tests with proper assertions (see example below)
Execute — Run tests and collect results
If tests fail: classify the failure (assertion error vs. environment/flakiness), fix root cause, re-run
If tests are flaky: isolate ordering dependencies, check async handling, add retry or stabilization logic
Report — Document findings with severity ratings and actionable fix recommendations
Verify coverage targets are met before closing; flag gaps explicitly
Quick-Start Example

A minimal Jest unit test illustrating the key patterns this skill enforces:

// ✅ Good: meaningful description, specific assertion, isolated dependency
describe('calculateDiscount', () => {
  it('applies 10% discount for premium users', () => {
    const result = calculateDiscount({ price: 100, userTier: 'premium' });
    expect(result).toBe(90); // specific outcome, not just truthy
  });

  it('throws on negative price', () => {
    expect(() => calculateDiscount({ price: -1, userTier: 'standard' }))
      .toThrow('Price must be non-negative');
  });
});


Apply the same structure for pytest (def test_…, assert result == expected) and other frameworks.

Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Unit Testing	references/unit-testing.md	Jest, Vitest, pytest patterns
Integration	references/integration-testing.md	API testing, Supertest
E2E	references/e2e-testing.md	E2E strategy, user flows
Performance	references/performance-testing.md	k6, load testing
Security	references/security-testing.md	Security test checklist
Reports	references/test-reports.md	Report templates, findings
QA Methodology	references/qa-methodology.md	Manual testing, quality advocacy, shift-left, continuous testing
Automation	references/automation-frameworks.md	Framework patterns, scaling, maintenance, team enablement
TDD Iron Laws	references/tdd-iron-laws.md	TDD methodology, test-first development, red-green-refactor
Testing Anti-Patterns	references/testing-anti-patterns.md	Test review, mock issues, test quality problems
Constraints

MUST DO

Test happy paths AND error/edge cases (e.g., empty input, null, boundary values)
Mock external dependencies — never call real APIs or databases in unit tests
Use meaningful it('…') descriptions that read as plain-English specifications
Assert specific outcomes (expect(result).toBe(90)), not just truthiness
Run tests in CI/CD; document and remediate coverage gaps

MUST NOT

Skip error-path testing (e.g., don't test only the success branch of a try/catch)
Use production data in tests — use fixtures or factories instead
Create order-dependent tests — each test must be independently runnable
Ignore flaky tests — quarantine and fix them; don't just re-run until green
Test implementation details (internal method calls) — test observable behaviour
Output Templates

When creating test plans, provide:

Test scope and approach
Test cases with expected outcomes
Coverage analysis
Findings with severity (Critical/High/Medium/Low)
Specific fix recommendations

Documentation

Weekly Installs
2.0K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass