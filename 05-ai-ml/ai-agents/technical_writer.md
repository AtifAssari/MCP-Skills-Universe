---
title: technical-writer
url: https://skills.sh/hungv47/product-skills/technical-writer
---

# technical-writer

skills/hungv47/product-skills/technical-writer
technical-writer
Installation
$ npx skills add https://github.com/hungv47/product-skills --skill technical-writer
SKILL.md
Technical Writer — Orchestrator

Productivity — Multi-agent orchestration. Scans a codebase and produces clear, structured documentation that new users can follow without reading source code.

Core Question: "Could a new team member understand this without asking anyone?"

Inputs Required
A codebase or project to document
(Optional) Target audience — developer, end-user, operator, or mixed
(Optional) Documentation type — README, User Guide, API Reference, or Configuration Guide
Output
Documentation artifact saved to project root or specified location (e.g., docs/, README.md)
Chain Position

Previous: none | Next: none (standalone)

Pairs well with: system-architecture (for architecture docs), task-breakdown (for contributor guides)

Re-run triggers: After PRs that modify environment variables, API routes, or configuration. After major version releases. When new features ship without documentation updates.

Multi-Agent Architecture
Agent Roster
Agent	File	Focus
scanner-agent	agents/scanner-agent.md	Maps project structure, file importance ranking, existing docs inventory
concept-extractor-agent	agents/concept-extractor-agent.md	Reads key files, extracts features, setup requirements, error patterns
audience-profiler-agent	agents/audience-profiler-agent.md	Identifies audience, calibrates vocabulary and depth
writer-agent	agents/writer-agent.md	Writes the documentation from extracted concepts for the profiled audience
staleness-checker-agent	agents/staleness-checker-agent.md	Compares documentation against current codebase for accuracy
critic-agent	agents/critic-agent.md	Quality gate review, audience calibration check, staleness integration
Execution Layers
Layer 1 (parallel):
  scanner-agent ──────────────┐
  concept-extractor-agent ────┤── run simultaneously
  audience-profiler-agent ────┘

Layer 2 (sequential):
  writer-agent ────────────────── writes documentation from all Layer 1 outputs
    → staleness-checker-agent ─── verifies documentation matches codebase
      → critic-agent ──────────── final quality review

Dispatch Protocol
Layer 1 dispatch — send brief to all three Layer 1 agents in parallel:
scanner-agent maps the project and ranks files by importance
concept-extractor-agent reads ranked files and extracts documentation content
audience-profiler-agent determines who reads the docs and how to write for them
Writer dispatch — send all Layer 1 outputs to writer-agent. It produces the documentation following references/doc-template.md (or references/ship-log-template.md in Route D), calibrated for the audience.
Staleness check — send writer output + codebase facts to staleness-checker-agent. It verifies every claim in the docs matches the current codebase.
Critic review — send documentation + staleness results to critic-agent.
Revision loop — if critic returns FAIL, re-dispatch affected agents. Maximum 2 rounds.
Save — write documentation to project root or specified location.
Routing Rules
Condition	Route
User specifies audience	audience-profiler-agent uses it directly (no inference needed)
User says "document this" (no type)	audience-profiler defaults to User Guide (developers) or README (library)
User says "audit docs"	Skip writer-agent; run scanner → staleness-checker → critic directly
User says "sync docs", "update docs", or --sync	Route C: Post-Change Sync (see below)
User says "ship log", "product context", "what does this app do", or --ship-log	Route D: Ship Log (see below)
Monorepo detected	scanner-agent identifies package boundaries; writer produces per-package docs
Critic PASS	Save and deliver
Critic FAIL	Re-dispatch cited agents with feedback
Route C: Post-Change Sync

Triggered by: /technical-writer --sync, "update the docs after this change", "sync docs", or "docs are stale after that PR."

This route cross-references the git diff against ALL existing documentation and makes targeted updates — not a full rewrite. It's the documentation equivalent of a patch, not a rebuild.

Execution flow:

scanner-agent ──────────────── inventory existing docs + read git diff
  → staleness-checker-agent ── compare diff against docs, find stale content
    → writer-agent ──────────── make targeted updates only (not full rewrite)
      → critic-agent ────────── verify factual accuracy of updates


What's different from the full route:

concept-extractor-agent and audience-profiler-agent are SKIPPED — the docs already exist with established audience and structure
scanner-agent reads the git diff (not the full codebase) to scope changes
writer-agent receives a list of stale sections and makes MINIMAL targeted edits — it does NOT rewrite sections that aren't affected by the diff
staleness-checker-agent focuses on the diff's blast radius: changed API routes, modified env vars, renamed files, updated config

What the staleness-checker looks for in sync mode:

File paths — did any documented paths change? (renamed, moved, deleted files)
API routes — did any endpoints change signature, parameters, or response shape?
Environment variables — were any added, removed, or renamed?
Configuration — did defaults, valid values, or required settings change?
Version numbers — did package.json version, Node/runtime version, or dependency versions change?
Feature descriptions — did any documented behavior change?
Setup steps — did installation or getting-started steps change?

What the writer-agent does in sync mode:

For factual updates (paths, versions, env vars): auto-fix directly
For narrative updates (feature descriptions, architecture explanations): flag for user approval before changing
Never rewrite sections unaffected by the diff
Add a <!-- synced: YYYY-MM-DD --> comment to updated sections for traceability
Route D: Ship Log

Triggered by: /technical-writer --ship-log, "write a ship log", "product context", "what does this app do", or "document the current state of the app."

This route produces a plain-language product snapshot saved to research/product-context.md. It answers the questions: What does this app do? What's been built? How do you use it? What's the tech stack? What shipped recently? Written so a non-technical person could understand, while still being precise enough for coding agents to use as context.

Why research/product-context.md: This is the canonical cross-stack artifact consumed by 12+ downstream skills (brand-system, content-create, seo, system-architecture, etc.). Writing the ship log here means every skill automatically gets current product context.

Execution flow:

scanner-agent ──────────────┐
concept-extractor-agent ────┤── Layer 1 (parallel) — scan codebase + git history
audience-profiler-agent ─────┘── (locked to "mixed: non-technical user + coding agent")

writer-agent ────────────────── writes ship log following references/ship-log-template.md
  → staleness-checker-agent ── verifies every claim against codebase
    → critic-agent ──────────── ship-log-specific quality gates


What's different from the full route:

audience-profiler-agent receives a pre-set audience in dispatch: { type: "mixed", technical_level: "dual", key_goal: "understand product state" }. The profiler returns this value directly without inference.
scanner-agent also extracts git shipping history (git log --oneline --since="6 months ago" or full history for young repos)
concept-extractor-agent focuses on user-facing features and workflows, not internals
writer-agent receives references/ship-log-template.md in its references field (NOT doc-template.md)
critic-agent applies ship-log-specific quality gates (see below) — replaces the standard checklist entirely

Pre-write step (orchestrator responsibility): Before dispatching writer-agent, the orchestrator checks for research/product-context.md:

If it exists with skill: icp-research in frontmatter: pass merge-mode: preserve-marketing to writer-agent
If it exists with skill: technical-writer in frontmatter: rename to product-context.v[N].md, pass merge-mode: overwrite to writer-agent
If it exists with unknown origin: rename to product-context.v[N].md, pass merge-mode: overwrite to writer-agent
If it doesn't exist: pass merge-mode: create to writer-agent

Referencing the artifact: After writing, the orchestrator checks if the project's CLAUDE.md references research/product-context.md. If not, suggest the user add: Read research/product-context.md for current product state (features, tech stack, shipping history).

Critical Gates

Before delivering, the critic-agent verifies ALL of these pass:

 Every user-facing feature has a documentation section
 Setup steps are numbered with expected outcomes after each step
 A new user could follow Getting Started independently without reading source code
 Code examples compile/run — no pseudocode unless explicitly labeled
 Configuration options list defaults and valid values
 Troubleshooting covers errors visible in the codebase's error handling

If any gate fails: the critic identifies which agent must fix it and the orchestrator re-dispatches.

Ship Log Quality Gates

When in ship log mode (Route D), the critic-agent verifies these INSTEAD of the standard gates:

 A non-technical person could read this and explain what the app does to someone else
 Every user-facing feature is listed with a plain-language description of what it does and how to use it
 Tech stack is listed with purpose for each choice (not just names)
 Shipping history includes at least the last 5 significant changes with dates
 No jargon leak in user-facing sections (What This App Does, Features, Shipping History, Current State) — technical terms are permitted in the "For Coding Agents" section only
 Current state section accurately reflects what's working, what's in progress, and known limitations
 The document works as agent context — a coding agent reading only this file would understand what to build next
Single-Agent Fallback

When context window is constrained or the project is small (fewer than 20 files):

Skip multi-agent dispatch
Scan project structure and identify key files using the 7-rank importance system
Read 5-10 highest-ranked files
Determine audience (developer, end-user, operator)
Write documentation following references/doc-template.md
Cross-check env vars, setup steps, and API endpoints against code
Run Critical Gates as self-review
Save to project root or specified location
Documentation Types
Type	Audience	Focus	Length
README	Developers discovering the project	What it does, quick start, contribution	1-3 pages
User Guide	End-users operating the product	Workflows, features, troubleshooting	5-20 pages
API Reference	Developers integrating	Endpoints, parameters, responses, errors	Varies
Configuration Guide	Operators deploying	Environment vars, settings, infrastructure	2-5 pages
Getting Started Tutorial	New users of any type	Single workflow, start to finish	1-2 pages
Ship Log	Humans + coding agents	Product snapshot, features, tech stack, shipping history	2-5 pages

Default to User Guide if the user says "document this" without specifying type. Default to Ship Log if the user says "product context" or "what does this app do."

File Importance Ranking (7 Ranks)

The scanner-agent ranks files by documentation value:

Rank	File Type	What It Reveals	Priority
1	Entry points (main.*, index.*, app.*)	App initialization, core structure	Read first
2	Route/endpoint definitions	Feature surface area	Read second
3	Config/env files	Setup requirements, feature flags	Read third
4	Models/Types/Schemas	Core data entities, relationships	Read for depth
5	Components/Views	UI structure, user interactions	Read for UX docs
6	Middleware/Interceptors	Auth, logging, error handling	Read for ops docs
7	Migration files	Data model evolution, schema requirements	Skim for setup
3 Audience Types
Audience	Vocabulary	Code Examples	Assumed Knowledge
End-user	Plain language, no jargon	Only CLI commands they run	Can install software, use a browser
Developer	Technical terms, API vocabulary	Request/response samples, code snippets	Can read code, use package managers
Operator	Infrastructure terminology	Config files, deployment commands	Understands networking, servers, CI/CD
Documentation Audit Mode

Trigger when asked to "audit docs", "check documentation", or "are docs up to date."

In audit mode, the orchestrator skips the writer-agent and runs:

scanner-agent — inventory all documentation files
staleness-checker-agent — compare each doc against current codebase
critic-agent — report findings with priority (security-relevant > setup > architecture > everything else)

Prioritize: auth docs and env var docs being stale is a security risk.

Anti-Patterns
Anti-Pattern	Problem	INSTEAD
Restating code as prose	"handleSubmit handles form submission" adds nothing	writer-agent describes user experience, not internal code
Missing prerequisites	User stuck at step 3 because step 0 was assumed	concept-extractor lists every dependency and version
Wall of text	Users scan, not read — long paragraphs get skipped	writer-agent uses tables, numbered lists, headers
Outdated screenshots	Screenshots rot faster than text	writer-agent prefers text descriptions of UI elements
Documenting internals	Users don't care about ORM layer	writer-agent documents behavior and interfaces
"See code for details"	Defeats purpose of documentation	concept-extractor extracts the relevant detail
Stale docs shipped as current	Actively mislead users	staleness-checker verifies every claim against codebase
Worked Example

User: "Document this project" (a Node.js REST API for task management)

Layer 1 (parallel):

scanner-agent → maps project: src/index.ts, src/routes/, src/models/, prisma/schema.prisma, package.json, .env.example. Existing README is stale (references Node 16, project uses Node 18).
concept-extractor-agent → reads ranked files: Express app with JWT auth, task CRUD with status workflow (todo→in-progress→done), team assignment, email notifications. Errors: 401 expired token, 403 cross-team access, 422 invalid status transition.
audience-profiler-agent → Developer audience (API consumers). Recommended type: README + API Reference.

Layer 2 (sequential):

writer-agent → writes README with Getting Started (5 numbered steps), API Reference, Configuration table, Troubleshooting section
staleness-checker-agent → flags: Node version in setup (docs say 16, code needs 18), missing SMTP_PORT env var (in code but not documented)
critic-agent → FAIL: 2 staleness issues must be fixed

Revision: writer-agent updates Node version and adds SMTP_PORT. Critic → PASS.

Artifact saved to README.md.

Before Starting
Step 0: Product Context

Check for existing context files: README.md, CLAUDE.md, research/product-context.md, package.json#description. Read all available context before scanning code.

Optional Artifacts
Artifact	Source	Benefit
product-context.md	icp-research (from hungv47/research-skills)	Product positioning and audience already defined
system-architecture.md	system-architecture	Architecture decisions pre-mapped
brand/BRAND.md + brand/DESIGN.md	brand-system (from hungv47/marketing-skills)	Brand voice, terminology, and design system
Artifact Template

On re-run: rename existing artifact to [name].v[N].md and create new with incremented version.

---
skill: technical-writer
version: 1
date: {{today}}
status: draft
audience: [end-user | developer | operator | mixed]
doc-type: [readme | user-guide | api-reference | config-guide | tutorial | ship-log]
---

Next Step

Documentation complete. Run review-chain for quality review. Run seo if docs are public-facing.

References
references/doc-template.md — Full documentation template with writing guidelines and code-to-doc mapping
references/ship-log-template.md — Ship log template for product context snapshots
Weekly Installs
9
Repository
hungv47/product-skills
GitHub Stars
1
First Seen
8 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass