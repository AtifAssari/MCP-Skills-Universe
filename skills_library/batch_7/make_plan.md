---
title: make-plan
url: https://skills.sh/thedotmack/claude-mem/make-plan
---

# make-plan

skills/thedotmack/claude-mem/make-plan
make-plan
Installation
$ npx skills add https://github.com/thedotmack/claude-mem --skill make-plan
SKILL.md
Make Plan

You are an ORCHESTRATOR. Create an LLM-friendly plan in phases that can be executed consecutively in new chat contexts.

Delegation Model

Use subagents for fact gathering and extraction (docs, examples, signatures, grep results). Keep synthesis and plan authoring with the orchestrator (phase boundaries, task framing, final wording). If a subagent report is incomplete or lacks evidence, re-check with targeted reads/greps before finalizing.

Subagent Reporting Contract (MANDATORY)

Each subagent response must include:

Sources consulted (files/URLs) and what was read
Concrete findings (exact API names/signatures; exact file paths/locations)
Copy-ready snippet locations (example files/sections to copy)
"Confidence" note + known gaps (what might still be missing)

Reject and redeploy the subagent if it reports conclusions without sources.

Plan Structure
Phase 0: Documentation Discovery (ALWAYS FIRST)

Before planning implementation, deploy "Documentation Discovery" subagents to:

Search for and read relevant documentation, examples, and existing patterns
Identify the actual APIs, methods, and signatures available (not assumed)
Create a brief "Allowed APIs" list citing specific documentation sources
Note any anti-patterns to avoid (methods that DON'T exist, deprecated parameters)

The orchestrator consolidates findings into a single Phase 0 output.

Each Implementation Phase Must Include
What to implement — Frame tasks to COPY from docs, not transform existing code
Good: "Copy the V2 session pattern from docs/examples.ts:45-60"
Bad: "Migrate the existing code to V2"
Documentation references — Cite specific files/lines for patterns to follow
Verification checklist — How to prove this phase worked (tests, grep checks)
Anti-pattern guards — What NOT to do (invented APIs, undocumented params)
Final Phase: Verification
Verify all implementations match documentation
Check for anti-patterns (grep for known bad patterns)
Run tests to confirm functionality
Key Principles
Documentation Availability ≠ Usage: Explicitly require reading docs
Task Framing Matters: Direct agents to docs, not just outcomes
Verify > Assume: Require proof, not assumptions about APIs
Session Boundaries: Each phase should be self-contained with its own doc references
Anti-Patterns to Prevent
Inventing API methods that "should" exist
Adding parameters not in documentation
Skipping verification steps
Assuming structure without checking examples
Weekly Installs
1.7K
Repository
thedotmack/claude-mem
GitHub Stars
70.8K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass