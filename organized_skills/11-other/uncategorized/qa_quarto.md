---
rating: ⭐⭐
title: qa-quarto
url: https://skills.sh/pedrohcgs/claude-code-my-workflow/qa-quarto
---

# qa-quarto

skills/pedrohcgs/claude-code-my-workflow/qa-quarto
qa-quarto
Installation
$ npx skills add https://github.com/pedrohcgs/claude-code-my-workflow --skill qa-quarto
SKILL.md
Adversarial Quarto vs Beamer QA Workflow

Compare Quarto HTML slides against their Beamer PDF benchmark using an iterative critic/fixer loop.

Philosophy: The Beamer PDF is the gold standard. The Quarto translation must be at least as good in every dimension.

Workflow
Phase 0: Pre-flight → Phase 1: Critic audit → Phase 2: Fixer → Phase 3: Re-audit → Loop until APPROVED (max 5 rounds)

Hard Gates (Non-Negotiable)
Gate	Condition
Overflow	NO content cut off
Plot Quality	Interactive charts >= static plots
Content Parity	No missing slides/equations/text
Visual Regression	Quarto >= Beamer in all dimensions
Slide Centering	Content centered, no jumping
Notation Fidelity	All math verbatim from Beamer
Phase 0: Pre-flight
Locate Beamer (.tex/.pdf) and Quarto (.qmd/.html) files
Check freshness (re-render if QMD newer than HTML)
Verify TikZ SVGs if applicable
Phase 1: Initial Audit

Launch the quarto-critic agent to compare Beamer vs Quarto comprehensively. Report saved to quality_reports/[Lecture]_qa_critic_round1.md.

Phase 2: Fix Cycle

If not APPROVED, launch quarto-fixer agent to apply fixes (Critical → Major → Minor), re-render, and verify.

Phase 3: Re-Audit

Re-launch critic to verify fixes. Loop back to Phase 2 if needed.

Iteration Limits

Max 5 fix rounds. After that, escalate to user with remaining issues.

Final Report

Save to quality_reports/[Lecture]_qa_final.md with hard gate status, iteration summary, and remaining issues.

Weekly Installs
16
Repository
pedrohcgs/claud…workflow
GitHub Stars
1.0K
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass