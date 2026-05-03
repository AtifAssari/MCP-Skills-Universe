---
title: writing-server-code
url: https://skills.sh/bitwarden/ai-plugins/writing-server-code
---

# writing-server-code

skills/bitwarden/ai-plugins/writing-server-code
writing-server-code
Installation
$ npx skills add https://github.com/bitwarden/ai-plugins --skill writing-server-code
SKILL.md
Repository Orientation

The server repo contains:

src/Api — REST API endpoints
src/Identity — Authentication/identity service
src/Core — Business logic, commands, queries, services
src/Infrastructure — Data access, repositories
Architectural Rationale
Command Query Separation (CQS)

New features should use the CQS pattern — discrete action classes instead of large entity-focused services. See ADR-0008.

Why CQS matters at Bitwarden: The codebase historically grew around entity-focused services (e.g., CipherService) that accumulated hundreds of methods. CQS breaks these into single-responsibility classes (CreateCipherCommand, GetOrganizationApiKeyQuery), making code easier to test, reason about, and modify without unintended side effects.

Commands = write operations. Change state, may return result. Named after the action: RotateOrganizationApiKeyCommand.

Queries = read operations. Return data, never change state.

When NOT to use CQS: When modifying existing service-based code, follow the patterns already in the file. Don't refactor to CQS unless explicitly asked. If asked to refactor, apply the pattern only to the scope requested.

Caching

When caching is needed, follow the conventions in CACHING.md. Use IFusionCache instead of IDistributedCache.

Don't implement caching unless requested. If a user describes a performance problem where caching might help, suggest it — but don't implement without confirmation.

GUID Generation

Always use CoreHelpers.GenerateComb() for entity IDs — never Guid.NewGuid(). Sequential COMBs prevent SQL Server index fragmentation that random GUIDs cause on clustered indexes, which is critical for Bitwarden's database performance at scale.

Critical Rules

These are the most frequently violated conventions. Claude cannot fetch the linked docs at runtime, so these are inlined here:

Use TryAdd* for DI registration (TryAddScoped, TryAddTransient) — prevents duplicate registrations when multiple modules register the same service
File-scoped namespaces — namespace Bit.Core.Vault; not namespace Bit.Core.Vault { ... }
Nullable reference types are enabled (ADR-0024) — use ! (null-forgiving) when you know a value isn't null; use required modifier for properties that must be set during construction
Async suffix on all async methods — CreateAsync, not Create, when the method returns Task
Controller actions return ActionResult<T> — not IActionResult or bare T
Testing with xUnit — use [Theory, BitAutoData] (not [AutoData]), SutProvider<T> for automatic SUT wiring, and Substitute.For<T>() from NSubstitute for mocking
Examples
GUID generation
// CORRECT — sequential COMB prevents index fragmentation
var id = CoreHelpers.GenerateComb();

// WRONG — random GUIDs fragment clustered indexes
var id = Guid.NewGuid();

DI registration
// CORRECT — idempotent, won't duplicate
services.TryAddScoped<ICipherService, CipherService>();

// WRONG — silently duplicates registration, last-wins causes subtle bugs
services.AddScoped<ICipherService, CipherService>();

Namespace style
// CORRECT — file-scoped
namespace Bit.Core.Vault.Commands;

// WRONG — block-scoped
namespace Bit.Core.Vault.Commands
{
    // ...
}

Further Reading
C# code style
Server architecture
Weekly Installs
33
Repository
bitwarden/ai-plugins
GitHub Stars
90
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass