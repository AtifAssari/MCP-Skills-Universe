---
title: skill-tuning
url: https://skills.sh/catlog22/claude-code-workflow/skill-tuning
---

# skill-tuning

skills/catlog22/claude-code-workflow/skill-tuning
skill-tuning
Installation
$ npx skills add https://github.com/catlog22/claude-code-workflow --skill skill-tuning
SKILL.md
Skill Tuning

Autonomous diagnosis and optimization for skill execution issues.

Architecture
┌─────────────────────────────────────────────────────┐
│  Phase 0: Read Specs (mandatory)                    │
│  → problem-taxonomy.md, tuning-strategies.md         │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│  Orchestrator (state-driven)                         │
│  Read state → Select action → Execute → Update → ✓ │
└─────────────────────────────────────────────────────┘
        ↓                           ↓
┌──────────────────────┐   ┌──────────────────┐
│  Diagnosis Phase     │   │ Gemini CLI       │
│  • Context          │   │ Deep analysis    │
│  • Memory           │   │ (on-demand)      │
│  • DataFlow         │   │                  │
│  • Agent            │   │ Complex issues   │
│  • Docs             │   │ Architecture     │
│  • Token Usage      │   │ Performance      │
└──────────────────────┘   └──────────────────┘
                ↓
        ┌───────────────────┐
        │  Fix & Verify     │
        │  Apply → Re-test  │
        └───────────────────┘

Core Issues Detected
Priority	Problem	Root Cause	Fix Strategy
P0	Authoring Violation	Intermediate files, state bloat, file relay	eliminate_intermediate, minimize_state
P1	Data Flow Disruption	Scattered state, inconsistent formats	state_centralization, schema_enforcement
P2	Agent Coordination	Fragile chains, no error handling	error_wrapping, result_validation
P3	Context Explosion	Unbounded history, full content passing	sliding_window, path_reference
P4	Long-tail Forgetting	Early constraint loss	constraint_injection, checkpoint_restore
P5	Token Consumption	Verbose prompts, state bloat	prompt_compression, lazy_loading
Problem Categories (Detailed Specs)

See specs/problem-taxonomy.md for:

Detection patterns (regex/checks)
Severity calculations
Impact assessments
Tuning Strategies (Detailed Specs)

See specs/tuning-strategies.md for:

10+ strategies per category
Implementation patterns
Verification methods
Workflow
Step	Action	Orchestrator Decision	Output
1	action-init	status='pending'	Backup, session created
2	action-analyze-requirements	After init	Required dimensions + coverage
3	Diagnosis (6 types)	Focus areas	state.diagnosis.{type}
4	action-gemini-analysis	Critical issues OR user request	Deep findings
5	action-generate-report	All diagnosis complete	state.final_report
6	action-propose-fixes	Issues found	state.proposed_fixes[]
7	action-apply-fix	Pending fixes	Applied + verified
8	action-complete	Quality gates pass	session.status='completed'
Action Reference
Category	Actions	Purpose
Setup	action-init	Initialize backup, session state
Analysis	action-analyze-requirements	Decompose user request via Gemini CLI
Diagnosis	action-diagnose-{context,memory,dataflow,agent,docs,token_consumption}	Detect category-specific issues
Deep Analysis	action-gemini-analysis	Gemini CLI: complex/critical issues
Reporting	action-generate-report	Consolidate findings → final_report
Fixing	action-propose-fixes, action-apply-fix	Generate + apply fixes
Verify	action-verify	Re-run diagnosis, check gates
Exit	action-complete, action-abort	Finalize or rollback

Full action details: phases/actions/

State Management

Single source of truth: .workflow/.scratchpad/skill-tuning-{ts}/state.json

{
  "status": "pending|running|completed|failed",
  "target_skill": { "name": "...", "path": "..." },
  "diagnosis": {
    "context": {...},
    "memory": {...},
    "dataflow": {...},
    "agent": {...},
    "docs": {...},
    "token_consumption": {...}
  },
  "issues": [{"id":"...", "severity":"...", "category":"...", "strategy":"..."}],
  "proposed_fixes": [...],
  "applied_fixes": [...],
  "quality_gate": "pass|fail",
  "final_report": "..."
}


See phases/state-schema.md for complete schema.

Orchestrator Logic

See phases/orchestrator.md for:

Decision logic (termination checks → action selection)
State transitions
Error recovery
Key Principles
Problem-First: Diagnosis before any fix
Data-Driven: Record traces, token counts, snapshots
Iterative: Multiple rounds until quality gates pass
Reversible: All changes with backup checkpoints
Non-Invasive: Minimal changes, maximum clarity
Usage Examples
# Basic skill diagnosis
/skill-tuning "Fix memory leaks in my skill"

# Deep analysis with Gemini
/skill-tuning "Architecture issues in async workflow"

# Focus on specific areas
/skill-tuning "Optimize token consumption and fix agent coordination"

# Custom issue
/skill-tuning "My skill produces inconsistent outputs"

Output

After completion, review:

.workflow/.scratchpad/skill-tuning-{ts}/state.json - Full state with final_report
state.final_report - Markdown summary (in state.json)
state.applied_fixes - List of applied fixes with verification results
Reference Documents
Document	Purpose
specs/problem-taxonomy.md	Classification + detection patterns
specs/tuning-strategies.md	Fix implementation guide
specs/dimension-mapping.md	Dimension ↔ Spec mapping
specs/quality-gates.md	Quality verification criteria
phases/orchestrator.md	Workflow orchestration
phases/state-schema.md	State structure definition
phases/actions/	Individual action implementations
Weekly Installs
68
Repository
catlog22/claude…workflow
GitHub Stars
1.9K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass