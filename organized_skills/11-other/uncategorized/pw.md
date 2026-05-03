---
rating: ⭐⭐
title: pw
url: https://skills.sh/alb-o/pw-rs/pw
---

# pw

skills/alb-o/pw-rs/pw
pw
Installation
$ npx skills add https://github.com/alb-o/pw-rs --skill pw
SKILL.md
commands

Use canonical ops via pw exec.

pw exec navigate --input '{"url":"..."}'
pw exec page.text --input '{"selector":"..."}'
pw exec page.html --input '{"selector":"..."}'
pw exec click --input '{"selector":"..."}'
pw exec fill --input '{"selector":"...","text":"..."}'
pw exec screenshot --input '{"output":"page.png"}'
pw exec page.eval --input '{"expression":"..."}'
pw exec page.read --input '{}'

For NDJSON loops, use pw batch.

setup

start daemon for fast warm execution:

scripts/start-daemon.sh


browser session management is via canonical connect op:

launch: pw exec connect --input '{"launch":true}'
discover: pw exec connect --input '{"discover":true}'
clear: pw exec connect --input '{"clear":true}'

auth in ./playwright/auth/*.json is auto-injected when configured.

context

runtime/profile state is profile-scoped under .pw-cli-v4. use --profile <name> for isolation.

wrappers

scripts/pw.nu exposes stable helpers (pw nav, pw click, pw eval, etc.) but internally calls only pw exec.

references
cli | auth | connect | daemon
page | protect | run | test
Weekly Installs
9
Repository
alb-o/pw-rs
GitHub Stars
3
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn