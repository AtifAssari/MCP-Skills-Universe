---
rating: ⭐⭐
title: ln-610-docs-auditor
url: https://skills.sh/levnikolaevich/claude-code-skills/ln-610-docs-auditor
---

# ln-610-docs-auditor

skills/levnikolaevich/claude-code-skills/ln-610-docs-auditor
ln-610-docs-auditor
Installation
$ npx skills add https://github.com/levnikolaevich/claude-code-skills --skill ln-610-docs-auditor
SKILL.md

Paths: File paths (shared/, references/, ../ln-*) are relative to skills repo root.

Type: L2 Coordinator Category: 6XX Audit

Docs Auditor
Mandatory Read

MANDATORY READ: Load shared/references/evaluation_coordinator_runtime_contract.md, shared/references/evaluation_summary_contract.md, shared/references/evaluation_research_contract.md MANDATORY READ: Load shared/references/research_tool_fallback.md

Purpose
audit documentation structure, relevance, comments, and factual accuracy
coordinate ln-611, ln-612, ln-613, ln-614
require research-backed standards before final scoring
Runtime Contract

Runtime family:

evaluation-runtime

Identifier:

docs-audit

Phase order:

PHASE_0_CONFIG
PHASE_1_DISCOVERY
PHASE_2_RESEARCH
PHASE_3_DELEGATE
PHASE_4_AGGREGATE
PHASE_5_REPORT
PHASE_6_SELF_CHECK
Worker Set
ln-611-docs-structure-auditor
ln-612-semantic-content-auditor
ln-613-code-comments-auditor
ln-614-docs-fact-checker
Worker Invocation (MANDATORY)

Use the Skill tool for delegated workers. Do not inline worker logic inside the coordinator.

TodoWrite format (mandatory):

Resolve audit scope and build manifest
Load project documentation tree
Run best-practice research
Delegate to domain audit workers
Aggregate worker findings
Generate audit report
Verify cleanup and self-check

Representative invocations:

Skill(skill: "ln-611-docs-structure-auditor", args: "{scope}")
Skill(skill: "ln-612-semantic-content-auditor", args: "{scope}")
Skill(skill: "ln-613-code-comments-auditor", args: "{scope}")
Skill(skill: "ln-614-docs-fact-checker", args: "{scope}")

Workflow
Phase 0: Config

Start evaluation-runtime with required_research=true.

Phase 1: Discovery

Discover documentation surfaces and scope.

Phase 2: Research

Mandatory research sources:

official docs or standards
MCP Ref
Context7 when framework docs matter
current web best-practice research
Phase 3: Delegate

Delegate specialized audit workers.

Child workers must use evaluation-worker-runtime and emit evaluation-compatible summaries recorded through evaluation-runtime.

Phase 4: Aggregate

Merge worker findings into one documentation audit result.

Phase 5: Report

Write final documentation audit output and coordinator summary.

Phase 6: Self-Check

Required checks:

 mandatory research completed
 all worker summaries recorded
 aggregate summary exists
 cleanup verified
 coordinator summary recorded
Summary Contract

Write summary_kind=evaluation-coordinator.

Definition of Done
 Evaluation runtime started
 Research completed
 All documentation audit workers completed
 Aggregation completed
 Final report written
 evaluation-coordinator summary written
 Runtime completed
Meta-Analysis

MANDATORY READ: Load shared/references/meta_analysis_protocol.md

After the coordinator run, analyze the session per protocol section 7 and include the protocol-formatted output with the final documentation audit result.

References
Workers: ../ln-611-docs-structure-auditor/SKILL.md, ../ln-612-semantic-content-auditor/SKILL.md, ../ln-613-code-comments-auditor/SKILL.md, ../ln-614-docs-fact-checker/SKILL.md

Version: 5.0.0 Last Updated: 2026-03-01

Weekly Installs
226
Repository
levnikolaevich/…e-skills
GitHub Stars
442
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn