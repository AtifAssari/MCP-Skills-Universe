---
title: golang-context
url: https://skills.sh/samber/cc-skills-golang/golang-context
---

# golang-context

skills/samber/cc-skills-golang/golang-context
golang-context
Installation
$ npx skills add https://github.com/samber/cc-skills-golang --skill golang-context
SKILL.md

Community default. A company skill that explicitly supersedes samber/cc-skills-golang@golang-context skill takes precedence.

Go context.Context Best Practices

context.Context is Go's mechanism for propagating cancellation signals, deadlines, and request-scoped values across API boundaries and between goroutines. Think of it as the "session" of a request — it ties together every operation that belongs to the same unit of work.

Best Practices Summary
The same context MUST be propagated through the entire request lifecycle: HTTP handler → service → DB → external APIs
ctx MUST be the first parameter, named ctx context.Context
NEVER store context in a struct — pass explicitly through function parameters
NEVER pass nil context — use context.TODO() if unsure
cancel() MUST always be deferred immediately after WithCancel/WithTimeout/WithDeadline
context.Background() MUST only be used at the top level (main, init, tests)
Use context.TODO() as a placeholder when you know a context is needed but don't have one yet
NEVER create a new context.Background() in the middle of a request path
Context value keys MUST be unexported types to prevent collisions
Context values MUST only carry request-scoped metadata — NEVER function parameters
Use context.WithoutCancel (Go 1.21+) when spawning background work that must outlive the parent request
Creating Contexts
Situation	Use
Entry point (main, init, test)	context.Background()
Function needs context but caller doesn't provide one yet	context.TODO()
Inside an HTTP handler	r.Context()
Need cancellation control	context.WithCancel(parentCtx)
Need a deadline/timeout	context.WithTimeout(parentCtx, duration)
Context Propagation: The Core Principle

The most important rule: propagate the same context through the entire call chain. When you propagate correctly, cancelling the parent context cancels all downstream work automatically.

// ✗ Bad — creates a new context, breaking the chain
func (s *OrderService) Create(ctx context.Context, order Order) error {
    return s.db.ExecContext(context.Background(), "INSERT INTO orders ...", order.ID)
}

// ✓ Good — propagates the caller's context
func (s *OrderService) Create(ctx context.Context, order Order) error {
    return s.db.ExecContext(ctx, "INSERT INTO orders ...", order.ID)
}

Deep Dives

Cancellation, Timeouts & Deadlines — How cancellation propagates: WithCancel for manual cancellation, WithTimeout for automatic cancellation after a duration, WithDeadline for absolute time deadlines. Patterns for listening (<-ctx.Done()) in concurrent code, AfterFunc callbacks, and WithoutCancel for operations that must outlive their parent request (e.g., audit logs).

Context Values & Cross-Service Tracing — Safe context value patterns: unexported key types to prevent namespace collisions, when to use context values (request ID, user ID) vs function parameters. Trace context propagation: OpenTelemetry trace headers, correlation IDs for log aggregation, and marshaling/unmarshaling context across service boundaries.

Context in HTTP Servers & Service Calls — HTTP handler context: r.Context() for request-scoped cancellation, middleware integration, and propagating to services. HTTP client patterns: NewRequestWithContext, client timeouts, and retries with context awareness. Database operations: always use *Context variants (QueryContext, ExecContext) to respect deadlines.

Cross-References
→ See the samber/cc-skills-golang@golang-concurrency skill for goroutine cancellation patterns using context
→ See the samber/cc-skills-golang@golang-database skill for context-aware database operations (QueryContext, ExecContext)
→ See the samber/cc-skills-golang@golang-observability skill for trace context propagation with OpenTelemetry
→ See the samber/cc-skills-golang@golang-design-patterns skill for timeout and resilience patterns
Enforce with Linters

Many context pitfalls are caught automatically by linters: govet, staticcheck. → See the samber/cc-skills-golang@golang-lint skill for configuration and usage.

Weekly Installs
1.8K
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