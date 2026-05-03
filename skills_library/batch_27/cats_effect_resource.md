---
title: cats-effect-resource
url: https://skills.sh/alexandru/skills/cats-effect-resource
---

# cats-effect-resource

skills/alexandru/skills/cats-effect-resource
cats-effect-resource
Installation
$ npx skills add https://github.com/alexandru/skills --skill cats-effect-resource
SKILL.md
Cats Effect Resource (Scala)
Quick start
Model each resource with Resource.make or Resource.fromAutoCloseable and keep release idempotent.
Compose resources with flatMap, mapN, parMapN, or helper constructors; expose Resource[F, A] from APIs.
Use Resource at lifecycle boundaries and call .use only at the program edges.
Read references/resource.md for patterns, best practices, and API notes.
Workflow
Identify acquisition, use, and release steps; decide if acquisition is blocking.
Implement a Resource[F, A] constructor using the smallest needed typeclass.
Compose resources into higher-level resources and keep finalizers minimal.
Decide how cancelation and errors should influence release logic.
Run with .use at the boundary (IOApp, service startup) and avoid leaking raw A.
Usage guidance
Prefer Resource over try/finally or bracket when composition and cancelation safety matter.
Use IO.blocking (or Sync[F].blocking) for acquisition and release when calling blocking JVM APIs.
For background fibers, use Resource or Supervisor to ensure cleanup on cancelation.
References
Load references/resource.md for API details, patterns, and examples.
For Kotlin/Arrow parallels, see the arrow-resource skill.
Install this skill with npx skills add https://github.com/alexandru/skills --skill cats-effect-resource.
Weekly Installs
35
Repository
alexandru/skills
GitHub Stars
38
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass