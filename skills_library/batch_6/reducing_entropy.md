---
title: reducing-entropy
url: https://skills.sh/softaworks/agent-toolkit/reducing-entropy
---

# reducing-entropy

skills/softaworks/agent-toolkit/reducing-entropy
reducing-entropy
Installation
$ npx skills add https://github.com/softaworks/agent-toolkit --skill reducing-entropy
Summary

Minimize total codebase size by systematically identifying and removing unnecessary code.

Focuses on final code amount, not effort or churn; a 50-line addition that deletes 200 lines is a win
Requires loading a reference mindset from the skill's philosophy directory before proceeding
Applies three core questions: what's the smallest codebase that solves this, does the change reduce total code, and what can be deleted as a result
Flags common traps like status quo bias, premature flexibility, and over-engineering for separation of concerns
SKILL.md
Reducing Entropy

More code begets more code. Entropy accumulates. This skill biases toward the smallest possible codebase.

Core question: "What does the codebase look like after?"

Before You Begin

Load at least one mindset from references/

List the files in the reference directory
Read frontmatter descriptions to pick which applies
Load at least one
State which you loaded and its core principle

Do not proceed until you've done this.

The Goal

The goal is less total code in the final codebase - not less code to write right now.

Writing 50 lines that delete 200 lines = net win
Keeping 14 functions to avoid writing 2 = net loss
"No churn" is not a goal. Less code is the goal.

Measure the end state, not the effort.

Three Questions
1. What's the smallest codebase that solves this?

Not "what's the smallest change" - what's the smallest result.

Could this be 2 functions instead of 14?
Could this be 0 functions (delete the feature)?
What would we delete if we did this?
2. Does the proposed change result in less total code?

Count lines before and after. If after > before, reject it.

"Better organized" but more code = more entropy
"More flexible" but more code = more entropy
"Cleaner separation" but more code = more entropy
3. What can we delete?

Every change is an opportunity to delete. Ask:

What does this make obsolete?
What was only needed because of what we're replacing?
What's the maximum we could remove?
Red Flags
"Keep what exists" - Status quo bias. The question is total code, not churn.
"This adds flexibility" - Flexibility for what? YAGNI.
"Better separation of concerns" - More files/functions = more code. Separation isn't free.
"Type safety" - Worth how many lines? Sometimes runtime checks in less code wins.
"Easier to understand" - 14 things are not easier than 2 things.
When This Doesn't Apply
The codebase is already minimal for what it does
You're in a framework with strong conventions (don't fight it)
Regulatory/compliance requirements mandate certain structures
Reference Mindsets

See references/ for philosophical grounding.

To add new mindsets, see adding-reference-mindsets.md.

Bias toward deletion. Measure the end state.

Weekly Installs
3.6K
Repository
softaworks/agent-toolkit
GitHub Stars
1.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass