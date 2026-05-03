---
rating: ⭐⭐⭐
title: golang
url: https://skills.sh/anntnzrb/agents/golang
---

# golang

skills/anntnzrb/agents/golang
golang
Installation
$ npx skills add https://github.com/anntnzrb/agents --skill golang
SKILL.md
Golang Development Skill
Activation Triggers
Working with .go files, go.mod, go.sum, go.work
User mentions Go, Golang, or Go-specific terms
Questions about Go libraries, frameworks, or tooling
Concurrency patterns (goroutines, channels, context)
Workflow: Research-First Approach

Before implementing, gather context from authoritative sources:

# Context7 docs for repo-specific guidance
context7 docs /gin-gonic/gin "how to set up middleware"
context7 docs /uber-go/zap "structured logging setup"

# gh search code for real-world implementation examples
gh search code "ratelimit.New(" --language=go
gh search code "errgroup.WithContext(" --language=go

# For style/idiom questions
context7 docs /uber-go/guide "style guide patterns and idioms"

Notes

Repository routing table lives in reference.md.

CLI Quick Reference
Module Management
go mod init <module>       # Initialize module
go mod tidy                # Sync dependencies
go get <pkg>@latest        # Add/update dependency
go get <pkg>@v1.2.3        # Specific version
go mod download            # Download dependencies
go mod why <pkg>           # Why is pkg needed
go mod graph               # Dependency graph

Build & Run
go build ./...             # Build all packages
go run .                   # Run current package
go install ./cmd/...       # Install binaries
go generate ./...          # Run go:generate directives

Testing
go test ./...              # Run all tests
go test -v ./...           # Verbose output
go test -race ./...        # Race detector
go test -cover ./...       # Coverage summary
go test -coverprofile=c.out ./... && go tool cover -html=c.out  # Coverage HTML
go test -bench=. ./...     # Run benchmarks
go test -fuzz=FuzzXxx ./...  # Fuzz testing
go test -run=TestName      # Run specific test
go test -count=1           # Disable test caching

Linting (golangci-lint)
golangci-lint run          # Run all linters
golangci-lint run --fix    # Auto-fix issues
golangci-lint linters      # List available linters

Workspaces (multi-module)
go work init ./mod1 ./mod2 # Initialize workspace
go work use ./mod3         # Add module to workspace
go work sync               # Sync workspace

Other Tools
go fmt ./...               # Format code
go vet ./...               # Static analysis
go doc <pkg>               # View documentation
go env                     # Environment variables
go version                 # Go version

Files
reference.md - Go 1.24+ features, project layout, Uber style highlights
cookbook/testing.md - Table-driven tests, testify, mocking, benchmarks
cookbook/concurrency.md - Goroutines, channels, context, errgroup
cookbook/patterns.md - Functional options, DI, error handling
Weekly Installs
17
Repository
anntnzrb/agents
GitHub Stars
1
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn