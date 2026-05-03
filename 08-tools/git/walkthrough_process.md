---
title: walkthrough-process
url: https://skills.sh/jasonharmongit/jh-skills/walkthrough-process
---

# walkthrough-process

skills/jasonharmongit/jh-skills/walkthrough-process
walkthrough-process
Installation
$ npx skills add https://github.com/jasonharmongit/jh-skills --skill walkthrough-process
SKILL.md
Walkthrough process (deep review)
Core intent

Use this skill to produce a high-context walkthrough for a reader who is new to the repo.

Default mode is process walkthrough:

explain how a named function/module/flow works
show where it sits in the larger system
trace entrypoint -> internal steps -> successful outcome

Branch-change walkthroughs are supported, but all change-specific instructions are isolated in Branch change mode (only when requested) near the end of this file.

Output file (required)
Read current branch with git branch --show-current.
Build branch_name by replacing / with - and stripping \ : * ? " < > |.
Ensure directory exists: mkdir -p ~/.cursor/plans/walkthroughs.
Write to ~/.cursor/plans/walkthroughs/<branch_name>.plan.md.
In chat, reply with only the absolute path to the file.
Workflow (default: process walkthrough)

Use this workflow unless the user explicitly asks for branch/PR/diff walkthrough.

1) Identify focus and gather context
Read the user request, attachments, and open files.
Identify the focus:
function (for example Foo.bar/2)
module
file
named process ("how does X flow work?")
Get repo root and branch:
git rev-parse --show-toplevel
git branch --show-current
Open relevant full files.
Map full function boundaries so references can link to complete functions.
2) Trace the end-to-end path

Build a path that answers both:

what this focus does locally
how it fits in the bigger picture

Trace in this order:

A sensible entrypoint (or user-specified start)
Routing/dispatch/plugs/callers that lead to the focus
The focus itself
Downstream calls and effects
Successful outcome (response, persistence, side effect, or emitted event)

Include unchanged helpers when they are necessary to understand the chain. Do not skip hops that a new reader would need.

3) Draft the walkthrough document

The output file must use this exact top-level order:

## Executive summary
## Flow
Step-numbered walkthrough sections
Optional ## Non-execution file changes (only for branch change mode)

Do not add meta framing before or after these sections.

Required section rules (process walkthrough)
Executive summary

## Executive summary must be the first heading.

Keep it short and simple. Write a plain-language nutshell explanation of what the relevant process does. Do not turn this section into a checklist or detailed breakdown.

No Reference line in executive summary.

Flow diagrams

## Flow must be the second top-level heading.

Use one Mermaid flowchart TD per discrete process.

Numbering rules
Nodes use labels 1., 2., 3. (with trailing period)
Flow is top-to-bottom
Walkthrough prose sections must match step order exactly
Shape rules
Trapezoid node ([/ ... \]) = context/plumbing/explanatory step
Rectangle node ([ ... ]) = focus step or a step directly needed to explain where the focus fits

Labels should be short and start with step number.

Step sections

After ## Flow, add ## walkthrough sections in diagram order.

Each section must:

Include process name and Step N. in the heading
Start immediately with **Reference:**
Use ### Behavior subsection
Explain top-to-bottom behavior with explicit line numbers
Use we voice consistently
Reference rules

Always write references as Markdown links using [](). Do not wrap references in backticks.

Each reference must point to either:

one full function (def/defp/defmacro, all clauses, correct arity span), or
one whole file

Label format:

function: Module.function/arity
whole file: human filename or module name

Destination format:

function: absolute path with #L<start>-L<end>
whole file: absolute path only (no #L...)

If a section needs multiple references, list them under Reference as concise bullets.

Prose style rules

Under every ### Behavior:

write in execution order
anchor explanations to line numbers (line 17, lines 42-56)
explain branches, data shapes, and key side effects
prefer plain language and connective detail
Audience and tone

Assume the reader is new to the codebase.

On first mention of a framework/layer/folder, give a one-sentence plain-language explanation of what it is for.

Voice should feel like paired coding:

direct
practical
clear
not report-like

Default to we:

we load...
we pattern match...
we call...
we return...
Branch change mode (only when requested)

Use this section only when the user explicitly asks for branch/PR/change walkthrough. Keep the rest of the skill (executive summary, flow order, references, prose style) the same.

Trigger phrases

Examples:

"walk me through this branch"
"walk me through this PR"
"explain what changed"
"review these diffs"
Additional required steps

On top of the default workflow:

Run git diff HEAD.
Classify changed code on the runtime path vs non-execution files.
Optionally resolve Linear issue context.
In summary and steps, explain old-vs-new behavior where code changed.
Section subsection rules in branch mode

For each step section:

If referenced code materially changed in diff, use exactly:
### Changes made
### Old behavior
### New behavior
If referenced code did not materially change, use:
### Behavior

When in doubt and the reference span changed, treat it as changed.

Non-execution file changes in branch mode

If changed files are not on runtime happy path:

add separate Mermaid block(s) under ## Flow with unconnected lettered rectangle nodes (a, b, c, ...)
add final ## Non-execution file changes section with (a), (b), (c) prose in matching order

Skip this entire lettered flow/section for normal process walkthroughs.

Optional Linear workflow (branch mode only)

Use Linear only for branch walkthroughs.

If user provides issue id or URL:

fetch and use it as intent context

If user does not provide one, optional sequence:

Match current branch against issue gitBranchName
Fallback to issue id embedded in branch name
Fallback heuristic match vs diff
If unresolved, continue without ticket

Never block walkthrough on missing Linear.

Router localhost exclusion (branch mode only)

When interpreting git diff HEAD, ignore lib/surge_web/router.ex hunks that only add localhost to host: scope constraints.

Do not treat those as material product behavior changes.

Weekly Installs
23
Repository
jasonharmongit/jh-skills
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn