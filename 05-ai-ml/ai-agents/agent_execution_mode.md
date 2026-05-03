---
rating: ⭐⭐⭐
title: agent-execution-mode
url: https://skills.sh/mwillbanks/agent-skills/agent-execution-mode
---

# agent-execution-mode

skills/mwillbanks/agent-skills/agent-execution-mode
agent-execution-mode
Installation
$ npx skills add https://github.com/mwillbanks/agent-skills --skill agent-execution-mode
SKILL.md
Agent Execution Mode

Use this skill whenever the user expects real completion: implementation, bug repair, hardening, architecture, design alignment, review, documentation, specification, repository-aware spec-driven delivery, or production-grade delivery.

This skill exists to stop the failure modes that make agent work untrustworthy: partial completion, self-approval, unmanaged sub-agent sprawl, token waste, stale docs, missing tests, missing review artifacts, and missing execution state.

When to use

Activate this skill when the request involves any of the following:

implementing or fixing behavior that should be complete when returned
bug investigation or bug fixing where the current behavior must be understood before edits begin
hardening an existing implementation after regressions, repeated failures, or correctness gaps
documentation creation or repair that must reflect the real project state instead of guessed behavior
specification or plan creation before implementation, especially when the work should be driven by existing repository specification, planning, or task artifacts
spec-driven delivery where implementation must stay governed by an existing repository-native specification, planning, task, ticket, or equivalent artifact packet
architecture or system design work that needs explicit decisions and durable documentation
code review, PR review, or self-review that must produce a reliable artifact
design-driven work where implementation must be checked against a specification or screenshot
post-mortem analysis after repeated prompt churn, missed requirements, or rework
work that benefits from delegated parallel discovery, implementation, validation, or review under a managed workflow
final reporting for substantial work

Infer the mode from task intent before defaulting. Use production only when the task does not clearly map to a more specific mode.

Modes

Supported modes:

production
bugfix
hardening
agent-review
agentic-self-review (compatibility alias of agent-review)
general-review
pr-review
prototype
design
documentation
specification-and-plan
spec-driven-delivery
architecture
post-mortem

Mode intent:

production: complete implementation using repo-native patterns, managed sub-agent delegation when it improves delivery, tests and docs updated where needed, and a mandatory independent agent-review gate before concluding.
bugfix: restate the bug, expected behavior, current evidence, and likely failure surface before editing. Implement the minimum correct repair, validate the fix, and run the mandatory agent-review gate.
hardening: everything in production and bugfix, plus stronger regression scrutiny, edge-case repair, abuse-case review, and stricter validation. The post-completion review gate is mandatory.
agent-review: act as the final reviewer using references/REVIEW_INSTRUCTIONS.md. Review only. Do not modify code unless the user explicitly changes the scope. In delegated post-completion use, follow the compact packet protocol from references/SUBAGENT_MANAGEMENT.md. Do not create a markdown artifact unless explicitly requested.
general-review: produce a review artifact using assets/TEMPLATE_REVIEW.md and the standard in references/REVIEW_INSTRUCTIONS.md.
pr-review: requires a PR link, uses GitHub MCP to inspect intent and diff, records the review in assets/TEMPLATE_PR_REVIEW.md, and submits inline feedback plus a summary review state through GitHub MCP.
prototype: reduced polish is allowed only when explicitly requested, but repository safety checks, validation honesty, and the post-completion review gate still apply.
design: design-focused work only. Use Figma MCP when a design specification exists; otherwise use screenshots or equivalent visual references. Do not claim runtime completeness unless it was actually implemented. The post-completion review gate is mandatory.
documentation: inspect the real project state and create or repair docs, runbooks, prompts, or operator guidance. Do not invent behavior, status, or validation that was not directly verified. Use agent-review when the documentation is substantial or when changed docs make product or operational claims.
specification-and-plan: detect the repository's existing specification-driven workflow before creating artifacts. Infer workflow shape from existing specs, PRDs, design docs, ADRs, OpenAPI, architecture or plan docs, task artifacts, tool-specific directories, and CI or enforcement signals. Follow the existing workflow when it is clear, fill missing stages conservatively when it is partial, and bootstrap a minimal lightweight structure only when no durable workflow exists. Use Speckit-specific behavior only when Speckit is clearly the intended workflow or the user explicitly asks for it.
spec-driven-delivery: implement against a governing repository-native SDD packet without erasing prior completed work. Map the repository's artifacts into the internal delivery stages, update the governing artifacts in place, route implementation and validation back through the same packet, preserve history, and always finish with the required post-mortem closeout before completion is claimed.
architecture: produce durable system decisions, reusable structure, and implementation when feasible. The post-completion review gate is mandatory.
post-mortem: analyze why repeated prompts, missed requirements, or rework happened. Recommend skills, documentation, agent.md, MCP tooling, or prompt changes that would have reduced friction or produced a more precise result earlier. Do not expand into code changes unless the user changes scope. This mode is analysis-only by default and does not add a nested mandatory agent-review unless the user explicitly requests one or the scope expands into durable repo changes.

recommendation-review is removed. Use general-review or pr-review instead.

Mode selection rules
infer documentation when the user asks to document, explain, update docs, produce a runbook, or align prompts or guidance to real behavior
infer specification-and-plan when the user asks for a specification, implementation plan, tasks, RFC, workflow design, or other durable planning artifacts before code changes
infer bugfix when the task centers on a failing behavior, regression, broken test, or defect explanation
infer hardening when the task centers on repeated breakage, production reliability, abuse cases, or closing correctness gaps across existing code
infer agent-review, general-review, or pr-review when the user primarily wants review rather than implementation
infer post-mortem when the user asks why repeated prompts were needed, what should have existed first, or how the workflow or prompt should change next time
infer spec-driven-delivery when implementation must remain governed by an existing repository-native spec, plan, tasks, tickets, or equivalent packet and the work must preserve prior completed history instead of replacing it
infer design or architecture when the output is primarily visual implementation alignment or system design decisions
use production only when the task is implementation-oriented and no more specific mode clearly fits
Non-negotiable behavior
Do not return a partial implementation as complete work.
Do not allow the implementation agent to approve its own work when independent review is available.
Do not skip the mandatory independent agent-review gate when delegated review is available.
Do not pressure, steer, or selectively brief a review sub-agent toward approval.
Do not turn a spec-governed rework into a fresh rewrite. Update the governing spec, plan, task, and related report artifacts in place and preserve completed history.
Do not impose Speckit, .specify, or any other foreign SDD structure on a repository that already uses a different workflow or has no clear signal that Speckit is intended.
Do not let a changed-surface review substitute for the mandatory final full-scope review of a spec-driven delivery.
Do not accept a review packet that hides the governing spec, the real changed scope, or the material validation evidence.
Do not omit the source intent from a worker or reviewer packet. If a specification was implemented, include the exact spec path and the relevant plan or task files when they exist. If there was no spec, include the original prompt or a compact faithful summary with the real goal and concrete specifics.
Do not hide relevant governing rules from the reviewer. When code changes are in scope, code-discipline and repo-standards-enforcement must be surfaced when they are relevant.
Do not spawn sub-agents without bounded ownership, acceptance criteria, and a positive expected return on token spend. The mandatory post-completion agent-review reviewer satisfies this gate by policy and is not blocked by discretionary ROI arguments.
Do not let overlapping sub-agents edit the same scope without an explicit merge plan.
Do not merge sub-agent output without manager review.
Do not default to production when the request clearly belongs to documentation, specification-and-plan, bugfix, review, design, architecture, or post-mortem.
Do not stop at visual parity when behavior, state handling, contracts, documentation, or architecture are part of correctness.
Do not leave TODOs, placeholders, mock production paths, or knowingly incomplete required work in production paths.
Do not begin a bugfix or hardening edit before stating the bug, expected behavior, evidence or reproduction, and likely failure surface.
Do not invent documentation claims, validation claims, or operational readiness statements that were not directly verified.
Do not ignore repository-native abstractions when reusable boundaries already exist.
Do not write code before resolving the applicable project validation and enforcement plan.
Do not skip tests, validation, or docs when the change materially requires them.
Do not claim completion if obvious QA failures, accessibility failures, contract gaps, or unresolved review findings remain in scope.
Do not use review language that hides severity or uncertainty.
Execution workflow

Follow this sequence unless the request explicitly narrows scope:

Identify or infer the mode from the task intent and create or update task, review, and report state when the work is substantial.
Gather the minimum context needed to stop guessing, including the source intent, relevant specs or planning artifacts, validation commands, repository rules, and affected artifacts.
For bugfix and hardening, restate the bug, expected behavior, evidence or reproduction, likely failure surface, and minimum safe repair before editing.
For specification-and-plan and spec-driven-delivery, inspect the repository for its existing SDD workflow shape before creating or updating artifacts. Look for spec-like documents such as spec.md, prd.md, design docs, ADRs, OpenAPI, architecture docs, plan docs, task files, issue or ticket references, tool-specific directories such as .kiro, .augment, .cursor, .specify, and CI or enforcement signals that reference planning or review artifacts.
Classify the workflow as structured, partial, or absent. Follow the existing workflow when structured, fill missing stages conservatively when partial, and bootstrap a minimal lightweight structure only when absent. Use Speckit behavior only when Speckit is clearly intended or explicitly requested.
For spec-driven-delivery, treat the governing repository-native packet as authoritative, update the existing artifacts in place instead of replacing them, and route implementation, validation, review, and closeout back through the same packet.
Internally normalize the work into stages such as spec, clarify, plan, tasks, analyze, implementation, validation, and delivery when useful, but map the repository's real artifacts into those stages instead of forcing file names or directory layouts onto the repository.
For orchestration modes, consult references/SUBAGENT_MANAGEMENT.md and .agents/evaluations/management.json if it exists before spawning helpers.
Resolve whether sub-agents improve delivery. The manager must prefer the smallest viable execution shape and use the compact packet contracts from references/SUBAGENT_MANAGEMENT.md. Parallelization is justified only when scopes are clearly disjoint, merge cost stays low, and token overhead is worth it. Partitionability alone does not justify multiple workers. This minimization rule does not suppress the mandatory post-completion agent-review reviewer.
When a delegated worker or reviewer is unavailable, request approval for the documented fallback path once if approval could make delegation available, wait up to 90 seconds for the delegation path to recover, and then use the fallback only if the same constraint still applies. Record the exact unavailability cause and the fallback choice in the execution artifacts.
Implement, review, document, spec, or analyze with repository-native patterns. The main agent is the manager: it assigns scope, checks outputs, and gates integration.
Validate behavior, design, static analysis, tests, documentation truthfulness, and repository-native enforcement using the project workflow.
Update documentation and required artifacts when behavior, contracts, architecture, or workflow rules changed.
State completion only when the work is actually complete for the chosen mode.
For production, bugfix, hardening, prototype, design, documentation, specification-and-plan, spec-driven-delivery, and architecture, immediately run an independent agent-review per references/WORKFLOWS.md. The dedicated review sub-agent is approved by default for this gate and must not be blocked by the general sub-agent minimization rules.
If the review verdict is not exactly APPROVE, treat every finding as blocking, fix the issues, revalidate, and rerun the review gate.
Finish only after the review gate returns APPROVE, or after an explicitly documented local fallback review when delegated review was truly unavailable or disallowed by higher-priority runtime or user constraints.
When the work required multiple corrective prompts, repeated re-scoping, or user dissatisfaction, recommend post-mortem mode and run it when the user asks. For spec-driven-delivery, the post-mortem closeout is mandatory before the work is considered complete.
Repository-aware SDD detection

Before creating, updating, or executing a spec-governed workflow, inspect the repository and infer its workflow shape instead of assuming a named tool.

Signals to inspect:

spec-like artifacts such as spec.md, prd.md, design docs, ADRs, RFCs, OpenAPI, architecture docs, or decision logs
planning artifacts such as plan.md, technical plans, migration plans, implementation notes, or architecture packets
task decomposition such as tasks.md, checklists, issues, tickets, milestones, or tracker exports
tool or workspace directories such as .specify, .kiro, .augment, .cursor, or other repository-owned workflow surfaces
CI, lint, validation, or review automation that expects specific planning or closeout artifacts
repo docs, agent instructions, or scripts that reference a durable planning workflow

Workflow classification:

structured: the repository already has a clear end-to-end SDD workflow. Follow it and extend it without breaking conventions.
partial: the repository has some durable planning artifacts but missing stages. Fill the missing stages conservatively and keep the additions aligned to the existing artifact style and location.
absent: no meaningful SDD workflow exists. Bootstrap a minimal lightweight structure that fits the repository's norms and the user request.

Rules:

Speckit-specific behavior is allowed only when Speckit is clearly in use or explicitly requested.
Internal normalization is allowed, but external artifacts must stay aligned to the repository's actual structure.
Prefer augmentation over replacement. Do not rename, relocate, or rewrite existing artifacts unless the requirement itself changed.

Detailed workflow rules live in references/WORKFLOWS.md and references/SUBAGENT_MANAGEMENT.md.

Token and context discipline
The manager must provide each sub-agent only the minimum context required for its task.
Use the compact manager-to-worker and manager-to-reviewer packet contracts from references/SUBAGENT_MANAGEMENT.md instead of freeform narrative when delegation is meaningful.
Do not forward full conversation history, full repository summaries, or unrelated file lists when a smaller scoped prompt will do.
Reuse a compact manager-prepared context packet across similar workers instead of rewriting large prompts repeatedly.
Prefer diffs, file paths, acceptance criteria, and validation commands over long narrative restatements.
If delegation overhead exceeds likely delivery gain, do not delegate. This efficiency rule does not override the mandatory post-completion agent-review reviewer.
Token savings must never come from hiding constraints, failing validation, or omitting known risks.
Alignment gating

When material ambiguity, missing decision points, or alignment risk would likely cause wrong-path execution, avoidable rework, or meaningful token waste, apply execution-alignment-gate before implementation when that skill is available.

Do not apply this gating behavior for obvious continuation messages, terse confirmations, already approved plan continuation, safe low-risk assumptions, or cases where the specification, accepted plan, repository rules, or manager instructions already define the correct path.

This gating behavior is optional and must not be used as a substitute for following the active execution mode, reading the specification, or complying with repository rules already in force.

When execution-alignment-gate is not available, apply the same discipline directly: identify whether ambiguity is material, ask only the minimum clarification needed, avoid open-ended clarification loops, prefer safe stated assumptions when risk is low, and do not guess when missing scope, boundaries, acceptance criteria, or validation expectations would likely cause failure.

When a sub-agent lacks scope, boundaries, acceptance criteria, or validation expectations from its manager, it must seek manager clarification rather than guess. If execution-alignment-gate is available, use its manager-mode behavior.

Sub-agent management requirements

For managed sub-agent work, keep repo-local evaluations under .agents/evaluations/management.json.

Required behavior:

prefer the smallest viable execution shape in this order: no sub-agent, read-only scout or evidence-gathering worker, single bounded writer, parallel bounded writers on disjoint scopes, independent reviewer
treat the dedicated agent-review reviewer as pre-approved for the mandatory post-completion review gate; do not block it with delegation-overhead heuristics or the smallest-viable-execution preference
do not use multiple writing workers when one bounded writer is sufficient
prefer read-only discovery workers before write delegation when uncertainty is high
parallelization is justified only when the scopes are clearly disjoint and merge cost stays low
consult the management file before spawning helpers when it exists
use the compact packet contracts from references/SUBAGENT_MANAGEMENT.md for meaningful worker and reviewer prompts
update it after each meaningful sub-agent run
track quality by agent type and prompt pattern
keep at most 20 entries in recentRuns and compress before adding another entry beyond that limit
roll repeated issues into repoLearnings
keep repoLearnings limited to durable rules, not anecdotal run history
decommission prompt patterns before decommissioning agent types
adjust prompt patterns before restricting agent types unless evidence clearly points to agent unsuitability
restore an agent type when evidence shows the prompt pattern, not the agent, caused the failure
keep cross-repository learnings in ~/.agents/learnings/sub-agent-management.md compressed and deduplicated

Use assets/TEMPLATE_MANAGEMENT.json for the repo-local file shape and references/SUBAGENT_MANAGEMENT.md for operating rules.

Tracking requirements

For implementation-oriented work, prefer the repository's existing durable tracking surface when one already exists. Use .agents/tasks/ only as the default fallback when the repository does not already provide a task-tracking convention and the user did not name a different tracking surface.

Required files:

.agents/tasks/TASK_INDEX.md
.agents/tasks/TASK_ID.md

Rules:

TASK_INDEX.md is a prepended markdown table. Newest rows go directly under the header.
Required columns: ID, Name, Description, Mode, Status, Thread IDs, Created At, Updated At.
ID is auto-generated, semantic, unique, lowercase, and hyphen-separated.
Both ID and Name must link to .agents/tasks/TASK_ID.md.
Each task file uses assets/TEMPLATE_TASK_STATE.md.
Task frontmatter must include id, name, short-description, thread-ids, created-at, updated-at, and state.
The markdown body title must be # TASK_ID - TASK_NAME.
All timestamps must be UTC.

Use assets/TEMPLATE_TASK_INDEX.md for the index shape.

Review requirements

For review work, prefer the repository's existing durable review surface when one already exists. Use .agents/reviews/ only as the default fallback when the repository does not already provide a review-tracking convention and the user did not name a different review surface.

Required files:

.agents/reviews/REVIEW_INDEX.md
.agents/reviews/REVIEW_ID.md

Rules:

REVIEW_INDEX.md is a prepended markdown table. Newest rows go directly under the header.
Required columns: ID, Name, PR #, Description, Mode, Status, Count, Created At, Updated At.
ID is auto-generated, semantic, unique, lowercase, and hyphen-separated.
Both ID and Name must link to .agents/reviews/REVIEW_ID.md.
PR # links to the GitHub PR when the review is PR-backed; otherwise use N/A.
Each review file uses assets/TEMPLATE_REVIEW.md or assets/TEMPLATE_PR_REVIEW.md.
Review frontmatter must include id, name, short-description, review-count, github-pr-number, github-pr-link, created-at, updated-at, and state.
The markdown body title must be # REVIEW_ID - REVIEW_NAME.
When a second or later review occurs for the same item, mark which existing findings were resolved and place new findings at the top of the new iteration.
general-review, pr-review, agent-review, and the compatibility alias agentic-self-review use the standard in references/REVIEW_INSTRUCTIONS.md.
Post-completion agent-review is normally delegated to a separate sub-agent. That reviewer is pre-approved for the mandatory post-completion gate and must not be blocked by the general sub-agent minimization rules. Use a local review against the same standard only when delegated review is unavailable or explicitly blocked. It does not create a markdown artifact unless explicitly requested.
If a delegated review packet omits the required intent source, relevant governing references, or material validation context, the reviewer must block the work instead of guessing.
If a review finding is disputed during the post-completion gate, only the user may dismiss it.
Reviews should also fold in the discipline from the code-discipline and repo-standards-enforcement skills when they are relevant to the code under review.

pr-review requirements:

requires a PR link
pull the PR diff and stated intent through GitHub MCP
review the code against the PR intent, not just the diff mechanics
record inline comment candidates, suggestions, and summary outcome in the markdown artifact
use GitHub MCP to submit inline comments and the overall review state: approved, changes-requested, comment, or rejected
on later review iterations, resolve or mark previously addressed findings before adding new ones
Design and validation requirements
design mode replaces the old design-only mode.
When a Figma specification is available, use Figma MCP first.
When Figma is not available, use screenshots or equivalent reference artifacts.
For documentation, derive claims from code, validated behavior, committed artifacts, or explicitly cited evidence. Unknowns must remain explicit unknowns.
For specification-and-plan, detect the repository's existing SDD workflow first. Follow it when present, fill missing stages conservatively when partial, and bootstrap only a lightweight structure when absent. Use Speckit-specific behavior only when Speckit is clearly intended.
For bugfix and hardening, capture the failing behavior and acceptance target before implementation, then verify the fix against that target after implementation.
For post-mortem, recommend concrete improvements in four buckets when relevant: skills, documentation, agent or instruction files, and MCP or tooling additions. Also explain how a tighter prompt would have produced a more precise or more efficient outcome.
For code-writing work, inspect the relevant project validation configuration and standards skill guidance before edits so the validation path is known up front. Biome, TypeScript, and skills such as repo-standards-enforcement or biome-enforcement are examples, not hardcoded requirements of this skill.
For code changes with UI impact, validate both design and implementation using Playwright through the Docker MCP.
Do not treat visual inspection alone as sufficient when interaction, state, or responsive behavior matters.
Final report requirements

For substantial implementation, architecture, or multi-step review work, prefer the repository's existing durable reporting surface when one already exists. Use .agents/reports/ only as the default fallback when the repository does not already provide a reporting convention and the user did not name a different reporting surface.

Required files:

.agents/reports/REPORT_INDEX.md
.agents/reports/REPORT_ID.md

Rules:

REPORT_INDEX.md is a prepended markdown table. Newest rows go directly under the header.
Recommended columns: ID, Name, Description, Mode, Status, Created At, Updated At.
ID is auto-generated, semantic, unique, lowercase, and hyphen-separated.
Both ID and Name link to .agents/reports/REPORT_ID.md.
Each report file uses assets/TEMPLATE_REPORT.md.
Report frontmatter must include id, name, short-description, mode, created-at, updated-at, and state.
Keep the latest run at the top of the report file.
Do not delete prior run entries.

Use assets/TEMPLATE_REPORT_INDEX.md for the index shape.

Documentation policy

Documentation is mandatory when:

existing documentation no longer matches behavior
architecture or module boundaries changed
a new component, workflow, or public contract was introduced
operational usage or testing strategy materially changed

Update the smallest correct documentation surface. Do not leave stale docs behind.

Mandatory agent-review gate

Before concluding any task, verify all applicable items:

completion claims match reality
required states and edge cases were handled
tests and validation were not skipped without cause
docs were updated when needed
review and report artifacts were updated when required by mode
design and implementation were both validated when UI work was involved
the post-completion review gate ran with the correct independence rules
the delegated review packet included the real source intent, relevant governing references, and material validation results
management evaluations and durable learnings were updated when sub-agents were used

For production, bugfix, hardening, prototype, design, documentation, specification-and-plan, spec-driven-delivery, and architecture, this gate is mandatory after completion has been stated. Do not skip it, compress it into a superficial pass, or treat earlier informal checking as a substitute.

If any answer is no, continue working or report the exact blocker.

Templates and references

Templates:

assets/TEMPLATE_TASK_INDEX.md
assets/TEMPLATE_TASK_STATE.md
assets/TEMPLATE_REVIEW_INDEX.md
assets/TEMPLATE_REVIEW.md
assets/TEMPLATE_PR_REVIEW.md
assets/TEMPLATE_REPORT_INDEX.md
assets/TEMPLATE_REPORT.md
assets/TEMPLATE_MANAGEMENT.json

References:

references/WORKFLOWS.md
references/REVIEW_INSTRUCTIONS.md
references/SUBAGENT_MANAGEMENT.md

Keep SKILL.md as the activation layer. Put deeper process rules in references/ and reusable document shapes in assets/.

Weekly Installs
27
Repository
mwillbanks/agent-skills
GitHub Stars
1
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn