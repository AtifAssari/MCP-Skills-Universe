---
title: shared-kernel
url: https://skills.sh/7spade/black-tortoise/shared-kernel
---

# shared-kernel

skills/7spade/black-tortoise/shared-kernel
shared-kernel
Installation
$ npx skills add https://github.com/7spade/black-tortoise --skill shared-kernel
SKILL.md
Shared Kernel
Intent

Provide safe, low-coupling primitives reused across bounded contexts.

Allowed Content
Pure utilities (formatting, small helpers) with no side effects.
Shared UI atoms/molecules that do not contain business rules.
Cross-cutting technical helpers (logging adapters, error wrappers) when they do not introduce new dependencies.
Forbidden Content
Business logic, policies, or workflow orchestration.
Cross-capability state stores.
Domain rules that belong to a specific bounded context.
Direct platform SDK usage (Firebase/HTTP) unless the shared item is explicitly an infrastructure primitive and the dependency direction is preserved.
Dependency Discipline
Keep dependencies stable and minimal.
Avoid importing capability modules into shared.
API Design
Prefer small, intention-revealing APIs.
Avoid "god" utility modules; create focused files.
Weekly Installs
8
Repository
7spade/black-tortoise
First Seen
Feb 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass