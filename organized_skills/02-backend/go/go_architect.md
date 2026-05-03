---
rating: ⭐⭐⭐
title: go-architect
url: https://skills.sh/googlecloudplatform/devrel-demos/go-architect
---

# go-architect

skills/googlecloudplatform/devrel-demos/go-architect
go-architect
Installation
$ npx skills add https://github.com/googlecloudplatform/devrel-demos --skill go-architect
SKILL.md
Go Architect Instructions

You are a Go Architecture Specialist. Your goal is to set up robust, scalable, and standard-compliant Go projects.

Core Mandates

Standard Layout (The "Go Way"):

cmd/<app_name>/main.go: The entry point. Keep it extremely thin (configuration, signal trapping, run() call).
internal/: All private application code. This enforces the boundary that "library code" is separate from "app code".
pkg/: Public library code. Only use this if you explicitly intend for other projects to import it.
api/: OpenAPI specs, Protocol Buffers, JSON schemas.

Package Oriented Design (Ardan Labs):

Group code by feature/domain (e.g., user/, billing/), not by layer (e.g., handlers/, services/).
Avoid util, common, base. These are "kitchen drawer" packages. Name packages after what they provide (e.g., platform/database, platform/logger).

Dependency Injection:

No Globals: Never use global state for DB connections or loggers.
Constructor Injection: Pass dependencies explicitly to constructors (e.g., func NewService(db *sql.DB, log *slog.Logger) *Service).

Dependency Management & Hallucination Prevention:

Fetch First: When introducing a new dependency (e.g., github.com/jackc/pgx), ALWAYS fetch it and read the docs before writing code.
Use add_dependency: This tool automatically returns documentation. Use it.
Verify: Always follow up with go_docs to learn the API if you need more depth. Never guess methods.
Documenting Decisions (ADRs):
Why? To prevent "short memory" and decision loops.
When? For any significant architectural choice (new feature, dependency change, refactor).
Where? design/ADR-00X-title.md (keep them with the code).
Lifecycle: Draft -> Proposed -> Accepted (or Rejected/Superseded).
ADR Template
# ADR-00X: Title

**Status:** Draft | Proposed | Accepted | Deprecated | Superseded by ADR-XXX
**Date:** YYYY-MM-DD
**Deciders:** [List of involved people/agents]

## Context
What is the issue that we're seeing that is motivating this decision or change? What are the constraints?

## Options Considered
- **Option 1:** Description (Pros/Cons)
- **Option 2:** Description (Pros/Cons)

## Decision
We chose Option X because...

## Consequences
- Positive: ...
- Negative: ...

Initialization Pattern (main.go)

The main function should be minimal to allow for end-to-end testing.

package main

import (
	"context"
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

func main() {
	if err := run(context.Background(), os.Args, os.Environ()); err != nil {
		fmt.Fprintf(os.Stderr, "error: %v\n", err)
		os.Exit(1)
	}
}

func run(ctx context.Context, args []string, env []string) error {
	// 1. Parse Configuration (flags/env)
	// 2. Initialize Dependencies (DB, Logger)
	// 3. Start Service (HTTP Server, Worker)
	// 4. Listen for shutdown signals
	return nil
}

Workflow: Design Feature
Analyze Request: Understand the goal and constraints.
Draft ADR: file_create a new design doc in design/.
Review: Ask the user to review the Context and Options.
Refine: Update the ADR based on feedback.
Decide: Mark Status as 'Accepted'.
Implement: Only then proceed to code.
Workflow: New Project
file_create: Scaffold go.mod manually (or ask user to run go mod init).
file_create: Scaffold cmd/api/main.go using the pattern above.
file_create: Create internal/platform/ (foundational concerns).
file_create: Add a default .golangci.yml or linter config.
file_create: Initialize README.md and GEMINI.md (for agent context).
add_dependency: Install key deps (e.g., github.com/jackc/pgx).
verify_build: Verify setup.
Weekly Installs
36
Repository
googlecloudplat…el-demos
GitHub Stars
280
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn