---
rating: ⭐⭐⭐
title: project-onboard
url: https://skills.sh/nixxel-company-limited/nixxel-skills/project-onboard
---

# project-onboard

skills/nixxel-company-limited/nixxel-skills/project-onboard
project-onboard
Installation
$ npx skills add https://github.com/nixxel-company-limited/nixxel-skills --skill project-onboard
SKILL.md
Project Onboard

A skill that onboards AI agents into any project by generating structured, task-routed context files. Unlike /init which produces a flat CLAUDE.md, this skill creates a progressive disclosure system where the agent reads only what it needs for the current task — saving tokens and eliminating redundant project exploration.

Invocation
/onboard                     Full onboard (all phases)
/onboard --quick             Phase 1+2 only (skip audit & interview)
/onboard Thai                Full onboard, confirm output language first
/onboard-update              Incremental update (changed files only)
/onboard-update --full       Re-scan everything, keep interview answers
/onboard-audit               Run feature audit only (Phase 3)
/onboard-audit --update      Update audit for changed files only
/onboard-suggest             Suggest skills for detected stack

Language Support

If the user appends a language name to the command (e.g., /onboard Thai, /onboard Japanese), confirm the language before proceeding:

"You requested output in Thai. This will generate all context files
and CLAUDE.md in Thai. Confirm? (yes/no)"


If confirmed, write ALL output files in that language — CLAUDE.md, context files, feature map, everything. The SKILL.md instructions themselves remain in English, but generated output respects the user's language choice.

Default language is English if not specified.

How It Works

The skill runs 4 phases. Each phase builds on the previous one. The agent knows more at each step, so later phases are smarter.

Phase 1: DISCOVER .......... auto-detect stack + research docs
Phase 2: GENERATE .......... create CLAUDE.md + context files
Phase 3: FEATURE AUDIT ..... map Page → API → DB → Feature (optional)
Phase 4: INTERVIEW ......... ask the developer (knows everything now)


Phase 3 and 4 are optional. After Phase 2, ask the user:

"Want me to audit existing features? (maps pages, endpoints, DB)"
"Want me to interview you for business context?"

If the user runs /onboard --quick, skip Phase 3 and 4.

Phase 1: DISCOVER

Two sub-phases. Do not ask the user anything during this phase.

Phase 1a: DETECT

Read project files to identify the tech stack and tooling. Do NOT use find or ls recursively. Read specific known files only.

Check these files (skip if they don't exist):

Package managers & stack:

package.json → Node.js ecosystem, framework, dependencies, scripts
pubspec.yaml → Flutter/Dart
go.mod → Go
requirements.txt / pyproject.toml / Pipfile → Python
Cargo.toml → Rust
composer.json → PHP
Gemfile → Ruby

Mobile:

package.json dep react-native → React Native
app.json / app.config.js → Expo
pubspec.yaml dep flutter → Flutter

State management:

@reduxjs/toolkit / zustand / jotai / @tanstack/react-query in deps
riverpod / bloc / provider in pubspec.yaml

Background jobs:

bullmq / bull / celery / sidekiq in deps
Queue processor files

i18n:

Locale files (en.json, th.json, etc.)
i18n library in deps (next-intl, react-i18next, flutter_localizations)

Configuration:

tsconfig.json → TypeScript settings
.eslintrc* / biome.json / .prettierrc → linting/formatting
docker-compose.yml / Dockerfile → containerization
vercel.json / netlify.toml / fly.toml → deploy target
.env.example → environment variables (NEVER read .env)

Database:

prisma/schema.prisma → Prisma schema
drizzle.config.ts → Drizzle ORM
knexfile.* / ormconfig.* → other ORMs
migrations/ or db/migrate/ → check migration tool

CI/CD & workflows:

.github/workflows/ → GitHub Actions
.gitlab-ci.yml → GitLab CI
.husky/ → git hooks

Testing:

jest.config* / vitest.config* / playwright.config* / cypress.config*
Count test files: how many *.test.* or *.spec.* files exist

Existing AI context:

CLAUDE.md → preserve, merge later
.cursor/rules/ → import conventions
AGENTS.md → existing agent instructions
.github/copilot-instructions.md → existing copilot rules

Documentation:

README.md → project description, setup
CONTRIBUTING.md → team conventions
CHANGELOG.md → recent changes, current version
docs/ → architecture docs
Phase 1b: RESEARCH

Use the information from Phase 1a to do targeted research.

1. Project docs — read what exists in the repo

Read README.md fully. Extract: project purpose, setup instructions, architecture notes. If CONTRIBUTING.md or docs/ exist, read those too.

2. Stack docs — pull up-to-date docs via Context7 (conditional)

Read .context/onboard-meta.json if it exists. For each major dependency:

If version has changed since last onboard → pull fresh docs
If docs are older than 7 days → pull fresh docs
If docs are fresh and version unchanged → SKIP, use cached

When pulling, query Context7 for the specific version detected. Focus on: conventions, breaking changes, migration guides, best practices.

Save results to .context/stack-docs/{lib}-{version}.md

3. Skills — search for relevant skills

Based on detected stack, search for available skills:

npx skills search {framework} if the CLI is available
Or note recommendations from known sources:
vercel-labs/agent-skills (React, Next.js, deploy)
VoltAgent/awesome-agent-skills (community collection)

Store recommendations for Phase 2 output and Phase 4 suggestion.

4. Ecosystem — verify actual tooling

Read package.json scripts to understand real build/test/dev commands. Read CI config to understand actual pipeline steps. Read tsconfig/eslint to understand actual code conventions. DO NOT assume — verify from config files.

Phase 2: GENERATE

Generate the output files. Read references/output-format.md for the complete templates and file structure.

PATH RULES — read carefully before writing any file:

Context files go in project-root/.context/ (a top-level dot folder)
Claude commands go in project-root/.claude/commands/
These are TWO SEPARATE directories at project root. Do NOT nest .context/ inside .claude/.
Wrong: .claude/context/, .claude/.context/, .claude/architecture.md
Correct: .context/architecture.md, .claude/commands/onboard-update.md

Before creating the first file, double-check: are you about to write to .context/ or .claude/context/? If the path contains .claude/context or .claude/.context, STOP — that's wrong. Fix it to .context/.

Output structure
project-root/
├── CLAUDE.md                          # ≤ 150 lines, task-routed
├── .context/                          # ⚠️ THIS IS project-root/.context/ — NOT .claude/context/
│   ├── architecture.md                # Directory map + patterns
│   ├── conventions.md                 # Coding standards (from config)
│   ├── workflow.md                    # CI/CD, deploy, branch strategy
│   ├── stack-docs/                    # Cached library docs
│   │   └── {lib}-{version}.md
│   ├── warnings.md                    # Things to watch out for
│   └── onboard-meta.json             # Metadata for incremental updates
└── .claude/
    ├── commands/
    │   ├── onboard-update.md          # /onboard-update command
    │   └── onboard-audit.md           # /onboard-audit command
    └── .claudeignore                  # (if not exists) auto-generated


⚠️ CRITICAL PATH WARNING: .context/ lives at project root — the same level as CLAUDE.md. NEVER create .claude/context/ — that is wrong. The two directories are separate:

.context/ = onboard context files (architecture, conventions, features, etc.)
.claude/ = Claude commands and config only
CLAUDE.md — CRITICAL RULES

CLAUDE.md is NOT documentation for humans. It is a decision tree for the AI agent.

Write it using the task-based routing pattern:

BEFORE [action] → read [file]
WHEN [situation] → read [file]


Never just list files. Always tell the agent WHEN to read each file.

Read references/output-format.md for the full CLAUDE.md template.

Context files — AI-first writing

Every context file must start with:

WHEN to read this file (one line)
HOW the agent should use the information
The actual content — concise, structured, actionable

Do NOT write prose. Write structured data the agent can act on.

onboard-meta.json
{
  "version": "2.0",
  "last_onboard": "ISO-8601",
  "last_update": "ISO-8601",
  "git_commit": "hash",
  "language": "en",
  "stack": ["nextjs", "prisma", "postgresql"],
  "platforms": {
    "web": true,
    "mobile": false,
    "backend": true
  },
  "categories_detected": [
    "pages-routing",
    "api-middleware",
    "data-layer",
    "auth-security",
    "background-events",
    "integrations-infra"
  ],
  "stack_docs": {
    "next": { "version": "15.1.0", "docs_pulled_at": "ISO-8601" }
  },
  "phases_completed": ["discover", "generate"],
  "interview_done": false,
  "audit_done": false
}

Merging with existing CLAUDE.md

If CLAUDE.md already exists:

Read it fully
Preserve all existing content
ADD missing sections (task routing, context references, warnings)
DO NOT overwrite user-written content
Mark generated sections with <!-- generated by project-onboard -->
Skill recommendations

After generating files, show the user what skills are available:

"Detected: Next.js + React + Prisma. Recommended skills:"
  1. vercel-react-best-practices — 40+ React performance rules
  2. web-design-guidelines — accessibility + UX audit
  
"Install with: npx skills add vercel-labs/agent-skills@vercel-react-best-practices"
"Want me to install any of these?"

Phase 3: UNIVERSAL AUDIT (optional)

Ask before running: "Want me to audit existing features? I'll scan pages, state, UI, API, data, auth, jobs, and integrations."

If yes, scan the codebase using 8 categories. Each category auto-detects and auto-skips if not found. Read references/universal-audit.md for full scanning strategies and output templates.

The 8 Categories
#	Category	Output file	What it covers
1	Pages & Routing	pages-routing.md	Pages, screens, navigation, deep links, route guards
2	State & Data Fetching	state-data.md	Stores, slices, providers, client caching, data fetching
3	Design System & UI	design-system.md	Components, theming, forms, i18n, accessibility
4	API & Middleware	api-middleware.md	Endpoints, middleware pipeline, validation, error handling
5	Data Layer	data-layer.md	DB schema, migrations, caching, transactions, seeds
6	Auth & Security	auth-security.md	Authentication, authorization, rate limits, CORS, secrets
7	Background & Events	background-events.md	Jobs, event-driven arch, scheduled tasks, service comms
8	Integrations & Infra	integrations-infra.md	External APIs, file storage, logging, config, health checks

Cross-reference all detected categories into _feature-map.md. Also identify orphans: unmapped endpoints, pages, state, jobs, DB tables.

Output files

Remember: .context/ is at project root, not inside .claude/.

.context/features/
  ├── _feature-map.md           # Cross-reference all categories per feature
  ├── pages-routing.md          # 1: Pages & Routing (web + mobile)
  ├── state-data.md             # 2: State & Data Fetching
  ├── design-system.md          # 3: Design System & UI
  ├── api-middleware.md          # 4: API & Middleware
  ├── data-layer.md             # 5: Data Layer
  ├── auth-security.md          # 6: Auth & Security
  ├── background-events.md      # 7: Background & Events
  ├── integrations-infra.md     # 8: Integrations & Infra
  └── audit-meta.json           # Coverage stats per category


After generating, update CLAUDE.md with task-routing rules:

BEFORE modifying or creating any page, screen, or route:
  → read .context/features/pages-routing.md
  → read .context/features/_feature-map.md

BEFORE modifying app state (stores/slices/providers):
  → read .context/features/state-data.md
  → read .context/features/pages-routing.md (check consumers)

BEFORE modifying UI components, theming, forms, or i18n:
  → read .context/features/design-system.md

BEFORE modifying or creating any API endpoint:
  → read .context/features/api-middleware.md
  → read .context/features/pages-routing.md (check callers)

BEFORE modifying database schema, caching, or migrations:
  → read .context/features/data-layer.md
  → read .context/features/_feature-map.md (check impact)

BEFORE modifying auth, permissions, or security config:
  → read .context/features/auth-security.md

BEFORE modifying background jobs, events, or service communication:
  → read .context/features/background-events.md

BEFORE modifying external integrations, logging, or config:
  → read .context/features/integrations-infra.md

Phase 4: INTERVIEW (optional)

The agent has now scanned and understood the entire project. Questions are informed by everything discovered in Phase 1-3.

Ask before running: "Want me to ask you some questions about the project? This helps me understand things code can't tell me."

If Phase 3 was completed — short interview (3 questions)

The agent already knows the codebase deeply. Ask only what code cannot reveal:

1. "[Summary from README + code]. Is this accurate?
    Any business context or domain terms I should know?"

2. "Any conventions, processes, or areas I should NOT touch
    without asking first?"

3. "Anything else you want me to know?"

If Phase 3 was skipped — full interview (4 groups)
Group 1: Business & Domain
1. "What does this project do? Who are the main users?"
2. "Any domain-specific terms I should understand?"
3. "What phase is this project in?
    (MVP / active dev / maintenance / legacy refactor)"

Group 2: Team & Workflow
4. "How many people work on this? Code review process?"
5. "Branch strategy? (trunk-based / gitflow / feature branches)"
6. "Deploy process? (auto/manual, staging environment?)"
7. "Any conventions you want me to always follow?"

Group 3: Code Quality & Testing
8. "Want to restructure the code?
    (e.g., extract business logic to service layer)"
    — If Phase 1 found logic in route handlers, mention it specifically.

9. "Do you want TDD? (write tests before implementation)"

10. "Testing strategy?"
    — Unit only
    — Unit + Integration
    — Unit + Integration + E2E
    — No tests yet, want to start

11. "Test framework preference?"
    — Mention what was detected: "Found [vitest/jest], correct?"
    — For E2E: Playwright / Cypress / other?

12. "Coverage target? (none / 60% / 80% / 90%+)"
    — If tests exist, mention current estimated coverage.

Group 4: AI Behavior
13. "Anything that AI agents frequently break in this project?"

14. "Files or folders I should never modify without asking?"

15. "How autonomous should I be?"
    — Conservative: always ask before acting
    — Balanced: act but explain
    — Autonomous: just do it

16. "Anything else I should know?"

Adaptive questions

Questions MUST adapt to what was discovered. Do not ask generic questions when you already have the answer from Phase 1-3.

Example — tests detected:

BAD:  "Do you want to write tests?"
GOOD: "Found Vitest with 23 test files, ~45% coverage.
       Want me to help increase coverage? Add E2E with Playwright?"


Example — logic in route handlers:

BAD:  "Want to restructure the code?"
GOOD: "Found business logic directly in route handlers
       (e.g., /api/pipelines has 120 lines of logic).
       Want me to extract it to a service layer?"

Interview output

Save answers to context files:

Business context → .context/business.md
Testing strategy → .context/testing-strategy.md
Update warnings.md with files/areas to protect
Update workflow.md with team process info
Update conventions.md with stated preferences
Update CLAUDE.md task-routing with new sections

Update onboard-meta.json: set interview_done: true.

Incremental Update (/onboard-update)

When the user runs /onboard-update:

Read .context/onboard-meta.json
Run git diff {last_commit}..HEAD --name-only to find changed files
For each changed file, determine which context files need updating:
package.json changed → re-detect stack, check if docs need refresh
prisma/schema.prisma changed → update db-schema.md + feature-map
Route files changed → update api-endpoints.md + feature-map
Page files changed → update pages-views.md + feature-map
Config files changed → update conventions.md or workflow.md
Update only affected context files
Update onboard-meta.json with new timestamp and commit hash
Show summary: "Updated X files based on Y changes since last onboard"

For /onboard-update --full:

Re-scan everything from Phase 1
Regenerate all context files
Preserve interview answers (do not re-ask)
Stack Docs Caching

Context7 docs are cached in .context/stack-docs/. Pull strategy:

Condition	Action
Never pulled	Pull now
Library version changed	Pull now (may have breaking changes)
Same version, docs ≤ 7 days old	Skip, use cache
Same version, docs > 7 days old	Pull fresh
User runs --force-docs	Pull everything
Future: Multi-agent Support

This skill currently generates output for Claude Code only. Future versions may support additional agents:

Claude Code  → CLAUDE.md + .context/
Cursor       → .cursor/rules/
Codex        → AGENTS.md
Copilot      → .github/copilot-instructions.md


The context files in .context/ are written in agent-neutral markdown. Adding support for other agents means generating a wrapper file that routes to the same context.

Reference files

Read these before generating output:

references/output-format.md — CLAUDE.md template, context file templates
references/feature-audit-format.md — Feature audit output templates
references/universal-audit.md — Full scanning strategies + output templates for all 8 audit categories
Weekly Installs
15
Repository
nixxel-company-…l-skills
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn