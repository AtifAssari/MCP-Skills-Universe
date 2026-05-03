---
rating: ⭐⭐⭐
title: qa-testing-nunit
url: https://skills.sh/vasilyu1983/ai-agents-public/qa-testing-nunit
---

# qa-testing-nunit

skills/vasilyu1983/ai-agents-public/qa-testing-nunit
qa-testing-nunit
Installation
$ npx skills add https://github.com/vasilyu1983/ai-agents-public --skill qa-testing-nunit
SKILL.md
C# Testing NUnit Fixtures
Quick Reference
Classify test scope first: API, component, or integration.
Lock runtime constraints before execution: Docker availability, framework target, and explicitly excluded suites.
Use this skill for test-suite architecture and fixture behavior, not for general service implementation or CI graph refactors.
Default to two files per handler/use case: <Feature>Fixture.cs and <Feature>Tests.cs.
For full-cycle API tests, use controller-focused structure: one fixture per controller/test family and one base ApiTest.cs + ApiFixture.cs (split by scenario family only when needed).
Do not translate SpecFlow/Taffy step definitions into C# line-by-line; rewrite scenario intent into idiomatic API tests.
For API migrations, avoid one global shared setup fixture; each controller/test family fixture owns its own dependencies.
Fixture ownership for API tests should include DB launcher + migrators + WireMock + WebApplicationFactory + client.
Reset mutable state in [SetUp]; dispose all owned infra in [OneTimeTearDown].
For DB bootstrapping, follow pricing-style DatabaseLauncher + MigratorContainer from tests/utils/Sc.Fin.Pricing.Tests.Utils/Testcontainers.
Use canonical migrator command dotnet Sc.Tool.FluentMigrator.dll migrateup -m /sql and avoid custom ready-check arguments in tests.
Keep migrator ordering explicit (dependency migrators first, domain migrator last) and support fixture-level optional migrator toggles when some suites do not need all DBs.
Add explicit migrator verification tests that assert launcher startup, migrator completion/order, and required tables.
Use iterative quality loop: code -> build -> run tests -> fix -> repeat.
For health endpoints, use [Test] + [TestCase] + [CancelAfter(...)] with method signature (string url, CancellationToken cancellationToken); keep [Test] together with [TestCase] to avoid NUnit analyzer issues.
If user excludes infra-dependent suites (for example component tests requiring Docker), run feasible categories first and report exactly what remains unvalidated.
If the task shifts into service design or backend refactoring, switch to $software-csharp-backend.
If the task shifts into nuke/Build.cs, category target wiring, or CI artifact publication, switch to $ops-nuke-cicd.
Workflow
Define boundary, dependencies, expected assertion depth, and environment constraints. Load references/nunit-structure.md.
Select fixture composition and lifecycle. Load references/fixture-pattern.md and references/testing-templates.md.
Implement scenario tests for the target layer. Load references/api-testing-nunit.md or references/component-testing-nunit.md.
Choose double vs real dependency strategy. Load references/dependency-strategy-matrix.md, then references/wiremock-setup.md or references/testcontainers-setup.md.
Add resilient async and eventual-consistency assertions. Load references/async-eventual-assertions.md.
Harden suite against flaky behavior. Load references/anti-flakiness.md.
Tune execution in CI. Load references/ci-parallelism-sharding.md and references/infrastructure-troubleshooting.md.
Validate changed suites through build-test feedback targets. For NUKE-based repositories, run BuildAll, LocalUnitTest, ApiTest/DbTest as needed, then TestAll; use $ops-nuke-cicd for pipeline-target changes.
If this is a migration from SpecFlow-style assets, produce migration trace artifacts. Use $docs-codebase with migration matrix and feature trace templates.
Resources
NUnit Structure: project layout, naming, categories, and lifecycle conventions.
Fixture Pattern: fixture boundaries, shared setup, teardown, and composition.
Testing Templates: copy-ready fixture/Testcontainers/WireMock templates.
API Testing with NUnit: endpoint-level tests with HTTP assertions and contract checks.
Component Testing with NUnit: in-process integration tests across collaborating components.
Dependency Strategy Matrix: decide WireMock vs Testcontainers by scenario.
WireMock Setup: deterministic stubs, request verification, and failure simulation.
Testcontainers Setup: container lifecycle, readiness, and test isolation.
Async Eventual Assertions: polling, timeouts, and message-driven verification.
Anti-Flakiness: reliability rules for stable execution.
CI Parallelism and Sharding: split test execution safely and efficiently.
Infrastructure Troubleshooting: diagnose startup failures, port collisions, and readiness issues.
Skill Data: curated Microsoft and .NET testing references for this skill.
Templates
NUnit Handler Fixture Template: base fixture for setup wiring and deterministic scenario configuration.
NUnit Handler Tests Template: base test class using fixture with Arrange/Act/Assert flow.
NUnit API Fixture Template: API fixture for controller-focused API-to-database full-cycle tests.
NUnit API Tests Template: base API test class with fixture isolation and parallel-safe lifecycle.
NUnit API Request Builder Template: deterministic request builder for scenario setup.
NUnit API TestCaseSources Template: reusable TestCaseData source methods.
NUnit WireMock Template: pricing-style WireMockServerWrapper and per-dependency *WiremockServer helper pattern.
NUnit Database Launcher Template: pricing-style DatabaseLauncher, ordered migrator chain, optional migrator toggles, and startup verification hooks.
Weekly Installs
40
Repository
vasilyu1983/ai-…s-public
GitHub Stars
59
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn