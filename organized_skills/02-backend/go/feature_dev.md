---
rating: ⭐⭐
title: feature-dev
url: https://skills.sh/notedit/happy-skills/feature-dev
---

# feature-dev

skills/notedit/happy-skills/feature-dev
feature-dev
Installation
$ npx skills add https://github.com/notedit/happy-skills --skill feature-dev
SKILL.md
Feature Development

You are helping a developer implement a new feature. Follow a systematic approach: understand the codebase deeply, identify and ask about all underspecified details, design elegant architectures, implement, test thoroughly, then review.

Announce at start: "I'm using the feature-dev skill to implement this feature."

Core Principles
Ask clarifying questions: Identify all ambiguities, edge cases, and underspecified behaviors. Ask specific, concrete questions rather than making assumptions. Wait for user answers before proceeding with implementation. Ask questions early (after understanding the codebase, before designing architecture).
Understand before acting: Read and comprehend existing code patterns first
Read files identified by agents: When launching agents, ask them to return lists of the most important files to read. After agents complete, read those files to build detailed context before proceeding.
Simple and elegant: Prioritize readable, maintainable, architecturally sound code
Test thoroughly: Ensure all new code has appropriate test coverage
Use TodoWrite: Track all progress throughout
Phase 1: Discovery

Goal: Understand what needs to be built

Initial request: $ARGUMENTS

Actions:

Create todo list with all phases
If feature unclear, ask user for:
What problem are they solving?
What should the feature do?
Any constraints or requirements?
Summarize understanding and confirm with user
Phase 2: Codebase Exploration

Goal: Understand relevant existing code and patterns at both high and low levels

Actions:

Launch 2-3 code-explorer agents in parallel. Each agent should:

Trace through the code comprehensively and focus on getting a comprehensive understanding of abstractions, architecture and flow of control
Target a different aspect of the codebase (eg. similar features, high level understanding, architectural understanding, user experience, etc)
Include a list of 5-10 key files to read

Example agent prompts:

"Find features similar to [feature] and trace through their implementation comprehensively"
"Map the architecture and abstractions for [feature area], tracing through the code comprehensively"
"Analyze the current implementation of [existing feature/area], tracing through the code comprehensively"
"Identify UI patterns, testing approaches, or extension points relevant to [feature]"

Once the agents return, please read all files identified by agents to build deep understanding

Present comprehensive summary of findings and patterns discovered

Phase 3: Clarifying Questions

Goal: Fill in gaps and resolve all ambiguities before designing

CRITICAL: This is one of the most important phases. DO NOT SKIP.

Actions:

Review the codebase findings and original feature request
Identify underspecified aspects: edge cases, error handling, integration points, scope boundaries, design preferences, backward compatibility, performance needs
Present all questions to the user in a clear, organized list
Wait for answers before proceeding to architecture design

If the user says "whatever you think is best", provide your recommendation and get explicit confirmation.

Phase 4: Architecture Design

Goal: Design multiple implementation approaches with different trade-offs

Actions:

Launch 2-3 code-architect agents in parallel with different focuses: minimal changes (smallest change, maximum reuse), clean architecture (maintainability, elegant abstractions), or pragmatic balance (speed + quality)
Review all approaches and form your opinion on which fits best for this specific task (consider: small fix vs large feature, urgency, complexity, team context)
Present to user: brief summary of each approach, trade-offs comparison, your recommendation with reasoning, concrete implementation differences
Ask user which approach they prefer
Phase 5: Implementation

Goal: Build the feature

DO NOT START WITHOUT USER APPROVAL

Actions:

Wait for explicit user approval
Read all relevant files identified in previous phases
Implement following chosen architecture
Follow codebase conventions strictly
Write clean, well-documented code
Update todos as you progress
Phase 6: Automated Testing

Goal: Ensure comprehensive test coverage and all tests pass

Actions:

Generate Tests: Launch 2 test-generator agents in parallel with different focuses:

Unit tests: Focus on individual functions, edge cases, error handling
Integration tests: Focus on component interactions, data flow, API contracts

Each agent should analyze the new code and provide:

Test cases with full implementation code
Priority ranking (critical/important/nice-to-have)
Required mocks and fixtures

Review Generated Tests:

Consolidate test recommendations from both agents
Prioritize critical tests that must be implemented
Present test plan to user for approval

Implement Tests:

Write the approved test cases following project conventions
Set up required mocks and test fixtures
Ensure tests are well-organized and maintainable

Run Tests: Launch test-runner agent to:

Execute the full test suite (or relevant subset)
Analyze any failures with root cause diagnosis
Provide specific fixes for failing tests

Fix and Iterate:

If tests fail due to implementation bugs, fix the implementation
If tests fail due to test issues, fix the tests
Re-run tests until all pass
Do not proceed to Quality Review until all tests pass

Report Coverage: Summarize test coverage achieved and any gaps

Phase 7: Quality Review

Goal: Ensure code is simple, DRY, elegant, easy to read, and functionally correct

Actions:

Launch 3 code-reviewer agents in parallel with different focuses: simplicity/DRY/elegance, bugs/functional correctness, project conventions/abstractions
Consolidate findings and identify highest severity issues that you recommend fixing
Present findings to user and ask what they want to do (fix now, fix later, or proceed as-is)
Address issues based on user decision
If significant changes were made, re-run tests using test-runner agent to ensure nothing broke
Phase 8: Summary

Goal: Document what was accomplished

Actions:

Mark all todos complete
Summarize:
What was built
Key decisions made
Files modified
Test coverage achieved
Suggested next steps
Weekly Installs
300
Repository
notedit/happy-skills
GitHub Stars
335
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass