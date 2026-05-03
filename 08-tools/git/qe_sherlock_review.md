---
title: qe-sherlock-review
url: https://skills.sh/proffesor-for-testing/agentic-qe/qe-sherlock-review
---

# qe-sherlock-review

skills/proffesor-for-testing/agentic-qe/qe-sherlock-review
qe-sherlock-review
Installation
$ npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill qe-sherlock-review
SKILL.md
Sherlock Review

<default_to_action> When investigating code claims:

OBSERVE: Gather all evidence (code, tests, history, behavior)
DEDUCE: What does evidence actually show vs. what was claimed?
ELIMINATE: Rule out what cannot be true
CONCLUDE: Does evidence support the claim?
DOCUMENT: Findings with proof, not assumptions

The 3-Step Investigation:

# 1. OBSERVE: Gather evidence
git diff <commit>
npm test -- --coverage

# 2. DEDUCE: Compare claim vs reality
# Does code match description?
# Do tests prove the fix/feature?

# 3. CONCLUDE: Verdict with evidence
# SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED


Holmesian Principles:

"Data! Data! Data!" - Collect before concluding
"Eliminate the impossible" - What cannot be true?
"You see, but do not observe" - Run code, don't just read
Trust only reproducible evidence </default_to_action>
Quick Reference Card
Evidence Collection Checklist
Category	What to Check	How
Claim	PR description, commit messages	Read thoroughly
Code	Actual file changes	git diff
Tests	Coverage, assertions	Run independently
Behavior	Runtime output	Execute locally
Timeline	When things happened	git log, git blame
Verdict Levels
Verdict	Meaning
✓ TRUE	Evidence fully supports claim
⚠ PARTIALLY TRUE	Claim accurate but incomplete
✗ FALSE	Evidence contradicts claim
? NONSENSICAL	Claim doesn't apply to context
Investigation Template
## Sherlock Investigation: [Claim]

### The Claim
"[What PR/commit claims to do]"

### Evidence Examined
- Code changes: [files, lines]
- Tests added: [count, coverage]
- Behavior observed: [what actually happens]

### Deductive Analysis

**Claim**: [specific assertion]
**Evidence**: [what you found]
**Deduction**: [logical conclusion]
**Verdict**: ✓/⚠/✗

### Findings
- What works: [with evidence]
- What doesn't: [with evidence]
- What's missing: [gaps in implementation/testing]

### Recommendations
1. [Action based on findings]

Investigation Scenarios
Scenario 1: "This Fixed the Bug"

Steps:

Reproduce bug on commit before fix
Verify bug is gone on commit with fix
Check if fix addresses root cause or symptom
Test edge cases not in original report

Red Flags:

Fix that just removes error logging
Works only for specific test case
Workarounds instead of root cause fix
No regression test added
Scenario 2: "Improved Performance by 50%"

Steps:

Run benchmark on baseline commit
Run same benchmark on optimized commit
Compare in identical conditions
Verify measurement methodology

Red Flags:

Tested only on toy data
Different comparison conditions
Trade-offs not mentioned
Scenario 3: "Handles All Edge Cases"

Steps:

List all edge cases in code path
Check each has test coverage
Test boundary conditions
Verify error handling paths

Red Flags:

catch {} swallowing errors
Generic error messages
No logging of critical errors
Example Investigation
## Case: PR #123 "Fix race condition in async handler"

### Claims Examined:
1. "Eliminates race condition"
2. "Adds mutex locking"
3. "100% thread safe"

### Evidence:
- File: src/handlers/async-handler.js
- Changes: Added `async/await`, removed callbacks
- Tests: 2 new tests for async flow
- Coverage: 85% (was 75%)

### Analysis:

**Claim 1: "Eliminates race condition"**
Evidence: Added `await` to sequential operations. No actual mutex.
Deduction: Race avoided by removing concurrency, not synchronization.
Verdict: ⚠ PARTIALLY TRUE (solved differently than claimed)

**Claim 2: "Adds mutex locking"**
Evidence: No mutex library, no lock variables, no sync primitives.
Verdict: ✗ FALSE

**Claim 3: "100% thread safe"**
Evidence: JavaScript is single-threaded. No worker threads used.
Verdict: ? NONSENSICAL (meaningless in this context)

### Conclusion:
Fix works but not for reasons claimed. Race condition avoided by
making operations sequential, not by adding synchronization.

### Recommendations:
1. Update PR description to accurately reflect solution
2. Add test for concurrent request handling
3. Remove incorrect technical claims

Agent Integration
// Evidence-based code review
await Task("Sherlock Review", {
  prNumber: 123,
  claims: [
    "Fixes memory leak",
    "Improves performance 30%"
  ],
  verifyReproduction: true,
  testEdgeCases: true
}, "qe-code-reviewer");

// Bug fix verification
await Task("Verify Fix", {
  bugCommit: 'abc123',
  fixCommit: 'def456',
  reproductionSteps: steps,
  testBoundaryConditions: true
}, "qe-code-reviewer");

Agent Coordination Hints
Memory Namespace
aqe/sherlock/
├── investigations/*   - Investigation reports
├── evidence/*         - Collected evidence
├── verdicts/*         - Claim verdicts
└── patterns/*         - Common deception patterns

Fleet Coordination
const investigationFleet = await FleetManager.coordinate({
  strategy: 'evidence-investigation',
  agents: [
    'qe-code-reviewer',        // Code analysis
    'qe-security-auditor',     // Security claim verification
    'qe-performance-validator' // Performance claim verification
  ],
  topology: 'parallel'
});

Related Skills
brutal-honesty-review - Direct technical criticism
context-driven-testing - Adapt to context
bug-reporting-excellence - Document findings
Remember

"It is a capital mistake to theorize before one has data." Trust only reproducible evidence. Don't trust commit messages, documentation, or "works on my machine."

The Sherlock Standard: Every claim must be verified empirically. What does the evidence actually show?

Weekly Installs
44
Repository
proffesor-for-t…entic-qe
GitHub Stars
334
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass