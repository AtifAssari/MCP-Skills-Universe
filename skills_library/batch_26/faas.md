---
title: faas
url: https://skills.sh/ivcota/skills/faas
---

# faas

skills/ivcota/skills/faas
faas
Installation
$ npx skills add https://github.com/ivcota/skills --skill faas
SKILL.md
FAAS — Find, ARCH, Automate, Specify-Test-Refine

A four-phase engineering framework for shipping features with confidence. Each phase has a required input, a guided process, and an exit gate. You do not advance to the next phase until the exit gate is satisfied.

References: 54321 Layer Model | RDD Stereotypes | Phase Details & Artifacts | Interview Mode

Mode Detection

Standard mode (default): Agent explores the codebase to discover entry points, patterns, and context.

Interview mode: Activated when the user says "interview mode", "no codebase access", "faas interview", or similar. The agent interviews the user instead of exploring code. Do not use Glob, Grep, or Read for codebase exploration. All context comes from the conversation. See Interview Mode for full process.

Input Detection

Accepts: inline text, file path, URL, or design/screenshot. Identify the form and extract feature intent before Phase 1.

Artifacts

Each run is scoped to a feature slug — slugify the first 4-6 significant words to kebab-case. Save artifacts under ./faas/{slug}/ at the project root.

Phase	Artifact	Phase	Artifact
Find	find.md	ARCH	arch.md
Automate	automate.md	STR	(tests go green)
Phase 1: Find

Build enough context to see the full target before writing a single line. See full process.

Derive the slug and create ./faas/{slug}/
Parse input — extract user goal, UI flows, API calls, data
Explore codebase — identify L4 and L5 entry points
List scenarios with acceptance criteria (Given/When/Then)
Ask targeted gap questions (one at a time, only what code can't answer)
Confirm with user before writing find.md

Exit gate: All entry points listed | Every scenario has an AC | You can answer "what does done look like?"

Phase 2: ARCH

Decide exactly what you're building and how before touching code. See full process.

RDD: enumerate doings/knowings → assign stereotypes → produce CRC cards → design collaborations
Map everything to 54321 layers
List every file to create/modify, define patterns (no TBDs), note out-of-scope
Order implementation steps
Confirm with user before writing arch.md

Exit gate: Every component named with stereotype + layer | CRC cards complete | File list complete | Steps ordered

Phase 3: Automate

Prove the architecture works and define the failure target. See full process.

Confirm test map with user before scaffolding
Scaffold stubs (signatures only, no real logic)
Scaffold failing tests at appropriate testing boundaries
Verify the walking skeleton runs end-to-end
Document weirdness in automate.md

Exit gate: Every Find scenario has a failing test | Skeleton runs E2E | All weirdness documented

Phase 4: Specify-Test-Refine (STR)

Make every test green, one scenario at a time. See full process.

Red → Green → Refactor, per scenario. Do not refactor during red. Do not add scope not in Find.

At handoff, ask: (A) User implements, or (B) agent implements scenario-by-scenario with review.

Done when: Every Find scenario passes | No tests skipped without documented reason | Working software ships

The Loop Closes

STR stops when all Find scenarios are green. If a test doesn't map to a Find scenario, walk it back to find.md.

Weekly Installs
9
Repository
ivcota/skills
GitHub Stars
1
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn