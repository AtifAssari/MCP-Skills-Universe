---
title: effect-ts
url: https://skills.sh/blogic-cz/agent-tools/effect-ts
---

# effect-ts

skills/blogic-cz/agent-tools/effect-ts
effect-ts
Installation
$ npx skills add https://github.com/blogic-cz/agent-tools --skill effect-ts
SKILL.md
Effect Expert

Use this skill when working with Effect services, layers, schema errors, config, and runtime integration.

Load Triggers

Load this skill when:

User mentions Effect, Layer, Context.Tag, Schema.TaggedError, Effect.gen, or Effect.fn
You are implementing or reviewing files that define Effect services, layers, or runtime boundaries
You are debugging Effect runtime behavior, missing spans, layer wiring, or boundary error mapping
You need test strategy for Effect code (@effect/vitest, test layers)
You need Effect runtime integration (TRPC/server boundaries)
First Step (Always)

Before substantial implementation, refactor, or formal review, fetch current recommendations:

effect-solutions list
effect-solutions show tsconfig
effect-solutions show basics
effect-solutions show services-and-layers
effect-solutions show data-modeling
effect-solutions show error-handling
effect-solutions show config
effect-solutions show testing
effect-solutions show cli


If effect-solutions CLI is unavailable, or if the task is trivial (for example a small wording tweak with no Effect design impact), skip the CLI calls and rely on the relevant reference file(s) in this skill.

Treat recommendations as time-sensitive guidance. Do not rely on stale memory.

Decision Tree
Service design or refactor -> references/services-and-layers.md
Typed errors, Option/Either, recovery -> references/error-handling.md
TRPC/server runtime boundary -> references/framework-integration.md
CLI tooling in agent-tools/* -> references/agent-tools-patterns.md
Testing and mocks -> references/testing-layers.md
Project Rules (Do Not Break)
Prefer service co-location (Context.Tag + static layer in one file)
Use Schema.TaggedError for domain errors
Do not access Option/Either internals via _tag; use helpers (match, isNone, isLeft)
For Effect dependencies, mock with Layers, not vi.mock()
Keep one clear provide boundary at entry points
Output Expectations

For substantial implementation/review/debug tasks, return:

Which effect-solutions show ... topics were checked
Which reference file(s) were used and why
Concrete change proposal following existing project patterns
Verification plan (typecheck/tests)
Reference Index
references/services-and-layers.md
references/error-handling.md
references/framework-integration.md
references/agent-tools-patterns.md
references/testing-layers.md
Weekly Installs
26
Repository
blogic-cz/agent-tools
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass