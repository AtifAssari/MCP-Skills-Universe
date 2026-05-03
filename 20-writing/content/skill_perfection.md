---
title: skill-perfection
url: https://skills.sh/omidzamani/dspy-skills/skill-perfection
---

# skill-perfection

skills/omidzamani/dspy-skills/skill-perfection
skill-perfection
Installation
$ npx skills add https://github.com/omidzamani/dspy-skills --skill skill-perfection
SKILL.md
Skill Perfection

A systematic process for auditing and fixing plugin skills in a single pass.

Core Principle

Audit + Fix in One Pass: When you find an issue, fix it immediately, then continue. This eliminates redundant research and multiple iterations.

Process Overview
[Optional Preflight] → Audit+Fix (single pass) → Verify (spot-check) → Report

Phase 1: Preflight (Optional, Advisory)

A Python-based preflight script is bundled for Python-heavy skills only.

When to Use Preflight
Skill Content	Use Preflight?
Mostly Python code blocks	✅ Yes
Mixed Python + other languages	⚠️ Optional (Python blocks only)
Non-Python (JS, Rust, Go, etc.)	❌ Skip, go to Phase 2
Skill about the preflight script itself	❌ Skip (conflict of interest)
Running Preflight
uv run python ${SKILL_DIR}/scripts/preflight.py <path-to-skill.md> --no-urls

Interpreting Results
Result	Action
✅ PASSED	Good signal. Proceed to Phase 2, trust syntax is valid.
❌ FAILED with clear errors (syntax error at line X)	Fix those specific issues, then proceed to Phase 2.
❌ FAILED with confusing/many errors	Ignore preflight entirely. Proceed to Phase 2, let LLM verify.
Script crashes or hangs	Ignore preflight entirely. Proceed to Phase 2.
Key Rule: Preflight is Advisory

The preflight script is a helper, not a gatekeeper. If it produces confusing output, skip it. The LLM-based Phase 2 is always authoritative.

Signs to ignore preflight:

More than 10 errors on a skill that "looks fine"
Errors that don't make sense (line numbers don't match)
Python tracebacks from the script itself
Timeouts or hanging

When in doubt, skip preflight and let the LLM verify everything.

Phase 2: Audit + Fix (Single Pass) - THE CORE

This is the main phase. Work through the skill file section by section.

2.1 Identify the Technology

From the skill's content, identify:

Primary technology/framework (e.g., LangGraph, React, Axum, Go-kit)
Version constraints if mentioned
Official documentation domain
2.2 Research Strategy

Batch similar lookups to minimize web calls:

Example: For a skill with 10 import statements from the same package,
do ONE search that covers them all, not 10 separate searches.


Documentation priority:

Official docs (use site: filter)
Official GitHub repo (examples, tests, README)
Package registry (PyPI, npm, crates.io, pkg.go.dev)
Official blog/changelog
2.3 For Each Verifiable Item
Item Type	What to Verify
Import/require statement	Package exists, path is current, not deprecated
API call	Signature matches official docs, parameters correct
Code example	Would execute, complete imports, correct syntax
URL/link	Accessible (WebFetch), points to claimed content
Version claim	Current/accurate
Best practice claim	Aligned with official recommendations
2.4 Fix-As-You-Go

When you find an issue:

STOP auditing that section
FIX the issue immediately (Edit tool)
LOG the change in memory: {location, old, new, reason, source_url}
CONTINUE auditing

All severities get fixed in one pass - don't defer anything.

2.5 Syntax Verification (LLM-based)

For code blocks, verify syntax by reading carefully:

Python: Check for matching parentheses, correct indentation, valid syntax JavaScript/TypeScript: Check for matching braces, valid syntax, correct imports
Rust: Check for matching braces, semicolons, valid syntax Go: Check for matching braces, correct package structure Any language: Apply your knowledge of that language's syntax rules

If unsure about syntax validity, note it but don't block on it - focus on semantic correctness against official docs.

Phase 3: Verification (Spot-Check)

After completing Phase 2:

Re-read the modified skill file
Spot-check 3-5 items you fixed (not everything)
Verify URLs you added/modified (WebFetch)

If spot-checks pass → Proceed to Phase 4 If spot-checks fail → Fix those specific items, re-check only those

Do NOT do a full re-audit. You already verified everything in Phase 2.

Phase 4: Generate Report

Create a concise report (<100 lines):

# Skill Perfection Report

**Skill**: {skill-name}
**Date**: {date}  
**Version**: {old} → {new}
**Status**: ✅ PERFECTED | ⚠️ NEEDS REVIEW

## Summary
- Items verified: {N}
- Issues found and fixed: {N}

## Changes Made

### High Priority
| Location | Change | Reason | Source |
|----------|--------|--------|--------|
| line 45 | `old` → `new` | why | [docs](url) |

### Medium/Low Priority
| Location | Change | Reason | Source |
|----------|--------|--------|--------|
| line 12 | `old` → `new` | why | [docs](url) |

## Verification
- [x] All imports verified against official docs
- [x] All API signatures match current documentation
- [x] Code examples are complete and correct
- [x] All URLs accessible

## Sources
1. {url}
2. {url}


Save to: {skill-directory}/PERFECTION_REPORT.md

Efficiency Guidelines
Metric	Target
Web searches	<20 per skill (batch similar items)
Iterations	1 audit+fix pass + 1 spot-check
Report length	<100 lines
Anti-Patterns

❌ Run preflight on non-Python skills ✅ Skip preflight, let LLM verify

❌ Trust confusing preflight output
✅ Ignore preflight when output doesn't make sense

❌ Separate audit pass, then separate update pass ✅ Fix issues as you find them

❌ Full re-audit after fixes ✅ Spot-check only changed items

❌ Research same API multiple times
✅ Batch similar lookups, cache results

Bundled Scripts
scripts/preflight.py

Purpose: Quick syntax check for Python-heavy skills Limitation: Only useful for Python; advisory only

# Use for Python skills
uv run python ${SKILL_DIR}/scripts/preflight.py skill.md --no-urls

# Skip for non-Python skills or if output is confusing


If preflight causes problems, ignore it entirely. The LLM-based audit is always the authoritative verification.

Weekly Installs
18
Repository
omidzamani/dspy-skills
GitHub Stars
74
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn