---
rating: ⭐⭐
title: code-review
url: https://skills.sh/mrgoonie/claudekit-skills/code-review
---

# code-review

skills/mrgoonie/claudekit-skills/code-review
code-review
Installation
$ npx skills add https://github.com/mrgoonie/claudekit-skills --skill code-review
Summary

Technical rigor in code review: receiving feedback critically, requesting systematic reviews, and verifying before any completion claims.

Three core practices: receiving feedback with technical evaluation over performative agreement, requesting reviews via code-reviewer subagent, and verification gates requiring evidence before status claims
Includes decision tree and protocols for handling feedback from human partners versus external reviewers, with explicit rules against performative responses
Verification gates require running fresh commands and reading output before claiming tests pass, builds succeed, or work is complete
Designed for subagent-driven development workflows, pull requests, and preventing false completion claims through evidence-based verification
SKILL.md
Code Review

Guide proper code review practices emphasizing technical rigor, evidence-based claims, and verification over performative responses.

Overview

Code review requires three distinct practices:

Receiving feedback - Technical evaluation over performative agreement
Requesting reviews - Systematic review via code-reviewer subagent
Verification gates - Evidence before any completion claims

Each practice has specific triggers and protocols detailed in reference files.

Core Principle

Technical correctness over social comfort. Verify before implementing. Ask before assuming. Evidence before claims.

When to Use This Skill
Receiving Feedback

Trigger when:

Receiving code review comments from any source
Feedback seems unclear or technically questionable
Multiple review items need prioritization
External reviewer lacks full context
Suggestion conflicts with existing decisions

Reference: references/code-review-reception.md

Requesting Review

Trigger when:

Completing tasks in subagent-driven development (after EACH task)
Finishing major features or refactors
Before merging to main branch
Stuck and need fresh perspective
After fixing complex bugs

Reference: references/requesting-code-review.md

Verification Gates

Trigger when:

About to claim tests pass, build succeeds, or work is complete
Before committing, pushing, or creating PRs
Moving to next task
Any statement suggesting success/completion
Expressing satisfaction with work

Reference: references/verification-before-completion.md

Quick Decision Tree
SITUATION?
│
├─ Received feedback
│  ├─ Unclear items? → STOP, ask for clarification first
│  ├─ From human partner? → Understand, then implement
│  └─ From external reviewer? → Verify technically before implementing
│
├─ Completed work
│  ├─ Major feature/task? → Request code-reviewer subagent review
│  └─ Before merge? → Request code-reviewer subagent review
│
└─ About to claim status
   ├─ Have fresh verification? → State claim WITH evidence
   └─ No fresh verification? → RUN verification command first

Receiving Feedback Protocol
Response Pattern

READ → UNDERSTAND → VERIFY → EVALUATE → RESPOND → IMPLEMENT

Key Rules
❌ No performative agreement: "You're absolutely right!", "Great point!", "Thanks for [anything]"
❌ No implementation before verification
✅ Restate requirement, ask questions, push back with technical reasoning, or just start working
✅ If unclear: STOP and ask for clarification on ALL unclear items first
✅ YAGNI check: grep for usage before implementing suggested "proper" features
Source Handling
Human partner: Trusted - implement after understanding, no performative agreement
External reviewers: Verify technically correct, check for breakage, push back if wrong

Full protocol: references/code-review-reception.md

Requesting Review Protocol
When to Request
After each task in subagent-driven development
After major feature completion
Before merge to main
Process
Get git SHAs: BASE_SHA=$(git rev-parse HEAD~1) and HEAD_SHA=$(git rev-parse HEAD)
Dispatch code-reviewer subagent via Task tool with: WHAT_WAS_IMPLEMENTED, PLAN_OR_REQUIREMENTS, BASE_SHA, HEAD_SHA, DESCRIPTION
Act on feedback: Fix Critical immediately, Important before proceeding, note Minor for later

Full protocol: references/requesting-code-review.md

Verification Gates Protocol
The Iron Law

NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE

Gate Function

IDENTIFY command → RUN full command → READ output → VERIFY confirms claim → THEN claim

Skip any step = lying, not verifying

Requirements
Tests pass: Test output shows 0 failures
Build succeeds: Build command exit 0
Bug fixed: Test original symptom passes
Requirements met: Line-by-line checklist verified
Red Flags - STOP

Using "should"/"probably"/"seems to", expressing satisfaction before verification, committing without verification, trusting agent reports, ANY wording implying success without running verification

Full protocol: references/verification-before-completion.md

Integration with Workflows
Subagent-Driven: Review after EACH task, verify before moving to next
Pull Requests: Verify tests pass, request code-reviewer review before merge
General: Apply verification gates before any status claims, push back on invalid feedback
Bottom Line
Technical rigor over social performance - No performative agreement
Systematic review processes - Use code-reviewer subagent
Evidence before claims - Verification gates always

Verify. Question. Then implement. Evidence. Then claim.

Weekly Installs
366
Repository
mrgoonie/claude…t-skills
GitHub Stars
2.0K
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass