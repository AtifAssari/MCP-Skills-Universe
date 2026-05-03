---
rating: ⭐⭐
title: decision-evaluation
url: https://skills.sh/freeacger/loom/decision-evaluation
---

# decision-evaluation

skills/freeacger/loom/decision-evaluation
decision-evaluation
Installation
$ npx skills add https://github.com/freeacger/loom --skill decision-evaluation
SKILL.md
Decision Evaluation
Overview

This skill evaluates one explicit design decision at a time.

It does not discover the whole design. It does not validate overall readiness. Its job is to compare real options for a bounded decision node and produce a recommendation with reasons.

When to Use

Use this skill when:

the design already contains a concrete decision node
the user is effectively asking "which of these approaches should we choose?"
the decision will materially affect architecture, implementation path, compatibility, cost, or operational risk

Typical examples include:

auth model
coordination pattern
storage strategy
sync model
state management approach
retry or execution model
workflow rollback policy
workflow approval strategy
methodology stop condition
methodology evidence threshold
framework routing rule
framework handoff contract
language or runtime selection
UI framework selection
data-layer library (ORM, query builder, validation) selection
tooling selection (bundler, linter, test runner, CI platform)

Do not use this skill when:

the design tree is not formed yet
the task is still broad design discovery
the main need is deeper refinement rather than bounded comparison
the task is a final readiness gate
Constraint Gathering

When the decision involves technology selection (language, framework, library, or tooling), perform this step before the formal comparison.

Ask the user to confirm:

Hard constraints: existing tech stack, license requirements, budget limits, deployment environment restrictions.
Preferences or already-excluded options.
Priority of evaluation dimensions (e.g., performance > ecosystem > learning curve).
Must-have requirements (TypeScript support, SSR capability, plugin system, etc.).

Filter the candidate list based on confirmed constraints. Only feasible options proceed to formal comparison.

Output: confirmed constraints + filtered candidate list.

When the decision is non-technical but still bounded, do not force technology-selection questions. Instead confirm the decision boundary, real alternatives, and the dimensions that matter for this workflow, methodology, or framework choice.

Core Responsibilities

Your responsibilities are:

Frame the exact decision question. For technology selections, frame the question based on constraints confirmed in the Constraint Gathering step.
Keep the work bounded to one explicit decision node.
Present 3 to 4 real options when real options exist.
Compare trade-offs clearly and concretely.
Recommend one option or a justified combination when appropriate.
Explain why the rejected options are not preferred in this context.
Record the result in a reusable decision record.
Comparison Standard

Compare options using the dimensions that matter to the decision. These often include:

implementation complexity
compatibility with the current system
operational risk
performance
maintainability
future flexibility
debugging and observability implications

Do not force every dimension into every decision. Use only the ones that actually matter.

Expected Outputs

Produce or update a design_state that includes:

design_target_type
decision_nodes
decisions
risks
optional downstream impact notes for the design tree
Diagram Conventions

Use character diagrams inside code blocks (no language tag) to visualize trade-offs and architecture topology.

Star Ratings

Use when comparing 3+ options across 2+ quantitative dimensions.

Overall Rating:

Auth0:      ★★★★☆  4/5
Keycloak:   ★★★☆☆  3/5
Self-build: ★☆☆☆☆  1/5

Dimension Breakdown:

Security:       Auth0 ★★★★★  Keycloak ★★★★☆  Self ★★☆☆☆
Speed-to-MVP:   Auth0 ★★★★★  Keycloak ★★★☆☆  Self ★☆☆☆☆
Cost-at-scale:  Auth0 ★★★☆☆  Keycloak ★★★★☆  Self ★★★★★


Rules:

★ (filled, U+2605) + ☆ (empty, U+2606), 5-star scale (max = ★★★★★)
Format: label ★★★★☆ 4/5
Always show all 5 stars (e.g. ★★☆☆☆, never ★★)
Overall rating section first, then Dimension Breakdown
Breakdown section: one dimension per row, all options on the same row
Always state the scale explicitly
Architecture Topology

Use when the decision changes component layout or system topology.

┌──────────────────┐
│  Load Balancer   │
└────────┬─────────┘
         │
    ┌────┴────┐
    ▼         ▼
 [API x2] [API x2]
    │         │
    └────┬────┘
         ▼
  ┌────────────┐
  │  Postgres  │
  └────────────┘

Boxes use ┌ ┐ └ ┘ ─ │ for infrastructure components
[brackets] for application components
Vertical flow primary; ──→ for horizontal connections
When to Add Diagrams
Star ratings: 3+ options × 2+ quantitative dimensions
Topology: the decision changes the physical or logical component layout
Do NOT add diagrams for simple yes/no or qualitative comparisons — use markdown tables
Max width: 78 characters
Entry and Exit Criteria

Enter when:

the decision node is explicit and bounded
the decision has at least two meaningful alternatives

Exit when:

there is a clear recommended option
the consequences of that decision are clear enough to feed back into the design
Handoff Rules
Hand back to design-refinement when the chosen option affects unresolved design branches.
Hand to design-readiness-check when this was the last major unresolved design issue.
Hand back to design-orchestrator if routing should be reconsidered after the decision lands.
Do not force broad design discovery into a bounded decision just to make progress.
Do not take over general design clarification work.
Weekly Installs
12
Repository
freeacger/loom
GitHub Stars
1
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass