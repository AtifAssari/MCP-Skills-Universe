---
rating: ⭐⭐⭐
title: go-backend-microservices
url: https://skills.sh/mindrally/skills/go-backend-microservices
---

# go-backend-microservices

skills/mindrally/skills/go-backend-microservices
go-backend-microservices
Installation
$ npx skills add https://github.com/mindrally/skills --skill go-backend-microservices
SKILL.md
Go Backend Development for Microservices
Core Principles
Apply Clean Architecture with clear separation into handlers, services, repositories, and domain models
Prioritize interface-driven development with explicit dependency injection
Write short, focused functions with a single responsibility
Ensure safe use of goroutines, and guard shared state with channels or sync primitives
Project Structure

Maintain modular project structure with clear directories:

project/
├── cmd/           # Application entry points
├── internal/      # Private application code
├── pkg/           # Public library code
├── api/           # API definitions (OpenAPI, protobuf)
├── configs/       # Configuration files
└── test/          # Additional test utilities

Error Handling
Always check and handle errors explicitly
Use wrapped errors for traceability: fmt.Errorf("context: %w", err)
Create custom error types for domain-specific errors
Return errors up the call stack with appropriate context
Log errors at the appropriate level with sufficient context
Context Propagation
Use context propagation for request-scoped values, deadlines, and cancellations
Pass context as the first parameter to functions
Respect context cancellation in long-running operations
Set appropriate timeouts for external calls
Observability

Implement OpenTelemetry for comprehensive observability:

Distributed Tracing
Add spans for significant operations
Propagate trace context across service boundaries
Include relevant attributes in spans
Metrics
Implement custom metrics for business operations
Use standard metric types (counters, gauges, histograms)
Export metrics in Prometheus format
Structured Logging
Use structured logging with consistent field names
Include trace IDs in log entries
Log at appropriate levels (debug, info, warn, error)
Security
Apply input validation rigorously on all external inputs
Use secure defaults for JWT tokens and cookies
Implement proper authentication and authorization
Sanitize data before logging to avoid leaking sensitive information
Use prepared statements for database queries
Testing
Unit Tests
Write table-driven unit tests with adequate coverage
Use parallel test execution where safe
Mock external dependencies using interfaces
Focus on testing business logic
Integration Tests
Separate integration tests from unit tests
Use test containers for database and service dependencies
Test actual API endpoints and responses
Concurrency
Use goroutines appropriately for concurrent operations
Guard shared state with channels or sync primitives
Implement proper graceful shutdown
Use worker pools for bounded concurrency
Documentation
Document with GoDoc-style comments
Keep comments up to date with code changes
Document public APIs thoroughly
Include examples in documentation where helpful
CI/CD Integration
Maintain CI integration for linting and testing
Use golangci-lint for comprehensive linting
Run tests on every pull request
Include code coverage reporting
Weekly Installs
310
Repository
mindrally/skills
GitHub Stars
88
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass