---
rating: ⭐⭐⭐
title: go-linting
url: https://skills.sh/cxuu/golang-skills/go-linting
---

# go-linting

skills/cxuu/golang-skills/go-linting
go-linting
Installation
$ npx skills add https://github.com/cxuu/golang-skills --skill go-linting
SKILL.md
Go Linting
Core Principle

More important than any "blessed" set of linters: lint consistently across a codebase.

Consistent linting helps catch common issues and establishes a high bar for code quality without being unnecessarily prescriptive.

Setup Procedure
Create .golangci.yml using the configuration below
Run golangci-lint run ./...
If errors appear, fix them category by category (formatting first, then vet, then style)
Re-run until clean
Minimum Recommended Linters

These linters catch the most common issues while maintaining a high quality bar:

Linter	Purpose
errcheck	Ensure errors are handled
goimports	Format code and manage imports
revive	Common style mistakes (modern replacement for golint)
govet	Analyze code for common mistakes
staticcheck	Various static analysis checks

Note: revive is the modern, faster successor to the now-deprecated golint.

Lint Runner: golangci-lint

Use golangci-lint as your lint runner. See the example .golangci.yml from uber-go/guide.

Example Configuration

See assets/golangci.yml when creating a new .golangci.yml or comparing your existing config against a recommended baseline.

Create .golangci.yml in your project root:

linters:
  enable:
    - errcheck
    - goimports
    - revive
    - govet
    - staticcheck

linters-settings:
  goimports:
    local-prefixes: github.com/your-org/your-repo
  revive:
    rules:
      - name: blank-imports
      - name: context-as-argument
      - name: error-return
      - name: error-strings
      - name: exported

run:
  timeout: 5m

Running
# Install
go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest

# Run all linters
golangci-lint run

# Run on specific paths
golangci-lint run ./pkg/...

Additional Recommended Linters

Beyond the minimum set, consider these for production projects:

Linter	Purpose	When to enable
gosec	Security vulnerability detection	Always for services handling user input
ineffassign	Detect ineffectual assignments	Always — catches dead code
misspell	Correct common misspellings in comments/strings	Always
gocyclo	Cyclomatic complexity threshold	When functions exceed ~15 complexity
exhaustive	Ensure switch covers all enum values	When using iota enums
bodyclose	Detect unclosed HTTP response bodies	Always for HTTP client code
Nolint Directives

When suppressing a lint finding, always explain why:

//nolint:errcheck // fire-and-forget logging; error is not actionable
_ = logger.Sync()


Rules:

Use //nolint:lintername — never bare //nolint
Place the comment on the same line as the finding
Include a justification after //
CI/CD Integration
GitHub Actions
# .github/workflows/lint.yml
name: Lint
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: stable
      - uses: golangci/golangci-lint-action@v6
        with:
          version: latest

Pre-commit Hook
#!/bin/sh
# .git/hooks/pre-commit
golangci-lint run --new-from-rev=HEAD~1


Use --new-from-rev to lint only changed code, keeping the feedback loop fast.

Available Scripts
scripts/setup-lint.sh — Generates .golangci.yml and runs initial lint
bash scripts/setup-lint.sh github.com/your-org/your-repo
bash scripts/setup-lint.sh --force github.com/your-org/your-repo  # overwrite existing
bash scripts/setup-lint.sh --dry-run                               # preview config
bash scripts/setup-lint.sh --json                                  # structured output


Validation: After generating .golangci.yml, run golangci-lint run ./... to verify the configuration is valid and produces expected output. If it fails with a config error, fix and retry.

scripts/setup-lint.sh generates a minimum config (5 core linters). For established projects, use assets/golangci.yml as a starting point — it adds gosec, ineffassign, misspell, gocyclo, and bodyclose.

Quick Reference
Task	Command/Action
Install golangci-lint	go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
Run linters	golangci-lint run
Run on path	golangci-lint run ./pkg/...
Config file	.golangci.yml in project root
CI integration	Run golangci-lint run in pipeline
Nolint directives	//nolint:name // reason — never bare //nolint
CI integration	Use golangci/golangci-lint-action for GitHub Actions
Pre-commit	golangci-lint run --new-from-rev=HEAD~1
Linter Selection Guidelines
When you need...	Use
Error handling coverage	errcheck
Import formatting	goimports
Style consistency	revive
Bug detection	govet, staticcheck
All of the above	golangci-lint with config
Related Skills
Style foundations: See go-style-core when resolving style questions that linters enforce (formatting, nesting, naming)
Code review: See go-code-review when combining linter output with a manual review checklist
Error handling: See go-error-handling when errcheck flags unhandled errors and you need to decide how to handle them
Testing: See go-testing when running linters alongside tests in CI pipelines
Weekly Installs
523
Repository
cxuu/golang-skills
GitHub Stars
82
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass