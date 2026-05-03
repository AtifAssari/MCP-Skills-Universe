---
title: webapp-testing
url: https://skills.sh/vudovn/antigravity-kit/webapp-testing
---

# webapp-testing

skills/vudovn/antigravity-kit/webapp-testing
webapp-testing
Installation
$ npx skills add https://github.com/vudovn/antigravity-kit --skill webapp-testing
SKILL.md
Web App Testing

Discover and test everything. Leave no route untested.

🔧 Runtime Scripts

Execute these for automated browser testing:

Script	Purpose	Usage
scripts/playwright_runner.py	Basic browser test	python scripts/playwright_runner.py https://example.com
	With screenshot	python scripts/playwright_runner.py <url> --screenshot
	Accessibility check	python scripts/playwright_runner.py <url> --a11y

Requires: pip install playwright && playwright install chromium

1. Deep Audit Approach
Discovery First
Target	How to Find
Routes	Scan app/, pages/, router files
API endpoints	Grep for HTTP methods
Components	Find component directories
Features	Read documentation
Systematic Testing
Map - List all routes/APIs
Scan - Verify they respond
Test - Cover critical paths
2. Testing Pyramid for Web
        /\          E2E (Few)
       /  \         Critical user flows
      /----\
     /      \       Integration (Some)
    /--------\      API, data flow
   /          \
  /------------\    Component (Many)
                    Individual UI pieces

3. E2E Test Principles
What to Test
Priority	Tests
1	Happy path user flows
2	Authentication flows
3	Critical business actions
4	Error handling
E2E Best Practices
Practice	Why
Use data-testid	Stable selectors
Wait for elements	Avoid flaky tests
Clean state	Independent tests
Avoid implementation details	Test user behavior
4. Playwright Principles
Core Concepts
Concept	Use
Page Object Model	Encapsulate page logic
Fixtures	Reusable test setup
Assertions	Built-in auto-wait
Trace Viewer	Debug failures
Configuration
Setting	Recommendation
Retries	2 on CI
Trace	on-first-retry
Screenshots	on-failure
Video	retain-on-failure
5. Visual Testing
When to Use
Scenario	Value
Design system	High
Marketing pages	High
Component library	Medium
Dynamic content	Lower
Strategy
Baseline screenshots
Compare on changes
Review visual diffs
Update intentional changes
6. API Testing Principles
Coverage Areas
Area	Tests
Status codes	200, 400, 404, 500
Response shape	Matches schema
Error messages	User-friendly
Edge cases	Empty, large, special chars
7. Test Organization
File Structure
tests/
├── e2e/           # Full user flows
├── integration/   # API, data
├── component/     # UI units
└── fixtures/      # Shared data

Naming Convention
Pattern	Example
Feature-based	login.spec.ts
Descriptive	user-can-checkout.spec.ts
8. CI Integration
Pipeline Steps
Install dependencies
Install browsers
Run tests
Upload artifacts (traces, screenshots)
Parallelization
Strategy	Use
Per file	Playwright default
Sharding	Large suites
Workers	Multiple browsers
9. Anti-Patterns
❌ Don't	✅ Do
Test implementation	Test behavior
Hardcode waits	Use auto-wait
Skip cleanup	Isolate tests
Ignore flaky tests	Fix root cause

Remember: E2E tests are expensive. Use them for critical paths only.

Weekly Installs
183
Repository
vudovn/antigravity-kit
GitHub Stars
7.3K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn