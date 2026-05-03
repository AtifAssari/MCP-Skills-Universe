---
rating: ⭐⭐
title: thai-interpreter
url: https://skills.sh/nxdus/thai-interpreter/thai-interpreter
---

# thai-interpreter

skills/nxdus/thai-interpreter/thai-interpreter
thai-interpreter
Installation
$ npx skills add https://github.com/nxdus/thai-interpreter --skill thai-interpreter
SKILL.md
Thai Interpreter

Interpret Thai user intent with two explicit modes while preserving meaning.

Use this mode selector first:

Literal Translation:
Translate Thai to natural English with high fidelity.
Preserve tone, nuance, and intent.
Do not compress unless requested.
Execution Translation:
Translate Thai to compact, execution-ready English.
Optimize for fewer tokens and direct agent action.
Keep wording concise; do not force a fixed response template.

Default to Execution Translation unless the user asks for direct/literal translation.

Use this workflow:

Extract user intent from Thai text.
Select translation mode based on user instruction.
Preserve key Thai domain terms, names, and literals exactly.
Produce English output in the chosen mode.
Validate any file write path for UTF-8 safety before finalizing.
Prompt Compression Rules

Apply these rules for Execution Translation:

Convert long Thai narrative into concise, actionable instructions.
Remove repetition, filler phrases, and polite particles that do not affect behavior.
Preserve non-negotiable requirements exactly as written.
Keep dates, numbers, IDs, file paths, and code literals unchanged.
Keep the compressed instruction under 8 lines when possible.
Literal Translation Rules

Apply these rules for Literal Translation:

Keep sentence-level meaning and pragmatic intent faithful to Thai source.
Preserve ambiguity if the original Thai is ambiguous.
Preserve names, domain terms, and quoted literals exactly.
Do not add implementation assumptions unless requested.
Keep formatting close to the source when practical.
Thai Text Safety Rules

Always protect Thai text writes:

Use UTF-8 explicitly when creating or updating files.
Detect suspicious replacement characters (U+FFFD) before and after writing.
If corruption appears, stop and rewrite from clean source text.
Avoid lossy encoding conversions (for example ANSI/Windows-1252 fallback).
Re-open written files and verify expected Thai snippets.

For deep checks and command recipes, read:

references/encoding-playbook.md
references/translation-rules.md

For automated checks and safe writes, use:

scripts/check-thai-encoding.ps1
scripts/write-utf8.ps1
Output Contract

When handling Thai requests, produce:

English translation in the selected mode.
Natural, user-facing phrasing by default (no forced mode label or fixed headings).
Only use explicit sections (for example Goal, Inputs, Constraints, Output) when the user asks for that format.
The implementation result (if execution is requested).
A brief encoding safety confirmation when files were changed.
Weekly Installs
39
Repository
nxdus/thai-interpreter
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass