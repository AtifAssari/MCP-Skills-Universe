---
rating: ⭐⭐
title: litestar-debugging
url: https://skills.sh/alti3/litestar-skills/litestar-debugging
---

# litestar-debugging

skills/alti3/litestar-skills/litestar-debugging
litestar-debugging
Installation
$ npx skills add https://github.com/alti3/litestar-skills --skill litestar-debugging
SKILL.md
Debugging
Execution Workflow
Reproduce the issue with the smallest possible app, route, or test case.
Identify the failing layer first: requests, routing, dependency injection, middleware, auth, responses, exception handling, or lifecycle.
Turn on only the minimum safe diagnostics needed: local debug=True, focused logs, or temporary assertions.
Inspect the boundary where the behavior diverges from expectation.
Fix the root cause, remove temporary diagnostics, and add a regression test.
Re-run the affected tests and re-check the surrounding contract for regressions.
Core Rules
Keep debug=True local-only.
Prefer deterministic logs, assertions, and focused reproduction apps over ad hoc print debugging.
Narrow the failing layer before changing code.
Use request and app loggers for evidence, not speculation.
Keep debug output free of secrets and sensitive payloads.
Remove temporary diagnostics once the root cause is understood.
Always codify the fix with a regression test when feasible.
Decision Guide
Use a tiny repro app when the existing app is too large to reason about quickly.
Use litestar-testing clients when the bug is observable through the HTTP or websocket contract.
Use litestar-logging when the main gap is missing evidence rather than a code defect.
Use debug=True only when local traceback detail materially shortens the investigation.
Hand off to the more specific Litestar skill once the failing subsystem is clear.
Reference Files

Read only the sections you need:

For reproduction strategy, layer isolation, and temporary diagnostic tactics, read references/reproduction-and-isolation.md.
For common subsystem debugging patterns across requests, auth, responses, exceptions, and lifecycle, read references/subsystem-patterns.md.
Recommended Defaults
Reproduce with the smallest route and the smallest input that still fails.
Keep one hypothesis at a time and test it quickly.
Add evidence before changing behavior.
Use logs to compare expected and actual values at subsystem boundaries.
Convert the repro into a stable test once the bug is found.
Anti-Patterns
Leaving debug=True or verbose diagnostics enabled after the fix.
Changing several subsystems at once before isolating the failure.
Catching broad exceptions to hide symptoms instead of understanding them.
Assuming a request, auth, or response bug without reproducing the exact contract.
Logging secrets, tokens, or raw sensitive request bodies during debugging.
Validation Checklist
Confirm the issue reproduces before the fix and stops reproducing after it.
Confirm both happy-path and failure-path contracts still behave correctly.
Confirm no sensitive values are leaked by temporary or permanent diagnostics.
Confirm the regression test fails before the fix and passes after it.
Confirm temporary debugging code is removed.
Cross-Skill Handoffs
Use litestar-logging when better evidence collection is the main need.
Use litestar-testing to codify the repro and lock the fix.
Use litestar-requests, litestar-responses, litestar-exception-handling, or litestar-authentication once the failing boundary is known.
Use litestar-metrics only after the runtime bug is understood and ongoing visibility is needed.
Litestar References
https://docs.litestar.dev/latest/usage/debugging.html
https://docs.litestar.dev/latest/usage/testing.html
Weekly Installs
15
Repository
alti3/litestar-skills
GitHub Stars
5
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass