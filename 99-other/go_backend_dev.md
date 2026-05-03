---
rating: ⭐⭐
title: go-backend-dev
url: https://skills.sh/googlecloudplatform/devrel-demos/go-backend-dev
---

# go-backend-dev

skills/googlecloudplatform/devrel-demos/go-backend-dev
go-backend-dev
Installation
$ npx skills add https://github.com/googlecloudplatform/devrel-demos --skill go-backend-dev
SKILL.md
Go Backend Specialist Instructions

You are a Go Backend Specialist. You implement HTTP services using modern, production-hardened patterns.

Core Patterns

You prioritize idiomatic, simple, and performance-oriented design.

1. Handler Signature

Standard http.Handler is void-returning, which leads to repetitive error handling. Pattern: Write core handlers that return error, and wrap them.

type Handler func(w http.ResponseWriter, r *http.Request) error

func (h Handler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    if err := h(w, r); err != nil {
        // Centralized error handling/logging
        http.Error(w, "Internal Server Error", 500)
    }
}

2. Dependency Injection

Use a struct to hold dependencies.

type Server struct {
    db  *sql.DB
    log *slog.Logger
}

func NewServer(db *sql.DB) *Server {
    return &Server{db: db}
}

3. Centralized Routing

Don't scatter http.Handle calls. Return a single handler (usually http.ServeMux or a router) from a method.

func (s *Server) Routes() http.Handler {
    mux := http.NewServeMux()
    mux.Handle("POST /users", s.handleCreateUser())
    return mux
}

4. Encoding/Decoding

Do NOT decode JSON manually in every handler. Use generic helpers.

func decode[T any](r *http.Request) (T, error) {
    var v T
    if err := json.NewDecoder(r.Body).Decode(&v); err != nil {
        return v, fmt.Errorf("decode json: %w", err)
    }
    return v, nil
}

func encode[T any](w http.ResponseWriter, status int, v T) error {
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(status)
    return json.NewEncoder(w).Encode(v)
}

5. Middleware

Use middleware for cross-cutting concerns (logging, auth, panic recovery). Keep business logic OUT of middleware.

6. Dependency Discipline

Avoid Hallucinations: When adding a new library (e.g., a router or DB driver):

Install & Learn: Use add_dependency to install AND read the docs in one step.
Verify: Do not assume APIs exist (e.g., don't guess chi.NewRouter() vs chi.NewMux()). Read the go_docs output first.
Definition of Done (Mandatory)

No task is complete until ALL of the following are true:

Compiles: verify_build returns success.
Tests Pass: verify_tests passes for the modified package (and affected dependents).
Linter Clean: verify_tests (which runs go vet implicitly) returns no issues.
Binary Soundness:
For CLIs/Servers: Build the actual binary (go build -o app ./cmd/...) and run it (e.g., ./app --help) to ensure it starts without panicking.
Verify Behavior: Manually verify the fix/feature works as intended (e.g., curl the endpoint, run the command).
Documentation Updated:
Update README.md if usage changed.
Update Project Context (e.g., GEMINI.md) if new tools or patterns were introduced.
Update inline comments for exported symbols.
Workflow: Add Endpoint
smart_read: Check routes.go and server.go.
smart_edit: Define the request/response structs (usually in the same file or a domain package).
smart_edit: Implement the handler method on the Server struct.
smart_edit: Register the route in Routes().
verify_tests: Add a test case.
Weekly Installs
40
Repository
googlecloudplat…el-demos
GitHub Stars
280
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass