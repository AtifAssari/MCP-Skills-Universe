---
rating: ⭐⭐⭐
title: go-guide
url: https://skills.sh/ar4mirez/samuel/go-guide
---

# go-guide

skills/ar4mirez/samuel/go-guide
go-guide
Installation
$ npx skills add https://github.com/ar4mirez/samuel --skill go-guide
SKILL.md
Go Guide

Applies to: Go 1.21+, Microservices, APIs, CLIs

Core Principles
Simplicity: Prefer simple, readable code over clever solutions
Concurrency: Use goroutines and channels for concurrent operations
Errors Are Values: Explicit error handling, no exceptions
Composition Over Inheritance: Interfaces and struct embedding
Standard Library First: Rich stdlib, minimize dependencies
Guardrails
Version & Dependencies
Use Go 1.21+ with Go modules (go.mod)
Run go mod tidy before committing
Pin major versions in go.mod
Code Style
Run gofmt / goimports before every commit
Run go vet and golangci-lint before committing
Package names: lowercase, no underscores (userservice not user_service)
Exported: PascalCase | Unexported: camelCase
Follow Effective Go guidelines
Error Handling
Always check errors: if err != nil { return err }
Return errors, don't panic (panic only for unrecoverable)
Wrap errors with context: fmt.Errorf("fetch user: %w", err)
Use custom error types for domain errors
Don't ignore errors with _ unless justified with comment
Concurrency
Use context.Context for cancellation and timeouts
Always set timeout for HTTP requests
Use sync.WaitGroup for goroutine coordination
Close channels from sender side only
Use select with default to avoid blocking
Interfaces
Accept interfaces, return structs
Define interfaces where they're used (not where implemented)
Keep interfaces small (1-3 methods ideal)
Use io.Reader, io.Writer from stdlib when applicable
Project Structure
myproject/
├── cmd/                    # Main applications
│   └── api/
│       └── main.go        # Entry point
├── internal/              # Private application code
│   ├── domain/           # Business logic
│   ├── service/          # Application services
│   ├── repository/       # Data access
│   └── http/             # HTTP handlers
├── pkg/                   # Public libraries (reusable)
├── api/                   # OpenAPI/Protobuf specs
├── go.mod
├── go.sum
└── README.md

internal/ for private code (not importable by other projects)
pkg/ only for truly reusable libraries
cmd/ for executables (one per subdirectory)
No global variables (use dependency injection)
Error Handling Patterns
Basic Pattern
func GetUser(id string) (*User, error) {
    user, err := db.FindUserByID(id)
    if err != nil {
        return nil, fmt.Errorf("get user %s: %w", id, err)
    }
    return user, nil
}

Custom Errors
type NotFoundError struct {
    Resource string
    ID       string
}

func (e *NotFoundError) Error() string {
    return fmt.Sprintf("%s with ID %s not found", e.Resource, e.ID)
}

// Check with errors.As
var notFound *NotFoundError
if errors.As(err, &notFound) {
    // Handle not found
}

Testing
Standards
Test files: *_test.go (same package)
Test functions: func TestFunctionName(t *testing.T)
Table-driven tests for multiple cases
Use t.Helper() in test helpers
Use subtests: t.Run("name", func(t *testing.T) {...})
Coverage target: >80% for business logic
Benchmark critical paths: func BenchmarkFunction(b *testing.B)
Table-Driven Tests
func TestCalculate(t *testing.T) {
    tests := []struct {
        name     string
        a, b     int
        expected int
        wantErr  bool
    }{
        {"positive numbers", 2, 3, 5, false},
        {"negative numbers", -2, -3, -5, false},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            result, err := Calculate(tt.a, tt.b)
            if tt.wantErr {
                if err == nil {
                    t.Error("expected error, got nil")
                }
                return
            }
            if err != nil {
                t.Fatalf("unexpected error: %v", err)
            }
            if result != tt.expected {
                t.Errorf("got %d, want %d", result, tt.expected)
            }
        })
    }
}

Tooling
Essential Commands
go fmt ./...                # Format code
go vet ./...                # Detect suspicious constructs
go test ./...               # Run all tests
go test -cover ./...        # With coverage
go test -race ./...         # Race detector
go build ./cmd/api          # Build
go mod tidy                 # Clean dependencies
golangci-lint run           # Comprehensive lint

Linter Configuration
# .golangci.yml
linters:
  enable:
    - gofmt
    - govet
    - staticcheck
    - ineffassign
    - misspell
    - gosec        # Security
    - errcheck     # Unchecked errors
    - gocyclo      # Cyclomatic complexity
    - dupl         # Code duplication

linters-settings:
  gocyclo:
    min-complexity: 10
  dupl:
    threshold: 100

Advanced Topics

For detailed patterns and examples, see:

references/patterns.md — HTTP server, database, middleware, concurrency patterns
references/pitfalls.md — Common do/don't examples
references/security.md — Security best practices and examples
External References
Effective Go
Go Code Review Comments
Standard Go Project Layout
Go Proverbs
golangci-lint
Weekly Installs
12
Repository
ar4mirez/samuel
GitHub Stars
8
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass