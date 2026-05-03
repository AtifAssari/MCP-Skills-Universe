---
title: verification-before-completion
url: https://skills.sh/bobmatnyc/claude-mpm-skills/verification-before-completion
---

# verification-before-completion

skills/bobmatnyc/claude-mpm-skills/verification-before-completion
verification-before-completion
Installation
$ npx skills add https://github.com/bobmatnyc/claude-mpm-skills --skill verification-before-completion
SKILL.md
Verification Before Completion
Overview

Claiming work is complete without verification is dishonesty, not efficiency.

Core principle: Evidence before claims, always.

Violating the letter of this rule is violating the spirit of this rule.

This skill enforces mandatory verification before ANY completion claim, preventing false positives, broken builds, and trust violations.

When to Use This Skill

Activate ALWAYS before claiming:

Success, completion, or satisfaction ("Done!", "Fixed!", "Great!")
Tests pass, linter clean, build succeeds
Committing, pushing, creating PRs
Marking tasks complete or delegating to agents

Use this ESPECIALLY when:

Under time pressure or tired
"Quick fix" seems obvious or confidence is high
Agent reports success or tests "should" pass
The Iron Law
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE


Without running the verification command in this message, claiming success is not allowed.

Core Principles
Evidence Required: Every claim needs supporting evidence
Fresh Verification: Must verify now, not rely on previous runs
Complete Verification: Full command, not partial checks
Honest Reporting: Report actual state, not hoped-for state
Quick Start

The five-step gate function:

IDENTIFY: What command proves this claim?
RUN: Execute the FULL command (fresh, complete)
READ: Full output, check exit code, count failures
VERIFY: Does output confirm the claim?
If NO: State actual status with evidence
If YES: State claim WITH evidence
ONLY THEN: Make the claim

Skip any step = lying, not verifying.

Key Patterns

Correct Pattern:

✅ [Run pytest] [Output: 34/34 passed] "All tests pass"


Incorrect Patterns:

❌ "Should pass now"
❌ "Looks correct"
❌ "Tests were passing"
❌ "I'm confident it works"

Red Flags - STOP Immediately

STOP when:

Using "should", "probably", "seems to"
Expressing satisfaction before verification
About to commit/push/PR without verification
Trusting agent success reports
Relying on partial verification

ALL of these mean: STOP. Run verification first.

Why This Matters

Statistics from real-world failures:

Verification cost: 2 minutes
Recovery cost: 120+ minutes (60x more expensive)
40% of unverified "complete" claims required rework

Core violation: "Lying leads to replacement"

Navigation

For detailed information:

Gate Function: Complete five-step verification process with decision trees
Verification Patterns: Correct verification patterns for tests, builds, deployments, and more
Red Flags and Failures: Common failure modes, red flags, and real-world examples with time/cost data
Integration and Workflows: Integration with other skills, CI/CD patterns, and agent delegation workflows
The Bottom Line

No shortcuts for verification.

Run the command. Read the output. THEN claim the result.

This is non-negotiable.

Weekly Installs
167
Repository
bobmatnyc/claud…m-skills
GitHub Stars
40
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass