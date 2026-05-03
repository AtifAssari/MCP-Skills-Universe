---
rating: ⭐⭐
title: devtu-self-evolve
url: https://skills.sh/mims-harvard/tooluniverse/devtu-self-evolve
---

# devtu-self-evolve

skills/mims-harvard/tooluniverse/devtu-self-evolve
devtu-self-evolve
Installation
$ npx skills add https://github.com/mims-harvard/tooluniverse --skill devtu-self-evolve
SKILL.md
ToolUniverse Self-Evolution Orchestrator

Coordinates the full development lifecycle by dispatching to specialized devtu skills.

The Cycle
Discover → Create → Test → Fix → Optimize → Ship → Repeat


Each phase maps to a dedicated skill:

Phase	Skill	What it does
Discover	devtu-auto-discover-apis	Gap analysis, web search for APIs, batch discovery
Create	devtu-create-tool	Build tool class + JSON config + test examples
Test	(this skill)	Launch researcher persona agents to find issues
Fix	devtu-fix-tool	Diagnose failures, implement fixes, validate
Optimize	devtu-optimize-skills	Improve skill reports, evidence handling, UX
Optimize	devtu-optimize-descriptions	Improve tool JSON descriptions for clarity
Docs	devtu-docs-quality	Validate documentation accuracy
Ship	devtu-github	Branch, commit, push, create PR
Quick Start

Pick an entry point based on what's needed:

"Run a test round" → jump to Testing Phase
"Expand coverage" → invoke Skill(skill="devtu-auto-discover-apis")
"Create a new tool" → invoke Skill(skill="devtu-create-tool")
"Fix a broken tool" → invoke Skill(skill="devtu-fix-tool")
"Improve skills" → invoke Skill(skill="devtu-optimize-skills")
"Full cycle" → follow all phases below in order
Phase 1: Discovery (optional)

Invoke Skill(skill="devtu-auto-discover-apis") to:

Run gap analysis on current tool categories
Search for life science APIs in underrepresented domains
Score and prioritize APIs by coverage, reliability, documentation
Phase 2: Tool Creation (optional)

Invoke Skill(skill="devtu-create-tool") for each new API:

Create Python tool class implementing the API
Create JSON config with parameters, descriptions, test examples
Register in _lazy_registry_static.py and default_config.py
Validate: python -m tooluniverse.cli test <ToolName>
Phase 3: Testing Phase

This is the core testing loop, run directly by this skill.

Setup
Check for open PRs: gh pr list --state open
If unmerged PR → use that branch; if merged → new branch from origin/main
Rebase: git fetch origin && git rebase origin/main
Researcher Persona Agents

Launch 2 agents per round (A + B) using the Agent tool with these parameters:

Each agent gets:

Domain specialty (oncology, genomics, pharmacology, etc.)
Research question (specific biological question)
5-7 test scenarios exercising different tools
Instructions to report issues with severity (HIGH/MEDIUM/LOW)
Issue IDs: Feature-{round}{letter}-{num} (e.g., Feature-59A-001)

Agent prompt template — see references/persona-template.md

Verification (CRITICAL)

Before implementing ANY agent-reported issue, verify via CLI:

python3 -m tooluniverse.cli run <ToolName> '<json_args>'


50%+ of agent reports are false positives from MCP interface confusion. Only fix verified issues.

Fix Principles
Prevent, don't recover — fix root cause, not symptoms
Validate at input — reject bad params early with clear guidance
Distinguish "no data" from "bad query" — different messages for each
Fix the abstraction — don't add alias lists that grow forever

Anti-patterns: hint text instead of validation, parameter aliases instead of fixing naming, post-hoc probing instead of pre-validation.

Skill Usefulness Testing (NEW — beyond tool testing)

Standard testing verifies tools work. Usefulness testing verifies skills actually solve scientist problems. Run this after standard testing:

Pick a real research question that the skill claims to answer (not a tool-level test)
Launch an agent following the skill workflow on the real question
Assess honestly: Does the skill produce an actionable answer, or just a data dump?

Score 1-10 rubric:

1-3: Tool catalog — lists tools without interpretation
4-6: Data collector — gathers data but doesn't help combine/interpret
7-8: Reasoning framework — guides interpretation with tables/scoring/synthesis
9-10: Decision engine — produces concrete, defensible recommendations

Common failure patterns found in usefulness tests:

Pattern	Score Impact	Fix
"Call A, then B, then C" without explaining what to DO with results	-3	Add interpretation tables
Tool params wrong (tool works but skill documents wrong names)	-2	Verify ALL tool params via get_tool_info()
Promises data the API can't deliver (e.g., DepMap CRISPR scores)	-2	Be honest about limitations; add computational procedure workaround
No synthesis phase at the end	-2	Add "so what?" phase that combines all evidence
No evidence grading	-1	Add T1-T4 or similar confidence tiers
No computational procedures for things tools can't do	-1	Add Python code blocks using scipy/pandas/numpy

When tools can't help, add computational procedures: Some analyses need Python code, not API calls. Skills should include working code blocks for:

Statistical testing (scipy.stats, FDR correction)
Data analysis from downloaded files (pandas + CSV from DepMap, TCGA, etc.)
Scoring algorithms (ACMG classification, viability scores)
Sequence analysis (Biopython)

See devtu-optimize-skills Patterns 14-15 for full guidance.

Phase 4: Fix & Commit
Implement verified fixes (see references/bug-patterns.md for code-level patterns)
Run code-simplifier: Skill(skill="simplify") — always after writing or modifying code
Lint: ruff check src/tooluniverse/<file>.py
Verify syntax: python -c "from tooluniverse.<module> import <Class>"
Test: python -m tooluniverse.cli run <Tool> '<json>'
Pre-commit hook pattern: stage → commit (fails, reformats) → re-stage → commit
Push: git push origin <branch>

Also see Skill(skill="devtu-code-optimization") for reusable fix patterns and anti-patterns.

Phase 5: Optimize (optional)

After fixes are stable:

Skill(skill="devtu-optimize-descriptions") — improve tool descriptions
Skill(skill="devtu-optimize-skills") — improve research skill quality
Skill(skill="devtu-docs-quality") — validate docs accuracy
Phase 6: Ship

Invoke Skill(skill="devtu-github") or manually:

Rebase: git fetch origin && git stash && git rebase origin/main && git stash pop
git push --force-with-lease origin <branch>
Create or update PR: gh pr create / verify with gh pr view <N> --json mergeable
Verify "mergeable": "MERGEABLE" before reporting done

GitHub repo: mims-harvard/ToolUniverse — always verify with git remote -v before pushing.

Git Rules (CRITICAL)
NEVER push to main — all work on feature branches
NEVER have multiple open fix PRs — keep adding to current branch
Always rebase before push: git fetch origin && git rebase origin/main
Commit message format: no "BUG" terminology, use "Feature" or "Fix"
No AI attribution in commits
Common Issue Categories
Category	Signal
Silent parameter miss	Wrong-field check; param ignored
Always-fires conditional	.get("field") on wrong type
Silent normalization	Auto-transform not disclosed
Wrong notation/case	Gene fusions, Title Case names
Substring match	Short symbol returns multiple targets
try/except indent	Mismatched → SyntaxError

Full patterns → references/bug-patterns.md

Round Tracking

After each round: advance counter, update patterns file, keep this SKILL.md under 150 lines.

Current round: 127 (rounds completed: 52-126)

Weekly Installs
118
Repository
mims-harvard/to…universe
GitHub Stars
1.3K
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn