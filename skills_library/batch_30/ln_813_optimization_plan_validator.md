---
title: ln-813-optimization-plan-validator
url: https://skills.sh/levnikolaevich/claude-code-skills/ln-813-optimization-plan-validator
---

# ln-813-optimization-plan-validator

skills/levnikolaevich/claude-code-skills/ln-813-optimization-plan-validator
ln-813-optimization-plan-validator
Installation
$ npx skills add https://github.com/levnikolaevich/claude-code-skills --skill ln-813-optimization-plan-validator
SKILL.md

Paths: File paths (shared/, references/, ../ln-*) are relative to skills repo root.

Type: L2 Coordinator Category: 8XX Optimization

Optimization Plan Validator

Coordinator for validating optimization plans before execution.

Mandatory Read

MANDATORY READ: Load shared/references/evaluation_coordinator_runtime_contract.md, shared/references/evaluation_summary_contract.md, shared/references/evaluation_research_contract.md MANDATORY READ: Load shared/references/agent_review_workflow.md, shared/references/agent_delegation_pattern.md MANDATORY READ: Load references/optimization_review_focus.md

Purpose
verify feasibility of optimization hypotheses
require source-backed research before plan approval
use parallel external agents plus local feasibility analysis
keep merge and refinement sequential
Inputs

Primary input:

.hex-skills/optimization/{slug}/context.md

Required context sections:

performance map
hypotheses
suspicion stack
test command
Runtime Contract

Runtime family:

evaluation-runtime

Identifier:

optimization-{slug}

Phase order:

PHASE_0_CONFIG
PHASE_1_LOAD_CONTEXT
PHASE_2_AGENT_LAUNCH
PHASE_3_RESEARCH_AND_FEASIBILITY
PHASE_4_MERGE
PHASE_5_REFINEMENT
PHASE_6_VERDICT
PHASE_7_SELF_CHECK
TodoWrite Format

Mandatory todo items:

Config
Load context
Agent launch
Research and feasibility
Merge
Refinement
Verdict
Self-check

The coordinator runs research inline (per shared/references/evaluation_research_contract.md) and refinement inline (per shared/agents/prompt_templates/iterative_refinement.md and shared/agents/prompt_templates/refinement_perspectives.md). Refinement advisor sessions are launched directly via shared/agents/agent_runner.mjs.

Workflow
Phase 0: Config
Resolve optimization slug.
Build evaluation runtime manifest with required_research=true.
Start evaluation-runtime.
Phase 1: Load Context
Load .hex-skills/optimization/{slug}/context.md.
Fail if required sections are missing.
Materialize agent-readable context when needed.
Phase 2: Agent Launch
Run health check.
Launch available agents.
Register every launched agent in evaluation-runtime.
If no agents are available, record agents_skipped_reason and continue.
Phase 3: Research And Feasibility

Required work:

coordinator performs research inline (official docs, MCP Ref, Context7, current web best-practice)
perform local feasibility validation in parallel while agents work

Minimum research lanes:

official documentation or standards
MCP Ref
Context7 for involved libraries
current web best-practice research

Feasibility checks:

files exist
no invalid overlap across hypotheses
every hypothesis traces to profiler or research evidence
unsupported removal hypotheses are flagged
high-level fixes are preferred over low-level churn when evidence supports them
Phase 4: Merge
Sync agents at the merge barrier.
Merge:
local feasibility findings
research findings
agent findings
Reject unsupported suggestions.
Apply accepted corrections directly to context.md.
Phase 5: Refinement

Refinement uses a 2-stage state machine per shared/agents/prompt_templates/iterative_refinement.md and shared/agents/prompt_templates/refinement_perspectives.md:

Stage 1 (parallel): dry_run_executor, new_dev_tester, adversarial_reviewer
Stage 2 (after merge): final_sweep

Rules:

Stage 1 runs in parallel, Stage 2 after merge
no skip when an advisor is available except runtime-backed failure or disablement
cleanup evidence is mandatory
Phase 6: Verdict

Possible verdicts:

GO
GO_WITH_CONCERNS
NO_GO

NO_GO when:

critical feasibility gaps remain
research does not support the plan
both local validation and agent review reject the plan
Phase 7: Self-Check

Required checks:

 context loaded and validated
 mandatory research completed
 local feasibility check completed
 all required agents resolved before merge
 merge summary exists
 refinement trace exists when an advisor was available
 cleanup verified
 coordinator summary recorded
Summary Contract

Write summary_kind=evaluation-coordinator.

Recommended payload:

status
final_result
report_path
worker_count
agent_count
issues_total
severity_counts
warnings
cleanup_verified
research_completed
Definition of Done
 Evaluation runtime started
 Optimization context validated
 Mandatory research completed
 Agents launched or explicitly skipped
 Feasibility analysis completed
 Merge completed after agent barrier
 Refinement executed or explicitly justified
 Verdict issued
 evaluation-coordinator summary written
 Runtime completed
Meta-Analysis

MANDATORY READ: Load shared/references/meta_analysis_protocol.md

After the coordinator run, analyze the session per protocol section 7 and include the protocol-formatted output with the final optimization-plan verdict.

References
Runtime: shared/references/evaluation_coordinator_runtime_contract.md, shared/references/evaluation_summary_contract.md
Research: shared/references/evaluation_research_contract.md
Review workflow: shared/references/agent_review_workflow.md, shared/references/agent_delegation_pattern.md
Focus: references/optimization_review_focus.md

Version: 1.0.0 Last Updated: 2026-03-15

Weekly Installs
102
Repository
levnikolaevich/…e-skills
GitHub Stars
445
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn