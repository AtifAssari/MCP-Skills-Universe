---
rating: ⭐⭐
title: review-merge-readiness
url: https://skills.sh/heyvhuang/ship-faster/review-merge-readiness
---

# review-merge-readiness

skills/heyvhuang/ship-faster/review-merge-readiness
review-merge-readiness
Installation
$ npx skills add https://github.com/heyvhuang/ship-faster --skill review-merge-readiness
SKILL.md
Requesting Code Review (Structured Review: Requirements Alignment + Production Readiness)

Goal: Make code review a repeatable process, not random comments.

Core principle: Review early, review often.

When Review is Required

Mandatory:

After completing important features
After each batch in workflow-execute-plans ends (default 3 tasks per batch)
Before merging to main branch

Optional but valuable:

When stuck (get a fresh perspective)
Before major refactoring (establish baseline first)
After fixing complex bugs (verify no new regressions)
How to Initiate (Minimum Information Set)
1) Determine Review Scope (git SHA)

Prefer using "baseline before plan/task started" as BASE_SHA:

# Common approach: use main as baseline
BASE_SHA=$(git merge-base HEAD main 2>/dev/null || git merge-base HEAD master)
HEAD_SHA=$(git rev-parse HEAD)


If you want to review just the most recent commit within a small task:

BASE_SHA=$(git rev-parse HEAD~1)
HEAD_SHA=$(git rev-parse HEAD)

2) Prepare Review Basis (Plan / Requirements)

Review must provide:

WHAT_WAS_IMPLEMENTED: What you just completed (1-3 bullet points)
PLAN_OR_REQUIREMENTS: Corresponding plan excerpt or requirements document path (e.g., run_dir/03-plans/feature-plan.md)
3) Get diff (Evidence)
git diff --stat "$BASE_SHA..$HEAD_SHA"
git diff "$BASE_SHA..$HEAD_SHA"

Review Execution Methods (Choose One)
Method A: Sub-Agent Review (if your system supports it)

Use template: review-merge-readiness/code-reviewer.md, fill in placeholders and execute.

Method B: Self Review (works without sub-agent)

Check each item per template checklist and output same structured result (Strengths + Issues by severity + Verdict).

Review Output Format (Must Be Structured)

Output must include:

Strengths: Specific positives (at least 1)
Issues: Categorized by severity:
Critical (Must Fix): Security/data loss/functionality bugs/would cause production incidents
Important (Should Fix): Obviously poor architecture/missing error handling/test gaps/requirements misalignment
Minor (Nice to Have): Style/small optimizations/documentation polish
Assessment: Merge readiness (Yes/No/With fixes) + 1-2 sentence technical reasoning

Each Issue must include:

Location: file:line
What's wrong
Why it matters
How to fix (provide minimal change suggestion)
Relationship with Other Review Skills
review-clean-code: More focused on "maintainability/cleanliness", suitable for deep code smell investigation
review-react-best-practices: More focused on React/Next.js performance patterns (waterfalls/bundle/re-renders). Use when the diff touches React UI, data fetching, or performance-sensitive areas.
This skill: More focused on "requirements alignment/production readiness/merge verdict" conclusion-oriented review

If you just need a "can we merge?" verdict: use this skill. If you want a deep health check: additionally invoke review-clean-code.

Weekly Installs
48
Repository
heyvhuang/ship-faster
GitHub Stars
338
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass