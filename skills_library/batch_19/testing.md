---
title: testing
url: https://skills.sh/dralgorhythm/claude-agentic-framework/testing
---

# testing

skills/dralgorhythm/claude-agentic-framework/testing
testing
Installation
$ npx skills add https://github.com/dralgorhythm/claude-agentic-framework --skill testing
SKILL.md
Testing Software
MCP Tools

Chrome DevTools (E2E testing):

Automate user flows in real browser
Capture screenshots for visual regression
Run Lighthouse for accessibility testing
Profile performance during test runs
Testing Pyramid
Unit Tests (Many): Fast, isolated, test single units
Integration Tests (Some): Test component interactions
E2E Tests (Few): Test complete user flows — use Chrome DevTools
Workflows
 Analyze: Use Glob and Grep to identify untested code
 Unit Tests: Cover all public functions
 Edge Cases: Test boundaries and error conditions
 Integration: Test external dependencies
 E2E: Use Chrome DevTools for browser automation
 Regression: Add test for each bug fix
Test Quality Standards
Deterministic

Tests must produce the same result every time.

Isolated

Tests should not depend on each other or shared state.

Clear

Test names should describe the behavior being tested.

Test Patterns
Arrange-Act-Assert (AAA) (TypeScript Example)
test("user registration sends welcome email", async () => {
  // Arrange
  const emailService = new MockEmailService();
  const userService = new UserService(emailService);

  // Act
  await userService.register("test@example.com");

  // Assert
  expect(emailService.sentEmails).toContainEqual({
    to: "test@example.com",
    subject: "Welcome!"
  });
});

E2E Testing with Chrome DevTools
// Use Chrome DevTools MCP for browser automation
// - Navigate to pages
// - Fill forms and click buttons
// - Capture screenshots for visual regression
// - Run Lighthouse accessibility audits
// - Check console for errors

Commands (Examples by Language)
# Run tests
npm test
pytest
go test ./...

# With coverage
npm test -- --coverage
pytest --cov=src
go test -cover ./...

Finding Untested Code

Use Glob and Grep to identify gaps:

Use Glob to find all source files and test files
Check which source files have corresponding test files
Use Grep to see if functions are referenced in tests
Weekly Installs
35
Repository
dralgorhythm/cl…ramework
GitHub Stars
76
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass