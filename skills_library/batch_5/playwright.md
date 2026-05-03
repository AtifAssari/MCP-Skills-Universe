---
title: playwright
url: https://skills.sh/pproenca/dot-skills/playwright
---

# playwright

skills/pproenca/dot-skills/playwright
playwright
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill playwright
SKILL.md
Playwright + Next.js Testing Best Practices

Comprehensive testing optimization guide for Playwright with Next.js applications. Contains 43 rules across 8 categories, prioritized by impact to guide reliable, fast, and maintainable E2E tests.

When to Apply

Reference these guidelines when:

Writing new Playwright tests for Next.js apps
Debugging flaky or failing tests
Optimizing test execution speed
Setting up authentication state reuse
Configuring CI/CD pipelines for testing
Testing Server Components and App Router features
Reviewing test code for reliability issues
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Test Architecture	CRITICAL	arch-
2	Selectors & Locators	CRITICAL	loc-
3	Waiting & Assertions	HIGH	wait-
4	Authentication & State	HIGH	auth-
5	Mocking & Network	MEDIUM-HIGH	mock-
6	Next.js Integration	MEDIUM	next-
7	Performance & Speed	MEDIUM	perf-
8	Debugging & CI	LOW-MEDIUM	debug-
Quick Reference
1. Test Architecture (CRITICAL)
arch-test-isolation - Use fresh browser context for each test
arch-parallel-execution - Enable parallel test execution
arch-page-object-model - Use Page Object Model for complex pages
arch-fixtures - Use fixtures for shared setup
arch-test-production - Test against production builds
arch-cleanup-state - Clean up test state after each test
2. Selectors & Locators (CRITICAL)
loc-role-selectors - Use role-based selectors over CSS
loc-data-testid - Use data-testid for dynamic elements
loc-label-selectors - Use getByLabel for form inputs
loc-text-selectors - Use getByText for static content
loc-avoid-xpath - Avoid XPath selectors
loc-chained-locators - Chain locators for specificity
loc-placeholder-selector - Use getByPlaceholder sparingly
3. Waiting & Assertions (HIGH)
wait-web-first-assertions - Use web-first assertions
wait-avoid-hard-waits - Avoid hard waits
wait-network-idle - Use network idle for complex pages
wait-action-retries - Let actions auto-wait before interacting
wait-soft-assertions - Use soft assertions for non-critical checks
wait-custom-timeout - Configure timeouts appropriately
4. Authentication & State (HIGH)
auth-storage-state - Reuse authentication with storage state
auth-multiple-roles - Use separate storage states for different roles
auth-session-storage - Handle session storage for auth
auth-api-login - Use API login for faster auth setup
auth-parallel-workers - Use worker-scoped auth for parallel tests
5. Mocking & Network (MEDIUM-HIGH)
mock-api-responses - Mock API responses for deterministic tests
mock-intercept-modify - Intercept and modify real responses
mock-har-files - Use HAR files for complex mock scenarios
mock-abort-requests - Abort unnecessary requests
mock-network-conditions - Simulate network conditions
6. Next.js Integration (MEDIUM)
next-wait-hydration - Wait for hydration before interacting
next-server-components - Test server components correctly
next-app-router-navigation - Test App Router navigation patterns
next-server-actions - Test server actions end-to-end
next-baseurl-config - Configure baseURL for clean navigation
7. Performance & Speed (MEDIUM)
perf-sharding - Use sharding for large test suites
perf-headless-ci - Use headless mode in CI
perf-browser-selection - Select browsers strategically
perf-reuse-server - Reuse development server when possible
perf-retries - Configure retries for flaky test recovery
8. Debugging & CI (LOW-MEDIUM)
debug-trace-viewer - Use trace viewer for failed tests
debug-screenshots-videos - Capture screenshots and videos on failure
debug-inspector - Use Playwright Inspector for interactive debugging
debug-ci-reporters - Configure reporters for CI integration
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Reference Files
File	Description
AGENTS.md	Complete compiled guide with all rules
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
284
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass