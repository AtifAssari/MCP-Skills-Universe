---
rating: ⭐⭐⭐
title: software-csharp-backend
url: https://skills.sh/vasilyu1983/ai-agents-public/software-csharp-backend
---

# software-csharp-backend

skills/vasilyu1983/ai-agents-public/software-csharp-backend
software-csharp-backend
Installation
$ npx skills add https://github.com/vasilyu1983/ai-agents-public --skill software-csharp-backend
SKILL.md
C# Backend
Quick Reference
Start by defining boundary: API, application service, domain logic, infrastructure, or background worker.
Select runtime profile early: controller API, minimal API, background worker, or mixed host.
For systems with evolving domain boundaries, prefer modular architecture over premature service splits.
Apply C# language rules first: clarity, nullability, immutability, explicit failures, cancellation-aware async.
Keep dependency direction inward and keep I/O at boundaries.
Choose persistence per use case: Dapper for query-heavy SQL paths, EF Core for aggregate-heavy relational writes, Mongo for document-first modules.
Treat reliability, observability, and security as default behavior, not follow-up work.
Use iterative quality loop: code -> build -> run tests -> fix -> repeat.
If deep controller/CQRS endpoint design is required, switch to $csharp-api-cqrs and use its MediatR + FluentResults handler template.
If the task is primarily NUnit fixture design, WireMock/Testcontainers setup, or flake reduction, switch to $qa-testing-nunit.
If the task is primarily nuke/Build.cs, CI target sequencing, or artifact publication, switch to $ops-nuke-cicd.
If the task is primarily legacy ILogger or Serilog rewrite automation, switch to $dev-structured-logs.
Workflow
Classify the requested change (new feature, refactor, bug fix, review).
Choose runtime shape before implementation details. Load references/scenario-guides.md and, for HTTP services, references/aspnet-core-api-patterns.md.
Apply language and coding standards. Load references/csharp-language-practices.md and references/dotnet-coding-standards.md.
Confirm architecture and boundaries before editing internals. Load references/backend-architecture-principles.md and references/modular-architecture-principles.md.
Choose persistence and consistency strategy from query/write shape. Load references/data-access-patterns.md; if EF Core is selected, load references/efcore-persistence-patterns.md.
Add resilience behavior for outbound I/O and long-running work. Load references/reliability-and-resilience.md and references/resilience-policy-defaults.md.
Define tests by risk and boundary. Load references/testing-practices.md.
Add logs, traces, metrics, health probes, and operability defaults. Load references/observability-standards.md, and for API/runtime deployment defaults load references/runtime-ops-checklist.md.
Validate auth, validation, and secrets handling. Load references/security-baseline.md.
Run feedback loop validation for changed behavior. For NUKE-based repositories, run BuildAll, LocalUnitTest, ApiTest (when relevant), and TestAll; use $ops-nuke-cicd for pipeline-target edits.
Run final review against anti-pattern checklist. Load references/code-review-checklist.md.
Decision Tree
If the issue is naming, nullability, exception usage, or async flow, read references/csharp-language-practices.md.
If the issue is project layout, DI, configuration, or layering, read references/dotnet-coding-standards.md.
If the issue is service boundaries or clean architecture drift, read references/backend-architecture-principles.md.
If the issue is module boundaries, composition hosts, or modular-monolith tradeoffs, read references/modular-architecture-principles.md.
If the issue is API style, middleware ordering, validation behavior, health/readiness, or graceful shutdown, read references/aspnet-core-api-patterns.md.
If the issue is SQL/Mongo/EF access, pagination, transactions, idempotency, or N+1, read references/data-access-patterns.md.
If EF Core is selected for relational persistence, also read references/efcore-persistence-patterns.md.
If the issue is system profile specific (high-throughput API, event-driven worker, multi-tenant service), read references/scenario-guides.md.
If the issue is retry/timeout/circuit behavior, cancellation propagation, or worker reliability, read references/reliability-and-resilience.md and references/resilience-policy-defaults.md.
If the issue is container/runtime readiness, startup config validation, caching defaults, or deployment reliability gates, read references/runtime-ops-checklist.md.
If the issue is target framework constraints, package/API compatibility, multi-targeting, or migration between .NET Framework/netstandard2.0 and modern .NET, read references/version-compatibility-notes.md.
If the issue is flaky tests or weak coverage strategy, read references/testing-practices.md.
If the issue is logs/traces/metrics/health checks, read references/observability-standards.md.
If the issue is input validation, auth boundaries, secret handling, or secure defaults, read references/security-baseline.md.
If the task is reviewing a PR for backend quality risks, read references/code-review-checklist.md.
If the task is designing or fixing build-test pipeline loop behavior, use $ops-nuke-cicd.
If the task needs deep HTTP controller + CQRS error-contract design, use $csharp-api-cqrs with MediatR + FluentResults conventions.
Do / Avoid

Do

Keep application services small and explicit about dependencies.
Return deterministic domain/application results for expected failures.
Pass CancellationToken through every async layer and external call.
Model options with validation and fail fast on invalid startup config.
Choose API style intentionally and keep middleware ordering explicit.
Keep persistence choices aligned to use-case shape, not team habit.
Make telemetry and security checks part of definition of done.

Avoid

Coupling domain logic directly to HTTP, DB driver types, or framework-specific classes.
Using retries without timeout and idempotency guarantees.
Swallowing exceptions or replacing root causes with vague error messages.
Mixing unit and integration concerns in the same test fixture.
Using async void outside event handlers.
Sharing one DbContext instance across concurrent operations/threads.
Captive dependencies (singleton depending on scoped service).
Shipping endpoints without structured logs, traces, metrics, and health signals.
Resources
C# Language Practices
Dotnet Coding Standards
Backend Architecture Principles
Modular Architecture Principles
ASP.NET Core API Patterns
Data Access Patterns
EF Core Persistence Patterns
Scenario Guides
Reliability and Resilience
Resilience Policy Defaults
Testing Practices
Observability Standards
Runtime Ops Checklist
Version Compatibility Notes
Security Baseline
Code Review Checklist
Skill Data: curated Microsoft references plus modular-architecture example context.
Templates
Service Class Template
Options Configuration Template
Resilient HTTP Client Template
Dapper Query Handler Template
Mongo Repository Template
Test Data Builder Template
Pull Request Checklist Template
Weekly Installs
43
Repository
vasilyu1983/ai-…s-public
GitHub Stars
59
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass