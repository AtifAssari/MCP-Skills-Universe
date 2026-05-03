---
title: jarvis-starter
url: https://skills.sh/dtdesigner36/jarvis-starter/jarvis-starter
---

# jarvis-starter

skills/dtdesigner36/jarvis-starter/jarvis-starter
jarvis-starter
Installation
$ npx skills add https://github.com/dtdesigner36/jarvis-starter --skill jarvis-starter
SKILL.md
JARVIS Starter — persistent project assistant

Installed once in a new project. Sets up infrastructure for the detected project type (Telegram bot, web app, API, landing page, game, parser, mobile app, etc.). Then stays as a quiet assistant.

Modes
1. Bootstrap (first invocation in empty/new project)

User writes:

> jarvis start: <project description>


Or just:

> jarvis: <description>


JARVIS runs the sequence:

Phase 0 — Brownfield scan (if the folder has package.json/pyproject.toml/go.mod/etc., parse stack before asking questions)

Phase 0.5 — Dev-stage check (see archive/bootstrap/brownfield-adopt.md). If ≥2 dev-stage signals hit (≥10 commits, mature lockfile, real src/, existing CLAUDE.md, living docs/, running CI) — default to Adopt mode, not Start. User can override with jarvis start --force.

Phase 1 — Classification (see archive/bootstrap/classification.md)

Phase 2 — Proposal (stack + skills from registry + GitHub discovery via on-demand/skill-discovery/)

Phase 3 — Bootstrap installer — MUST run bash {{SKILL_PATH}}/scripts/bootstrap.sh <archetype> via the Bash tool after the user confirms Phase 2 ({{SKILL_PATH}} is where the skill is installed). This script actually copies universal templates + archetype overlay, creates .jarvis/, installs hooks into .claude/hooks/, and merges hooks into .claude/settings.json via jq. Reading the script and describing what it would do is not acceptable — it must be run.

After bootstrap.sh completes — call stack-matcher for proactive skill recommendations: bash {{SKILL_PATH}}/core/skill-discovery/stack-matcher.sh --archetype <archetype> --stack "<detected-tags>". Show its output to the user as part of Phase 2 proposal — this fulfills the "skill discovery" promise from the SKILL.md description.

Phase 4 — Verification. Mandatory checks:

jq '.hooks.PostToolUse' .claude/settings.json returns an array containing JARVIS hooks (post-edit + post-bash)
jq '.hooks.UserPromptSubmit' .claude/settings.json returns an array containing the JARVIS hook (pre-prompt)
.claude/hooks/post-edit.sh, post-bash.sh, pre-prompt.sh exist and are executable
.jarvis/state.md, .jarvis/memory.md, .jarvis/focus.md are created
CLAUDE.md and wiki/HOME.md are present
If any check fails — return to Phase 3 and re-run the installer, do not continue

Phase 5 — Token audit + optimization advice (CLAUDE.md size, wiki file count, check .gitignore / LICENSE / .env.example)

Phase 6 — git init + initial commit (if .git/ is missing) + offer to create a private GitHub repo via gh repo create. Write bootstrap-complete: true into .jarvis/state.md.

2. Adopt (existing project in active development)

User writes:

> jarvis adopt


Or jarvis start: <desc> auto-redirects here when Phase 0.5 detects dev-stage signals.

Philosophy: observe first, install only gaps, respect everything the user already built.

JARVIS runs (see archive/bootstrap/brownfield-adopt.md):

Phase A — Observe (read-only): stack, existing CLAUDE.md, hooks, docs, secret-scanners, issue tracking
Phase B — Gap analysis: for each core feature, check if the project already solves that problem. Skip if yes.
Phase C — Proposal: show interactive gap matrix. User approves / picks features / declines.
Phase D — Soft install: only checked features, in .jarvis/ namespace + new jarvis-*.sh hook files (never touches existing hooks / CLAUDE.md / docs).
Phase E — Record: write state to .jarvis/state.md including which features were skipped and why.

Hard rules in Adopt mode:

.jarvis/ is the only new directory at project root
CLAUDE.md gets one line max: <!-- JARVIS context: see .jarvis/state.md -->
Hooks are new files (jarvis-<feature>.sh), never appended to existing hooks
settings.json is structurally merged, never overwritten
No archetype overlay — user can run jarvis evolve <archetype> later
No wiki/ created if docs/ already exists
3. Persistent mode (after bootstrap or adopt)

JARVIS lives in .jarvis/ and works through core hooks:

🎯 Core (0 tokens at rest, active via hooks):

Wiki auto-maintenance — PostToolUse detects events (new module, large edit, new Prisma model) and injects short reminders into the tool result. See core/wiki-maintenance/.
Task Routing — UserPromptSubmit analyzes the prompt, classifies complexity (Trivial/Simple/Medium/Complex/Architectural), recommends model and plan mode. See core/task-routing/.
Memory & Wiki recall — UserPromptSubmit matches prompt topic against .jarvis/memory.md and wiki/Systems/*.md, injects a hint "already solved: ...". See core/memory-recall/.
Focus tracker — PostToolUse passively updates .jarvis/focus.md (shell-only, 0 tokens). See core/focus-tracker/.
Security watch — PostToolUse scans for hardcoded secrets and .env leaks. See core/security-watch/.

🔍 On-demand commands. JARVIS commands split in two: a small set of real shell scripts and a larger set of markdown instructions Claude reads on demand. The markdown ones aren't standalone programs — they guide Claude through a workflow. Most on-demand commands are the second kind.

Real shell scripts (executable):

jarvis self-audit — audit of JARVIS itself from shell: which hooks actually fired, usage counts, stale wiki (real output from core/self-audit/report.sh)

Model-prompted workflows (markdown Claude reads):

jarvis status — brief summary (Claude reads .jarvis/state.md + focus.md)
jarvis find "<need>" — Claude searches the curated registry and suggests a GitHub query; no automatic install
jarvis evolve <layer> — Claude applies an archetype overlay
jarvis decide "<q>" — help with an architectural decision
jarvis suggest — quality improvement suggestions
jarvis docs — wiki freshness check
jarvis audit — comprehensive audit of your project (wiki/tokens/deps)
jarvis security — security audit workflow (live secret-scan runs from hooks; the audit command is a walkthrough)
jarvis route "<task>" — manually classify task complexity

📦 Rare commands: remember, forget, history, focus, optimize — markdown workflows in archive/subcommands-rare/.

🔌 Plugins (off by default):

school-mode — for those who want not just to build but to learn. Creates a separate school-wiki/ with a topic index for the project's stack. Deep exploration happens only on request via jarvis school topic <area>. Activation: jarvis school on. NOT proactively offered — user decides.
For vibe-coders (primary audience)

JARVIS is a "smart programmer friend" for people who:

Describe ideas in free form
Don't know which model to pick (Opus vs Sonnet vs Haiku)
Don't know when to enable plan mode
Don't know which libraries are worth installing

JARVIS makes these decisions for them or with them, in plain language.

For technically literate users

Same hooks, but you can disable the ones that get in the way. All JARVIS decisions are suggestions, not enforcement. If something annoys you — jarvis off (or per-hook via .jarvis/plugins.md).

Installation
# Install the skill
npx skills add dtdesigner36/jarvis-starter --yes

# New / empty project
> jarvis start: <project description>

# Existing project already in development
> jarvis adopt


If you type jarvis start in an existing project, JARVIS detects the dev-stage and auto-switches to Adopt (with a confirmation prompt).

Important rules

Do NOT suggest enabling school-mode — user decides

Do NOT output status automatically at session start — only on jarvis status

Bootstrap = actually calling scripts/bootstrap.sh, not imitating it. The only way to activate JARVIS hooks is to run bash {{SKILL_PATH}}/scripts/bootstrap.sh <archetype> via the Bash tool in Phase 3. Describing "what the installer would do" or manually creating individual files is not acceptable — the hooks must actually end up in .claude/settings.json. If Phase 4 verification doesn't find the hooks — the installer didn't run, repeat Phase 3.

Core hooks work always after bootstrap (can be disabled via .jarvis/plugins.md)

Wiki is mandatory infrastructure in Start mode; in Adopt mode — respect existing docs, do not create parallel wiki/

Priority: quality > token optimization

Brownfield-safe default: when dev-stage is detected, default path is Adopt (gap-analysis, zero overwrite), not Start. See archive/bootstrap/brownfield-adopt.md.

ADR moment = MANDATORY jarvis decide. On any choice between 2+ alternatives in the categories below, the model must first run the decide flow (see on-demand/decide.md) and record the result in wiki/Decisions/ or wiki/Architecture/, and only then proceed with implementation. Trigger categories:

Library choice (aiogram vs python-telegram-bot, Prisma vs Drizzle, Express vs NestJS, ...)
Storage choice (Redis vs in-memory vs DB, SQLite vs PostgreSQL, JSON vs YAML)
Architectural pattern (monorepo vs polyrepo, event-driven vs sync, REST vs GraphQL vs gRPC)
Interaction protocol (webhook vs polling, WebSocket vs SSE)
Stack / runtime change (Python 3.11 → 3.12, Node → Bun, ...)
Significant architecture refactor (monolith split, framework swap)

Exceptions — trivial edits that don't create irreversible decisions (rename a variable, add a log, cosmetics). When in doubt — call decide rather than skip.

If the pre-prompt.sh hook detects ADR signals in the prompt, it injects a reminder "this is an ADR moment — call jarvis decide". The model must not ignore such a reminder.

File architecture

See README.md for full structure. Key points:

core/ — always-on hooks
on-demand/ — on-request commands
plugins/ — optional extensions (school-mode)
archive/ — bootstrap and rare commands
Weekly Installs
18
Repository
dtdesigner36/ja…-starter
GitHub Stars
1
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn