---
rating: ⭐⭐
title: go-context
url: https://skills.sh/cxuu/golang-skills/go-context
---

# go-context

skills/cxuu/golang-skills/go-context
go-context
Installation
$ npx skills add https://github.com/cxuu/golang-skills --skill go-context
SKILL.md
Go Context Usage
Context as First Parameter

Functions that use a Context should accept it as their first parameter:

func F(ctx context.Context, /* other arguments */) error
func ProcessRequest(ctx context.Context, req *Request) (*Response, error)


This is a strong convention in Go that makes context flow visible and consistent across codebases.

Don't Store Context in Structs

Do not add a Context member to a struct type. Instead, pass ctx as a parameter to each method that needs it:

// Bad: Context stored in struct
type Worker struct {
    ctx context.Context  // Don't do this
}

// Good: Context passed to methods
type Worker struct{ /* ... */ }

func (w *Worker) Process(ctx context.Context) error {
    // Context explicitly passed — lifetime clear
}


Exception: Methods whose signature must match an interface in the standard library or a third-party library may need to work around this.

Don't Create Custom Context Types

Do not create custom Context types or use interfaces other than context.Context in function signatures:

// Bad: Custom context type
type MyContext interface {
    context.Context
    GetUserID() string
}

// Good: Use standard context.Context with value extraction
func Process(ctx context.Context) error {
    userID := GetUserID(ctx)
}

Where to Put Application Data

Consider these options in order of preference:

Function parameters — most explicit and type-safe
Receiver — for data that belongs to the type
Globals — for truly global configuration (use sparingly)
Context value — only for request-scoped data

Context values are appropriate for:

Request IDs and trace IDs
Authentication/authorization info that flows with requests
Deadlines and cancellation signals

Context values are not appropriate for:

Optional function parameters
Data that could be passed explicitly
Configuration that doesn't vary per-request
Common Patterns

Read references/PATTERNS.md when deriving contexts (WithTimeout, WithCancel, WithDeadline), checking cancellation in loops or HTTP handlers, using context values with typed keys, or needing the quick reference table.

Deriving Contexts

Always defer cancel() immediately after creating a derived context:

ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
defer cancel()

Checking Cancellation
select {
case <-ctx.Done():
    return ctx.Err()
default:
    // Do work
}

Context Immutability

Contexts are immutable — it's safe to pass the same ctx to multiple concurrent calls that share the same deadline and cancellation signal.

Related Skills
Goroutine coordination: See go-concurrency when using context for goroutine cancellation, select-based timeouts, or errgroup
Error handling: See go-error-handling when deciding how to wrap or return ctx.Err() cancellation errors
Interface design: See go-interfaces when designing APIs that accept context alongside interfaces
Request-scoped logging: See go-logging when injecting loggers into context or adding request IDs to structured log output
Weekly Installs
469
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