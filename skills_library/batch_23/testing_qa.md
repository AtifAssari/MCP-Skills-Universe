---
title: testing-qa
url: https://skills.sh/sickn33/antigravity-awesome-skills/testing-qa
---

# testing-qa

skills/sickn33/antigravity-awesome-skills/testing-qa
testing-qa
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill testing-qa
SKILL.md
Testing/QA Workflow Bundle
Overview

Comprehensive testing and quality assurance workflow covering unit tests, integration tests, E2E tests, browser automation, and quality gates for production-ready software.

When to Use This Workflow

Use this workflow when:

Setting up testing infrastructure
Writing unit and integration tests
Implementing E2E tests
Automating browser testing
Establishing quality gates
Performing code review
Workflow Phases
Phase 1: Test Strategy
Skills to Invoke
test-automator - Test automation
test-driven-development - TDD
Actions
Define testing strategy
Choose testing frameworks
Plan test coverage
Set up test infrastructure
Configure CI integration
Copy-Paste Prompts
Use @test-automator to design testing strategy

Use @test-driven-development to implement TDD workflow

Phase 2: Unit Testing
Skills to Invoke
javascript-testing-patterns - Jest/Vitest
python-testing-patterns - pytest
unit-testing-test-generate - Test generation
tdd-orchestrator - TDD orchestration
Actions
Write unit tests
Set up test fixtures
Configure mocking
Measure coverage
Integrate with CI
Copy-Paste Prompts
Use @javascript-testing-patterns to write Jest tests

Use @python-testing-patterns to write pytest tests

Use @unit-testing-test-generate to generate unit tests

Phase 3: Integration Testing
Skills to Invoke
api-testing-observability-api-mock - API testing
e2e-testing-patterns - Integration patterns
Actions
Design integration tests
Set up test databases
Configure API mocks
Test service interactions
Verify data flows
Copy-Paste Prompts
Use @api-testing-observability-api-mock to test APIs

Phase 4: E2E Testing
Skills to Invoke
playwright-skill - Playwright testing
e2e-testing-patterns - E2E patterns
webapp-testing - Web app testing
Actions
Design E2E scenarios
Write test scripts
Configure test data
Set up parallel execution
Implement visual regression
Copy-Paste Prompts
Use @playwright-skill to create E2E tests

Use @e2e-testing-patterns to design E2E strategy

Phase 5: Browser Automation
Skills to Invoke
browser-automation - Browser automation
webapp-testing - Browser testing
screenshots - Screenshot automation
Actions
Set up browser automation
Configure headless testing
Implement visual testing
Capture screenshots
Test responsive design
Copy-Paste Prompts
Use @browser-automation to automate browser tasks

Use @screenshots to capture marketing screenshots

Phase 6: Performance Testing
Skills to Invoke
performance-engineer - Performance engineering
performance-profiling - Performance profiling
web-performance-optimization - Web performance
Actions
Design performance tests
Set up load testing
Measure response times
Identify bottlenecks
Optimize performance
Copy-Paste Prompts
Use @performance-engineer to test application performance

Phase 7: Code Review
Skills to Invoke
code-reviewer - AI code review
code-review-excellence - Review best practices
find-bugs - Bug detection
security-scanning-security-sast - Security scanning
Actions
Configure review tools
Run automated reviews
Check for bugs
Verify security
Approve changes
Copy-Paste Prompts
Use @code-reviewer to review pull requests

Use @find-bugs to detect bugs in code

Phase 8: Quality Gates
Skills to Invoke
lint-and-validate - Linting
verification-before-completion - Verification
Actions
Configure linters
Set up formatters
Define quality metrics
Implement gates
Monitor compliance
Copy-Paste Prompts
Use @lint-and-validate to check code quality

Use @verification-before-completion to verify changes

Testing Pyramid
        /       /  \    E2E Tests (10%)
      /----     /      \  Integration Tests (20%)
    /--------   /          \ Unit Tests (70%)
  /------------```

## Quality Gates Checklist

- [ ] Unit test coverage > 80%
- [ ] All tests passing
- [ ] E2E tests for critical paths
- [ ] Performance benchmarks met
- [ ] Security scan passed
- [ ] Code review approved
- [ ] Linting clean

## Related Workflow Bundles

- `development` - Development workflow
- `security-audit` - Security testing
- `cloud-devops` - CI/CD integration
- `ai-ml` - AI testing

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

Weekly Installs
75
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass