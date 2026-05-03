---
title: check
url: https://skills.sh/juliusbrussee/cavekit/check
---

# check

skills/juliusbrussee/cavekit/check
check
Installation
$ npx skills add https://github.com/juliusbrussee/cavekit --skill check
SKILL.md
check — drift report

Pure diagnostic. Reports violations. Writes nothing. User decides remedy.

LOAD
Read SPEC.md. If missing → "no spec, nothing to check." Stop.
Parse invocation args:
§V → check invariants only (default)
§I → check interfaces
§T → audit task status vs code
--all → all three
CHECK §V — invariants

For each V:

Translate invariant into verifiable claim about code.
Grep / read relevant files.
Classify: HOLD / VIOLATE / UNVERIFIABLE.
Record address + file:line evidence.
CHECK §I — interfaces

For each I item:

Locate implementation.
Classify:
MATCH — shape in code = shape in spec.
DRIFT — impl exists, shape differs.
MISSING — impl absent.
EXTRA — code exposes surface not in §I.
CHECK §T — tasks

For each T:

If x: verify claimed work present.
If ~: note as in-progress.
If .: note as pending.
Flag x rows with no evidence as STALE.
REPORT

Caveman. Grouped by severity.

## §V drift
V2 VIOLATE: auth/mw.go:47 uses `<` not `≤`. see §B.1.
V5 UNVERIFIABLE: no test covers ∀ req path.

## §I drift
I.api DRIFT: POST /x returns `{result}` not `{id}`. route.go:112.
I.cmd MISSING: `foo bar` absent from cli/*.go.

## §T drift
T3 STALE: status `x`, no middleware file exists.

## summary
2 violate. 1 missing. 1 stale. 1 unverifiable.
next: spec skill with `bug:` or fix code at cited lines.

REMEDY HINTS (not actions)

End report with one-line hint per class:

VIOLATE / DRIFT → invoke spec skill bug: <V.n> or fix code.
MISSING → invoke build skill on §T.n if task exists; else spec skill amend §T.
STALE → spec skill amend §T to uncheck.
EXTRA → spec skill amend §I to document, or delete code.

Never invoke fixes. Report only.

NON-GOALS
Zero writes. No SPEC.md edits. No code edits.
No sub-agents. Main thread reads.
No scores, no grades. Binary per item: holds or drifts.
Weekly Installs
592
Repository
juliusbrussee/cavekit
GitHub Stars
815
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass