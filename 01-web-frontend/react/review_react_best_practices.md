---
rating: ⭐⭐
title: review-react-best-practices
url: https://skills.sh/heyvhuang/ship-faster/review-react-best-practices
---

# review-react-best-practices

skills/heyvhuang/ship-faster/review-react-best-practices
review-react-best-practices
Installation
$ npx skills add https://github.com/heyvhuang/ship-faster --skill review-react-best-practices
SKILL.md
React Best Practices Review (Performance-First)

Use this skill to turn “React feels slow / Next.js page is heavy / too many requests” into a repeatable, prioritized review.

This skill is intentionally built like a rule library:

SKILL.md: how to review + how to search rules
references/rules/*: one rule per file (taggable, sortable, easy to evolve)
When to apply

Use when:

Building or refactoring React components
Working in Next.js (App Router) on RSC boundaries, Server Actions, data fetching
Reviewing PRs for performance regressions
Bundle size increases / slow HMR / cold start issues
UI jank / unnecessary re-renders / hydration issues
Review method (prioritized)
Start with CRITICAL rules first (waterfalls + bundle).
Only then go to HIGH (server patterns + serialization).
Then MEDIUM (re-render + rendering).
Then LOW-MEDIUM micro-optimizations (JS hot paths).

Section ordering lives in: references/rules/_sections.md

How to use the rules efficiently
Search by keyword
rg -n "waterfall|Promise\\.all|defer await" references/rules
rg -n "barrel|optimizePackageImports|dynamic" references/rules
rg -n "cache\\(|React\\.cache|serialization|RSC" references/rules
rg -n "memo\\(|useMemo|useCallback|dependencies" references/rules

Search by tag

Each rule has tags: in YAML frontmatter.

rg -n "tags:.*bundle" references/rules
rg -n "tags:.*rerender" references/rules

Output format (recommended)

When reviewing code, output:

Summary (1 paragraph)
Critical fixes (must-fix, biggest wins)
High impact (should-fix)
Medium / Low (nice-to-have)

For each issue include:

Rule name (and file under references/rules/)
Location (path:line)
Why it matters (latency / bundle / CPU / UX)
Minimal fix direction (prefer small diffs)

If running in a Ship Faster run directory, persist the report to:

run_dir/evidence/react-best-practices-review.md
Rule library

Rules live in:

references/rules/
Rule template: references/rules/_template.md
Weekly Installs
51
Repository
heyvhuang/ship-faster
GitHub Stars
338
First Seen
Feb 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass