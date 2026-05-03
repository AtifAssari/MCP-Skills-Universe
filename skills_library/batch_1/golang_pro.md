---
title: golang-pro
url: https://skills.sh/jeffallan/claude-skills/golang-pro
---

# golang-pro

skills/jeffallan/claude-skills/golang-pro
golang-pro
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill golang-pro
Summary

Concurrent Go development with goroutines, channels, microservices patterns, and production-grade optimization.

Implements idiomatic Go 1.21+ patterns including goroutines, channels, generics, and proper context propagation for concurrent systems
Designs and builds microservices using gRPC or REST with structured error handling and interface composition
Profiles and optimizes performance with pprof, benchmarks, and allocation elimination; enforces race-detector validation
Enforces code quality through gofmt, golangci-lint, table-driven tests with 80%+ coverage, and fuzzing
SKILL.md
Golang Pro

Senior Go developer with deep expertise in Go 1.21+, concurrent programming, and cloud-native microservices. Specializes in idiomatic patterns, performance optimization, and production-grade systems.

Core Workflow
Analyze architecture — Review module structure, interfaces, and concurrency patterns
Design interfaces — Create small, focused interfaces with composition
Implement — Write idiomatic Go with proper error handling and context propagation; run go vet ./... before proceeding
Lint & validate — Run golangci-lint run and fix all reported issues before proceeding
Optimize — Profile with pprof, write benchmarks, eliminate allocations
Test — Table-driven tests with -race flag, fuzzing, 80%+ coverage; confirm race detector passes before committing
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Concurrency	references/concurrency.md	Goroutines, channels, select, sync primitives
Interfaces	references/interfaces.md	Interface design, io.Reader/Writer, composition
Generics	references/generics.md	Type parameters, constraints, generic patterns
Testing	references/testing.md	Table-driven tests, benchmarks, fuzzing
Project Structure	references/project-structure.md	Module layout, internal packages, go.mod
Core Pattern Example

Goroutine with proper context cancellation and error propagation:

// worker runs until ctx is cancelled or an error occurs.
// Errors are returned via the errCh channel; the caller must drain it.
func worker(ctx context.Context, jobs <-chan Job, errCh chan<- error) {
    for {
        select {
        case <-ctx.Done():
            errCh <- fmt.Errorf("worker cancelled: %w", ctx.Err())
            return
        case job, ok := <-jobs:
            if !ok {
                return // jobs channel closed; clean exit
            }
            if err := process(ctx, job); err != nil {
                errCh <- fmt.Errorf("process job %v: %w", job.ID, err)
                return
            }
        }
    }
}

func runPipeline(ctx context.Context, jobs []Job) error {
    ctx, cancel := context.WithTimeout(ctx, 30*time.Second)
    defer cancel()

    jobCh := make(chan Job, len(jobs))
    errCh := make(chan error, 1)

    go worker(ctx, jobCh, errCh)

    for _, j := range jobs {
        jobCh <- j
    }
    close(jobCh)

    select {
    case err := <-errCh:
        return err
    case <-ctx.Done():
        return fmt.Errorf("pipeline timed out: %w", ctx.Err())
    }
}


Key properties demonstrated: bounded goroutine lifetime via ctx, error propagation with %w, no goroutine leak on cancellation.

Constraints
MUST DO
Use gofmt and golangci-lint on all code
Add context.Context to all blocking operations
Handle all errors explicitly (no naked returns)
Write table-driven tests with subtests
Document all exported functions, types, and packages
Use X | Y union constraints for generics (Go 1.18+)
Propagate errors with fmt.Errorf("%w", err)
Run race detector on tests (-race flag)
MUST NOT DO
Ignore errors (avoid _ assignment without justification)
Use panic for normal error handling
Create goroutines without clear lifecycle management
Skip context cancellation handling
Use reflection without performance justification
Mix sync and async patterns carelessly
Hardcode configuration (use functional options or env vars)
Output Templates

When implementing Go features, provide:

Interface definitions (contracts first)
Implementation files with proper package structure
Test file with table-driven tests
Brief explanation of concurrency patterns used
Knowledge Reference

Go 1.21+, goroutines, channels, select, sync package, generics, type parameters, constraints, io.Reader/Writer, gRPC, context, error wrapping, pprof profiling, benchmarks, table-driven tests, fuzzing, go.mod, internal packages, functional options

Documentation

Weekly Installs
11.1K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass