---
rating: ⭐⭐⭐
title: task-brief
url: https://skills.sh/freeacger/loom/task-brief
---

# task-brief

skills/freeacger/loom/task-brief
task-brief
Installation
$ npx skills add https://github.com/freeacger/loom --skill task-brief
SKILL.md
Task Brief
Overview

Turn a raw natural-language request into a structured task brief that another executor can use without reading the original message.

This skill is a task specification normalizer. Its job is to surface the real goal, capture the completion standard, and make critical constraints explicit. It does not do design-stage routing, task decomposition, implementation planning, or execution.

The value is straightforward: a good brief reduces misunderstanding, prevents wasted work on the wrong problem, and makes handoff cleaner for another model, agent, or human.

Core Responsibilities

task-brief should only:

Restate the real user goal, not just the surface wording.
Define the success criteria in observable terms.
Capture the deliverables the task is expected to produce.
Surface constraints that materially change execution.
Record short assumptions when the user has left gaps.
Ask at most one clarifying question when one critical unknown remains.
Make one lightweight judgment about whether the task needs design work.

task-brief should not:

route the task between design skills
decompose the task into sub-tasks
draw dependency diagrams
write implementation steps
propose migration sequencing
default to codebase investigation just to sharpen the brief

If the real task is root-cause investigation, use systematic-debugging instead of turning task-brief into a debugging workflow.

When to Use

Trigger on:

requests with multiple sub-goals or unclear priority order
requests that span domains (for example data + UI + API)
requests where the stated problem may not be the real problem
requests that will likely be handed off to another executor
requests where missing context would force high-impact assumptions
requests where the user explicitly asks for help clarifying the task itself

Do NOT trigger on:

single, unambiguous actions ("delete this function", "run the tests")
requests where the intent is already clear and the execution path is obvious
follow-up messages that only refine an existing task in progress
requests that explicitly ask for a design tree or design-stage decomposition

If in doubt, ask this question: can an executor start correctly from the brief alone? If yes, the brief is probably sufficient.

Complexity Tiers

Classify the request into one of these tiers before writing the brief.

Tier	Signal	Response
Direct	Single goal, clear scope, no critical missing information	Write a concise brief. Usually Needs Design is no.
Clarify	One critical unknown remains, or the stated goal may be inaccurate	Write the brief first, ask exactly one clarifying question, and keep the rest minimal.
Structured	Multiple goals, cross-domain context, or a handoff-friendly brief is needed	Write the full brief, but stop at the brief. Do not decompose or route inside this skill.

Clarify has three common sub-cases:

Missing parameter: you know the goal, but one detail is missing.
Ambiguous intent: the goal could reasonably mean two substantially different things.
Inaccurate goal: the user stated a solution, symptom, or oddly scoped target instead of the underlying goal.

For inaccurate goals, detect these signals:

Solution-as-goal: the user names a technique ("add Redis caching") rather than the problem it solves.
Symptom-as-goal: the user names an error state ("fix timeout errors") rather than the desired outcome.
Scope anomaly: the stated scope looks unnaturally narrow or broad for the problem.

When one of those signals appears:

rewrite the User Goal around the best-guess underlying intent
mark that guess as an assumption
ask one clarifying question that confirms the real target

Do not default to codebase search just to sharpen the question. If the task is actually debugging, route to systematic-debugging.

Output: Task Brief

Always output the brief in this format. Omit Clarifying Question if none is needed. Omit fields only when they add no value.

## Task Brief

**Task Type:** [analysis | transformation | generation | investigation | other]

**User Goal:**
[1-2 sentences. State the real intent, not the surface request. Start with a verb.]

**Success Criteria:**
- [Observable completion signal 1]
- [Observable completion signal 2]

**Deliverables:**
- [Concrete artifact 1]
- [Concrete artifact 2]

**Clarifying Question:**
[Exactly one question when one critical unknown remains. Omit this field if no question is needed.]

**Constraints:**
- Scope: [data source, file range, system boundary, etc.]
- Format: [output language, file type, response length, etc.]
- Risk: [what must not be broken, changed, or leaked]
- Other: [time range, locale, performance budget, etc.]

**Assumptions:**
- [Short inference made because the user did not specify it]

**Needs Design:** [yes | no]

Output Rendering

Keep the English field names and enum literals canonical for protocol stability.

English responses should render the headings in English only.
Chinese responses may render bilingual headings with Chinese first and English in parentheses.
Do not hardcode bilingual headings into this canonical English template.
Compression Rules

These rules govern how to convert a raw message into the brief.

Keep:

the underlying goal
constraints that eliminate whole categories of solutions
domain context that changes the execution path

Remove:

filler phrases
repeated restatements of the same goal
reasoning the executor does not need to act

Convert (vague -> actionable):

"make it better" -> identify the dimension: performance, readability, UX, security
"something's wrong" -> specify observed vs. expected behavior
"soon" / "quickly" -> ask for a concrete deadline only if it affects approach
"the usual format" -> infer from context or mark it as an assumption
"add Redis to the API" -> ask what problem the user is trying to solve

When intent is ambiguous:

if two substantially different interpretations are plausible, surface both explicitly
ask one question that forces the choice
defer deliverables that depend on that choice rather than guessing

Don't over-correct:

preserve the user's framing when it carries real intent
do not invent goals or constraints the user did not imply
if uncertain whether a detail matters, keep it and mark it as an assumption
Examples
Example 1 - Direct

User input:

"Extract all TODO comments from the codebase and output them as a markdown list grouped by file."

Task Brief:

## Task Brief

**Task Type:** transformation

**User Goal:**
Collect all TODO comments across the codebase and organize them into a readable markdown list grouped by file.

**Success Criteria:**
- The output lists TODO comments grouped by file.
- Each TODO entry includes a line number.

**Deliverables:**
- Markdown list of TODO comments grouped by file

**Constraints:**
- Scope: entire repository
- Format: markdown output

**Assumptions:**
- "TODO" means the literal string `TODO` or `TODO:`.

**Needs Design:** no

Example 2 - Clarify

User input:

"I need to migrate our auth system to JWT. Can you help me figure out what needs to change?"

Task Brief:

## Task Brief

**Task Type:** investigation

**User Goal:**
Identify what needs to change to migrate the current authentication system to JWT-based auth without mis-scoping the migration.

**Success Criteria:**
- The affected auth components are identified.
- The migration target is clear enough to begin design or impact analysis.

**Deliverables:**
- Auth migration change brief

**Clarifying Question:**
What does the current auth system use now: session cookies, a third-party identity provider, API keys, or something else?

**Constraints:**
- Scope: authentication-related behavior only
- Risk: do not assume a stateless-token migration path if the current system is session-based or third-party managed

**Assumptions:**
- JWT means standard stateless tokens rather than JWE.

**Needs Design:** yes

Example 3 - Structured

User input:

"Build me a dashboard that shows real-time sales data pulled from our Postgres DB, with a chart for daily revenue and a table for top 10 products. It should update every 30 seconds and be shareable via a link."

Task Brief:

## Task Brief

**Task Type:** generation

**User Goal:**
Build a shareable dashboard that displays live sales data from Postgres, including a daily revenue chart and a top-products table that refresh every 30 seconds.

**Success Criteria:**
- The dashboard shows daily revenue and top products from live data.
- The dashboard refreshes every 30 seconds.
- The dashboard can be accessed through a stable shareable URL.

**Deliverables:**
- Live sales dashboard

**Clarifying Question:**
Does "shareable via a link" mean publicly accessible without auth, or accessible only to authenticated users?

**Constraints:**
- Scope: dashboard behavior only
- Format: browser-based UI
- Risk: no database writes and no credential exposure in client-side code

**Assumptions:**
- The data source is an existing Postgres database with fields needed for revenue and top-product aggregation.

**Needs Design:** yes

Example 4 - Ambiguous Intent

User input:

"Our API docs are a mess - can you help fix them?"

Task Brief:

## Task Brief

**Task Type:** analysis

**User Goal:**
Improve the API documentation, but the target is ambiguous between two materially different outcomes:

- Interpretation A: audit and rewrite the documentation content itself
- Interpretation B: change the documentation tooling or site structure

**Success Criteria:**
- The intended direction is confirmed before work starts.

**Deliverables:**
- Deferred until the direction is confirmed

**Clarifying Question:**
Is the real problem the documentation content, or the tooling and presentation layer?

**Constraints:**
- Scope: public API documentation only
- Risk: external developer experience may be affected by public doc changes

**Assumptions:**
- "API docs" refers to developer-facing HTTP API documentation rather than internal notes.

**Needs Design:** yes

Example 5 - Inaccurate Goal

User input:

"Add Redis caching to our API endpoints."

Task Brief:

## Task Brief

**Task Type:** investigation

**User Goal:**
Reduce API latency or backend load, assuming Redis was proposed as a technique rather than as the confirmed goal.

**Success Criteria:**
- The real performance problem is identified.
- The task target is reframed around the actual bottleneck instead of a preselected technique.

**Deliverables:**
- Performance-problem brief

**Clarifying Question:**
What performance problem are you seeing right now: slow endpoints, high database load, or something else?

**Constraints:**
- Scope: API behavior only
- Risk: do not assume caching is appropriate before the bottleneck is known

**Assumptions:**
- The user wants better performance but has not yet confirmed where the bottleneck is.

**Needs Design:** no

Acceptance Criteria

A good task brief passes these checks:

Standalone: an executor can start correctly from the brief alone, or knows the one question that must be answered first.
Intent-preserving: the User Goal captures what the user actually wants, not just what they said.
Constraint-complete: missing any included constraint would materially risk wrong-path execution.
Non-padded: the brief stays short when the task is simple.
Actionable deliverables: each deliverable is a concrete artifact or outcome.
Goal-honest: the brief reframes solution-as-goal and symptom-as-goal requests honestly.
Scope-clean: the brief does not drift into design routing, decomposition, or implementation planning.
Single-question discipline: when clarification is needed, the brief asks one focused question, not a questionnaire.

A brief is not useful if:

it restates the user's message in different words without adding clarity
it introduces goals or constraints the user did not imply
it turns a simple request into a long clarification session
it drifts into design trees, sub-task decomposition, or implementation plans
Weekly Installs
15
Repository
freeacger/loom
GitHub Stars
1
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass