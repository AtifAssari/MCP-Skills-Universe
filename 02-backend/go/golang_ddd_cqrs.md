---
rating: ⭐⭐
title: golang-ddd-cqrs
url: https://skills.sh/joeyave/golang-ddd-skills/golang-ddd-cqrs
---

# golang-ddd-cqrs

skills/joeyave/golang-ddd-skills/golang-ddd-cqrs
golang-ddd-cqrs
Installation
$ npx skills add https://github.com/joeyave/golang-ddd-skills --skill golang-ddd-cqrs
SKILL.md
Golang DDD CQRS

Use this skill to split application logic into clear commands and queries without turning Go code into ceremony-heavy enterprise scaffolding.

Start Here
Use CQRS when a service has meaningful write-side behavior, mixed read and write models, or application services that are hard to reason about.
Skip or minimize CQRS when the service is mostly simple CRUD or login-like flows with little business behavior.
Workflow
Split the use cases into writes and reads.
Commands mutate state and may return errors.
Queries return data and should not perform business mutations.
Name them in business language.
Prefer ScheduleTraining, CancelTraining, ApproveReschedule, AvailableHours.
Avoid default CRUD names unless the business really speaks that way.
Introduce separate handlers when it improves clarity.
Use one command handler type per command when the logic or dependencies differ.
Use one query handler type per query when read concerns differ.
Keep interfaces narrow and owned by the handler that consumes them.
Keep handlers orchestration-only.
Domain rules belong in the domain layer.
Transport mapping belongs in ports.
Database or external API details belong in adapters.
Shape the ports around CQRS.
HTTP or gRPC ports may call commands directly.
If a create command needs a follow-up read, prefer 204 No Content plus content-location when practical, or execute an explicit query after the command.
Keep port-specific error translation at the edge.
Test the application layer as orchestration.
Mock repositories and outbound services with tiny handwritten mocks.
Keep business-scenario assertions in domain tests unless the behavior truly belongs to application orchestration.
Guardrails
Do not create separate command and query packages if the service is still trivial.
Do not let commands return large read models by default.
Do not hide business logic in command handlers just because they are convenient.
Do not keep one giant application service if separate handlers would shrink interfaces and tests.
Use These References
Read references/cqrs-guidelines.md for naming, packaging, and tradeoffs.
Read references/application-tests-and-errors.md for handler testing and transport-agnostic errors.
Deliverables
command and query boundaries that match the use cases,
business-oriented names,
narrow handler-owned interfaces,
thin transport code,
handler tests focused on orchestration instead of domain internals.
Weekly Installs
9
Repository
joeyave/golang-…d-skills
GitHub Stars
2
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass