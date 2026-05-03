---
title: rebuttal-writing
url: https://skills.sh/lingzhi227/agent-research-skills/rebuttal-writing
---

# rebuttal-writing

skills/lingzhi227/agent-research-skills/rebuttal-writing
rebuttal-writing
Installation
$ npx skills add https://github.com/lingzhi227/agent-research-skills --skill rebuttal-writing
SKILL.md
Rebuttal Writing

Generate structured, evidence-based rebuttals to peer review comments.

Input
$0 — Reviewer comments (text file, or pasted directly)
Optional: current paper draft for reference
References
Rebuttal prompts and format templates: ~/.claude/skills/rebuttal-writing/references/rebuttal-prompts.md
Workflow
Step 1: Parse Review Comments

For each reviewer:

Extract individual concerns/questions/weaknesses
Categorize each: major concern, minor concern, question, suggestion
Identify the core issue behind each concern
Step 2: Generate Responses

For each concern:

Acknowledge the reviewer's point
Respond with evidence — cite specific sections, equations, experiments, or results from the paper
Describe what was done (not what will be done) — "We have added...", "Our experiments show..."
If additional experiments are needed, describe the new results concretely
Step 3: Format Rebuttal

Use the standard rebuttal format:

# Response to Reviewers

We thank all reviewers for their constructive feedback. We address each concern below.

## Reviewer #1

**Concern #1:** [extracted concern]
**Author Response:** [detailed response with evidence]

**Concern #2:** [extracted concern]
**Author Response:** [detailed response with evidence]

## Reviewer #2
...

Step 4: Summary of Changes

Add a brief summary at the top listing all major changes made to the paper:

New experiments added
Sections revised
Clarifications made
Rules
Reply with what was done, not what will be done — "We have conducted additional experiments" not "We will conduct..."
Be specific — Reference exact sections, table numbers, equation numbers
Be respectful — Thank reviewers, acknowledge valid concerns
Address every concern — Do not skip any reviewer point
Provide evidence — Every response should include concrete data, citations, or reasoning
Keep responses concise — Detailed enough to address the concern, but not padded
Highlight changes — When referring to modified text, use blue text or clearly mark revisions
Related Skills
Upstream: self-review, paper-revision
Downstream: paper-compilation
See also: data-analysis
Weekly Installs
141
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