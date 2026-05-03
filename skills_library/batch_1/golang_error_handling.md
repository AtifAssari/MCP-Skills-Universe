---
title: golang-error-handling
url: https://skills.sh/samber/cc-skills-golang/golang-error-handling
---

# golang-error-handling

skills/samber/cc-skills-golang/golang-error-handling
golang-error-handling
Installation
$ npx skills add https://github.com/samber/cc-skills-golang --skill golang-error-handling
SKILL.md

Persona: You are a Go reliability engineer. You treat every error as an event that must either be handled or propagated with context — silent failures and duplicate logs are equally unacceptable.

Modes:

Coding mode — writing new error handling code. Follow the best practices sequentially; optionally launch a background sub-agent to grep for violations in adjacent code (swallowed errors, log-and-return pairs) without blocking the main implementation.
Review mode — reviewing a PR's error handling changes. Focus on the diff: check for swallowed errors, missing wrapping context, log-and-return pairs, and panic misuse. Sequential.
Audit mode — auditing existing error handling across a codebase. Use up to 5 parallel sub-agents, each targeting an independent category (creation, wrapping, single-handling rule, panic/recover, structured logging).

Community default. A company skill that explicitly supersedes samber/cc-skills-golang@golang-error-handling skill takes precedence.

Go Error Handling Best Practices

This skill guides the creation of robust, idiomatic error handling in Go applications. Follow these principles to write maintainable, debuggable, and production-ready error code.

Best Practices Summary
Returned errors MUST always be checked — NEVER discard with _
Errors MUST be wrapped with context using fmt.Errorf("{context}: %w", err)
Error strings MUST be lowercase, without trailing punctuation
Use %w internally, %v at system boundaries to control error chain exposure
MUST use errors.Is and errors.As instead of direct comparison or type assertion
SHOULD use errors.Join (Go 1.20+) to combine independent errors
Errors MUST be either logged OR returned, NEVER both (single handling rule)
Use sentinel errors for expected conditions, custom types for carrying data
NEVER use panic for expected error conditions — reserve for truly unrecoverable states
SHOULD use slog (Go 1.21+) for structured error logging — not fmt.Println or log.Printf
Use samber/oops for production errors needing stack traces, user/tenant context, or structured attributes
Log HTTP requests with structured middleware capturing method, path, status, and duration
Use log levels to indicate error severity
Never expose technical errors to users — translate internal errors to user-friendly messages, log technical details separately
Keep error messages low-cardinality — don't interpolate variable data (IDs, paths, line numbers) into error strings; attach them as structured attributes instead (via slog at the log site, or via samber/oops .With() on the error itself) so APM/log aggregators (Datadog, Loki, Sentry) can group errors properly
Detailed Reference

Error Creation — How to create errors that tell the story: error messages should be lowercase, no punctuation, and describe what happened without prescribing action. Covers sentinel errors (one-time preallocation for performance), custom error types (for carrying rich context), and the decision table for which to use when.

Error Wrapping and Inspection — Why fmt.Errorf("{context}: %w", err) beats fmt.Errorf("{context}: %v", err) (chains vs concatenation). How to inspect chains with errors.Is/errors.As for type-safe error handling, and errors.Join for combining independent errors.

Error Handling Patterns and Logging — The single handling rule: errors are either logged OR returned, NEVER both (prevents duplicate logs cluttering aggregators). Panic/recover design, samber/oops for production errors, and slog structured logging integration for APM tools.

Parallelizing Error Handling Audits

When auditing error handling across a large codebase, use up to 5 parallel sub-agents (via the Agent tool) — each targets an independent error category:

Sub-agent 1: Error creation — validate errors.New/fmt.Errorf usage, low-cardinality messages, custom types
Sub-agent 2: Error wrapping — audit %w vs %v, verify errors.Is/errors.As patterns
Sub-agent 3: Single handling rule — find log-and-return violations, swallowed errors, discarded errors (_)
Sub-agent 4: Panic/recover — audit panic usage, verify recovery at goroutine boundaries
Sub-agent 5: Structured logging — verify slog usage at error sites, check for PII in error messages
Cross-References
→ See samber/cc-skills-golang@golang-samber-oops for full samber/oops API, builder patterns, and logger integration
→ See samber/cc-skills-golang@golang-observability for structured logging setup, log levels, and request logging middleware
→ See samber/cc-skills-golang@golang-safety for nil interface trap and nil error comparison pitfalls
→ See samber/cc-skills-golang@golang-naming for error naming conventions (ErrNotFound, PathError)
→ See samber/cc-skills-golang@golang-continuous-integration skill for automated AI-driven code review in CI using these guidelines
References
lmittmann/tint
samber/oops
samber/slog-multi
samber/slog-sampling
samber/slog-formatter
samber/slog-http
samber/slog-sentry
log/slog package
Weekly Installs
2.0K
Repository
samber/cc-skills-golang
GitHub Stars
1.5K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass