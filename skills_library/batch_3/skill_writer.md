---
title: skill-writer
url: https://skills.sh/getsentry/skills/skill-writer
---

# skill-writer

skills/getsentry/skills/skill-writer
skill-writer
Installation
$ npx skills add https://github.com/getsentry/skills --skill skill-writer
SKILL.md
Skill Writer

Use this as the single canonical workflow for skill creation and improvement. Primary success condition: maximize high-value input coverage before authoring while minimizing wasted runtime tokens.

Load only the path(s) required for the task. SKILL.md is the primary router: every bundled reference file should have a direct "open when..." reason here.

Core Workflow References
Open when you need to...	Read
choose the minimum workflow path for create, update, iterate, or research-first work	references/mode-selection.md
choose the simplest adequate execution shape before deciding files	references/execution-shapes.md
apply writing constraints for depth, concision, and portability	references/design-principles.md
decide what belongs in SKILL.md, references/, SPEC.md, or subfolders	references/reference-architecture.md
create or update the maintenance contract for a skill	references/spec-template.md
find missing high-signal sources, including history and regressions	references/source-discovery.md
run the full synthesis pass with depth gates and source capture	references/synthesis-path.md
author or update SKILL.md, SPEC.md, and supporting files	references/authoring-path.md
improve trigger language and false-positive/false-negative behavior	references/description-optimization.md
iterate from positive, negative, or fix examples	references/iteration-path.md
store persistent working and holdout examples for future revisions	references/iteration-evidence.md
choose a response template, schema, or output contract	references/output-contracts.md
troubleshoot overloaded layouts, hidden refs, or other structure failures	references/structure-troubleshooting.md
verify a risky, disputed, or explicitly requested change	references/evaluation-path.md
register the skill and run final validation checks	references/registration-validation.md
Artifact Layout References
Open when you need to...	Read
keep the whole skill inline in one coherent SKILL.md	references/artifact-layouts/inline-skill-layout.md
split optional deep knowledge into focused routed references	references/artifact-layouts/reference-backed-skill-layout.md
add scripts for deterministic automation or validation	references/artifact-layouts/script-backed-skill-layout.md
define a skill that is usually invoked with explicit arguments	references/artifact-layouts/argument-driven-skill-layout.md
ship reusable templates, schemas, or other static assets	references/artifact-layouts/asset-template-skill-layout.md
Workflow Mechanic References
Open when you need to...	Read
break a task into fixed ordered steps	references/workflow-mechanics/prompt-chaining.md
classify requests and route them to different downstream paths	references/workflow-mechanics/routing-workflows.md
split independent work into parallel units or votes	references/workflow-mechanics/parallel-workflows.md
discover work units dynamically and coordinate worker outputs	references/workflow-mechanics/orchestrator-workers.md
critique and revise output against a rubric	references/workflow-mechanics/evaluator-loops.md
run validate-fix-repeat checks during authoring or execution	references/workflow-mechanics/validation-loops.md
validate a plan before executing a risky action	references/workflow-mechanics/plan-validate-execute.md
Claude Code References
Open when you need to...	Read
use Claude-specific frontmatter or invocation controls	references/claude-code/frontmatter-and-invocation.md
use Claude argument fields or substitution variables	references/claude-code/argument-substitutions.md
build a skill that runs in isolated context: fork	references/claude-code/subagent-fork-skills.md
build a skill that uses Claude hooks for deterministic enforcement	references/claude-code/hook-backed-skills.md
use Claude shell preprocessing for dynamic context injection	references/claude-code/dynamic-context.md
Example Profiles
Open when you need to...	Read
see the expected depth for a documentation-heavy skill	references/examples/documentation-skill.md
see the expected depth for a security-review skill	references/examples/security-review-skill.md
see the expected depth for a workflow-process skill	references/examples/workflow-process-skill.md
see what a good routed skill looks like	references/examples/router-skill.md
see what a good evaluator-loop skill looks like	references/examples/evaluator-loop-skill.md
see what a good subagent-fork skill looks like	references/examples/subagent-fork-skill.md
see what a good hook-backed skill looks like	references/examples/hook-backed-skill.md
Step 1: Resolve target, path, and shape
Resolve the intended operation (create, update, synthesize, iterate) and inspect workspace prior art before choosing where files belong.
Choose the target skill root from observed conventions. If the canonical location is still unclear after inspection, ask one direct question before editing files.
Read references/mode-selection.md to choose the minimum required workflow paths.
Read references/execution-shapes.md to choose the primary execution shape.
Default to the simplest adequate shape. If selecting a more complex shape, record why simpler shapes were rejected.
Load only the exact artifact-layout, workflow-mechanic, and provider-specific leaf files required by that shape.
Record portability implications before using provider-specific mechanics.
Step 2: Run synthesis when needed

Read references/synthesis-path.md.

Use this path for new skills, material changes, and research-first planning.
Collect and score relevant sources with provenance.
Read references/source-discovery.md when source material is thin, stale, or ambiguous.
Produce source-backed decisions and coverage/gap status, including the class and execution-shape choice.
Load example profiles only when they add concrete depth for the selected class or shape.
If the skill uses provider-specific mechanics, include current official provider docs and capture usage constraints.
Do not move to authoring until depth gates pass.
Step 3: Run iteration first when improving from outcomes/examples

Read references/iteration-path.md first when selected path includes iteration (for example operation iterate).

Capture and anonymize examples with provenance.
Read references/iteration-evidence.md when examples should persist beyond the current turn.
Re-evaluate skill behavior against working and holdout slices.
Propose improvements from positive/negative/fix evidence.
Carry concrete behavior deltas into authoring.

Skip this step when selected path does not include iteration.

Step 4: Author or update skill artifacts

Read references/authoring-path.md.

Write or update SKILL.md in imperative voice with trigger-rich description.
Keep SKILL.md as the runtime router, not an encyclopedia.
Read references/reference-architecture.md before adding bulk instructions or new reference files.
Create or update SPEC.md using references/spec-template.md when creating a new skill or materially changing its contract.
Create focused reference files, subfolders, scripts, and assets only when each one has a clear "open when..." reason.
If you add a bundled reference file, add a direct routing entry for it in this SKILL.md.
Prefer checklists, tables, templates, and input/output examples over explanatory prose.
Follow only the specific artifact-layout, workflow-mechanic, Claude-specific, and output-contract references selected for this skill.
For advanced execution shapes, add the required routing, delegation, or safety contracts before considering the skill complete.
For authoring/generator skills, include transformed examples in references:
happy-path
secure/robust variant
anti-pattern + corrected version
Step 5: Optimize description quality

Read references/description-optimization.md.

Validate should-trigger and should-not-trigger query sets.
Reduce false positives and false negatives with targeted description edits.
Keep trigger language generic across providers unless the skill is intentionally provider-specific.
Step 6: Evaluate only when needed
Read references/evaluation-path.md only when the user asks for evaluation, the change is high-risk, or the architecture choice is non-obvious.
If you run evaluation, start with the lightweight qualitative check.
Run deeper evals only when requested or risk warrants it.
Record outcomes and unresolved risks when evaluation is run.
Step 7: Register and validate

Read references/registration-validation.md.

Apply repository registration steps for the active layout you verified in the workspace.
Run quick validation with strict depth gates.
Reject shallow outputs that fail depth gates or required artifact checks.
Output format

Return:

Summary
Changes Made
Validation Results
Open Gaps
Weekly Installs
619
Repository
getsentry/skills
GitHub Stars
657
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn