---
title: explain-like
url: https://skills.sh/arjenschwarz/agentic-coding/explain-like
---

# explain-like

skills/arjenschwarz/agentic-coding/explain-like
explain-like
Installation
$ npx skills add https://github.com/arjenschwarz/agentic-coding --skill explain-like
SKILL.md
Explain Like

Explain code changes or design documents at three progressive expertise levels to ensure understanding and catch logical gaps.

When to Use
PR/Branch Explanations: After completing work, explain changes to verify clarity
Design Validation: After writing a design doc, explain it back to catch missing pieces

Both workflows serve knowledge transfer - helping others (or your future self) understand complex changes.

Workflow

Determine the subject:

Branch/PR changes? → Gather commits and diffs from git
Design document? → Read the specified design file

Generate three explanations (all three, always):

Beginner (0-2 years): Foundational concepts, analogies, "what" and "why"
Intermediate (5-10 years): Implementation details, patterns, trade-offs
Expert (10+ years): Architecture implications, edge cases, future considerations

For design validation: After explaining, list any gaps or inconsistencies discovered

Optionally save output to file for documentation (see "Saving Output" below)

Explanation Structure

For each level, follow this format:

## Beginner Level

### What Changed / What This Does
[Plain language summary - assume no domain knowledge]

### Why It Matters
[Business or user impact in simple terms]

### Key Concepts
[Define any technical terms used, with analogies where helpful]

---

## Intermediate Level

### Changes Overview
[Technical summary with specific files/components affected]

### Implementation Approach
[Patterns used, architectural decisions, how pieces fit together]

### Trade-offs
[What alternatives existed, why this approach was chosen]

---

## Expert Level

### Technical Deep Dive
[Detailed implementation, edge cases handled, performance considerations]

### Architecture Impact
[How this affects the broader system, coupling, future extensibility]

### Potential Issues
[Edge cases, failure modes, things to monitor]

For Branch/PR Changes

Gather context first:

# Detect default branch (main, master, etc.)
BASE=$(git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@^refs/remotes/origin/@@' || echo "main")

# Get commit history
git log --oneline $BASE..HEAD

# Get full diff
git diff $BASE...HEAD

# If PR exists, get PR description
gh pr view --json title,body,commits


Focus explanations on:

What problem is being solved
How the solution works
Why this approach over alternatives
For Design Validation

After generating the three explanations, add a validation section:

## Validation Findings

### Gaps Identified
[List any missing requirements, undefined behaviors, or unclear sections]

### Logic Issues
[Contradictions, circular dependencies, impossible states]

### Questions Raised
[Things that became unclear when explaining at different levels]

### Recommendations
[Specific improvements to the design document]


The act of explaining at beginner level often reveals assumed knowledge that should be documented. Expert-level explanation reveals edge cases and integration concerns.

Saving Output

When the user requests saving (or as part of a final review), write the explanation to a file:

For design docs: Save alongside the design in the same specs folder as explanation.md
For branch/PR changes: Save to specs/<feature-name>/explanation.md if a matching spec exists, otherwise offer to create one

Ask before saving if the user hasn't explicitly requested it.

Tone Guidelines
Beginner: Patient, uses analogies, avoids jargon or defines it immediately
Intermediate: Professional, assumes familiarity with common patterns
Expert: Concise, focuses on non-obvious implications and edge cases
Weekly Installs
17
Repository
arjenschwarz/ag…c-coding
GitHub Stars
18
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass