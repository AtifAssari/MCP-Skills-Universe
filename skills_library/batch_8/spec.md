---
title: spec
url: https://skills.sh/juliusbrussee/cavekit/spec
---

# spec

skills/juliusbrussee/cavekit/spec
spec
Installation
$ npx skills add https://github.com/juliusbrussee/cavekit --skill spec
SKILL.md
spec — spec mutator

Read FORMAT.md at repo root if not already loaded. Caveman skill applies to all writes here.

DISPATCH

Inspect user request and project state:

No SPEC.md at repo root AND args describe idea → NEW
No SPEC.md AND from-code in args → DISTILL
SPEC.md exists AND args start bug: → BACKPROP
SPEC.md exists AND args start amend → AMEND
SPEC.md exists, no args → ask user which mode
NEW — idea → spec

Input: user idea.

Steps:

Extract goal (1 line, caveman). → §G.
List constraints user stated or implied. → §C.
List external surfaces user named. → §I.
Propose initial invariants. → §V (numbered V1…).
Break goal into ordered tasks. → §T pipe table, all status ., ids T1…
§B section with header row only (id|date|cause|fix).

Write to SPEC.md. Show user full file. Ask: "spec OK? suggest edits or invoke build."

DISTILL — code → spec

Walk repo. Produce §G (infer from README/package.json/main entry), §C (infer from stack), §I (enumerate public APIs/CLIs/configs), §V (derive from tests and assertions), §T (one task per known TODO or missing test), §B (empty).

Caveman everywhere. Flag uncertain items with ? in text so user can confirm.

BACKPROP — bug → §B + §V

Input: bug: <description>.

Steps:

Parse bug description.
Find root cause (read relevant code).
Decide: would a new invariant catch recurrence? If yes → draft V<next>.
Append §B row: B<next>|<date>|<cause>|V<N>.
Append new invariant to §V.
If fix also changes behavior → add/update §T rows.
Show diff. Apply only on user OK.

Rule: every bug gets a §B entry. Invariant optional but preferred.

AMEND — targeted edit

Input: amend §V.3 or amend §T etc.

Read that section. Show current. Ask user what changes. Write. Show diff.

Never silently rewrite sections user did not name.

OUTPUT RULES
Caveman format per FORMAT.md.
Preserve identifiers, paths, code verbatim.
Numbering monotonic — never reuse §V.N or §B.N.
§T row cites column ! list §V/§I deps: T5|.|impl auth mw|V2,I.api.
NON-GOALS
No sub-agents. Main thread writes.
No dashboards, no logs, no state files beyond SPEC.md itself.
No auto-build after spec. User invokes build explicitly.
Weekly Installs
590
Repository
juliusbrussee/cavekit
GitHub Stars
815
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail