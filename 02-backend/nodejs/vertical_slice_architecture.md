---
rating: ⭐⭐⭐
title: vertical-slice-architecture
url: https://skills.sh/mryll/skills/vertical-slice-architecture
---

# vertical-slice-architecture

skills/mryll/skills/vertical-slice-architecture
vertical-slice-architecture
Installation
$ npx skills add https://github.com/mryll/skills --skill vertical-slice-architecture
SKILL.md
Vertical Slice Architecture
Quick Reference: The 5 Rules
One feature = one directory containing handler, request/response types, validation, and tests
One entry point per feature — a setup/registration function that receives the router and dependencies. Name varies by convention (Setup, RegisterRoute, Map); the role is the invariant, not the name.
Minimize coupling between slices, maximize coupling within a slice
No premature abstractions — no shared repository/service layers until genuine duplication emerges across multiple slices
Test each feature primarily through its entry point, verifying outcomes (DB state, API calls, response). Platform/adapter tests are also encouraged.
Project Structure
{project}/
  features/              # or internal/features/ (Go), Features/ (.NET)
    {domain}/            # orders/, users/, kvs/
      {operation}/       # create/, list/, delete/
        handler          # Single entry point + orchestration
        request/response # DTOs
        validator        # Input validation (optional)
        test             # Co-located integration test
        internal/        # Feature-private helpers (optional)
  platform/              # or Infrastructure/ — shared cross-cutting concerns
    middleware/           # Auth, error handling, idempotency
    database/            # Connection pooling, circuit breakers
    observability/       # Metrics, tracing, structured logging
    opqueue/             # Operation queues, outbox patterns (if needed)
  main                   # Composition root wires features + infrastructure

Workflow: Adding a New Feature
Create directory: features/{domain}/{operation}/
Define the handler with a single exported setup function
Define request/response types (inline for simple cases)
Add validation logic
Register in the composition root (main)
Write integration test that calls the setup function, sends request, verifies outcomes
Workflow: Adding Cross-Cutting Concerns

Place in platform/ (not inside a feature). Examples:

Auth middleware, error handling, request logging
Database connection pooling, circuit breakers
Idempotency middleware, operation queues, event notifications
Observability (metrics, tracing, structured logging)
Workflow: Extracting Shared Logic

Only extract when genuine duplication emerges across multiple slices (use judgment — the "3+ slices" heuristic is guidance, not a hard rule):

Duplicate business rule: extract to a domain entity/value object
Duplicate data access pattern: extract to a shared repository (only for that specific pattern)
Duplicate HTTP helper: extract to platform/httpx/
Key Decisions by Language

Detect the project's language/framework and consult the appropriate reference:

Patterns per language: See references/patterns-by-language.md for Go, .NET, Java, TypeScript, Python
Testing per language: See references/testing.md for testcontainers, mock verification, integration test patterns
Core principles: See references/principles.md for detailed rules, anti-patterns, and shared domain model guidance
Single Entry Point Contract

Every feature exposes one primary setup/registration function. Internal types stay private. The entry point name is conventional — the invariant is: one public function per feature that wires the slice to the framework.

Language	Convention	Signature	DI mechanism
Go	Setup or RegisterRoute	func Setup(r gin.IRoutes, repo Repository)	Explicit params
.NET	Map (static)	static void Map(IEndpointRouteBuilder app)	DI container resolves deps in handler
Java/Kotlin	@RestController class	Controller discovered by component scan	Spring DI (constructor injection)
TypeScript	setup	function setup(router: Router, db: Database): void	Explicit params
Python	setup	def setup(router: APIRouter, db: Database) -> None	Explicit params or Depends()

Exceptions: Versioned APIs may have SetupV1/SetupV2 wrappers sharing internal handler wiring. Frameworks with auto-discovery (Spring, NestJS) use the controller/module class itself as the entry point.

Testing

See references/testing.md for full testing strategy per language, including feature integration tests, platform/adapter tests, mock verification patterns, and test naming conventions.

Weekly Installs
136
Repository
mryll/skills
GitHub Stars
1
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass