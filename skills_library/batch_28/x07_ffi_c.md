---
title: x07-ffi-c
url: https://skills.sh/x07lang/x07-website/x07-ffi-c
---

# x07-ffi-c

skills/x07lang/x07-website/x07-ffi-c
x07-ffi-c
Installation
$ npx skills add https://github.com/x07lang/x07-website --skill x07-ffi-c
SKILL.md
x07-ffi-c

Use this skill when embedding an X07 program as a library.

Canonical commands
Emit C + header from a project manifest:
x07 build --project x07.json --out target/out.c --emit-c-header target/out.h
Notes
--emit-c-header disables emitting a main entrypoint, so the output is linkable/embeddable.
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