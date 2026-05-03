---
rating: ⭐⭐
title: to-prd
url: https://skills.sh/mattpocock/skills/to-prd
---

# to-prd

skills/mattpocock/skills/to-prd
to-prd
Installation
$ npx skills add https://github.com/mattpocock/skills --skill to-prd
SKILL.md

This skill takes the current conversation context and codebase understanding and produces a PRD. Do NOT interview the user — just synthesize what you already know.

The issue tracker and triage label vocabulary should have been provided to you — run /setup-matt-pocock-skills if not.

Process

Explore the repo to understand the current state of the codebase, if you haven't already. Use the project's domain glossary vocabulary throughout the PRD, and respect any ADRs in the area you're touching.

Sketch out the major modules you will need to build or modify to complete the implementation. Actively look for opportunities to extract deep modules that can be tested in isolation.

A deep module (as opposed to a shallow module) is one which encapsulates a lot of functionality in a simple, testable interface which rarely changes.

Check with the user that these modules match their expectations. Check with the user which modules they want tests written for.

Write the PRD using the template below, then publish it to the project issue tracker. Apply the needs-triage triage label so it enters the normal triage flow.
Problem Statement

The problem that the user is facing, from the user's perspective.

Solution

The solution to the problem, from the user's perspective.

User Stories

A LONG, numbered list of user stories. Each user story should be in the format of:

As an , I want a , so that

This list of user stories should be extremely extensive and cover all aspects of the feature.

Implementation Decisions

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

A description of the things that are out of scope for this PRD.

Further Notes

Any further notes about the feature.

Weekly Installs
27.9K
Repository
mattpocock/skills
GitHub Stars
53.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass