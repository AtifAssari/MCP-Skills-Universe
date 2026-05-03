---
title: workflow
url: https://skills.sh/bntvllnt/agent-skills/workflow
---

# workflow

skills/bntvllnt/agent-skills/workflow
workflow
Installation
$ npx skills add https://github.com/bntvllnt/agent-skills --skill workflow
SKILL.md
Workflow

High-velocity solo development. Idea to production same-day.

Agent Capabilities
Capability	Used For	Required	Fallback
File read/write	Specs, config, history	Yes	—
Code search (grep/glob)	Discovery, context	Yes	—
Shell/command execution	Quality gates (lint, build, test)	Yes	List commands for user to run
Codebase intelligence (npx codebase-intelligence)	Structural analysis for TS/TSX projects (graph, metrics, blast radius)	No	grep/glob/read (manual exploration)
Task/todo tracking	Phase management	Recommended	Track in spec Progress section
User interaction	Stuck escalation, risk flags	Recommended	Log decisions in spec Notes
Web/doc search	Pattern lookup	No	Use embedded patterns

Fallback rule: If your agent lacks a capability, use the fallback. Never skip the workflow step — adapt the method.

Commands
Command	Action	Reference
plan {idea}	Create spec	plan.md
spike {question}	Time-boxed exploration	spike.md
ship / ship {idea}	Implement + validate	ship.md
fix / fix {bug}	Scientific debug + regression fix	fix.md
review	Portable multi-perspective review spec with line-by-line + rule-by-rule coverage	review.md
spec-review	Adversarial spec analysis	spec-review.md
focus	Priority analysis + task proposals	focus.md
done	Validate + retro + archive	done.md
drop	Abandon, preserve learnings	drop.md
workflow	Show state + suggest next	Status (below)

No flags needed. The agent auto-detects intent from context:

"review the spec" → manual review pause
"skip tests" → skip test gate (documented)
"fix this bug" → dedicated bug fix with regression test
"emergency fix" → bypass spec ceremony
"production ready" → production validation
Flow
Features: focus → plan {idea} → ship → [implement/review/fix loop] → done
Bug fixes: fix {bug} → [investigate/TDD/validate] → done


Quick mode (<2h): ship {idea} → done Don't know what to work on: focus

Philosophy
Spec-first: All work needs a spec (creates one if missing)
Ship loop: Build → review → fix until clean
Quality gates: lint → typecheck → build → test → E2E → coverage (auto-detected per project)
E2E-first testing: Default to E2E tests. Unit tests only for pure functions
TDD enforced: RED → GREEN → REFACTOR per AC. Tests written before implementation (BLOCKING)
Mock boundary: Real systems preferred. Mock only third-party APIs without sandbox (last resort)
AC-driven coverage: Every Must Have + Error AC maps to an E2E test in the scenario registry
Anti-regression: Bug fixes require E2E regression test + anti-cascade diff (BLOCKING)
Failure mode testing: Every HIGH/MED failure hypothesis gets a defensive E2E test
Human controls deployment: Agent codes, you push/deploy
Done same-day: Scope to what ships today
Own planning: Never use the host agent's built-in plan mode (EnterPlanMode, etc.). This skill writes real spec files to specs/active/.
Spec Tiers
Tier	Size	Spec	Task Tracking
trivial	<5 LOC	None — just do it	No
micro	<30 LOC	Inline comment in code	No
mini	<100 LOC	Spec file, minimal	Yes (if available)
standard	100+ LOC	Full spec with checklist	Yes (if available)
Action Router
User input
  │
  ├─ "plan", "spec", "design"           → Load references/actions/plan.md
  ├─ "spike", "explore", "investigate"   → Load references/actions/spike.md
  ├─ "ship", "implement", "build"         → Load references/actions/ship.md
  ├─ "fix", "debug", "repair"            → Load references/actions/fix.md
  ├─ "review", "check code"              → Load references/actions/review.md
  ├─ "review spec", "analyze spec",
  │  "challenge spec"                    → Load references/actions/spec-review.md
  ├─ "focus", "what should i do",
  │  "prioritize", "overwhelmed"         → Load references/actions/focus.md
  ├─ "done", "finish", "complete"        → Load references/actions/done.md
  ├─ "drop", "abandon"                   → Load references/actions/drop.md
  └─ "workflow", "what's next", "what now",
     "what's up", "whats up", "status"  → Status Action (below)


Loading rule: Read the action file BEFORE executing. The action file contains all logic, task templates, and references needed.

Status Action

No separate action file — logic is inline here. Detect current state, suggest next action:

1. Check specs/active/ for active spec
2. Check git status for uncommitted work
3. Check task list for in-progress items

State → Suggestion:
  No spec, no changes    → "Ready. Run: plan {idea}"
  Active spec, no code   → "Spec ready. Run: ship"
  Active spec, code WIP  → "In progress. Run: ship (resumes)"
  Active spec, code done → "Ready to close. Run: done"
  No spec, dirty tree    → "Uncommitted work. Run: ship (creates spec) or done"


Output: Follow status-output.md.

Project Structure
specs/
  active/       ← Current work (0-1 specs)
  backlog/      ← Queued work from focus
  shipped/      ← Completed features
  dropped/      ← Abandoned with learnings
  history.log   ← One-line per feature shipped/dropped

Configuration

All behavior is configurable by editing the skill files directly.

What to change	Edit
Action logic, gates, limits	references/actions/{action}.md
Output format	references/templates/{action}-output.md
Spec structure	references/spec-template.md
Quality gate commands/levels	references/quality-gates.md
Session resume, stuck detection	references/session-management.md
References

Actions:

Plan | Ship | Fix | Review | Spec Review | Focus | Done | Drop | Spike

Output templates:

Plan + Spec Review | Ship | Fix | Review | Focus | Done | Drop | Spike | Status

Review standards:

Core portable review spec | Executor patterns | Production Standards

The portable review spec is normative. Executor patterns are optional implementation guidance.

Specs & gates:

Spec template | Quality gates | Session management | Memory update | Testing automation | E2E scenarios | Codebase intelligence

Patterns:

Implementation | Planning | Debugging | Decisions | Decomposition | Regression testing
Weekly Installs
61
Repository
bntvllnt/agent-skills
GitHub Stars
14
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn