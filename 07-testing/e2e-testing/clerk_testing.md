---
rating: ⭐⭐
title: clerk-testing
url: https://skills.sh/clerk/skills/clerk-testing
---

# clerk-testing

skills/clerk/skills/clerk-testing
clerk-testing
Installation
$ npx skills add https://github.com/clerk/skills --skill clerk-testing
Summary

E2E testing utilities for Clerk authentication flows in Playwright and Cypress.

Supports both Playwright and Cypress frameworks with framework-specific setup patterns (globalSetup for Playwright, custom commands for Cypress)
Provides clerkSetup() and setupClerkTestingToken() utilities to initialize test environments and bypass bot detection
Includes storageState persistence to reuse authenticated sessions across tests, reducing test execution time
Requires test API keys (pk_test_*, sk_test_*) and offers best practices for avoiding common pitfalls like production credentials and repeated UI-based sign-ins
SKILL.md
Testing
Decision Tree
Framework	Documentation
Overview	https://clerk.com/docs/guides/development/testing/overview
Playwright	https://clerk.com/docs/guides/development/testing/playwright/overview
Cypress	https://clerk.com/docs/guides/development/testing/cypress/overview
Mental Model

Test auth = isolated session state. Each test needs fresh auth context.

clerkSetup() initializes test environment
setupClerkTestingToken() bypasses bot detection
storageState persists auth between tests for speed
Workflow
Identify test framework (Playwright or Cypress)
WebFetch the appropriate URL from decision tree above
Follow official setup instructions
Use pk_test_* and sk_test_* keys only
Best Practices
Use setupClerkTestingToken() before navigating to auth pages
Use test API keys: pk_test_xxx, sk_test_xxx
Save auth state with storageState for faster tests
Use page.waitForSelector('[data-clerk-component]') for Clerk UI
Anti-Patterns
Pattern	Problem	Fix
Production keys in tests	Security risk	Use pk_test_* keys
No setupClerkTestingToken()	Auth fails	Call before navigation
UI-based sign-in every test	Slow tests	Use storageState
Framework-Specific

Playwright: Use globalSetup for auth state Cypress: Add addClerkCommands({ Cypress, cy }) to support file

See Also
clerk-setup - Install Clerk before adding tests
clerk-nextjs-patterns - Next.js patterns being tested
Demo Repo
Weekly Installs
4.9K
Repository
clerk/skills
GitHub Stars
40
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn