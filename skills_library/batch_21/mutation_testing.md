---
title: mutation-testing
url: https://skills.sh/aj-geddes/useful-ai-prompts/mutation-testing
---

# mutation-testing

skills/aj-geddes/useful-ai-prompts/mutation-testing
mutation-testing
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill mutation-testing
SKILL.md
Mutation Testing
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Mutation testing assesses test suite quality by introducing small changes (mutations) to source code and verifying that tests fail. If tests don't catch a mutation, it indicates gaps in test coverage or test quality. This technique helps identify weak or ineffective tests.

When to Use
Evaluating test suite effectiveness
Finding untested code paths
Improving test quality metrics
Validating critical business logic is well-tested
Identifying redundant or weak tests
Measuring real test coverage beyond line coverage
Ensuring tests actually verify behavior
Quick Start

Minimal working example:

# Install Stryker
npm install --save-dev @stryker-mutator/core @stryker-mutator/jest-runner

# Initialize configuration
npx stryker init

# Run mutation testing
npx stryker run

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Stryker for JavaScript/TypeScript	Stryker for JavaScript/TypeScript
PITest for Java	PITest for Java
mutmut for Python	mutmut for Python
Mutation Testing Reports	Mutation Testing Reports
Best Practices
✅ DO
Target critical business logic for mutation testing
Aim for 80%+ mutation score on important code
Review survived mutants to improve tests
Mark equivalent mutants to exclude them
Use mutation testing in CI for critical modules
Test boundary conditions thoroughly
Verify actual behavior, not just code execution
❌ DON'T
Expect 100% mutation score everywhere
Run mutation testing on all code (too slow)
Ignore equivalent mutants
Test getters/setters with mutations
Run mutations on generated code
Skip mutation testing on complex logic
Focus only on line coverage
Weekly Installs
285
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass