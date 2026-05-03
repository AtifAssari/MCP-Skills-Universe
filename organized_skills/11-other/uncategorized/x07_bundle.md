---
rating: ⭐⭐
title: x07-bundle
url: https://skills.sh/x07lang/x07-website/x07-bundle
---

# x07-bundle

skills/x07lang/x07-website/x07-bundle
x07-bundle
Installation
$ npx skills add https://github.com/x07lang/x07-website --skill x07-bundle
SKILL.md
x07-bundle

Use x07 bundle to produce a native executable that can be run directly on the target machine without the X07 toolchain installed at runtime.

x07 bundle runs the canonical auto-repair loop by default (--repair=...), so it can format/lint/apply quickfixes before compiling. Use --repair=off when debugging.

Canonical commands

Bundle an OS-world CLI executable:

x07 bundle --project x07.json --profile os --out dist/app
run it: ./dist/app --help
if bundling fails with fuel exhausted, override:
x07 bundle --project x07.json --profile os --solve-fuel 500000000 --out dist/app

Bundle a policy-enforced OS-world executable:

x07 bundle --project x07.json --profile sandbox --out dist/app
requires a base policy (via profiles.sandbox.policy or --policy)
Runtime ABI

The bundled executable:

reads standard process args (argc/argv)
encodes them into argv_v1 input bytes
calls the compiled program entrypoint (x07_solve_v2)
writes program output bytes directly to stdout (no framing)
Emit artifacts (debug / CI)
x07 bundle ... --emit-dir dist/emit
emits report.json, program.freestanding.c, wrapper.main.c, and bundle.combined.c
for run-os-sandboxed, also emits policy.used.json
Report contract

x07 bundle prints a machine JSON report to stdout:

schema_version: "x07.bundle.report@0.2.0"
report contains the underlying runner report used to compile the native artifact
Weekly Installs
8
Repository
x07lang/x07-website
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass