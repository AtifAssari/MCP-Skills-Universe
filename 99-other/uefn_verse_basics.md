---
title: uefn-verse-basics
url: https://skills.sh/flohhhhh/skills/uefn-verse-basics
---

# uefn-verse-basics

skills/flohhhhh/skills/uefn-verse-basics
uefn-verse-basics
Installation
$ npx skills add https://github.com/flohhhhh/skills --skill uefn-verse-basics
SKILL.md
UEFN Verse Basics
Overview

Use this skill for practical "get started and keep moving" support in UEFN + Verse. Treat Epic docs as source of truth and guide users through a concrete, testable loop.

Read Order
references/docs-map.md for source routing.
references/bootstrap-checklist.md for end-to-end onboarding and DX loop.
Execution Model
Confirm the user stage: install, new project, first Verse file, compile, playtest, debug, or team workflow.
Give only the next actionable step set (avoid dumping all docs at once).
Prefer the smallest working loop: create Verse file -> build Verse code -> place device -> launch session -> verify behavior -> iterate.
If blocked, diagnose by failure class: environment, compile, session/push, device wiring, runtime logic.
Always include the exact Epic page link used.
Minimal UEFN Verse Patterns

Keep these snippets tiny and adapt imports/devices to the target island.

First Device Skeleton
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

hello_world_device := class(creative_device):
    OnBegin<override>()<suspends>:void =
        Print("Hello from UEFN Verse")

Editable Device Reference
using { /Fortnite.com/Devices }

example_device := class(creative_device):
    @editable
    Button:button_device = button_device{}

DX Guardrails
State clearly which steps require UEFN GUI interactions.
In compile loops, prefer Build Verse Code first, then Push Verse Changes for Verse-only edits.
After changing placed device behavior, use Push Changes when needed so level state/device updates are applied.
In troubleshooting, start with Message Log + Verse Build status, then validate device placement and editable assignments.
For collaborative projects, prefer Unreal Revision Control workflows early (sync/check-out/check-in discipline).
Weekly Installs
10
Repository
flohhhhh/skills
GitHub Stars
2
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass