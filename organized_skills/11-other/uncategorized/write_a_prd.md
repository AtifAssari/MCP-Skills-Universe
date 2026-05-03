---
rating: ⭐⭐
title: write-a-prd
url: https://skills.sh/sones3/skills/write-a-prd
---

# write-a-prd

skills/sones3/skills/write-a-prd
write-a-prd
Installation
$ npx skills add https://github.com/sones3/skills --skill write-a-prd
SKILL.md

This skill will be invoked when the user wants to create a PRD.

Ask the user for a concise but clear description of the problem they want to solve, the outcome they want, who it is for, and any initial ideas for solutions.

Reuse the discussion already present in the current thread.

If the problem, constraints, and key decisions have already been clarified earlier in the conversation, do not repeat the same interview. Only ask follow-up questions for unresolved, ambiguous, or conflicting points.

Explore the repo to verify their assertions and understand the current state of the codebase when relevant.

Use repo findings to answer factual questions yourself instead of asking the user unnecessarily. Call out existing behavior, terminology, and constraints that materially affect the PRD.

Interview the user relentlessly about every aspect of this plan until you reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Make sure the discussion covers the complete feature surface, including:

primary actors and goals
core workflows
permissions and roles
edge cases and failure modes
integrations and external dependencies
rollout or migration constraints
explicit out-of-scope items
Once you have a complete understanding of the problem and solution, use the template below to write the PRD.

The PRD should stay focused on business value, user-facing behavior, scope, constraints, and open questions. Do not turn it into an implementation spec.

The user stories must be exhaustive but not repetitive. They should cover the full surface area of the feature, including normal flows, edge cases, permissions, failure and recovery flows, and lifecycle actions when relevant.

Show the draft PRD to the user and revise it until they approve it.

Do not submit the PRD as a GitHub issue until the user explicitly approves the final draft.

Once the user approves the draft, submit the PRD as a GitHub issue.
Problem Statement

The problem that the user is facing, from the user's perspective.

Goals

A concise list of the primary outcomes this feature should achieve.

Solution

The solution to the problem, from the user's perspective.

User Stories

A LONG, numbered list of user stories. Each user story should be in the format of:

As an <actor>, I want a <feature>, so that <benefit>

This list of user stories should be exhaustive but not repetitive. It should cover all important aspects of the feature, including primary flows, edge cases, permissions and roles, failure and recovery flows, and lifecycle actions when relevant.

Scope

A description of what is included in this PRD.

Constraints

Business, product, platform, compliance, integration, or rollout constraints that affect the feature.

Engineering Notes

Only include product-relevant technical constraints or commitments that materially affect scope or feasibility.

Do NOT include implementation plans, module breakdowns, file paths, code snippets, API shapes, schema details, or test strategy by default.

Out of Scope

A description of the things that are out of scope for this PRD.

Open Questions

Any unresolved questions that remain after discussion.

Further Notes

Any further notes about the feature.

Weekly Installs
11
Repository
sones3/skills
GitHub Stars
3
First Seen
Mar 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass