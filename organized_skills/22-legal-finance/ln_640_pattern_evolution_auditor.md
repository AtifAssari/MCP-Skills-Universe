---
rating: ⭐⭐
title: ln-640-pattern-evolution-auditor
url: https://skills.sh/levnikolaevich/claude-code-skills/ln-640-pattern-evolution-auditor
---

# ln-640-pattern-evolution-auditor

skills/levnikolaevich/claude-code-skills/ln-640-pattern-evolution-auditor
ln-640-pattern-evolution-auditor
Installation
$ npx skills add https://github.com/levnikolaevich/claude-code-skills --skill ln-640-pattern-evolution-auditor
SKILL.md

Paths: File paths (shared/, references/, ../ln-*) are relative to skills repo root.

Type: L2 Coordinator Category: 6XX Audit

Pattern Evolution Auditor
Mandatory Read

MANDATORY READ: Load shared/references/evaluation_coordinator_runtime_contract.md, shared/references/evaluation_summary_contract.md, shared/references/evaluation_research_contract.md MANDATORY READ: Load shared/references/research_tool_fallback.md

Purpose
audit implemented architectural patterns against current best practices
coordinate ln-641 through ln-647
require research before pattern scoring
Runtime Contract

Runtime family:

evaluation-runtime

Identifier:

pattern-audit

Phase order:

PHASE_0_CONFIG
PHASE_1_DISCOVERY
PHASE_2_RESEARCH
PHASE_3_BOUNDARY_AUDITS
PHASE_4_PATTERN_ANALYSIS
PHASE_5_AGGREGATE
PHASE_6_REPORT
PHASE_7_SELF_CHECK
Worker Set
ln-641-pattern-analyzer
ln-642-layer-boundary-auditor
ln-643-api-contract-auditor
ln-644-dependency-graph-auditor
ln-645-open-source-replacer
ln-646-project-structure-auditor
ln-647-env-config-auditor
Worker Invocation (MANDATORY)

Use the Skill tool for delegated workers. Do not inline worker logic inside the coordinator.

TodoWrite format (mandatory):

Resolve audit scope and build manifest
Load architecture patterns and layers
Run best-practice research
Run boundary and contract audits
Analyze pattern compliance and gaps
Aggregate worker findings
Generate audit report
Verify cleanup and self-check

Representative invocations:

Skill(skill: "ln-641-pattern-analyzer", args: "{scope}")
Skill(skill: "ln-642-layer-boundary-auditor", args: "{scope}")
Skill(skill: "ln-643-api-contract-auditor", args: "{scope}")
Skill(skill: "ln-644-dependency-graph-auditor", args: "{scope}")
Skill(skill: "ln-645-open-source-replacer", args: "{scope}")
Skill(skill: "ln-646-project-structure-auditor", args: "{scope}")
Skill(skill: "ln-647-env-config-auditor", args: "{scope}")

Workflow
Start evaluation-runtime.
Discover candidate patterns and applicability.
Run mandatory research first:
official docs or standards
MCP Ref
Context7 when library/framework patterns are involved
current web best-practice research
Run boundary audits before pattern scoring.
Run pattern analysis only after boundary results and research exist.
Aggregate scores and produce the final pattern report.
Definition of Done
 Evaluation runtime started
 Pattern applicability resolved
 Best-practice research completed
 Boundary audit summaries recorded
 Pattern analysis summaries recorded
 Final report written
 evaluation-coordinator summary written
 Runtime completed
Meta-Analysis

MANDATORY READ: Load shared/references/meta_analysis_protocol.md

After the coordinator run, analyze the session per protocol section 7 and include the protocol-formatted output with the final pattern audit result.

References
Workers: ../ln-641-pattern-analyzer/SKILL.md, ../ln-642-layer-boundary-auditor/SKILL.md, ../ln-643-api-contract-auditor/SKILL.md, ../ln-644-dependency-graph-auditor/SKILL.md, ../ln-645-open-source-replacer/SKILL.md, ../ln-646-project-structure-auditor/SKILL.md, ../ln-647-env-config-auditor/SKILL.md
Shared pattern refs: references/layer_rules.md, references/pattern_library.md, references/scoring_rules.md

Version: 2.0.0 Last Updated: 2026-02-08

Weekly Installs
275
Repository
levnikolaevich/…e-skills
GitHub Stars
442
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn