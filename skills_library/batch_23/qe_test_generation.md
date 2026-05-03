---
title: qe-test-generation
url: https://skills.sh/proffesor-for-testing/agentic-qe/qe-test-generation
---

# qe-test-generation

skills/proffesor-for-testing/agentic-qe/qe-test-generation
qe-test-generation
Installation
$ npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill qe-test-generation
SKILL.md
QE Test Generation
Purpose

Guide the use of v3's AI-powered test generation capabilities including pattern-based test synthesis, multi-framework support, and intelligent test case derivation from code analysis.

Activation
When generating tests for new code
When improving test coverage
When migrating tests between frameworks
When applying TDD patterns
When generating edge case tests
Quick Start
# Generate unit tests for a file
aqe test generate --file src/services/UserService.ts --framework jest

# Generate tests with coverage target
aqe test generate --scope src/api/ --coverage 90 --type unit

# Generate integration tests
aqe test generate --file src/controllers/AuthController.ts --type integration

# Generate from patterns
aqe test generate --pattern repository --target src/repositories/

Agent Workflow
// Spawn test generation agents
Task("Generate unit tests", `
  Analyze src/services/PaymentService.ts and generate comprehensive Jest tests.
  Include:
  - Happy path tests for all public methods
  - Edge cases and boundary conditions
  - Error handling scenarios
  - Mock external dependencies
  Output to tests/unit/services/PaymentService.test.ts
`, "qe-test-generator")

// Pattern-based generation
Task("Apply test patterns", `
  Scan src/repositories/ and apply repository test pattern:
  - CRUD operation tests
  - Query builder tests
  - Transaction tests
  - Connection error handling
`, "qe-pattern-matcher")

Test Generation Strategies
1. Code Analysis Based
await testGenerator.analyzeAndGenerate({
  source: 'src/services/OrderService.ts',
  analysis: {
    methods: true,
    branches: true,
    dependencies: true,
    errorPaths: true
  },
  output: {
    framework: 'jest',
    style: 'describe-it',
    assertions: 'expect'
  }
});

2. Pattern-Based Generation
await testGenerator.applyPattern({
  pattern: 'service-layer',
  targets: ['src/services/*.ts'],
  customizations: {
    mockStrategy: 'jest.mock',
    asyncHandling: 'async-await',
    errorAssertion: 'toThrow'
  }
});

3. Coverage-Driven Generation
await testGenerator.fillCoverageGaps({
  coverageReport: 'coverage/lcov.info',
  targetCoverage: 90,
  prioritize: ['uncovered-branches', 'error-paths'],
  maxTests: 50
});

Framework Support
Framework	Unit	Integration	E2E	Mocking
Jest	✅	✅	⚠️	jest.mock
Vitest	✅	✅	⚠️	vi.mock
Mocha	✅	✅	❌	sinon
Pytest	✅	✅	❌	pytest-mock
JUnit	✅	✅	❌	Mockito
Test Quality Checks
quality_checks:
  assertions:
    minimum_per_test: 1
    meaningful: true

  isolation:
    no_shared_state: true
    proper_setup_teardown: true

  naming:
    descriptive: true
    follows_convention: true

  coverage:
    branches: 80
    statements: 85

Skill Composition
After generating tests → Run /mutation-testing to verify test quality
Before generating → Use /test-automation-strategy to choose framework and patterns
Related → /qe-coverage-analysis to find where tests are needed most
Gotchas
Agent truncates output on files >3000 lines — scope generation to individual modules, not entire directories
Components that pass unit tests individually may have zero integration wiring — always generate at least one integration test per module boundary
When generating tests for a new codebase, check which framework is installed (jest vs vitest vs mocha) — they have different mock APIs and Claude will use the wrong one
Completion theater: agent may claim "comprehensive tests generated" but leave stubs or hardcoded values — always run the generated tests before accepting
Fleet must be initialized before using QE agents: run aqe health to diagnose, or aqe init to re-initialize if you get "Fleet not initialized"
Coordination

Primary Agents: qe-test-generator, qe-pattern-matcher, qe-test-architect Coordinator: qe-test-generation-coordinator Related Skills: qe-coverage-analysis, qe-test-execution

Weekly Installs
55
Repository
proffesor-for-t…entic-qe
GitHub Stars
334
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass