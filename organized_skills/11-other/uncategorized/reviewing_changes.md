---
rating: ⭐⭐
title: reviewing-changes
url: https://skills.sh/bitwarden/android/reviewing-changes
---

# reviewing-changes

skills/bitwarden/android/reviewing-changes
reviewing-changes
Installation
$ npx skills add https://github.com/bitwarden/android --skill reviewing-changes
SKILL.md
Reviewing Changes - Android Additions

This skill provides Android-specific workflow additions that complement the base bitwarden-code-reviewer agent standards.

Instructions

IMPORTANT: Work systematically through each step before providing feedback. Each checklist file includes structured thinking guidance for its review passes.

Step 1: Retrieve Additional Details

Retrieve any additional information linked to the pull request using available tools (JIRA MCP, GitHub API).

If pull request title and message do not provide enough context, request additional details from the reviewer:

Link a JIRA ticket
Associate a GitHub issue
Link to another pull request
Add more detail to the PR title or body

Android metadata checks — flag as ❓ if any of these are missing:

PR includes *Screen.kt or Composable changes but has no screenshots
PR adds new ViewModel or Repository but has no test plan or test file changes
Step 2: Detect Change Type with Android Refinements

Use the base change type detection from the agent, with Android-specific refinements:

Android-specific patterns:

Feature Addition: New ViewModel, new Repository, new @Composable functions, new *Screen.kt files
UI Refinement: Changes only in *Screen.kt, *Composable.kt, ui/ package files
Infrastructure: Changes to .github/workflows/, gradle/, build.gradle.kts, libs.versions.toml
Dependency Update: Changes only to libs.versions.toml or build.gradle.kts with version bumps
Step 3: Load Appropriate Checklist

Based on detected type, read the relevant checklist file:

Dependency Update → checklists/dependency-update.md (expedited review)
Bug Fix → checklists/bug-fix.md (focused review)
Feature Addition → checklists/feature-addition.md (comprehensive review)
UI Refinement → checklists/ui-refinement.md (design-focused review)
Refactoring → checklists/refactoring.md (pattern-focused review)
Infrastructure → checklists/infrastructure.md (tooling-focused review)

The checklist provides:

Multi-pass review strategy
Type-specific focus areas
What to check and what to skip
Structured thinking guidance
Step 4: Execute Review Following Checklist

Follow the checklist's multi-pass strategy, thinking through each pass systematically.

Step 5: Consult Android Reference Materials As Needed

Load reference files only when needed for specific questions:

Re-reviews → invoke reviewing-incremental-changes agent skill; scope to changed lines only, do not flag new issues in unchanged code
Issue prioritization → reference/priority-framework.md (Critical vs Suggested vs Optional)
Phrasing feedback → reference/review-psychology.md (questions vs commands, I-statements)
Architecture questions → reference/architectural-patterns.md (MVVM, Hilt DI, module org, error handling)
Security questions (quick reference) → reference/security-patterns.md (common patterns and anti-patterns)
Security questions (comprehensive) → docs/ARCHITECTURE.md#security (full zero-knowledge architecture)
Testing questions → reference/testing-patterns.md (unit tests, mocking, null safety)
UI questions → reference/ui-patterns.md (Compose patterns, theming)
Style questions (project-specific) → reference/style-patterns.md (Kotlin rules enforced in review)
Style questions (general) → docs/STYLE_AND_BEST_PRACTICES.md
Core Principles
Priority order: Security → Correctness → Breaking Changes → Performance → Maintainability
Appropriate depth: Match review rigor to change complexity and risk
Specific references: Always use file:line_number format for precise location
Actionable feedback: Say what to do and why, not just what's wrong
Efficient reviews: Use multi-pass strategy, skip what's not relevant
Android patterns: Validate MVVM, Hilt DI, Compose conventions, Kotlin idioms
Weekly Installs
79
Repository
bitwarden/android
GitHub Stars
8.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn