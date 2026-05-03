---
rating: ⭐⭐
title: ops-nuke-cicd
url: https://skills.sh/vasilyu1983/ai-agents-public/ops-nuke-cicd
---

# ops-nuke-cicd

skills/vasilyu1983/ai-agents-public/ops-nuke-cicd
ops-nuke-cicd
Installation
$ npx skills add https://github.com/vasilyu1983/ai-agents-public --skill ops-nuke-cicd
SKILL.md
NUKE CI/CD
Quick Reference
Start from existing nuke/Build.cs targets and preserve output contracts before refactoring.
Keep target graph intent explicit: use DependsOn for hard prerequisites, After for ordering, Triggers for composed flows, and OnlyWhenDynamic for runtime gates.
Use this skill for pipeline orchestration and build contracts, not for application-service refactors or NUnit fixture internals.
Separate fast local feedback (build + filtered tests) from full CI validation (unit + api + db + merged coverage).
Use the iterative loop code -> build -> run tests -> fix -> repeat for both feature work and test hardening.
Run preflight checks before expensive targets: SDK version, Docker availability (when required), and expected file paths.
Use wrapper commands (when available): ./build.sh BuildAll, ./build.sh LocalUnitTest, ./build.sh ApiTest, ./build.sh TestAll.
Use category filters intentionally, including exclusion filter patterns such as TestCategory!=ComponentTests&TestCategory!=DbTests&TestCategory!=ApiTest.
Keep UnitTest scoped to non-API categories and create a dedicated ApiTest target for TestCategory=ApiTest.
Keep TestAll composed from UnitTest + ApiTest (+ DbTest) and coverage merge.
When migrating from legacy docker-compose/SpecFlow orchestration, decommission compose-first test flow and keep pipeline focused on NUnit API categories.
Avoid running parallel dotnet test invocations against the same project output path in one job to prevent file-lock/MSBuild manifest failures.
Keep shell commands robust for zsh: avoid unquoted globs in direct shell commands and validate paths before sed/cat/ls.
Emit coverage and test artifacts deterministically (coverage.cobertura.xml, HTML summary, JUnit XML).
Build one or more Docker images with traceable tags (build id, commit sha), then publish digest-pinned deploy variables into deploy.env (image count is repository-specific).
Branch behavior on IsLocalBuild only for performance and environment-output concerns, not correctness.
If the task shifts into service implementation details, switch to $software-csharp-backend.
If the task shifts into fixture design, WireMock/Testcontainers setup, or anti-flake test structure, switch to $qa-testing-nunit.
Workflow
Model or review target graph sequencing and execution constraints. Load references/nuke-target-graph-design.md.
Design the build-test loop for early failures and rapid signal. Load references/build-test-feedback-loop.md.
Define and verify test category filters for unit/API/DB/component separation. Load references/test-categories-and-filters.md.
Implement coverage and test reporting with merge/publish outputs. Load references/coverage-and-reporting.md.
Implement Docker build/push with tag + digest capture and deployment outputs. Load references/docker-build-push-patterns.md.
Enforce stable artifact contracts and environment outputs. Load references/artifacts-and-output-contracts.md.
Tune local vs CI behavior without hiding pipeline defects. Load references/local-vs-ci-behavior.md.
Harden reliability, logs, and diagnostics for CI incident response. Load references/pipeline-reliability-and-observability.md.
Run command hygiene and environment preflight checks before final run. Load references/execution-preflight-and-command-hygiene.md.
Run anti-pattern review before finalizing. Load references/nuke-pipeline-antipatterns.md.
Decision Tree
If target ordering is incorrect or unexpected targets run, use references/nuke-target-graph-design.md.
If feedback loop is too slow or flaky, use references/build-test-feedback-loop.md.
If test scope is wrong in CI or local runs, use references/test-categories-and-filters.md.
If coverage or JUnit artifacts are missing/partial, use references/coverage-and-reporting.md.
If Docker outputs are not traceable or digest pinning is missing, use references/docker-build-push-patterns.md.
If downstream jobs cannot consume artifacts or env outputs, use references/artifacts-and-output-contracts.md.
If local and CI behavior diverge unexpectedly, use references/local-vs-ci-behavior.md.
If failures are hard to debug from logs, use references/pipeline-reliability-and-observability.md.
If failures come from shell quoting, glob expansion, missing files, or environment prerequisites, use references/execution-preflight-and-command-hygiene.md.
If pipeline quality regresses during refactors, use references/nuke-pipeline-antipatterns.md.
Do / Avoid

Do

Keep targets deterministic and side effects explicit.
Keep test stages isolated by category and risk profile.
Keep coverage/report merge as a first-class target in the graph.
Keep Docker outputs traceable through tag, digest, and exported env variables.
Keep artifact paths and names stable across branches and CI systems.

Avoid

Mixing orchestration and hidden side effects inside unrelated targets.
Running expensive integration tests before compile/unit gates.
Changing output file names without updating consumer jobs.
Using local-only shortcuts that invalidate CI parity.
Ignoring digest capture and shipping mutable image references.
Resources
NUKE Target Graph Design
Build-Test Feedback Loop
Test Categories and Filters
Coverage and Reporting
Docker Build Push Patterns
Artifacts and Output Contracts
Local vs CI Behavior
Pipeline Reliability and Observability
Execution Preflight and Command Hygiene
NUKE Pipeline Antipatterns
Skill Data: curated Microsoft and .NET CI/CD references for this skill.
Templates
NUKE Target Template Build and Test
NUKE Target Template Docker Build Push Digest
Test Result and Coverage Publishing Checklist
CI Troubleshooting Checklist
PR Pipeline Quality Checklist
Weekly Installs
41
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