---
rating: ⭐⭐
title: explanatory-playground
url: https://skills.sh/petekp/claude-code-setup/explanatory-playground
---

# explanatory-playground

skills/petekp/claude-code-setup/explanatory-playground
explanatory-playground
Installation
$ npx skills add https://github.com/petekp/claude-code-setup --skill explanatory-playground
SKILL.md
Explanatory Playground

Build an explainer that teaches a real system, not just a debug widget.

Pair two layers whenever possible:

a reader-facing narrative that explains the system in human order
an interactive artifact that proves the explanation with source links, runtime traces, or live controls

If the user already has a finished study guide markdown and just wants a polished presentation, use interactive-study-guide instead. If the user only needs a narrow debug panel with no broader teaching goal, transparent-ui may be enough.

Failure Modes To Prevent
Pretty diagrams that are not anchored to real code or behavior
Exhaustive file tours that follow repository order instead of conceptual order
Runtime instrumentation with no explanatory story
Prose that sounds confident but is not backed by code, tests, or traces
Monolithic playgrounds that try to teach the entire codebase at once
Core Principles

Narrative owns the order. Borrow the key idea from literate programming: present the system in the order that helps a human understand it, not the order files happen to exist on disk.

Evidence beats vibes. Every major claim in the artifact should be grounded in one or more of: exact source locations, a trace/log, a test, a typed contract, or a controlled experiment inside the playground.

Show the stable concepts first. Start with actors, boundaries, invariants, and the happy path before diving into edge cases or implementation detail.

Make the reader do small experiments. Good understanding comes from changing an input, replaying a transition, or stepping through a failure path.

Prefer one subsystem at a time. If the request sounds codebase-wide, identify the workflow or subsystem that best answers the user's question and teach that first.

Default Deliverable

Unless the user explicitly wants chat-only output, aim to ship a paired artifact:

Narrative spine - a concise explainer doc or page section that answers the reader's core questions in order
Interactive playground - panels, controls, timelines, or diagrams tied to the actual system
Source index - links to the authority files, tests, entrypoints, and probes used to support the explanation

Follow the blueprint in references/guide-blueprint.md. Apply the literate-programming rules in references/literate-programming.md. Use references/patterns.md only for the system patterns that actually fit. When runtime evidence matters, normalize it with references/trace-adapters.md.

If the repo does not already have an explanatory package, bootstrap one with:

python3 scripts/scaffold.py <repo-root> "<topic>" --shape docs


Use --shape hybrid when a Next.js-style dev route is appropriate. The scaffold creates the narrative control plane first so the later UI work has a grounded structure.

Workflow
1. Calibrate the teaching target

Before building anything, pin down:

the subsystem or workflow to explain
who the artifact is for: newcomer, adjacent engineer, or debugger
the questions the artifact must answer
the boundary: whole system, request path, data pipeline, state container, render loop, and so on

A good framing prompt is:

"After ten minutes with this artifact, what should the reader be able to explain or modify confidently?"
2. Build an evidence ledger

Read just enough of the codebase to ground the explanation:

entrypoints
key tests
architecture docs or ADRs if present
recent churn or TODO/FIXME hints when relevant
the source files that actually own state, orchestration, and side effects

Extract:

main actors and nouns
inputs and outputs
state and transitions
invariants or promised behaviors
ordering and timing concerns
failure paths
exact file anchors worth linking from the artifact

Do not start designing visuals until you know what the system is actually doing.

3. Design the narrative spine

Organize the artifact around a small number of reader questions. Use the section templates in references/guide-blueprint.md.

A strong default sequence is:

Why this subsystem exists
The key actors and boundaries
The happy-path walkthrough
State, invariants, and source of truth
Timing, branching, or failure behavior
Hands-on probes the reader can run
Where to read next in the real code

Do not mirror the folder tree unless the folder tree itself is the concept being taught.

4. Apply literate-programming discipline

For each section:

lead with the concept or question
show only the code excerpt needed for that concept
explain why that excerpt matters before enumerating implementation detail
link back to the full source
keep prose and interactive controls adjacent so the reader can test the claim immediately

Use named chunks, short excerpts, and explicit cross-references. The reader should feel guided, not dumped into raw source.

5. Choose the artifact shape

Pick the lightest structure that can teach the idea well:

Embedded dev route: best when the real app context matters and live state is useful
Standalone explainer page/app: best when the teaching artifact needs more editorial freedom
Hybrid doc + playground: best for multi-session onboarding or architecture-heavy topics

If the repo has no convention, a reasonable default is:

docs/explanatory/<topic>/
app/__dev/<topic>/page.tsx
src/devtools/<topic>/*


Adapt to the project's actual layout instead of forcing this shape.

When starting from zero, run the scaffold after choosing the shape:

python3 scripts/scaffold.py <repo-root> "<topic>" --shape docs
python3 scripts/scaffold.py <repo-root> "<topic>" --shape hybrid


docs is framework-neutral and creates:

guide.md
source-index.md
chunk-manifest.md
reader-lab.md

hybrid additionally creates a Next.js-style app/__dev/<topic>/page.tsx, a shared explainer model in src/devtools/<topic>/artifact.ts, and a normalized trace layer in src/devtools/<topic>/trace.ts.

Use references/chunk-manifest.md to keep the narrative units crisp while you fill in the scaffold.

6. Instrument minimally and honestly

Prefer the least invasive evidence source that answers the reader's question:

existing tests, fixtures, and logs
dev-only wrappers or observers
event emitters or trace buffers
controlled test inputs and replay tools

When adding instrumentation:

keep it dev-only
capture timestamps and causal metadata
store enough history to replay important transitions
label speculative vs observed behavior clearly

If you scaffolded a hybrid artifact, make trace.ts the single normalization layer for runtime evidence. Adapt emitters, store transitions, request lifecycles, or wrapper probes into that shape before building panel-specific views.

7. Build panels that answer specific questions

Every panel needs a job. Good panel prompts:

"What state are we in right now?"
"What just happened, and why?"
"Which module owns this decision?"
"What changed between step A and step B?"
"What fails if this invariant breaks?"
"Which files should I open next?"

Include only the panels that earn their place. Use the shared affordances and domain patterns in references/patterns.md.

8. Add reader experiments

A great explanatory playground lets the reader verify understanding. Add a few targeted probes:

trigger the happy path
pause and scrub through history
inject a malformed input or edge case
compare before/after snapshots
toggle a guard, feature flag, or branch condition
reveal which invariant was preserved or violated

Favor a few high-signal scenarios over a kitchen-sink control surface.

9. Verify the artifact as a teaching tool

Before finishing, check whether a fresh reader could answer:

What is this subsystem for?
What is the main execution path?
Where does state live?
What must remain true?
Where do timing or branching issues show up?
Which files are the authority?
What would I change first if behavior X were wrong?

If the answer is no, simplify and sharpen the artifact until it teaches.

Output Quality Bar

A strong result usually has:

a clear narrative spine with stable section headings
interactive panels tied to actual code or traces
file links or source anchors for every major concept
one or more "try this" reader experiments
explicit invariants and failure modes
a path from overview to real implementation details
Cleanup And Promotion

If the artifact is temporary:

keep it behind a dev-only route or flag
add a clear removal note at the top of created files
summarize what to delete when the user is done

If the artifact will remain useful for onboarding:

promote the narrative into repo docs or a durable explainer page
keep the interactive portion lightweight enough that it does not rot faster than the system it teaches
Weekly Installs
18
Repository
petekp/claude-code-setup
GitHub Stars
35
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass