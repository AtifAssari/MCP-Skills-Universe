---
title: request-refactor-plan
url: https://skills.sh/mattpocock/skills/request-refactor-plan
---

# request-refactor-plan

skills/mattpocock/skills/request-refactor-plan
request-refactor-plan
Installation
$ npx skills add https://github.com/mattpocock/skills --skill request-refactor-plan
Summary

Interview-driven refactoring planner that breaks changes into tiny, safe commits and files a GitHub issue.

Conducts a detailed user interview to understand the problem, explore alternatives, and nail down exact scope before planning
Verifies assertions by exploring the repository and assesses existing test coverage in the affected codebase
Breaks implementation into the smallest possible commits, each leaving the codebase in a working state
Generates a structured GitHub issue with problem statement, solution, detailed commit plan, decision document, testing strategy, and out-of-scope items
SKILL.md

This skill will be invoked when the user wants to create a refactor request. You should go through the steps below. You may skip steps if you don't consider them necessary.

Ask the user for a long, detailed description of the problem they want to solve and any potential ideas for solutions.

Explore the repo to verify their assertions and understand the current state of the codebase.

Ask whether they have considered other options, and present other options to them.

Interview the user about the implementation. Be extremely detailed and thorough.

Hammer out the exact scope of the implementation. Work out what you plan to change and what you plan not to change.

Look in the codebase to check for test coverage of this area of the codebase. If there is insufficient test coverage, ask the user what their plans for testing are.

Break the implementation into a plan of tiny commits. Remember Martin Fowler's advice to "make each refactoring step as small as possible, so that you can always see the program working."

Create a GitHub issue with the refactor plan. Use the following template for the issue description:

Problem Statement

The problem that the developer is facing, from the developer's perspective.

Solution

The solution to the problem, from the developer's perspective.

Commits

A LONG, detailed implementation plan. Write the plan in plain English, breaking down the implementation into the tiniest commits possible. Each commit should leave the codebase in a working state.

Decision Document

A list of implementation decisions that were made. This can include:

The modules that will be built/modified
The interfaces of those modules that will be modified
Technical clarifications from the developer
Architectural decisions
Schema changes
API contracts
Specific interactions

Do NOT include specific file paths or code snippets. They may end up being outdated very quickly.

Testing Decisions

A list of testing decisions that were made. Include:

A description of what makes a good test (only test external behavior, not implementation details)
Which modules will be tested
Prior art for the tests (i.e. similar types of tests in the codebase)
Out of Scope

A description of the things that are out of scope for this refactor.

Further Notes (optional)

Any further notes about the refactor.

Weekly Installs
7.1K
Repository
mattpocock/skills
GitHub Stars
53.2K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass