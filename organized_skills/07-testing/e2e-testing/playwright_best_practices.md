---
rating: ⭐⭐
title: playwright-best-practices
url: https://skills.sh/0xbigboss/claude-code/playwright-best-practices
---

# playwright-best-practices

skills/0xbigboss/claude-code/playwright-best-practices
playwright-best-practices
Installation
$ npx skills add https://github.com/0xbigboss/claude-code --skill playwright-best-practices
SKILL.md
Playwright Best Practices
CLI Context: Prevent Context Overflow

When running Playwright tests from Claude Code or any CLI agent, always use minimal reporters to prevent verbose output from consuming the context window.

Use --reporter=line or --reporter=dot for CLI test runs. Configure playwright.config.ts to default to minimal reporters when CI or CLAUDE env vars are set — see playwright-patterns.md for the config snippet.

Locator Priority (Most to Least Resilient)

Always prefer user-facing attributes:

page.getByRole('button', { name: 'Submit' }) — accessibility roles
page.getByLabel('Email') — form control labels
page.getByPlaceholder('Search...') — input placeholders
page.getByText('Welcome') — visible text (non-interactive)
page.getByAltText('Logo') — image alt text
page.getByTitle('Settings') — title attributes
page.getByTestId('submit-btn') — explicit test contracts
CSS/XPath — last resort, avoid
Core Rules
Web-first assertions: always await expect(locator).toBeVisible(), never expect(await locator.isVisible()).toBe(true) — web-first matchers auto-wait and retry
Test isolation: each test creates its own data; never share state between tests
Auth state reuse: save authenticated state via setup project + storageState; never log in via UI in every test
Fixtures over beforeEach: fixtures encapsulate setup + teardown, run on-demand, and compose
Anti-Patterns
page.waitForTimeout(ms) — use auto-waiting locators instead
page.locator('.class') — use role/label/testid
XPath selectors — fragile, use user-facing attributes
Shared state between tests — each test creates own data
UI login in every test — use setup project + storageState
Manual assertions without await — use web-first assertions
Hardcoded waits — rely on Playwright's auto-waiting
Default reporter in CI/agent — use --reporter=line or --reporter=dot
Checklist
 Locators use role/label/testid, not CSS classes or XPath
 All assertions use await expect() web-first matchers
 Page objects define locators in constructor
 No page.waitForTimeout() — use auto-waiting
 Tests isolated — no shared state
 Auth state reused via setup project
 Network mocks set up before navigation
 Test data created per-test or via fixtures
 Debug logging added for complex flows
 Minimal reporter (line/dot) used in CI/agent contexts

See playwright-patterns.md for Page Object Model, fixtures, network mocking, and configuration examples.

Weekly Installs
213
Repository
0xbigboss/claude-code
GitHub Stars
43
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass