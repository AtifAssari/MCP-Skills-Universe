---
title: testing-mastery
url: https://skills.sh/tai-ch0802/skills-bundle/testing-mastery
---

# testing-mastery

skills/tai-ch0802/skills-bundle/testing-mastery
testing-mastery
Installation
$ npx skills add https://github.com/tai-ch0802/skills-bundle --skill testing-mastery
SKILL.md
Testing Mastery — Unified Testing Skill

Write tests that document intent, catch regressions, and run fast. Choose the right strategy for the right situation.

Decision Tree: Which Testing Strategy?
Is this a new feature?
├─ YES → Use TDD (see references/tdd-cycle.md)
│        Write failing test → Minimal code → Refactor
└─ NO
   ├─ Is this a bug fix?
   │  └─ YES → Write regression test first, then fix
   ├─ Is this a critical user flow (login, checkout)?
   │  └─ YES → E2E test (see references/e2e-playwright.md)
   └─ Is this business logic / data transformation?
      └─ YES → Unit + Integration tests (see references/unit-integration.md)

Testing Pyramid
        /\          E2E (Few, ~10%)
       /  \         Critical user flows only
      /----\
     /      \       Integration (Some, ~20%)
    /--------\      API, DB, service contracts
   /          \
  /------------\    Unit (Many, ~70%)
                    Functions, classes, utilities

Core Principles
Principle	Rule
AAA	Arrange → Act → Assert
Fast	Unit < 100ms, Integration < 1s
Isolated	No test depends on another
Behavior	Test WHAT, not HOW
Minimal	One assertion per test (ideally)
Quick Reference
I need to...	Use	Reference
Build feature test-first	TDD (RED-GREEN-REFACTOR)	tdd-cycle.md
Write unit/integration tests	Mocking, data strategies, patterns	unit-integration.md
Test critical user flows in browser	E2E with Playwright	e2e-playwright.md
Anti-Patterns (Universal)
❌ Don't	✅ Do
Test implementation details	Test observable behavior
Write tests after shipping	Write tests before/during
Duplicate test code	Use factories & fixtures
Complex test setup	Simplify or split
Ignore flaky tests	Fix root cause
Skip cleanup	Reset state in teardown
Multiple asserts per test	One behavior per test
🔧 Runtime Scripts
Script	Purpose	Command
scripts/test_runner.py	Unified test execution	python scripts/test_runner.py <project_path>
scripts/playwright_runner.py	Browser E2E testing	python scripts/playwright_runner.py <url>
	With screenshot	python scripts/playwright_runner.py <url> --screenshot
	Accessibility check	python scripts/playwright_runner.py <url> --a11y

Remember: The test is the specification. If you can't write a test for it, you don't understand the requirement.

Weekly Installs
10
Repository
tai-ch0802/skills-bundle
GitHub Stars
1
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn