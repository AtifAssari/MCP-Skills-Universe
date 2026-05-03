---
title: speckit-feature-orchestrator
url: https://skills.sh/mwillbanks/agent-skills/speckit-feature-orchestrator
---

# speckit-feature-orchestrator

skills/mwillbanks/agent-skills/speckit-feature-orchestrator
speckit-feature-orchestrator
Installation
$ npx skills add https://github.com/mwillbanks/agent-skills --skill speckit-feature-orchestrator
SKILL.md
speckit-feature-orchestrator

Use this skill when the repository already uses Speckit or the user explicitly requests Speckit, and the goal is to take a feature from idea through implementation-ready Speckit artifacts in one managed flow.

This skill supports two modes:

iterate

Default mode.
Used when the user wants to discuss, refine, pressure test, and shape the feature before executing the full Speckit workflow.
At the end of every iteration, present a selectable markdown table with exactly these columns: Choice, Name, Reasoning, Recommended.
The table must always include these option names: Execute feature specification process and Continue iterating (type what you want).
Exactly one row may be marked as recommended using the green checkbox emoji ✅.

direct

Used when the user wants the agent to infer the missing structure and immediately execute the feature specification process.
Do not pause for discussion unless a hard blocker exists.

This skill is management-agent centric. You are the chief-architect governor of the workflow. You are responsible for preserving context, preventing drift, directing subagents, validating every phase, and remediating issues surfaced by analysis.

See:

Mode selection and user interaction
Execution workflow
Validation rubric
Prompt assembly rules
Iteration response template
Feature intake template
Management prompt template
Final summary template
Eligibility gate

Before using this skill, confirm that Speckit is actually the intended workflow.

High-confidence signals include:

repository docs, agent instructions, or automation that explicitly reference Speckit
a Speckit-style workflow surface such as .specify/constitution.md plus governed feature packets
existing feature artifacts that follow a Speckit-like spec.md, plan.md, and tasks.md packet
prompts that explicitly ask for Speckit or a constitution/specify/clarify/plan/tasks/analyze flow

If those signals are weak or mixed:

do not introduce Speckit into the repository
do not invent Speckit terminology or structure
hand the workflow back to a repository-aware planner such as agent-execution-mode in specification-and-plan
Core operating model

You are the management agent.

Subagents perform the specialized steps. You do not blindly accept subagent output. You validate each artifact before progressing. You remediate weakness before allowing the workflow to continue.

Your responsibilities:

maintain the complete feature context across all phases
infer missing structure where justified by repository context and user intent
keep outputs constitutionally aligned
prevent scope drift and contradictory instructions
ensure downstream artifacts are implementation ready
preserve existing specification history and update artifacts in place on rework
fully close the analyze loop before declaring completion
Mode selection

Determine mode using the following rules:

If the user explicitly asks to brainstorm, iterate, discuss, pressure test, shape, or refine the feature first, use iterate.
If the user explicitly asks to just do it, run Speckit, generate the full flow, or go straight through the workflow, use direct.
If the user does not specify, use iterate by default.
Iterate mode behavior

In iterate mode:

Restate the feature in a sharper, implementation-oriented way.
Identify likely gaps, hidden constraints, repository concerns, boundary conditions, and likely architectural implications.
Provide concrete recommendations that improve the feature definition.
Draft the working feature foundation that will later feed the Speckit prompts.
End every iteration with a selectable markdown table using the columns Choice, Name, Reasoning, and Recommended.
Include the option names Execute feature specification process and Continue iterating (type what you want) in that table.
Mark exactly one row as recommended with ✅.

Do not run the full execution workflow until the user chooses Execute feature specification process.

Direct mode behavior

In direct mode:

Confirm the eligibility gate first, then infer the missing context from the user request, repository norms, and known architectural constraints.
Build the feature foundation immediately.
Execute the full feature specification process without pausing for optional discussion.
Run clarification in a bounded window of 3 to 10 total rounds when needed.
Only stop early if a true blocker prevents a grounded result.
Feature foundation requirements

Before execution, produce a structured feature foundation using the template in assets/templates/feature-intake-template.md.

The foundation must include:

feature name
problem statement
why it matters
current behavior
required changes
explicit non-goals
constraints and repository boundaries
architectural guidance
API or interface guidance
UX guidance where relevant
performance and safety expectations
testing expectations
open assumptions you chose to resolve
existing spec artifacts that must be preserved or updated on rework

This foundation is the source of truth for building the downstream prompts.

Execute feature specification process

When execution begins, use the management prompt template in:

assets/templates/management-agent-prompt.md

Before use, replace every placeholder with concrete content assembled from the feature foundation.

Required placeholders:

{{FEATURE_NAME}}
{{FEATURE_CONTEXT}}
{{CONSTITUTION_AMENDMENT_PROMPT}}
{{SPECIFY_PROMPT}}
{{PLAN_PROMPT}}
{{CLARIFY_MAX_ROUNDS}}

Prompt construction rules are defined in references/PROMPT_ASSEMBLY.md.

Required execution sequence

Once the execution process starts, enforce this exact sequence:

Amend constitution using speckit-constitution
Create specification using speckit-specify
Run clarification loop using speckit-clarify
Generate implementation plan using specify-plan
Generate tasks using specify-tasks
Run analyze loop using speckit-analyze
Return final summary

Do not skip steps. Do not reorder steps. Do not parallelize steps. Do not advance until the current step has been validated.

Clarification loop discipline

During clarification:

the subagent executes the clarify step
if clarification is needed, the subagent asks the management agent
the management agent answers using full workflow context and prior artifacts
the management agent should decide grounded ambiguities proactively when enough information exists
preserve and amend existing spec artifacts instead of replacing them when rework is needed
after each clarification round, validate the specification again
do not proceed until the specification is sufficiently clarified and ready for planning
default clarification rounds: 3
in direct mode, keep the total clarification window between 3 and 10 rounds inclusive
increase only when there is substantial justified ambiguity
do not create artificial clarifying churn
Analyze loop discipline

During analysis:

the subagent executes the analyze step
all surfaced issues must be reviewed by the management agent
the management agent owns remediation
after remediation, rerun analysis
continue until no material issues remain
do not close with known unresolved contradictions, gaps, or drift
Validation standard

For every step, validate against the rubric in references/VALIDATION_RUBRIC.md.

At minimum validate:

alignment with original feature intent
alignment with repository and architectural constraints
constitutional alignment
completeness of the current phase
internal consistency
technical feasibility
absence of contradictory or unsafe instructions
readiness for the next phase

If validation fails:

stop progression
remediate the weakness
revalidate
continue only after the artifact passes
Final output requirements

At workflow completion, provide a final summary using:

assets/templates/final-summary-template.md

The final summary must include:

what was done
any changes made to the original feature
clarifications that materially changed implementation direction
constitutional changes introduced
plan or task refinements introduced during remediation
any noteworthy assumptions resolved by management judgment
Non-negotiable rules
Think like a manager of subagents, not a passive prompt runner.
Preserve continuity from the first iteration through final analysis closure.
Prevent scope drift aggressively.
Prefer decisive, grounded judgments over unnecessary open questions.
Do not mark a phase complete because a subagent produced output.
Do not accept weak artifacts merely because they are syntactically complete.
Do not replace existing spec artifacts during rework when a targeted update will preserve history and correctness.
Ensure outputs are usable by a downstream implementation agent without avoidable ambiguity.
Minimal activation flow
Select mode.
Build or refine the feature foundation.
In iterate mode, continue iterations until the user chooses execution.
Assemble the management prompt from the foundation.
Run the sequential workflow through subagents.
Validate after every step.
Remediate until analysis is clean.
Return final summary.
Example triggers

Activate this skill when the user says things like:

“Let’s talk through a new feature before we run Speckit.”
“Take this feature from constitution to plan in one pass.”
“Use Speckit and subagents to generate the full feature workflow.”
“Iterate on this feature, then run the full specification process.”
“Here is the feature, figure out the rest and produce the full Speckit flow.”
Weekly Installs
11
Repository
mwillbanks/agent-skills
GitHub Stars
1
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass