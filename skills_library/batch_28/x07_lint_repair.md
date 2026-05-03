---
title: x07-lint-repair
url: https://skills.sh/x07lang/x07-website/x07-lint-repair
---

# x07-lint-repair

skills/x07lang/x07-website/x07-lint-repair
x07-lint-repair
Installation
$ npx skills add https://github.com/x07lang/x07-website --skill x07-lint-repair
SKILL.md
x07-lint-repair

Use this skill when an X07 file fails linting and the agent needs a repeatable converge loop.

Note: x07 run, x07 build, and x07 bundle run the same auto-repair loop by default (--repair=...). Use this skill when you want raw diagnostics or tighter control.

Canonical converge loop

Lint (machine-readable JSON report):

x07 lint --input src/main.x07.json --json

Apply tool-provided quickfixes (when diagnostics include JSON Patch quickfixes):

x07 fix --input src/main.x07.json --write --json

If a custom fix is needed, apply an explicit JSON Patch (RFC 6902):

x07 ast apply-patch --in src/main.x07.json --patch /tmp/repair.patch.json --validate

Canonicalize after patching:

x07 fmt --input src/main.x07.json --write --json

Repeat (max 3 iterations). If still failing, stop and change strategy (reduce scope, regenerate the x07AST cleanly, or ask for clarification).

Related:

If the failure came from x07 test --pbt (a counterexample repro), use x07 fix --from-pbt <repro.json> --write to generate a deterministic regression test.
Weekly Installs
9
Repository
x07lang/x07-website
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass