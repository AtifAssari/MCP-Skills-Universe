---
title: analyze-plugin
url: https://skills.sh/richfrem/agent-plugins-skills/analyze-plugin
---

# analyze-plugin

skills/richfrem/agent-plugins-skills/analyze-plugin
analyze-plugin
Installation
$ npx skills add https://github.com/richfrem/agent-plugins-skills --skill analyze-plugin
SKILL.md
Dependencies

This skill requires Python 3.8+ and standard library only. No external packages needed.

To install this skill's dependencies:

pip-compile ./requirements.in
pip install -r ./requirements.txt


See ../../requirements.txt for the dependency lockfile (currently empty — standard library only).

Plugin & Skill Analyzer

Perform deep structural and content analysis on agent plugins and skills. Extract reusable patterns that feed the virtuous cycle of continuous improvement.

Two Analysis Modes
Single Plugin Mode

Deep-dive into one plugin. Use when you want to fully understand a plugin's architecture.

Comparative Mode

Analyze multiple plugins side-by-side. Use when looking for common patterns across a collection.

Analysis Framework

Execute these phases sequentially. Do not skip phases.

Phase 0: Quick Compliance Pre-Check

Before deep analysis, run a rapid compliance scan to surface blockers:

Manifest check:

# plugin.json must be in .claude-plugin/ (not root)
ls .claude-plugin/plugin.json && jq . .claude-plugin/plugin.json

name present and kebab-case (no spaces, no uppercase)?
version follows semver (X.Y.Z) if present?
No unknown fields causing warnings?

Structure check:

Component dirs (commands/, agents/, skills/, hooks/) at plugin ROOT (not inside .claude-plugin/)?
All file names use kebab-case?
SKILL.md (not README.md) inside each skill directory?

Security scan:

# Hardcoded credentials
grep -rn "password\|api_key\|secret" --include="*.md" --include="*.json" --include="*.sh" .

# Hardcoded paths (should use ${CLAUDE_PLUGIN_ROOT})
grep -rn "/Users/\|/home/" --include="*.json" --include="*.sh" .


Report Phase 0 findings before proceeding. If CRITICAL issues found (invalid JSON, hardcoded credentials, missing required fields), flag them prominently in the final report.

Phase 1: Inventory

Run the deterministic inventory script first:

python3 "scripts/inventory_plugin.py" --path <plugin-dir> --format json


If the script is unavailable, manually enumerate:

Walk the directory tree

Classify every file by type:

SKILL.md → Skill definition
commands/*.md → Command definition
references/*.md → Reference material (progressive disclosure)
scripts/*.py → Executable scripts
README.md → Plugin documentation
plugin.json → Plugin manifest
*.json → Configuration (MCP, hooks, etc.)
*.yaml / *.yml → Pipeline/config data
*.html → Artifact templates
*.mmd → Architecture diagrams
Other → Assets/misc

Record for each file: path, type, line count, byte size

Output a structured inventory as a markdown checklist with one checkbox per file

Phase 2: Structure Analysis

Evaluate the plugin's architectural decisions:

Dimension	What to Look For
Layout	How are skills/commands/references organized? Flat vs nested?
Progressive Disclosure	Is SKILL.md lean (<500 lines) with depth in references/?
Component Ratios	Skills vs commands vs scripts — what's the balance?
Naming Patterns	Are names descriptive? Follow kebab-case? Use gerund form?
README Quality	Does it have a file tree? Usage examples? Architecture diagram?
Standalone vs Supercharged	Can it work without MCP tools? What's enhanced with them?
Phase 3: Content Analysis

For each file, load the appropriate question set from references/analysis-questions-by-type.md and work through every checkbox. See the process diagram in analyze-plugin-flow.mmd for the full pipeline visualization.

For each SKILL.md, evaluate:

Frontmatter Quality:

Is the description written in third person?
Does it include specific trigger phrases?
Is it under 1024 characters?
Does it clearly state WHEN to trigger?

Body Structure:

Does it have a clear execution flow (numbered phases/steps)?
Are there decision trees or branching logic?
Does it use tables for structured information?
Are there output templates or format specifications?
Does it link to references/ for deep content?

Interaction Design:

Does it use guided discovery interviews before execution?
What question types are used? (open-ended, numbered options, yes/no, table-based comparisons)
Does it present smart defaults with override options?
Are there confirmation gates before expensive/irreversible operations?
Does it use recap-before-execute to verify understanding?
Does it offer numbered next-action menus after completion?
Does it negotiate output format with the user?
Are there inline progress indicators during multi-step workflows?

For Commands, evaluate:

Are they written as instructions FOR the agent (not documentation for users)?
Do they specify required arguments?
Do they reference MCP tools with full namespaces?

For Reference Files, evaluate:

Do they contain domain-specific deep knowledge?
Are they organized by topic/domain?
Do files >100 lines have a table of contents?

For Scripts, evaluate:

Are they Python-only (no .sh/.ps1)?
Do they have --help documentation?
Do they handle errors gracefully?
Are they cross-platform compatible?
Phase 4: Pattern Extraction

Identify instances of known patterns from references/pattern-catalog.md. Also watch for novel patterns not yet cataloged.

For each pattern found, document:

Pattern: [name]
Plugin: [where found]
File: [specific file]
Description: [how it's used here]
Quality: [exemplary / good / basic]
Reusability: [high / medium / low]
Confidence: [high (≥3 plugins) / medium (2) / low (1)]
Lifecycle: [proposed / validated / canonical / deprecated]


Before adding a new pattern, check the catalog's deduplication rules. If an existing pattern covers ≥80% of the behavior, update its frequency instead.

Key pattern categories to search for:

Architectural Patterns — Standalone/supercharged, connector abstraction, meta-skills
Execution Patterns — Phase-based workflows, decision trees, bootstrap/iteration modes
Content Patterns — Severity frameworks, confidence scoring, priority tiers, checklists
Output Patterns — HTML artifacts, structured tables, ASCII diagrams, template systems
Knowledge Patterns — Progressive disclosure, dialect tables, domain references, tribal knowledge extraction
Interaction Design Patterns — Discovery interviews, option menus, confirmation gates, smart defaults, recap-before-execute, output format negotiation, progress indicators
Phase 5: Anti-Pattern & Security Detection

Load the full check tables from references/security-checks.md.

Execution order:

Run security checks FIRST (P0 — Critical severity items)
Then run structural anti-pattern checks
Apply contextual severity based on plugin type/complexity
Flag any LLM-native attack vectors (skill impersonation, context poisoning, injection via references)

If inventory_plugin.py was run with --security, use its deterministic findings as ground truth.

Phase 6: Synthesis & Scoring

Load the maturity model and scoring rubric from references/maturity-model.md.

Steps:

Assign maturity level (L1-L5)
Score each of the 6 dimensions (1-5) using the weighted rubric
Calculate overall score (weighted average, Scoring v2.0)
Generate the summary report using the template
For comparative mode, generate the Ecosystem Scorecard
Output

Generate a structured markdown report. For single plugins, output inline. For collections, create an artifact file with the full analysis.

Iteration Directory Isolation: All analysis reports must be saved into explicitly versioned and isolated outputs (e.g. analysis-reports/target-run-1/) to prevent destructive overrides on re-runs. Asynchronous Benchmark Metric Capture: Once the audit run completes, immediately log the resulting total_tokens and duration_ms to a timing.json file to calculate the cost of the deep-dive analysis.

Always end with Virtuous Cycle Recommendations: specific, actionable improvements for agent-plugin-analyzer (this plugin), agent-scaffolders, and agent-skill-open-specifications based on patterns discovered.

Weekly Installs
22
Repository
richfrem/agent-…s-skills
GitHub Stars
2
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail