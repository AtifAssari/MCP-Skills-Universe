---
title: execute
url: https://skills.sh/alpoxdev/hypercore/execute
---

# execute

skills/alpoxdev/hypercore/execute
execute
Installation
$ npx skills add https://github.com/alpoxdev/hypercore --skill execute
SKILL.md
Execute

Receive a task, classify its difficulty, think proportionally, and start working immediately.

<request_routing>

Positive triggers
A direct task instruction with a clear deliverable: "add pagination to the user list", "implement dark mode toggle".
An explicit execution request: "do this", "build this", "make this work".
A scoped feature or change request that does not require extended planning: "refactor this", "add tests", "clean up this component".
Out-of-scope
Bug reports with error messages or failing symptoms. Route to bug-fix.
Repository-wide build, CI, or deployment failures. Route to deploy-fix.
Pre-release validation or build readiness checks. Route to pre-deploy.
Strategic planning or architecture decisions. Route to a dedicated planning or architecture skill when available; in this repo prefer prd-maker for requirements and framework-specific architecture skills for implementation architecture.
Code review or quality audit. Route to a dedicated review or QA skill when available; in this repo prefer qa for systematic QA work.
Security analysis. Route to a dedicated security skill when available; in this repo use framework-specific security skills such as tanstack-start-security when applicable.
Explicit workflow invocations such as $autoresearch-skill, $ralph, or another $skill request. Preserve the explicitly requested workflow instead of treating the prompt as a generic execute task.
Boundary cases
If the request mixes a bug fix with new work, execute owns it when the primary intent is the new work.
If the task scope is genuinely unclear (no deliverable identifiable), ask one clarifying question — then execute.
If the user asks for a persistent guaranteed-completion loop ("keep going until done", "until max score", or Ralph-style repetition), route to Ralph when available rather than silently downgrading it to one-shot execute.
If the task turns out to require architectural decisions mid-flight, pause and consult the user rather than guessing.

</request_routing>

<argument_validation>

If ARGUMENT is missing or too vague to identify a deliverable, ask briefly:

What should I execute?
- Task or feature to implement
- Target files or area
- Any constraints or requirements


Do not over-interrogate. One round of clarification maximum, then start working.

</argument_validation>

<difficulty_classification>

Classify before thinking. Use these signals:

Difficulty	Signals	Thinking depth
Easy	Single file, clear scope, familiar pattern, mechanical change	1-3 thoughts
Medium	Multi-file, some ambiguity, moderate scope, requires context gathering	4-6 thoughts
Hard	Cross-cutting, architectural impact, unfamiliar domain, complex interactions	7+ thoughts

For compound tasks (e.g. "refactor + add tests"), classify by the hardest sub-task. Treat the compound as one deliverable, not separate jobs.

When uncertain, round up one level. It is cheaper to over-think slightly than to redo work.

</difficulty_classification>

<mandatory_reasoning>

Adaptive Sequential Thinking

Always run sequential-thinking before implementation. The number of thoughts scales with difficulty:

Easy (1-3 thoughts):

What exactly needs to change
Where to change it
How to verify

Medium (4-6 thoughts):

Scope and deliverable clarity
Relevant code exploration plan
Implementation approach
Edge cases or risks
Verification strategy
(Optional) Alternative approach comparison

Hard (7+ thoughts):

Scope and deliverable clarity
Codebase context and dependencies
Design approach
Implementation breakdown
Edge cases and failure modes
Cross-cutting impact
Verification strategy 8+ (as needed) Revision, branching, deeper analysis

Announce the classification briefly before starting:

Difficulty: [easy/medium/hard] — [one-line reason]


</mandatory_reasoning>

<execution_rules>

Core principle: act, don't deliberate
Start implementing after thinking. Do not present options or wait for confirmation.
If a decision point arises where both paths are reasonable, pick the simpler one and note it.
Only pause for user input when the task itself is ambiguous (what to do), not when the approach is ambiguous (how to do it).
Keep scope to what was asked. Do not add unrequested improvements.
Implementation
Read relevant code before editing.
Make targeted changes — smallest diff that achieves the deliverable.
Run targeted validation after changes (typecheck, test, build as appropriate).
If validation fails, fix it within scope. Do not leave broken state.

</execution_rules>

Step	Task	Tool
1	Validate input — identify the deliverable	-
2	Classify difficulty (easy/medium/hard)	-
3	Think proportionally	sequential-thinking
4	Explore relevant code	Read/Grep/Glob
5	Implement	Edit/Write
6	Validate (typecheck/test/build)	Bash
7	Report outcome and changed files	-

Steps 4-6 may repeat as needed. The goal is a working deliverable, not a single pass.

<completion_report>

After execution, report briefly:

## Done

**Task**: [what was executed]
**Difficulty**: [easy/medium/hard]
**Changes**: [list of changed files]
**Validation**: [what was verified and result]


If anything remains unverified, say what and why.

</completion_report>

Execution checklist:

 ARGUMENT validated — deliverable is clear
 Difficulty classified
 sequential-thinking completed (proportional depth)
 Relevant code read before editing
 Implementation complete
 Validation executed (typecheck/test/build)
 Outcome reported with changed files

Forbidden:

 Presenting options and waiting for selection (this is execute, not diagnose)
 Over-thinking easy tasks (1-3 thoughts max for easy)
 Under-thinking hard tasks (7+ thoughts minimum for hard)
 Expanding scope beyond what was asked
 Claiming completion without running validation
Weekly Installs
25
Repository
alpoxdev/hypercore
GitHub Stars
3
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass