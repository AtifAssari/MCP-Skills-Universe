---
title: effect-index
url: https://skills.sh/mepuka/effect-ontology/effect-index
---

# effect-index

skills/mepuka/effect-ontology/effect-index
effect-index
Installation
$ npx skills add https://github.com/mepuka/effect-ontology --skill effect-index
Summary

Quick router to the right Effect skill based on your coding task.

Organized decision tree with 12 focused skills covering Effect fundamentals, error handling, concurrency, streams, dependency injection, HTTP, validation, data structures, logging, queues, and testing
Cross-skill pattern references linking common workflows (retries, resource management, graceful shutdown, service design) to both relevant skills and the 130+ pattern examples in the Patterns Hub
Local Effect source code reference guide with grep commands and file paths for searching implementations before coding
Tip to check the Patterns Hub decision tree first for "How do I...?" questions
SKILL.md
Effect Skill Index

Use this as a quick router to the right Skill for your task. Each entry links to a focused Skill optimized for a coding agent’s limited context.

Decision Tree
I need to write or refactor some Effect code → Foundations
I need robust error handling/retries → Errors & Retries
I must run things in parallel / manage fibers → Concurrency & Fibers
This is a data pipeline / batching / backpressure → Streams & Pipelines
I need DI/services/layers or test/live wiring → Layers & Services
Opening files/sockets/servers with cleanup → Resources & Scope
Add HTTP endpoints / JSON responses → HTTP & Routing
Validate inputs / parse config → Config & Schema
Value-based equality / high-perf immutable collections → Data Structures
Time, logging, spans/tracing → Time/Tracing/Logging
Queues, PubSub, background workers → Queues & Background
Write tests/mocks for services → Testing & Mocking
Looking for specific patterns or examples → Patterns Hub (130+ patterns)
Cross-Skill Patterns

All patterns are now available locally in the Patterns Hub (130+ patterns):

Retry transient failures → Errors & Retries + retry-based-on-specific-errors.mdx
Resource-safe streaming → Streams & Pipelines + stream-manage-resources.mdx
Graceful shutdown → Queues & Background + execute-long-running-apps-with-runfork.mdx
Service layer design → Layers & Services + model-dependencies-as-services.mdx
HTTP server setup → HTTP & Routing + build-a-basic-http-server.mdx
Schema validation → Config & Schema + define-contracts-with-schema.mdx
Testing with mocks → Testing & Mocking + mocking-dependencies-in-tests.mdx

Tip: For any "How do I...?" question, check the Patterns Hub decision tree first!

Local Source Reference

CRITICAL: Always search local Effect source before implementing

The full Effect source code is available at docs/effect-source/. Every Effect skill now includes a "Local Source Reference" section with:

Key source files for that skill's domain
Example grep commands to find implementations
Workflow for searching before coding
Quick Access to Source
All Effect packages: docs/effect-source/
Core library: docs/effect-source/effect/src/
Platform APIs: docs/effect-source/platform/src/
SQL: docs/effect-source/sql/src/
Schema: docs/effect-source/schema/src/
Example: Finding Effect.gen
grep -F "Effect.gen" docs/effect-source/effect/src/Effect.ts

Workflow Reminder
Read the relevant skill (from decision tree above)
Review the skill's "Local Source Reference" section
Search the Effect source code for the API you need
Study the implementation and types
Write your code based on real implementations

See CLAUDE.local.md for complete source reference guide

References
Agent Skills overview: Introducing Agent Skills
Skills guide: Claude Code Skills Documentation
Local Patterns Hub: ../effect-patterns-hub/SKILL.md (130+ patterns)
Pattern Documentation: ../../docs/effect-patterns/
AGENTS.md: ../../AGENTS.md (Effect best practices for AI agents)
EffectPatterns (upstream source): PaulJPhilp/EffectPatterns
Weekly Installs
309
Repository
mepuka/effect-ontology
GitHub Stars
5
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass