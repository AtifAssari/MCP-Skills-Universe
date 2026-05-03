---
title: tdd-guide
url: https://skills.sh/aaaaqwq/claude-code-skills/tdd-guide
---

# tdd-guide

skills/aaaaqwq/claude-code-skills/tdd-guide
tdd-guide
Installation
$ npx skills add https://github.com/aaaaqwq/claude-code-skills --skill tdd-guide
SKILL.md
TDD Guide

Test-driven development skill for generating tests, analyzing coverage, and guiding red-green-refactor workflows across Jest, Pytest, JUnit, and Vitest.

Table of Contents
Capabilities
Workflows
Tools
Input Requirements
Limitations
Capabilities
Capability	Description
Test Generation	Convert requirements or code into test cases with proper structure
Coverage Analysis	Parse LCOV/JSON/XML reports, identify gaps, prioritize fixes
TDD Workflow	Guide red-green-refactor cycles with validation
Framework Adapters	Generate tests for Jest, Pytest, JUnit, Vitest, Mocha
Quality Scoring	Assess test isolation, assertions, naming, detect test smells
Fixture Generation	Create realistic test data, mocks, and factories
Workflows
Generate Tests from Code
Provide source code (TypeScript, JavaScript, Python, Java)
Specify target framework (Jest, Pytest, JUnit, Vitest)
Run test_generator.py with requirements
Review generated test stubs
Validation: Tests compile and cover happy path, error cases, edge cases
Analyze Coverage Gaps
Generate coverage report from test runner (npm test -- --coverage)
Run coverage_analyzer.py on LCOV/JSON/XML report
Review prioritized gaps (P0/P1/P2)
Generate missing tests for uncovered paths
Validation: Coverage meets target threshold (typically 80%+)
TDD New Feature
Write failing test first (RED)
Run tdd_workflow.py --phase red to validate
Implement minimal code to pass (GREEN)
Run tdd_workflow.py --phase green to validate
Refactor while keeping tests green (REFACTOR)
Validation: All tests pass after each cycle
Tools
Tool	Purpose	Usage
test_generator.py	Generate test cases from code/requirements	python scripts/test_generator.py --input source.py --framework pytest
coverage_analyzer.py	Parse and analyze coverage reports	python scripts/coverage_analyzer.py --report lcov.info --threshold 80
tdd_workflow.py	Guide red-green-refactor cycles	python scripts/tdd_workflow.py --phase red --test test_auth.py
framework_adapter.py	Convert tests between frameworks	python scripts/framework_adapter.py --from jest --to pytest
fixture_generator.py	Generate test data and mocks	python scripts/fixture_generator.py --entity User --count 5
metrics_calculator.py	Calculate test quality metrics	python scripts/metrics_calculator.py --tests tests/
format_detector.py	Detect language and framework	python scripts/format_detector.py --file source.ts
output_formatter.py	Format output for CLI/desktop/CI	python scripts/output_formatter.py --format markdown
Input Requirements

For Test Generation:

Source code (file path or pasted content)
Target framework (Jest, Pytest, JUnit, Vitest)
Coverage scope (unit, integration, edge cases)

For Coverage Analysis:

Coverage report file (LCOV, JSON, or XML format)
Optional: Source code for context
Optional: Target threshold percentage

For TDD Workflow:

Feature requirements or user story
Current phase (RED, GREEN, REFACTOR)
Test code and implementation status
Limitations
Scope	Details
Unit test focus	Integration and E2E tests require different patterns
Static analysis	Cannot execute tests or measure runtime behavior
Language support	Best for TypeScript, JavaScript, Python, Java
Report formats	LCOV, JSON, XML only; other formats need conversion
Generated tests	Provide scaffolding; require human review for complex logic

When to use other tools:

E2E testing: Playwright, Cypress, Selenium
Performance testing: k6, JMeter, Locust
Security testing: OWASP ZAP, Burp Suite
Weekly Installs
28
Repository
aaaaqwq/claude-…e-skills
GitHub Stars
53
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass