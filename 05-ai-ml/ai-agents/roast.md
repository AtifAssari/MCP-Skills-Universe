---
rating: ⭐⭐⭐
title: roast
url: https://skills.sh/notque/claude-code-toolkit/roast
---

# roast

skills/notque/claude-code-toolkit/roast
roast
Installation
$ npx skills add https://github.com/notque/claude-code-toolkit --skill roast
SKILL.md
Roast: Devil's Advocate Analysis
Overview

This skill produces evidence-based constructive critique through 5 specialized HackerNews commenter personas: Skeptical Senior, Well-Actually Pedant, Enthusiastic Newcomer, Contrarian Provocateur, and Pragmatic Builder. The workflow spawns these personas in parallel, validates all claims against actual files and lines, and synthesizes findings into an improvement-focused report.

Key constraints baked into the workflow:

CLAUDE.md must be read and followed before analysis begins
Read-only mode (no Write, Edit, destructive Bash) is mandatory — enforced via read-only-ops skill invocation
Every claim must reference specific file:line locations and be validated against actual evidence before appearing in the final report
All 5 personas must complete before validation begins — no partial analysis
Final report must include both validated strengths and problems, prioritized by impact
Unvalidated claims are dismissed; unfounded critiques are shown with evidence explaining why
Analysis must be direct and focused — no elaborate frameworks beyond the 5-persona + validation pattern
Sarcasm and mockery are stripped during synthesis; technical accuracy and file references are preserved
Instructions
Phase 1: ACTIVATE READ-ONLY MODE

Goal: Establish guardrails before any analysis begins.

Invoke the read-only-ops skill:

skill: read-only-ops


This ensures no modifications can occur during the analysis workflow.

Allowed operations:

Read tool for file contents
Glob tool for file patterns
Grep tool for content search
Bash: ls, wc, du, git status, git log, git diff

Forbidden operations:

Write tool -- no file creation
Edit tool -- no file modification
Bash: rm, mv, cp, mkdir, touch, git add, git commit, git push

If read-only mode cannot be activated, stop immediately. Never proceed with unguarded analysis.

Gate: Read-only mode active. Proceed only when gate passes.

Phase 2: GATHER CONTEXT

Goal: Understand the target thoroughly before spawning critical perspectives.

Step 1: Identify target type

Input	Target	Action
No argument	README.md + repo structure	Read README, survey project layout
@file.md	Specific file	Read that file, identify related files
Description	Described concept	Search repo for related implementation

Step 2: Read key files

Use Read tool to examine: README.md, main documentation, key implementation files relevant to the target.

Step 3: Survey structure

Use Glob to map the landscape:

**/*.md for documentation coverage
Source code organization and entry points
Configuration files and dependency declarations

Step 4: Search for patterns

Use Grep to find: specific claims to verify, usage patterns, dependency references, related test files.

Step 5: Ground verbal descriptions

If user describes a concept rather than pointing to a file, search the repo for existing implementation. Critique grounded in actual code beats critique of a strawman every time. Never analyze a verbal description without confirming the code exists.

Gate: Target identified and sufficient context gathered. Proceed only when gate passes.

Phase 3: SPAWN ROASTER AGENTS (Parallel)

Goal: Launch 5 agents in parallel, each embodying a roaster persona, analyzing the target with full evidence-gathering discipline.

Launch 5 general-purpose agents in parallel via Task tool. Load the full persona specification from the corresponding agent file into each prompt.

The 5 parallel tasks:

Skeptical Senior (agents/reviewer-code.md, senior lens) Focus: Sustainability, maintenance burden, long-term viability

Well-Actually Pedant (agents/reviewer-code.md, pedant lens) Focus: Precision, intellectual honesty, terminological accuracy

Enthusiastic Newcomer (agents/reviewer-perspectives.md, newcomer lens) Focus: Onboarding experience, documentation clarity, accessibility

Contrarian Provocateur (agents/reviewer-perspectives.md, contrarian lens) Focus: Fundamental assumptions, alternative approaches

Pragmatic Builder (agents/reviewer-domain.md, pragmatic-builder lens) Focus: Production readiness, operational concerns

Each agent must:

Invoke read-only-ops skill first to enforce no-modification guardrails
Follow their systematic 5-step review process
Tag ALL claims as [CLAIM-N] with specific file:line references
Provide concrete evidence for every claim — vague critiques are worthless and must be rejected during validation
Search for actual implementation details rather than analyzing verbal descriptions

See references/personas.md for full prompt template and claim format.

CRITICAL: Wait for all 5 agents to complete before proceeding to Phase 4. Do not begin validation on partial results. Every persona must contribute before synthesis can happen.

Gate: All 5 agents complete with tagged claims. Proceed only when gate passes.

Phase 4: COORDINATE (Validate Claims)

Goal: Verify every [CLAIM-N] against actual evidence before including in the report.

Collect and validate every [CLAIM-N] from all 5 agents.

Step 1: Collect all claims

Extract every [CLAIM-N] tag from all 5 agent outputs. For each, track:

Claim ID and text
Source persona (Senior, Pedant, Newcomer, Contrarian, Builder)
Referenced file:line location

Step 2: Validate each claim

For each [CLAIM-N], read the referenced file/line using Read tool and assign a verdict:

Verdict	Meaning	Criteria
VALID	Claim is accurate	Evidence directly supports it
PARTIAL	Overstated but has merit	Some truth, some exaggeration
UNFOUNDED	Not supported	Evidence contradicts or doesn't exist
SUBJECTIVE	Opinion, can't verify	Matter of preference/style

Critical: You must read the file and check the line. Visual inspection misses nuance. "Obviously valid" is a rationalization word. Do not accept a claim because it sounds right or all personas agree on it — consensus is not the same as correctness.

Step 3: Cross-reference

Note claims found independently by multiple agents. If 3+ personas independently identify the same issue, escalate to HIGH priority regardless of individual severity.

Step 4: Prioritize

Sort VALID and PARTIAL findings by impact:

HIGH: Core functionality, security, or maintainability
MEDIUM: Important improvements with moderate impact
LOW: Minor issues or polish

Gate: All claims validated with evidence. Proceed only when gate passes.

Phase 5: SYNTHESIZE (Generate Report)

Goal: Transform aggressive persona outputs into constructive, actionable report.

Follow the full template in references/report-template.md. Key synthesis rules:

Filter by verdict: Only VALID and PARTIAL claims appear in improvement opportunities
Dismissed section: UNFOUNDED claims go in dismissed section with evidence showing why. Transparency matters — users need to understand why certain critiques don't hold up.
Subjective section: SUBJECTIVE claims noted as opinion-based. User decides.
Strengths required: Coordinator validates what works well. Not just problems. Include "Validated Strengths" section.
Constructive tone: Strip sarcasm, mockery, dismissive language from agent outputs. Preserve technical accuracy and file references.
Implementation roadmap: Group actions by immediacy (immediate / short-term / long-term)

Validation Summary Table (include in report):

## Claim Validation Summary

| Claim | Agent | Verdict | Evidence |
|-------|-------|---------|----------|
| [CLAIM-1] | Senior | VALID | [file:line shows X] |
| [CLAIM-2] | Pedant | PARTIAL | [true that X, but Y mitigates] |
| [CLAIM-3] | Newcomer | UNFOUNDED | [code shows otherwise] |


Gate: Report complete with all sections populated. Analysis done.

Examples
Example 1: Roast a README

User says: "Roast this repo"

skill: roast


Actions:

Activate read-only mode (Phase 1)
Read README.md, survey repo structure, identify key files (Phase 2)
Spawn 5 persona agents in parallel, each analyzing README + structure (Phase 3)
Collect all [CLAIM-N] tags, validate each against actual files (Phase 4)
Synthesize constructive report with prioritized improvement opportunities (Phase 5) Result: Evidence-based critique with actionable improvements and validated strengths
Example 2: Roast a Design Doc

User says: "Poke holes in the architecture doc"

skill: roast @README.md


Actions:

Activate read-only mode, read the target document (Phases 1-2)
Survey related implementation files referenced by the doc (Phase 2)
Spawn 5 agents focused on that document and its claims (Phase 3)
Validate claims against both doc content and referenced code (Phase 4)
Report with architecture-specific improvements and alternatives (Phase 5) Result: Multi-perspective architecture review grounded in implementation
Example 3: Roast an Approach

User says: "Devil's advocate on using SQLite for the error learning database"

skill: roast the idea of using SQLite for the error learning database


Actions:

Search repo for existing SQLite implementation and related code (Phase 2)
Spawn agents to critique both the concept AND actual code found (Phase 3)
Validate claims against implementation evidence (Phase 4)
Report grounded in real code, not just theoretical critique (Phase 5) Result: Critique anchored in actual implementation, not a strawman
Error Handling
Error: "Agent Returns Claims Without File References"

Cause: Persona agent skipped evidence-gathering or analyzed verbally Solution:

Dismiss ungrounded claims as UNFOUNDED — they cannot be validated
If majority of claims lack references, re-run that specific agent with explicit instruction to cite file:line
Never promote ungrounded claims to the validated findings section
Error: "Read-Only Mode Not Activated"

Cause: Phase 1 skipped or read-only-ops skill invocation failed Solution:

Stop all analysis immediately
Invoke read-only-ops before proceeding
If skill unavailable, manually enforce: no Write, Edit, or destructive Bash
Error: "Agent Attempts to Fix Issues"

Cause: Persona agent crossed from analysis into implementation Solution:

Discard any modifications attempted
Extract only the analytical findings from that agent's output
Remind: this is read-only analysis, fixes are the user's decision
Error: "No Target Found or Empty Repository"

Cause: User invoked roast without specifying target and no README.md exists Solution:

Check for alternative entry points: CONTRIBUTING.md, docs/, main source files
If repo has code but no docs, analyze the code structure and entry points
If truly empty, inform user and ask for a specific file or concept to analyze
References
Reference Files
${CLAUDE_SKILL_DIR}/references/report-template.md: Full report output template with tone transformation rules
${CLAUDE_SKILL_DIR}/references/personas.md: Persona specifications, prompt template, and claim format
agents/reviewer-code.md: Code quality reviewer (senior and pedant lenses)
agents/reviewer-perspectives.md: Perspectives reviewer (newcomer and contrarian lenses)
agents/reviewer-domain.md: Domain reviewer (pragmatic-builder lens)
Dependencies
read-only-ops skill: Enforces no-modification guardrails during analysis
Weekly Installs
8
Repository
notque/claude-c…-toolkit
GitHub Stars
353
First Seen
Mar 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail