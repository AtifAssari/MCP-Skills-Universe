---
title: golang-senior-lead
url: https://skills.sh/modra40/claude-codex-skills-directory/golang-senior-lead
---

# golang-senior-lead

skills/modra40/claude-codex-skills-directory/golang-senior-lead
golang-senior-lead
Installation
$ npx skills add https://github.com/modra40/claude-codex-skills-directory --skill golang-senior-lead
SKILL.md
Golang Senior/Lead Developer Expertise

Skill ini mengandung accumulated wisdom dari 20+ tahun production experience. Setiap recommendation sudah battle-tested di high-traffic systems.

Core Philosophy

KISS (Keep It Stupid Simple) - Kode terbaik adalah kode yang tidak perlu ditulis. Setiap line of code adalah liability.

Less is More - Jangan over-engineer. Solve today's problem, not imaginary future problems. YAGNI (You Ain't Gonna Need It).

Explicit over Implicit - Go menghargai explicitness. Jangan gunakan magic. Kode harus readable tanpa documentation.

Fail Fast, Fail Loud - Error harus di-handle segera, jangan di-ignore. Panic early jika state tidak valid.

Project Structure (Production-Grade)
project-name/
├── cmd/                    # Entry points (main packages)
│   ├── api/               
│   │   └── main.go        # HTTP API server
│   └── worker/            
│       └── main.go        # Background worker
├── internal/               # Private packages (tidak bisa di-import external)
│   ├── domain/            # Business entities & interfaces (CORE)
│   │   ├── user.go        # Entity + Repository interface
│   │   └── order.go
│   ├── usecase/           # Business logic (orchestration)
│   │   └── user/
│   │       ├── service.go
│   │       └── service_test.go
│   ├── repository/        # Data access implementations
│   │   └── postgres/
│   │       └── user.go
│   ├── handler/           # HTTP/gRPC handlers
│   │   └── http/
│   │       └── user.go
│   └── pkg/               # Internal shared utilities
│       ├── validator/
│       └── logger/
├── pkg/                    # Public packages (bisa di-import external)
├── config/                 # Configuration files
├── migrations/             # Database migrations
├── scripts/                # Build/deploy scripts
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── go.mod
├── go.sum
├── Makefile
└── .golangci.yml          # Linter config


Critical Rules:

internal/ = private, tidak bisa di-import dari luar module
domain/ = ZERO dependencies ke infrastructure. Pure business logic.
Dependency flow: handler → usecase → repository. NEVER backwards.
Error Handling Golden Rules
// ❌ NEVER ignore errors
result, _ := someFunction()

// ✅ ALWAYS handle or propagate
result, err := someFunction()
if err != nil {
    return fmt.Errorf("someFunction failed: %w", err) // wrap with context
}

// ❌ NEVER use panic for expected errors
if user == nil {
    panic("user not found") // WRONG!
}

// ✅ Return error for expected failures
if user == nil {
    return nil, ErrUserNotFound
}

// Sentinel errors (define di package level)
var (
    ErrNotFound     = errors.New("not found")
    ErrUnauthorized = errors.New("unauthorized")
)

Concurrency Patterns (Race Condition Prevention)

Lihat references/concurrency.md untuk patterns lengkap.

Quick Rules:

Selalu gunakan sync.Mutex untuk shared state
Prefer channels untuk communication, mutex untuk state protection
SELALU run go test -race ./... sebelum merge
Gunakan context.Context untuk cancellation propagation
Docker Best Practices

Lihat references/docker.md untuk Dockerfile dan docker-compose templates.

Quick Rules:

Multi-stage builds untuk minimal image size
Non-root user untuk security
.dockerignore wajib
Health checks wajib untuk orchestration
Pin specific versions, NEVER use latest
Recommended Libraries (Battle-Tested)

Lihat references/libraries.md untuk complete list dengan use cases.

Essential Stack:

Category	Library	Reason
HTTP Router	chi atau gin	Chi lebih Go-idiomatic, Gin lebih feature-rich
Database	sqlx + pgx	Raw SQL power + type safety
Validation	validator/v10	De-facto standard
Config	viper atau envconfig	Viper untuk complex, envconfig untuk simple
Logging	zerolog atau zap	Structured, fast, production-ready
Testing	testify + testcontainers	Assertions + integration tests
Debugging Workflow

Lihat references/debugging.md untuk advanced techniques.

Quick Commands:

# Race detector
go test -race ./...

# CPU profiling
go test -cpuprofile cpu.prof -bench .

# Memory profiling  
go test -memprofile mem.prof -bench .

# Deadlock detection
GODEBUG=schedtrace=1000 ./app

# Detailed stack traces
GOTRACEBACK=all ./app

Code Review Checklist

Sebelum approve PR, pastikan:

Error Handling - Semua error di-handle, tidak ada _ untuk error
Race Conditions - Shared state dilindungi, go test -race pass
Resource Leaks - Semua defer Close() ada, context digunakan
Tests - Unit tests ada, edge cases covered
Naming - Clear, Go conventions (MixedCaps, not snake_case)
Simplicity - Tidak over-engineered, KISS principle
Testing Strategy
// Table-driven tests (Go idiom)
func TestCalculatePrice(t *testing.T) {
    tests := []struct {
        name     string
        input    float64
        expected float64
        wantErr  bool
    }{
        {"normal price", 100, 110, false},
        {"zero price", 0, 0, false},
        {"negative price", -1, 0, true},
    }
    
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got, err := CalculatePrice(tt.input)
            if (err != nil) != tt.wantErr {
                t.Errorf("error = %v, wantErr %v", err, tt.wantErr)
            }
            if got != tt.expected {
                t.Errorf("got %v, want %v", got, tt.expected)
            }
        })
    }
}

Performance Quick Wins
Preallocate slices - make([]T, 0, expectedSize)
Avoid string concatenation in loops - Use strings.Builder
Sync.Pool untuk frequent allocations
Buffer channels - Prevent goroutine blocking
Index database queries - Explain analyze sebelum deploy
Common Pitfalls to Avoid
Pitfall	Consequence	Prevention
Nil pointer dereference	Panic crash	Always check nil before access
Goroutine leak	Memory leak	Use context for cancellation
Closing nil channel	Panic	Check before close
Data race	Undefined behavior	go test -race
Slice append gotcha	Data corruption	Copy when needed
Additional References
references/concurrency.md - Concurrency patterns lengkap
references/docker.md - Docker templates dan best practices
references/libraries.md - Complete library recommendations
references/debugging.md - Advanced debugging techniques
references/patterns.md - Design patterns untuk Go
Weekly Installs
12
Repository
modra40/claude-…irectory
GitHub Stars
5
First Seen
Jan 24, 2026