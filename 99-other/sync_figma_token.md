---
title: sync-figma-token
url: https://skills.sh/firebenders/sync-figma-token-skill/sync-figma-token
---

# sync-figma-token

skills/firebenders/sync-figma-token-skill/sync-figma-token
sync-figma-token
Installation
$ npx skills add https://github.com/firebenders/sync-figma-token-skill --skill sync-figma-token
SKILL.md
sync-figma-token

Use this skill for token parity workflows (code tokens vs Figma variables).

MANDATORY prerequisite: load figma-use before every use_figma call.

Non-negotiable safety rule

After producing dry-run output, you MUST STOP and ask for approval.

Do NOT run any write use_figma calls in the same turn as dry-run output.
Ask a normal confirmation question (example: "Apply these changes? (yes/no)").
Only proceed on explicit affirmative approval.
If the response is unclear or negative, do not apply writes.
Standard source formats (required)

Prefer real token sources in this order:

Design Tokens JSON (tokens.json, tokens/*.json, DTCG-style)
Style Dictionary input JSON
Platform theme sources (Compose/Kotlin/TS) only when JSON source is unavailable

If source format is non-standard, explicitly state assumptions in dry-run output.

Required policies before writes
direction: code_to_figma (default), figma_to_code, bidirectional
deletePolicy: default archive_only (NOT delete)
conflictPolicy: prefer_code, prefer_figma, manual_review
namingPolicy: token key normalization strategy
modePolicy: code mode <-> Figma mode mapping

Never delete by default. Deletion requires explicit user instruction.

Normalization rules

Normalize both sides to canonical rows:

key (canonical token name)
type (COLOR, FLOAT, STRING, BOOLEAN)
modeValues (light/dark/etc.)
aliasTarget
scopes
codeSyntax

Name normalization examples:

color.bg.primary <-> color/bg/primary
Neutral10 <-> Neutral/10 only if explicitly mapped by naming policy
Value validation (required)

Dry-run must validate values, not only presence/type.

COLOR: compare RGBA with tolerance epsilon = 0.0001
FLOAT: strict numeric comparison unless tolerance is configured
STRING/BOOLEAN: strict equality
Aliases: compare canonical alias targets
Drift categories

Each drift item must include one of:

missing_in_figma
missing_in_code
value_mismatch
alias_mismatch
type_mismatch
mode_mismatch
scope_mismatch
code_syntax_mismatch
broken_alias
Dry-run output format

Always return:

Headline summary:
{
  "create": 0,
  "update": 0,
  "aliasFix": 0,
  "scopeFix": 0,
  "syntaxFix": 0,
  "archive": 0,
  "delete": 0
}

Detailed drift list with token keys and before/after values.

Then ask:

Dry-run complete. Apply these changes? (yes/no)

Report persistence (required)

Persist report JSON every run:

/tmp/sync-figma-token-dry-run-{runId}.json
/tmp/sync-figma-token-final-{runId}.json

If file persistence fails, mention that explicitly in output.

Conflict handling

When conflicting data is found (type/mode/alias ambiguity):

If conflictPolicy=manual_review, list conflicts and STOP.
If conflictPolicy=prefer_code, update Figma to source values/types.
If conflictPolicy=prefer_figma, keep Figma and emit drift as informational.
Apply order

Apply deltas in this order:

Ensure collections/modes
Create missing primitives
Create/update semantic aliases
Apply value updates
Apply scopes and code syntax
Archive stale tokens per deletePolicy

Never parallelize write use_figma calls.

Success condition

After apply, run a fresh diff. Success = unresolved drift is zero, or only explicitly approved exceptions remain.

Weekly Installs
241
Repository
firebenders/syn…en-skill
GitHub Stars
17
First Seen
Mar 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass