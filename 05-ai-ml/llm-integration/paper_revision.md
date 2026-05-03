---
rating: ⭐⭐
title: paper-revision
url: https://skills.sh/lingzhi227/agent-research-skills/paper-revision
---

# paper-revision

skills/lingzhi227/agent-research-skills/paper-revision
paper-revision
Installation
$ npx skills add https://github.com/lingzhi227/agent-research-skills --skill paper-revision
SKILL.md
Paper Revision

Systematically revise papers based on reviewer feedback.

Input
$0 — Reviewer comments/feedback
$1 — Current paper draft (main.tex or paper directory)
References
Revision workflow and prompts: ~/.claude/skills/paper-revision/references/revision-prompts.md
Workflow
Step 1: Parse and Prioritize Concerns

For each reviewer comment:

Extract the specific concern
Classify: major revision, minor revision, question, suggestion
Map to affected paper section(s)
Prioritize: address major concerns first
Step 2: Plan Revisions

Create a revision plan:

Concern → Affected Section → Required Action → New Content/Experiment


Categories of actions:

Clarification: Rewrite text for clarity
Additional experiment: Run new experiment, add results
New analysis: Add ablation, statistical test, or comparison
Structural change: Move, merge, or split sections
Citation: Add missing references
Step 3: Execute Revisions

For each planned revision:

Read the current section
Apply targeted edits (preserve surrounding structure)
If new experiments needed: use experiment-code skill
If new figures/tables needed: use figure-generation / table-generation skills
Mark changes (use \textcolor{blue}{...} for revised text)
Step 4: Verify Improvements
Re-run self-review skill to check if scores improved
Verify all reviewer concerns are addressed
Check that revisions don't introduce new issues
Ensure page count still fits venue requirements
Step 5: Write Revision Summary

Generate a diff summary:

List all changes made with section references
Note any new experiments, figures, or tables added
Cross-reference each change to the reviewer concern it addresses
Rules
Address EVERY reviewer concern — do not skip any
Preserve paper structure unless structural change is explicitly needed
New results must come from actual experiments, not hallucinated
Mark all revised text clearly for the reviewers
Keep a copy of the previous version before revising
Compare new scores vs previous scores after revision
Related Skills
Upstream: self-review
Downstream: paper-compilation
See also: rebuttal-writing, paper-writing-section
Weekly Installs
159
Repository
lingzhi227/agen…h-skills
GitHub Stars
42
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass