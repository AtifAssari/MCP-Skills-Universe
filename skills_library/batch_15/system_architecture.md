---
title: system-architecture
url: https://skills.sh/hungv47/product-skills/system-architecture
---

# system-architecture

skills/hungv47/product-skills/system-architecture
system-architecture
Installation
$ npx skills add https://github.com/hungv47/product-skills --skill system-architecture
SKILL.md
System Architecture Designer — Orchestrator

Productivity — Multi-agent orchestration. Transforms product specifications into a comprehensive technical blueprint covering stack, schema, APIs, and deployment.

Core Question: "Will this still work at 10x scale with 10x team?"

Inputs Required
Product specification, PRD, or description of what needs to be built
Scale expectations (users, requests, data volume) — gathered via interview if missing
Known constraints (existing stack, compliance, budget, team skills)
Output
architecture/system-architecture.md
Chain Position

Previous: discover or task-breakdown (optional) | Next: task-breakdown (optional) | Cross-stack: reads solution-design.md (from research-skills), user-flow.md (from product-skills)

Re-run triggers: When product spec changes significantly, when scale requirements change (10x growth), when migrating core infrastructure, or when adding major new integrations.

Multi-Agent Architecture
Agent Manifest
Agent	File	Focus
stack-selection-agent	agents/stack-selection-agent.md	Technology choices with rationale and alternatives
infrastructure-agent	agents/infrastructure-agent.md	Deployment, CI/CD, monitoring, env vars
schema-agent	agents/schema-agent.md	Database tables, relationships, indexes, queries
api-agent	agents/api-agent.md	Endpoints, auth, request/response contracts
integration-agent	agents/integration-agent.md	File structure, service connections, feature blueprints
scaling-agent	agents/scaling-agent.md	Bottleneck analysis, failure modes, edge cases
critic-agent	agents/critic-agent.md	Quality gate review, internal consistency
Execution Layers
Layer 1 (parallel):
  stack-selection-agent ──┐
  infrastructure-agent ───┘─── run simultaneously

Layer 2 (sequential):
  schema-agent ─────────────── depends on stack choice
    → api-agent ────────────── depends on stack + schema
      → integration-agent ──── depends on stack + schema + API
        → scaling-agent ────── validates everything above
          → critic-agent ───── final quality review

Dispatch Protocol
Gather context — extract user types, data entities, critical flows, scale profile, and constraints from the product spec. If missing, run the Architecture Interview (see below).
Layer 1 dispatch — send brief + constraints to stack-selection-agent and infrastructure-agent in parallel.
Layer 2 sequential chain — pass stack output to schema-agent, then stack + schema to api-agent, then all three to integration-agent, then everything to scaling-agent.
Critic review — send assembled document to critic-agent.
Revision loop — if critic returns FAIL, re-dispatch affected agents with feedback. Maximum 2 revision rounds.
Assembly — merge all agent outputs into the 12-section artifact template. Save to architecture/system-architecture.md.
Routing Logic
Condition	Route
User provides tech stack upfront	Skip stack-selection-agent; pass user's stack directly to schema-agent
User needs stack recommendations	Run stack-selection-agent first
Critic returns PASS	Assemble and deliver
Critic returns FAIL	Re-dispatch only the agents cited in critic's issues
Revision round > 2	Deliver with critic's remaining issues noted as Open Questions
Dependency Classification

When designing integrations and service boundaries, classify every external dependency into one of four categories. Each category has a different testing strategy:

Category	What it is	Testing strategy	Example
In-process	Pure computation, no I/O	Test directly, no mocks needed	Validation logic, formatters, calculators
Local-substitutable	Has a lightweight local stand-in	Use the stand-in in tests	PGLite for Postgres, LocalStack for AWS, MailHog for email
Remote but owned	Your own services	Ports & Adapters — define interface, test with in-memory adapter	Your auth service, your billing API
True external	Third-party, no stand-in	Mock at the boundary only	Stripe API, Twilio, OpenAI

Document the category for each dependency in the Service Connections section. This directly informs testing strategy in task-breakdown and review-chain.

Critical Gates

Before delivering, the critic-agent verifies ALL of these pass:

 Every tech choice has a rationale (not just "it's popular")
 API endpoints exist for every user-facing feature
 Database schema covers all entities mentioned in product spec
 Deployment section includes complete env var list
 File structure matches chosen framework conventions
 Auth model covers all user roles and permission levels
 At least one architectural trade-off is documented with alternatives considered
 Every external dependency is classified (in-process / local-substitutable / remote-owned / true-external)

If any gate fails: the critic identifies which agent must fix it and the orchestrator re-dispatches with specific feedback.

Single-Agent Fallback

When context window is constrained or the product is simple (fewer than 3 user types, fewer than 5 data entities):

Skip multi-agent dispatch
Execute Steps 1-4 from the original process sequentially:
Step 1: Gather context and constraints
Step 2: Architecture decisions (use references/tech-stack-patterns.md and references/tech-stack-matrix.md)
Step 3: Generate all 12 sections of the architecture document
Step 4: Validation cross-reference
Run the Critical Gates checklist as self-review
Save to architecture/system-architecture.md
Before Starting
Step 0: Product Context

Check for research/product-context.md. If missing: interview for product dimensions (what, who, problem, differentiator, scale, integrations) and save to research/product-context.md. Or recommend running icp-research (from hungv47/research-skills) to bootstrap it.

If research/product-context.md has a date field older than 30 days, recommend re-running icp-research (from research-skills) to refresh it. Tip: /navigate status (from meta-skills) gives a single-pass freshness report across all upstream artifacts.

Required Artifacts

None — this skill can run standalone.

Optional Artifacts
Artifact	Source	Benefit
product-context.md	icp-research (from hungv47/research-skills)	Industry context, user personas, and constraints
task-breakdown.md	task-breakdown	Feature list already decomposed into buildable units
solution-design.md	solution-design (from hungv47/research-skills)	Business initiatives and constraints from strategy track
.agents/product/flow/*.md	user-flow (from hungv47/product-skills)	Per-flow user flow diagrams + platform-surface matrix; read every file in the directory. Feeds API endpoint design and feature scoping.
Two Modes of Operation

Mode 1: Tech Stack Already Chosen User provides tech stack upfront. Skip stack-selection-agent. Focus on schema, API, file structure, and implementation details.

Mode 2: Need Tech Stack Recommendations User needs help choosing stack. Run stack-selection-agent first, then chain remaining agents.

Architecture Interview

If the user provides only a vague description ("build me an app", "I need a platform"):

What is the product and its core value proposition?
Who are the primary users? Expected concurrent users at launch and at 12 months?
What are the 3-5 critical user flows?
What data needs to be stored and queried?
Existing tech stack or team skill constraints?
Specific integrations needed? (payments, email, auth providers, etc.)
Performance requirements? (real-time updates, complex queries, offline support)
Security/compliance needs? (SOC2, HIPAA, GDPR, PCI)

All 8 answers are necessary before dispatching agents.

Anti-Patterns
Anti-Pattern	Problem	INSTEAD
Premature microservices	Adds operational complexity before product-market fit	Start monolith, extract services at pain points
Schema without queries	Tables look clean but critical queries require full scans	Design schema around access patterns via schema-agent
Auth as afterthought	Retrofitting permissions breaks existing flows	api-agent defines roles and permissions before endpoint design
Missing error states	Happy-path-only architecture crumbles in production	scaling-agent traces failure modes for every critical operation
"We'll add monitoring later"	Debugging production without observability is guesswork	infrastructure-agent includes logging and error tracking in v1
Over-engineering for scale	Building for 1M users when you have 100 wastes months	scaling-agent designs for 10x current load, plans for 100x
Worked Example

User: "I need architecture for a SaaS invoicing tool. Small businesses send invoices, clients pay online. Need Stripe integration."

Orchestrator gathers context:

Users: business owners (send invoices), clients (view/pay)
Scale: ~500 businesses, ~2000 invoices/month at launch
Integrations: Stripe for payments, SendGrid for email
Constraints: small team, fast launch needed

Layer 1 dispatch (parallel):

stack-selection-agent → recommends Next.js + Supabase + Clerk + Stripe + Vercel
infrastructure-agent → plans Vercel deployment, GitHub Actions CI/CD, Sentry monitoring

Layer 2 chain (sequential):

schema-agent → designs businesses, invoices, payments, clients tables with indexes on (business_id, status) and (stripe_payment_id)
api-agent → maps POST /api/invoices (business_owner), GET /api/pay/:token (public), POST /api/webhooks/stripe (stripe_signature)
integration-agent → designs file structure, Stripe checkout flow, SendGrid email integration
scaling-agent → identifies invoice PDF generation as first bottleneck at 10x, traces webhook failure modes

Critic review: PASS — all 7 quality gates pass.

Artifact saved to architecture/system-architecture.md with all 12 sections.

Artifact Template

On re-run: rename existing artifact to system-architecture.v[N].md and create new with incremented version.

---
skill: system-architecture
version: 1
date: {{today}}
status: draft
---

# System Architecture: [Product Name]

## 1. System Overview
## 2. Tech Stack
## 3. File & Folder Structure
## 4. Database Schema
## 5. API Architecture
## 6. State Management & Data Flow
## 7. Service Connections
## 8. Authentication & Authorization
## 9. Key Features Implementation
## 10. Deployment & Infrastructure
## 11. Monitoring & Debugging
## 12. Security Review

### 12a. Threat Model (STRIDE)
For each critical data flow, evaluate: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege.
See `references/security-patterns.md` for the STRIDE template.

### 12b. OWASP Top 10 Scan
Architecture-level check against OWASP Top 10 categories. Focus on design decisions, not code patterns.
See `references/security-patterns.md` for the checklist.

### 12c. LLM/AI Security (conditional — include only if system uses AI/LLM)
Prompt injection vectors, output sanitization, tool validation, cost amplification.
See `references/security-patterns.md` for the LLM security checklist.

### 12d. Not Flagged (false-positive exclusions applied)
List any patterns that were checked but excluded per the false-positive exclusion rules.

## Not Included
[Explicitly excluded items with rationale — what this architecture intentionally does NOT cover]

## Open Questions
## Next Step
Run `task-breakdown` to decompose this architecture into implementable tasks.

References
references/tech-stack-patterns.md — Tech choice comparisons and recommendations
references/tech-stack-matrix.md — Stack comparison matrix
references/file-structure-patterns.md — Directory structures by framework
references/database-patterns.md — Common schemas and query patterns
references/api-patterns.md — REST best practices and endpoint examples
references/auth-patterns.md — Authentication implementations
references/deployment-patterns.md — CI/CD and infrastructure patterns
references/failure-modes.md — Failure mode criticality, error tracing table, shadow path analysis
references/interaction-edge-cases.md — UI and interaction edge case categories
references/security-patterns.md — STRIDE threat model, OWASP Top 10 architecture checks, LLM/AI security, false-positive exclusions
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