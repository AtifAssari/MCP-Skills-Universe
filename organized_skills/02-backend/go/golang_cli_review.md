---
rating: ⭐⭐⭐
title: golang-cli-review
url: https://skills.sh/adamos486/skills/golang-cli-review
---

# golang-cli-review

skills/adamos486/skills/golang-cli-review
golang-cli-review
Installation
$ npx skills add https://github.com/adamos486/skills --skill golang-cli-review
SKILL.md
Go CLI Code Review

Review Go CLI applications and produce an actionable checklist of findings.

Review Workflow
Gather code - Read all Go files in the CLI project
Analyze - Evaluate against review categories (see below)
Produce checklist - Use template from references/review-checklist.md
Review Categories

Evaluate each area systematically:

CLI Structure & Framework
Framework usage (prefer Cobra for complex CLIs)
Command hierarchy and discoverability
Help text quality with examples
Version command following semver
Error Handling
RunE vs Run (must return errors)
Error wrapping with %w and context
User-facing error actionability
Meaningful exit codes (0=success, 1=error, 2=usage)
No panics in normal paths
Flag & Argument Design
Lowercase-kebab-case naming
Short flags for common options (-v, -o, -q)
Required flags marked and validated early
Sensible defaults
Clear descriptions
Input/Output
stderr for errors/progress, stdout for data
Machine-readable output support (--json, --format)
Quiet and verbose mode support
Non-TTY mode handling (no prompts)
Security
Secrets via env vars or files, never flags
Path traversal prevention
No shell injection
URL scheme validation
No sensitive data in logs
Testing
Command-level unit tests
Error path coverage
Integration tests for critical flows
Performance & Resources
Context-based cancellation
Signal handling (SIGINT/SIGTERM)
Proper resource cleanup (defer)
No goroutine leaks
Go Idioms
Effective Go style compliance
Immediate error handling
Package naming conventions
Interface/struct patterns
Reference Material

For patterns and examples, see references/cli-patterns.md.

Output Format

Use the checklist template from references/review-checklist.md:

## Critical Issues
- [ ] **[C1]** `file.go:123` - Description
  - **Impact:** ...
  - **Fix:** ...

## Warnings
- [ ] **[W1]** `file.go:45` - Description
  - **Why:** ...
  - **Fix:** ...

## Suggestions
- [ ] **[S1]** `file.go:78` - Description
  - **Consider:** ...

## Positive Patterns
- **[P1]** `file.go:90` - What was done well


Severity levels:

Critical: Security issues, crashes, data loss - must fix
Warning: Bugs, anti-patterns, maintenance concerns - should fix
Suggestion: Style, optimization, minor improvements - nice to have
Positive: Good practices worth highlighting
Weekly Installs
23
Repository
adamos486/skills
GitHub Stars
7
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass