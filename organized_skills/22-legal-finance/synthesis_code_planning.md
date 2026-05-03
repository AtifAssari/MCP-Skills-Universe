---
rating: ⭐⭐
title: synthesis-code-planning
url: https://skills.sh/rajivpant/synthesis-skills/synthesis-code-planning
---

# synthesis-code-planning

skills/rajivpant/synthesis-skills/synthesis-code-planning
synthesis-code-planning
Installation
$ npx skills add https://github.com/rajivpant/synthesis-skills --skill synthesis-code-planning
SKILL.md
Code Planning

A structured methodology for approaching code tasks that produces higher-quality implementations by evaluating multiple approaches before committing to one.

Inputs

Before generating code, gather three inputs:

Task description -- what needs to be built or changed
Existing code -- the current codebase or relevant files (if any)
Contextual documentation -- relevant API docs, framework guides, coding standards, or architectural decisions
Process
Step 1: Analyze

Carefully analyze the task description and existing code. Consider:

What is the actual goal (not just the literal request)?
What constraints does the existing code impose?
What are the performance, maintainability, and correctness requirements?
What best practices apply to this language, framework, or domain?
Step 2: Generate approaches

Produce at least two distinct approaches to address the task. For each approach, document:

Approach 1: [Brief description]

Pros:
[Advantage 1]
[Advantage 2]
Cons:
[Drawback 1]
[Drawback 2]

Approach 2: [Brief description]

Pros:
[Advantage 1]
[Advantage 2]
Cons:
[Drawback 1]
[Drawback 2]

Generate more approaches when the problem space is ambiguous or when the first two approaches have significant trade-offs against each other.

Step 3: Evaluate and select

Select the optimal solution and justify the choice with specific reasoning:

Reference the pros and cons of each approach
Explain why the chosen approach best addresses the task requirements
Acknowledge what is sacrificed by not choosing the alternatives
If the decision is close, state that explicitly
Step 4: Implement

Implement the chosen solution by modifying or creating code:

Mark changes clearly when modifying existing code
Follow the conventions and patterns already present in the codebase
Optimize for performance, maintainability, and adherence to best practices
Include necessary error handling and edge case coverage
When to skip multi-approach evaluation

For trivial changes (typo fixes, single-line config changes, renaming a variable), skip Steps 2-3 and implement directly. The threshold: if the implementation is obvious and unambiguous, proceed without generating alternatives.

Principles
Framework-first: prefer built-in features over custom solutions
Convention over configuration: follow established patterns in the codebase
Root cause over symptom: fix the underlying problem, not its surface manifestation
Less code is better: a one-line config change beats 50 lines of custom code
Weekly Installs
13
Repository
rajivpant/synth…s-skills
GitHub Stars
3
First Seen
Mar 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass