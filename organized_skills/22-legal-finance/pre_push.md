---
rating: ⭐⭐⭐
title: pre-push
url: https://skills.sh/morphet81/cheat-sheets/pre-push
---

# pre-push

skills/morphet81/cheat-sheets/pre-push
pre-push
Installation
$ npx skills add https://github.com/morphet81/cheat-sheets --skill pre-push
SKILL.md

Run pre-push checks to ensure code quality before pushing to remote.

Usage:

/pre-push - Run all pre-push checks for the current project

Instructions:

Check for npm pre-push script:

Look for package.json in the current directory
If found, check if it has a pre-push script in the scripts section
If the script exists, run npm run pre-push and report the results
If successful, inform the user and STOP here

If no pre-push script exists, auto-detect and run checks in parallel:

a. Identify project type:

Check for package.json (Node.js/JavaScript/TypeScript project)
Check for pyproject.toml, setup.py, requirements.txt (Python project)
Check for Cargo.toml (Rust project)
Check for go.mod (Go project)
Check for other language-specific files

b. Detect available checks (linting, tests, build) for the project type. Then run independent checks in parallel using the Task tool (subagent_type: general-purpose) with run_in_background: true:

Spawn one agent per independent check category (e.g., linting agent, test agent, build agent)
Checks that don't depend on each other should run concurrently — typically linting and tests are independent, while build may depend on type-checking

c. Linting checks:

Node.js/JavaScript/TypeScript:

Check for ESLint: eslint in package.json scripts or .eslintrc* file
Check for Prettier: prettier in package.json scripts or .prettierrc* file
Check for TypeScript: tsc in package.json scripts or tsconfig.json file
Run: npm run lint or npx eslint . or npm run type-check or npx tsc --noEmit

Python:

Check for: pylint, flake8, black, mypy, ruff
Run available linters (e.g., pylint src/, flake8 ., black --check ., mypy .)

Rust:

Run: cargo fmt --check and cargo clippy

Go:

Run: go fmt ./... and golint ./... or go vet ./...

d. Test checks:

Node.js: Check for test scripts in package.json

Run: npm test or npm run test:ci (if available)

Python:

Check for: pytest, unittest, nose2
Run: pytest or python -m pytest or python -m unittest discover

Rust:

Run: cargo test

Go:

Run: go test ./...

e. Build checks:

If applicable, try building the project to ensure no compilation errors
Node.js: npm run build (if script exists)
Rust: cargo build
Go: go build ./...

Report results:

Wait for all parallel agents to complete and aggregate their results
Provide a clear summary of all checks performed
Report pass/fail status for each check
If any checks fail, show the errors and suggest fixes
Include the commands that were run for transparency
If all checks pass, confirm the code is ready to push

Handle edge cases:

If no tests or linting tools are detected, warn the user and ask if they want to proceed without checks
If commands fail due to missing dependencies, suggest installation commands
If in a monorepo or workspace, detect and handle appropriately

Example output format:

## Pre-Push Checks

### Linting
ESLint passed
Prettier check passed
TypeScript compilation passed

### Testing
All tests passed (24 tests, 0 failures)

### Build
Build successful

---

All pre-push checks passed! Code is ready to push.

Commands run:
- npm run lint
- npm test
- npm run build


On failure:

## Pre-Push Checks

### Linting
ESLint failed

Error in src/components/Button.tsx:
  15:7  error  'onClick' is missing in props validation  react/prop-types

### Testing
All tests passed

---

Pre-push checks failed. Please fix the issues above before pushing.

Weekly Installs
66
Repository
morphet81/cheat-sheets
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass