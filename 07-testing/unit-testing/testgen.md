---
title: testgen
url: https://skills.sh/johnlindquist/claude/testgen
---

# testgen

skills/johnlindquist/claude/testgen
testgen
Installation
$ npx skills add https://github.com/johnlindquist/claude --skill testgen
SKILL.md
Test Generator

AI-powered test generation and test suite management.

Prerequisites
# Gemini for AI generation
pip install google-generativeai
export GEMINI_API_KEY=your_api_key

# Test runners (install as needed)
npm install -D jest vitest mocha
npm install -D @stryker-mutator/core  # Mutation testing

AI Test Generation
Generate Unit Tests
# Read code and generate tests
CODE=$(cat src/utils.ts)

gemini -m pro -o text -e "" "Generate comprehensive unit tests for this code:

$CODE

Requirements:
1. Use Jest/Vitest syntax
2. Cover happy path, edge cases, and error conditions
3. Include descriptive test names
4. Mock external dependencies
5. Test each exported function

Output only the test code, ready to save to a file."

Generate Tests for Specific Function
gemini -m pro -o text -e "" "Generate unit tests for this function:

\`\`\`typescript
export function calculateDiscount(price: number, percentage: number): number {
  if (percentage < 0 || percentage > 100) {
    throw new Error('Invalid percentage');
  }
  return price * (1 - percentage / 100);
}
\`\`\`

Include tests for:
- Valid inputs
- Boundary values (0%, 100%)
- Invalid inputs (negative, >100)
- Edge cases (zero price)

Use Jest syntax."

TDD Loop
# 1. Write failing test first
gemini -m pro -o text -e "" "Write a failing test for: [feature description]"

# 2. Run test (should fail)
npm test -- --watch

# 3. Implement minimal code to pass

# 4. Refactor

# 5. Repeat

Test Runners
Jest
# Run all tests
npx jest

# Watch mode
npx jest --watch

# Specific file
npx jest src/utils.test.ts

# With coverage
npx jest --coverage

# Update snapshots
npx jest -u

# Verbose output
npx jest --verbose

# Run matching pattern
npx jest -t "should calculate"

Vitest
# Run tests
npx vitest

# Watch mode
npx vitest --watch

# Run once
npx vitest run

# Coverage
npx vitest --coverage

# UI mode
npx vitest --ui

# Specific file
npx vitest src/utils.test.ts

Mocha
# Run tests
npx mocha

# Watch mode
npx mocha --watch

# Specific file
npx mocha test/utils.test.js

# With reporter
npx mocha --reporter spec

Coverage Analysis
Generate Coverage Report
# Jest
npx jest --coverage --coverageReporters=text --coverageReporters=html

# Vitest
npx vitest run --coverage

# View HTML report
open coverage/index.html

Coverage Thresholds
// jest.config.js or vitest.config.ts
{
  "coverageThreshold": {
    "global": {
      "branches": 80,
      "functions": 80,
      "lines": 80,
      "statements": 80
    }
  }
}

Find Uncovered Code
# Text coverage report
npx jest --coverage --coverageReporters=text

# Ask AI for suggestions
UNCOVERED=$(npx jest --coverage --coverageReporters=json --silent | jq '.coverageMap')
gemini -m pro -o text -e "" "Given this coverage report, suggest tests for uncovered code:

$UNCOVERED"

Mutation Testing

Test the tests themselves using Stryker:

# Check if installed
npx stryker --version

# Initialize
npx stryker init

# Run mutation testing
npx stryker run

# With reporters
npx stryker run --reporters clear-text,json,html

Interpret Results
Killed mutants: Tests caught the bug (good)
Survived mutants: Tests missed the bug (need more tests)
Timeout mutants: Mutant caused infinite loop
No coverage: Code not covered by any test
Workflow Patterns
New Feature Testing
# 1. Generate test scaffold
CODE=$(cat src/new-feature.ts)
gemini -m pro -o text -e "" "Generate test file scaffold for: $CODE" > src/new-feature.test.ts

# 2. Run tests (should fail)
npx jest src/new-feature.test.ts

# 3. Implement feature
# 4. Run tests (should pass)
# 5. Add edge case tests
# 6. Check coverage
npx jest src/new-feature.test.ts --coverage

Regression Test Generation
# After fixing a bug, generate regression test
BUG_DESC="Users could submit empty forms"
FIX=$(git diff HEAD~1)

gemini -m pro -o text -e "" "Generate a regression test for this bug fix:

Bug: $BUG_DESC

Fix:
$FIX

The test should fail if the bug is reintroduced."

Integration Test Generation
gemini -m pro -o text -e "" "Generate integration tests for this API endpoint:

\`\`\`typescript
// POST /api/users
// Body: { name: string, email: string }
// Response: { id: string, name: string, email: string }
\`\`\`

Include:
- Success case
- Validation errors
- Duplicate email handling
- Authentication required

Use supertest or similar."

Best Practices
Test behavior, not implementation - Focus on what, not how
One assertion per test - When practical
Descriptive names - Should document what's tested
Arrange-Act-Assert - Clear test structure
Mock external deps - Isolate unit under test
Run tests in CI - Automated verification
Maintain coverage - Don't let it drop
Use mutation testing - Verify test quality
Weekly Installs
28
Repository
johnlindquist/claude
GitHub Stars
23
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass