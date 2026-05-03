---
title: retro
url: https://skills.sh/codewithjv/agent-skills/retro
---

# retro

skills/codewithjv/agent-skills/retro
retro
Installation
$ npx skills add https://github.com/codewithjv/agent-skills --skill retro
SKILL.md
Retro

Run a retrospective on the work that just happened.

This skill is for understanding:

what went wrong
what took too long
what wasted tokens or effort
what dead ends appeared
what actually worked well
what should change next time

The goal is not just to list mistakes.

The goal is to find the underlying causes and propose changes that improve future performance.

When to Use

Activate this skill when the user asks to:

do a retro
review what went wrong
figure out why a task took too long
find inefficiencies or wasted effort
understand repeated failure patterns
improve the workflow for next time
Inputs to Review

Look across the full context that shaped the outcome:

the chat history
the user's instructions
the skills used
the repo or task context
the tool behavior
the sequence of decisions taken

If relevant, also look at:

error outputs
retries
abandoned approaches
unclear handoffs
changes in user intent during the task
Interaction Mode

Do not assume every retro should be one-shot.

Use judgment:

If the failure pattern is already clear from context, produce the retro directly.
If the causes are ambiguous, contested, emotional, or likely to benefit from richer operator insight, engage the user with a short iterative retro first.

In iterative mode:

ask a small number of focused questions
use the answers to refine the root-cause analysis
then produce the final retro

Good questions are about:

what the user noticed that the agent missed
which failure mattered most
whether the problem was skill, prompt, tool, workflow, or judgment
what durable fix the user wants to see in the system

Do not ask broad or redundant questions just to prolong the retro. Ask only when it will materially improve the resulting persistent changes.

What to Look For
1. Errors and mistakes

Find:

wrong assumptions
incorrect tool use
missed instructions
factual or process errors
2. Inefficiencies

Find:

wasted token-heavy exploration
duplicated work
unnecessary retries
avoidable browsing or searching
places where a simple tool or script would have been better
3. Dead ends

Find:

lines of investigation that did not help
loops caused by unclear context
repeated attempts that should have been abandoned earlier
4. What worked well

Protect the good parts.

Find:

useful framing from the user
effective skills
strong workflow steps
fast paths that worked
good heuristics that should be preserved

Do not propose changes that accidentally break those strengths.

Root Cause Analysis

Do not stop at the surface symptom.

For each meaningful problem, ask:

What happened?
Why did it happen?
What allowed it to happen?
What is the deeper pattern underneath it?

Root causes often come from:

unclear user request framing
missing or weak skill instructions
bad skill boundaries
missing shared vocabulary
poor repo/context visibility
no lightweight tool for a repeated task
bad workflow sequencing
no checkpoint or review gate

Prefer a small number of real causes over a long list of shallow complaints.

If using iterative mode, test your draft causes against the user's answers before finalizing them.

Output

Produce a retrospective with these sections:

Retro Summary
What the task was
Whether it went well overall
The biggest issues
The biggest strengths
What Went Wrong
Concrete failures, mistakes, delays, or dead ends
Root Causes
The underlying causes behind the issues
Separate symptoms from causes
What Worked Well
The good patterns worth preserving
Why they worked
Recommended Changes

Suggest concrete improvements for next time.

These must be practical, durable changes rather than reminders to "be more careful" or "do better."

NEVER save retro learnings to memory. The only valid output artifacts are:

Skills - update an existing skill or create a new one (SKILL.md files)
Formulas - update an existing formula or create a new one (.formula.toml files)
Docs - markdown files committed to the repo (runbooks, checklists, reference docs)

Memory is not a valid destination for retro outcomes. If a learning isn't worth encoding into a skill, formula, or repo doc, it isn't worth persisting.

Valid changes include:

updating an existing skill's instructions or checklist
creating a new skill
updating a formula's steps
creating a new formula
adding a checklist or runbook as a markdown file in the repo
creating a CLI script committed to the repo
adding a review gate to a skill or formula
changing workflow sequencing in a skill or formula

For each suggestion, explain:

what should change
why it would help
whether it is high leverage or optional
what artifact should be updated (skill, formula, or repo doc)
the exact file path where the change should be made
Highest-Leverage Next Step

End with the single most valuable change to make first.

This must be one concrete change to a skill, formula, or repo doc, such as:

update a specific skill's SKILL.md
add a step or checklist to a formula
create a helper script in the repo
add a review or validation gate to a skill or formula
write or update a runbook/checklist markdown file in the repo

Do not end with vague advice like:

"be more careful"
"check more often"
"communicate better"
"do better next time"

The chosen next step must be a change to a skill, formula, or repo doc. Never memory.

If you used iterative mode, the output should reflect what changed after questioning the user rather than ignoring their added signal.

Good Behavior
Be honest but not noisy
Focus on future improvement, not blame
Preserve what already works
Prefer structural fixes over one-off hacks
Be specific enough that the human could actually implement the suggestion
All recommendations must result in changes to skills, formulas, or repo docs — never memory
When the user's observations can materially improve the retro, engage them briefly before finalizing
Weekly Installs
30
Repository
codewithjv/agent-skills
GitHub Stars
1
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass