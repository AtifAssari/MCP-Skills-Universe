---
rating: ⭐⭐⭐⭐⭐
title: write-guide
url: https://skills.sh/vercel/next.js/write-guide
---

# write-guide

skills/vercel/next.js/write-guide
write-guide
Installation
$ npx skills add https://github.com/vercel/next.js --skill write-guide
SKILL.md
Writing Guides
Goal

Produce a technical guide that teaches a real-world use case through progressive examples. Concepts are introduced only when the reader needs them.

Each guide solves one specific problem. Not a category of problems. If the outline has 5+ steps or covers multiple approaches, split it.

Structure

Every guide follows this arc: introduction, example setup, 2-5 progressive steps, next steps.

Each step follows this loop: working code → new requirement → friction → explanation → resolution → observable proof.

Sections: introduction (no heading, 2 paragraphs max), ## Example (what we're building + source link), ### Step N (action-oriented titles, 2-4 steps), ## Next steps (summary + related links).

Headings should tell a story on their own. If readers only saw the headings, they'd understand the guide's takeaway.

Template
---
title: {Action-oriented, e.g., "Building X" or "How to Y"}
description: {One sentence}
nav_title: {Short title for navigation}
---

{What the reader will accomplish and why it matters. The friction and how this approach resolves it. 2 paragraphs max.}

## Example

As an example, we'll build {what we're building}.

We'll start with {step 1}, then {step 2}, and {step 3}.

{Source code link.}

### Step 1: {Action-oriented title}

{Brief context, 1-2 sentences.}

```tsx filename="path/to/file.tsx"
// Minimal working code
```

{Explain what happens.}

{Introduce friction: warning, limitation, or constraint.}

{Resolution: explain the choice, apply the fix.}

{Verify the fix with observable proof.}

### Step 2: {Action-oriented title}

{Same pattern: context → code → explain → friction → resolution → proof.}

### Step 3: {Action-oriented title}

{Same pattern.}

## Next steps

You now know how to {summary}.

Next, learn how to:

- [Related guide 1]()
- [Related guide 2]()

Workflow
Research: Check available skills for relevant features. Read existing docs for context and linking opportunities.
Plan: Outline sections. Verify scope (one problem, 2-4 steps). Each step needs a friction point and resolution.
Write: Follow the template above. Apply the rules below.
Review: Re-read the rules, verify, then present.
Rules
Progressive disclosure. Start with the smallest working example. Introduce complexity only when the example breaks. Name concepts at the moment of resolution, after the reader has felt the problem. Full loop: working → new requirement → something breaks → explain why → name the fix → apply → verify with proof → move on.
Show problems visually. Console errors, terminal output, build warnings, slow-loading pages. "If we refresh the page, we can see the component blocks the response."
Verify resolutions with observable proof. Before/after comparisons, browser reloads, terminal output. "If we refresh the page again, we can see it loads instantly."
One friction point per step. If a step has multiple friction points, split it.
Minimal code blocks. Only the code needed for the current step. Collapse unchanged functions with function Header() {}.
No em dashes. Use periods, commas, or parentheses instead.
Mechanical, observable language. Describe what happens, not how it feels.
No selling, justifying, or comparing. No "the best way," no historical context, no framework comparisons.
Don't	Do
"creates friction in the pipeline"	"blocks the response"
"needs dynamic information"	"depends on request-time data"
"requires dynamic processing"	"output can't be known ahead of time"
"The component blocks the response — causing delays"	"The component blocks the response. This causes delays."
References

Read these guides in docs/01-app/02-guides/ before writing. They demonstrate the patterns above.

public-static-pages.mdx — intro → example → 3 progressive steps → next steps. Concepts named at point of resolution. Problems shown with build output.
forms.mdx — progressive feature building without explicit "Step" labels. Each section adds one capability.
Weekly Installs
579
Repository
vercel/next.js
GitHub Stars
139.3K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass