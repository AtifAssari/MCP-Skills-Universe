---
rating: ⭐⭐
title: speccy
url: https://skills.sh/slamb2k/mad-skills/speccy
---

# speccy

skills/slamb2k/mad-skills/speccy
speccy
Installation
$ npx skills add https://github.com/slamb2k/mad-skills --skill speccy
SKILL.md
Speccy - Interview-Driven Specification Builder

When this skill is invoked, IMMEDIATELY output the banner below before doing anything else. Pick ONE tagline at random — vary your choice each time. CRITICAL: Reproduce the banner EXACTLY character-for-character. The first line of the art has 4 leading spaces — you MUST preserve them.

{tagline}

⠀   ██╗███████╗██████╗ ███████╗ ██████╗ ██████╗██╗   ██╗
   ██╔╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝╚██╗ ██╔╝
  ██╔╝ ███████╗██████╔╝█████╗  ██║     ██║      ╚████╔╝
 ██╔╝  ╚════██║██╔═══╝ ██╔══╝  ██║     ██║       ╚██╔╝
██╔╝   ███████║██║     ███████╗╚██████╗╚██████╗   ██║
╚═╝    ╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═════╝   ╚═╝


Taglines:

🔍 Tell me everything...
🧠 Let's think this through!
📋 Spec it before you wreck it!
🎤 Interview mode: ACTIVATED
💡 Great specs start with great questions!
🏗️ Measure twice, code once!
📝 No assumption left behind!
🎯 Precision engineering starts here!
Output Formatting

After the banner, display parsed input:

┌─ Input ────────────────────────────────────────
│  {Field}:  {value}
│  Flags:    {parsed flags or "none"}
└────────────────────────────────────────────────


Pre-flight results:

── Pre-flight ───────────────────────────────────
  ✅ {dep}           {version or "found"}
  ⚠️ {dep}           not found → {fallback detail}
  ❌ {dep}           missing → stopping
──────────────────────────────────────────────────


Stage/phase headers: ━━ {N} · {Name} ━━━━━━━━━━━━━━━━━━━━━━━━━

Status icons: ✅ done · ❌ failed · ⚠️ degraded · ⏳ working · ⏭️ skipped

Interview the user through multiple rounds of targeted questions to build a comprehensive specification, then write it directly using the spec template in references/spec-template.md.

Interview prompts and question guidelines: references/interview-guide.md Spec template and writing guidelines: references/spec-template.md

Pre-flight

Before starting, check all dependencies in this table:

Dependency	Type	Check	Required	Resolution	Detail
prime	skill	ls .claude/skills/prime/SKILL.md ~/.claude/skills/prime/SKILL.md ~/.claude/plugins/marketplaces/slamb2k/skills/prime/SKILL.md 2>/dev/null	no	fallback	Context loading; falls back to manual project scan

For each row, in order:

Test file existence (check both paths for symlinked skills)
If found: continue silently
If missing: apply Resolution strategy
After all checks: proceed to context gathering
Stage 1: Context Gathering

Before asking any questions, build a thorough understanding of the project:

Capture GOAL — the user's argument describing what needs to be specified
Load project context — invoke /prime to load domain-specific context (CLAUDE.md, specs, memory). If /prime is unavailable, fall back to the manual scan below.
Scan the project (skip items already loaded by /prime):
Read CLAUDE.md if present (project conventions, structure, domain)
Scan specs/ directory for existing specifications
Scan existing design docs for context
Read relevant source code that relates to the GOAL
Check memory for prior decisions or open questions related to the GOAL
Identify knowledge gaps — what must you learn from the user to write a complete, unambiguous specification?

Group gaps into interview categories:

Architecture & Technical Design — stack, patterns, data flow, integrations
Requirements & Scope — what's in, what's out, must-haves vs nice-to-haves
UI & UX — user flows, interaction patterns, accessibility, responsive
Security & Auth — authentication, authorization, data protection
Infrastructure & Deployment — hosting, CI/CD, environments, IaC
Data & Storage — schemas, persistence, migrations, caching
Testing & Quality — test strategy, coverage, acceptance criteria
Concerns & Tradeoffs — known risks, alternatives considered, constraints
Stage 2: Interview Rounds

Conduct multiple rounds of questions using AskUserQuestion. Continue until all knowledge gaps are resolved.

Question Rules
4 questions per round maximum (AskUserQuestion limit)
Non-obvious questions only — don't ask things you can determine from reading the code or docs. The user's time is valuable.
Recommendations — where you have an informed opinion based on the codebase, project conventions, or industry best practice, mark one option as recommended by listing it first and appending (Recommended) to its label. At least one question per round should have a recommendation where possible.
Concise options — 2-4 options per question, each with a clear description of implications and tradeoffs
Progressive depth — start with high-level architecture and scope, then drill into implementation details in later rounds
Build on answers — use previous round answers to inform next questions. Don't re-ask decided topics.
Track decisions — maintain a running list of all decisions made. Present this list at the start of each round so the user can see progress.
Round Structure

Each round follows this pattern:

Progress update — brief summary of decisions made so far (after round 1)
Category label — which interview category this round covers
Questions — 3-4 targeted questions via AskUserQuestion
Evaluate — after answers, determine if more questions are needed
Completion Criteria

Stop interviewing when ALL of the following are true:

All identified knowledge gaps have been addressed
No answer has raised new unresolved questions
You have enough information to write every section of the spec template
The user has confirmed scope boundaries (what's in and what's out)

When complete, briefly present a Decision Summary — a numbered list of all decisions made across all rounds — and confirm with the user before proceeding to spec generation.

Stage 3: Generate Specification

Once the interview is complete and decisions are confirmed:

Create specs/ directory if it doesn't exist:

mkdir -p specs


Read the spec template from references/spec-template.md

Generate the spec by filling the template with:

The original GOAL as the introduction and purpose
All decisions from the interview rounds, mapped to the appropriate sections
Code/architecture context discovered in Stage 1
Acceptance criteria derived from requirements decisions
Test strategy aligned with the project's existing patterns

Write the spec file to specs/{name}.md where {name} is a kebab-case slug derived from the GOAL (e.g., specs/user-auth.md, specs/payment-integration.md). Use the Write tool directly.

The specs/ directory is the standard location — /build and /prime both scan it automatically.

Output & Handoff

After the spec is created, report to the user:

┌─ Speccy · Report ──────────────────────────────
│
│  ✅ Spec complete
│
│  📄 File:       {spec file path}
│  📋 Sections:   {count}
│  💬 Rounds:     {interview rounds conducted}
│  ❓ Questions:  {total questions asked}
│
│  📝 Key decisions
│     • {decision 1}
│     • {decision 2}
│     • {decision 3}
│
│  🔗 Links
│     Spec: {spec file path}
│
│  ⚡ Next steps
│     1. Review the spec: {path}
│     2. Run `/build {spec path}` to implement (reads the file automatically)
│
└─────────────────────────────────────────────────


Then immediately ask the user via AskUserQuestion:

Question: "Spec written to {spec file path}. Ready to build?" Options:

"Clear context & build (Recommended)" — clear the conversation first, then run /build
"Build now" — invoke /build immediately in the current context
"Review first" — stop here so the user can review the spec before building
"Done" — stop here, no build

If the user selects "Clear context & build":

Run /clear to clear the conversation context
Then invoke /build {spec file path}:
Skill(skill: "build", args: "{spec file path}")

/build reads the spec file via Plan Resolution and executes the full pipeline with maximum context window available.

If the user selects "Build now":

Invoke /build {spec file path} directly:
Skill(skill: "build", args: "{spec file path}")

/build reads the spec file via Plan Resolution and executes the full pipeline. The current conversation context is preserved.

In both cases, do not attempt to implement the spec yourself — always delegate to /build.

If the user selects "Review first" or "Done", stop and display:

⚡ To build later, run: /build {spec file path}


IMPORTANT: After generating the spec, do NOT enter plan mode, do NOT start implementing directly, and do NOT offer to execute the plan yourself. The only path to implementation is through /build.

Weekly Installs
10
Repository
slamb2k/mad-skills
GitHub Stars
2
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass