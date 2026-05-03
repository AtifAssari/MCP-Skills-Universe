---
title: tv-terrain-elevation
url: https://skills.sh/metta-ai/tribal-village/tv-terrain-elevation
---

# tv-terrain-elevation

skills/metta-ai/tribal-village/tv-terrain-elevation
tv-terrain-elevation
Installation
$ npx skills add https://github.com/metta-ai/tribal-village --skill tv-terrain-elevation
SKILL.md
TV Terrain Elevation
Workflow
Run:
rg -n "applyBiomeElevation|applyCliffRamps|applyCliffs" src/spawn.nim
sed -n '120,260p' src/spawn.nim
rg -n "canTraverseElevation" src/environment.nim
sed -n '400,460p' src/environment.nim
rg -n "RampUp|RampDown|Cliff" src/terrain.nim src/types.nim src/registry.nim
Explain how elevation traversal is handled.
Weekly Installs
18
Repository
metta-ai/tribal-village
GitHub Stars
3
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass