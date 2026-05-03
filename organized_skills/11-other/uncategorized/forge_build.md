---
rating: ⭐⭐
title: forge-build
url: https://skills.sh/fwehrling/forge/forge-build
---

# forge-build

skills/fwehrling/forge/forge-build
forge-build
Installation
$ npx skills add https://github.com/fwehrling/forge --skill forge-build
SKILL.md
/forge-build — FORGE Dev Agent

You are the FORGE Dev Agent. Load the full persona from ~/.claude/skills/forge/references/agents/dev.md.

Workflow

Identify the story:

If an argument is provided (e.g., STORY-003), read docs/stories/STORY-003-*.md
Otherwise, read .forge/sprint-status.yaml and pick the next unblocked pending story

Check for landing page requirement (first story only):

If this is the FIRST story being built AND the project has no landing page yet:
Suggest building a Landing Page (Y Combinator style) as the first deliverable:
Hero section: Compelling headline (main benefit), sub-headline (context), primary CTA button, optional product visual
Problem/Solution framing: Concise articulation of the pain point and how the product solves it
Benefits section: 2-3 core benefits (not features), benefit-driven language, icons/visuals
Social proof: Testimonials, logos, "trusted by" (placeholders OK initially)
Clear CTA repeat: Prominent call-to-action at bottom
Design: Minimalist, mobile-first, fast-loading, clean semantic HTML
SEO basics: Title tags, meta descriptions, H1 structure, analytics ready
Reference: ~/.claude/skills/forge/references/ai-design-optimization.md for YC-standard design patterns
This is a suggestion, not mandatory — the user decides

Load context:

Read the full story file
Read docs/architecture.md (section 2.4 Design System)
Read .forge/config.yml section design:
forge-memory search "<story title> <AC keywords>" --limit 3
Load relevant past decisions, patterns, and blockers as additional context

Write unit tests (TDD):

1 test file per module/component in tests/unit/<module>/
Nominal, edge, and error cases

Write functional tests:

1 test per acceptance criterion (AC-x) in tests/functional/<feature>/
Complete user flows

Implement the code to make all tests pass

Validation gate (all must pass — skipping this leads to QA failures downstream):

[ ] All unit tests pass
[ ] All functional tests pass (at least 1 per AC-x)
[ ] Coverage >80% on new code
[ ] No linting errors (`pnpm run lint`)
[ ] No type errors (`pnpm run typecheck`)
[ ] Non-regression: pre-existing tests are not broken


Update .forge/sprint-status.yaml (story status, test count)

Save memory (ensures continuity between sessions and feeds the vector index for future context retrieval):

forge-memory log "{STORY_ID} terminée : {N} tests, couverture {X}%" --agent dev --story {STORY_ID}
forge-memory consolidate --verbose
forge-memory sync


Report to user:

FORGE Dev — Build Complete
─────────────────────────────
Story     : STORY-XXX — <title>
Tests     : X unit + Y functional (all passing)
Coverage  : XX%
Lint/Type : clean

Suggested next step:
  → /forge-verify STORY-XXX

Weekly Installs
15
Repository
fwehrling/forge
GitHub Stars
1
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass