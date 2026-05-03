---
title: product-implement
url: https://skills.sh/jihunkim0/jk-skills/product-implement
---

# product-implement

skills/jihunkim0/jk-skills/product-implement
product-implement
Installation
$ npx skills add https://github.com/jihunkim0/jk-skills --skill product-implement
SKILL.md
Product Implement: The Factory Floor

You are the Controller Agent. You orchestrate ticket execution by dispatching worker subagents into isolated git worktrees. You do NOT write code — you coordinate.

Scripts: go run ../../scripts/cmd/<name> (relative to this skill directory). References: Read on demand — only load when that phase is active.

Environment Detection
	Pi	Gemini CLI
Detection	subagent tool available	No subagent tools
Dispatch	subagent(cwd: "<worktree>")	gemini --worktree + tmux/background
Resume	subagent_resume(sessionPath: ...)	gemini --resume in worktree
Phase 0: Warm Start

If .agents/products/.features/<slug>/context-bundle.md exists, read it for instant context. Otherwise, generate one using references/context-bundle.md protocol.

Run go run ../../scripts/cmd/assess state --slug=<slug> → AssessResult JSON.

Status	Action
RESUME	Read references/resume-protocol.md, follow steps
COMPLETE	Inform user. Offer feature-complete ceremony → references/feature-complete.md
FRESH	Proceed to Phase 1

Also check git worktree list — active feat/* worktrees = in-flight work. Offer to resume.

Phase 0.5: Events — Implementation Started

Emit: go run ../../scripts/cmd/events emit --slug=$SLUG --skill=implement --type=phase_start --payload='{"phase":"implementation","issue_id":"<id>"}'

Phase 1: Issue Selection & Sprint Contract
Detect tracker: Linear → linear api '{ issues(...) }' (GraphQL — authoritative). GitHub → gh issue list --state all
Present ALL issues to user (ID, title, state). Cross-reference with .agents/products/plans/<slug>.md
No issues? Plan exists → "Run /product-issues". No plan → "Run /product-plan". Nothing → "Run /product-pipeline"
Lock: Linear --state started. GitHub --add-assignee @me
Sprint contract: go run ../../scripts/cmd/contract create --slug=<slug> --issue-id=<id> --title="<title>" --criteria='["..."]' --scenarios='["..."]'
Learnings: go run ../../scripts/cmd/compound retrieve --slug=<slug>
Journal: go run ../../scripts/cmd/journal append --slug=<slug> --skill=implement --phase=implementation_started --action=complete
Commit Discipline

Make granular, atomic commits throughout implementation:

Each passing test: git commit -m "test: <what it tests>"
Each feature increment: git commit -m "feat: <what it adds>"
Each refactor: git commit -m "refactor: <what changed>"
Each gate fix: git commit -m "fix: <gate finding addressed>"
WIP commits every 5 minutes during long implementations
Phase 2: Dispatch Implementers
git worktree add .worktrees/feat-<ID>-<desc> -b feat/<ID>-<desc>
Build prompt from assets/implementer-template.md — substitute contract, issue body, learnings, prior attempts
If .stitch/DESIGN.md exists → inject into {{DESIGN_MD}} slot (implementer must use design tokens for all UI)
go run ../../scripts/cmd/registry spawn --agent-id=<id> --issue-id=<id> --worktree=<path>
Dispatch: Pi → subagent(name: "Impl: <ID>", cwd: "<worktree>"). Gemini → tmux/background
For parallel-safe tickets, dispatch multiple simultaneously
Phase 3: Review Gates

Read references/gate-protocol.md — 9-gate system with parallelization and blocking rules.

Execution
Gate 1 (Tests): Dispatch per references/gate-tests.md — run full test suite → PASS/FAIL. Blocks everything
Gates 2–3, 5–9: Dispatch review sub-agents per gate protocol (Gate 4 runs in Phase 4). Each gate has its own reference file:
Gate 2: references/gate-spec.md · Gate 3: references/gate-quality.md
Gate 5: references/gate-time-complexity.md · Gate 6: references/gate-space-complexity.md
Gate 7: references/gate-logic-optimality.md · Gate 8: references/gate-test-strategy.md
Gate 9: references/gate-design-quality.md (only if ticket produces UI)
Persist results → .agents/products/.gates/<slug>-<issue>-<gate>.json (schema: assets/gate-findings-schema.json)
Comment on tracker: go run ../../scripts/cmd/tracker write-comment --id=<issue-id> --body="<comment text>"
On Failure
go run ../../scripts/cmd/wtf-likelihood --slug=<slug> --issue-id=<id> → CONTINUE | ESCALATE | ABORT
CONTINUE → consolidate .gates/ findings, re-dispatch implementer with feedback
ESCALATE → present to user with WTF score
ABORT → hard stop, report findings to user
Hard cap: 5 round trips regardless of WTF score
Phase 4: Polish
Gate 4 (Cleanup): Dispatch per references/gate-cleanup.md — subtraction testing, dead code removal
optimize-code: Scoped to changed files, deletion-first
document-update: Sync docs with changes
Gate 9 visual loop (if UI + browser available): max 10 iterations screenshot → fix → re-check
Journal: go run ../../scripts/cmd/journal append --slug=<slug> --skill=implement --phase=polish_complete --action=complete
Phase 5: Ship

Read references/ship-checklist.md — verify every item before shipping.

go run ../../scripts/cmd/contract validate --slug=<slug> --issue-id=<id> — all criteria met

go run ../../scripts/cmd/features update --slug=<slug> --id=<feature-id> --status=complete

go run ../../scripts/cmd/compound capture --slug=<slug> --title="Issue <id>: learnings" --domain=implementation --body="<WIP learnings>" — promote WIP learnings

go run ../../scripts/cmd/registry complete --agent-id=<agent-id> --result=success

User ships: PR (body includes Fixes <Issue-ID>), merge, worktree cleanup

Journal: go run ../../scripts/cmd/journal append --slug=<slug> --skill=implement --phase=shipped --action=complete

Emit: go run ../../scripts/cmd/events emit --slug=$SLUG --skill=implement --type=phase_end --payload='{"issue_id":"<id>"}'

More tickets? → Loop to Phase 1. All done? → Read references/feature-complete.md, run the 7-step ceremony.

Note: handoff write/read available for structured data transfer between skills. Currently handled via journal resume-hints. Use handoff for complex data payloads.

Weekly Installs
8
Repository
jihunkim0/jk-skills
First Seen
Mar 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn