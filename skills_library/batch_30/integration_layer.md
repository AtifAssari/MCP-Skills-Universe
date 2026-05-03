---
title: integration-layer
url: https://skills.sh/7spade/black-tortoise/integration-layer
---

# integration-layer

skills/7spade/black-tortoise/integration-layer
integration-layer
Installation
$ npx skills add https://github.com/7spade/black-tortoise --skill integration-layer
SKILL.md
Integration Layer
Intent

Implement external integrations (Firebase, Data Connect, HTTP, SDKs) behind stable ports so the rest of the app stays framework-agnostic.

Layer Boundaries
Only integration/infrastructure may import Firebase/AngularFire/DataConnect SDKs.
Expose interfaces/tokens to Application; never expose platform types.
Repository Adapters
Implement repository ports with minimal mapping:
DTO <-> Domain mapping happens here (or in dedicated mappers within integration).
Keep mapping deterministic; normalize timestamps/IDs.
Streams and Signals
Integration may return Observables (streaming) or Promises (commands).
Convert to signals at the Application boundary (store/facade), not in templates.
Ensure cleanup: avoid manual subscriptions unless lifecycle-bound.
Data Connect
Treat generated SDK as read-only output.
After schema changes, regenerate before app code changes.
Enforce auth directives and least-privilege queries.
Security
Never trust client input.
Keep secrets in env/secret manager, not in source.
Avoid string-concatenated queries; use parameterized APIs.
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