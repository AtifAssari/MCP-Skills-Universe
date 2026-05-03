---
rating: ⭐⭐⭐
title: ue5-audio-builder
url: https://skills.sh/koshimazaki/ue-audio-skills/ue5-audio-builder
---

# ue5-audio-builder

skills/koshimazaki/ue-audio-skills/ue5-audio-builder
ue5-audio-builder
Installation
$ npx skills add https://github.com/koshimazaki/ue-audio-skills --skill ue5-audio-builder
SKILL.md
Build System — Full Pipeline Audio Generator

Orchestrate all three layers (MetaSounds + Blueprint + Wwise) to generate complete game audio systems from a single description.

Process
Parse — Identify audio behaviours needed
Decompose — Map to MetaSounds (DSP), Blueprint (triggers), Wwise (mixing)
Generate — Build each layer using templates + knowledge
Wire — Connect layers (AudioLink, RTPC, events)
Validate — Check types, connections, paths
Available Patterns (10)
Pattern	MetaSounds	Blueprint	Wwise
gunshot	Random → WavePlayer → Filter → Envelope	Fire event → trigger	RandomSeqContainer + reverb bus
footsteps	Surface → TriggerRoute → per-surface chains	Line trace → surface detect	SwitchContainer + attenuation
ambient	Looped layers + random details + LFO drift	Zone overlap volumes	BlendContainer + RTPC volumes
ui_sound	Sine + AD Envelope (procedural)	UI event router	UI bus (non-spatial)
weather	State-driven layers + crossfade + dynamic filter	Weather state reader	StateGroup + SwitchContainer
spatial	ITD Panner + processing chain	Position tracking	Distance attenuation + HRTF
vehicle_engine	Trigger Sequence → layered Wave Players + Compressor	RPM/throttle params	Engine bus + RTPC
sfx_generator	7-stage synth (Gen→Spectral→Filter→Amp→FX)	Parameter inputs	FX bus chain
preset_morph	Morph 0-1 → MapRange → filter params	Morph slider	Blend preset bus
macro_sequence	Graph variables → InterpTo → filter chain	Step triggers	Sequence bus
MCP Tools
Single System
build_audio_system(pattern="gunshot", name="PlayerRifle", params={...})

AAA Project (6 categories)
build_aaa_project(project_name="MyGame")


Generates: player_footsteps, player_weapons, npc_footsteps, ambient_wind, weather, ui — each with dedicated bus, work units, events.

3 Execution Modes
Mode	Condition	What happens
Full	Wwise + UE5 connected	Creates everything live
Wwise-only	Wwise connected, no UE5	Creates Wwise hierarchy + offline MetaSounds spec
Offline	Neither connected	Dry-run preview of all layers

Auto-detected from connection state. No config needed.

Cross-Layer Wiring
Connection	From	To
wwise_event → metasound_asset	Wwise Event	MetaSounds Source
rtpc → ms_input	Wwise GameParameter	MetaSounds graph input
bp → wwise	Blueprint PostEvent	Wwise Event
bp → ms_param	Blueprint SetFloatParameter	MetaSounds graph input
audiolink	MetaSounds output	Wwise Audio Input
AAA Bus Structure (auto-generated)
Master Audio Bus
├── SFX
│   ├── SFX_Footsteps
│   ├── SFX_Weapons
│   └── SFX_NPC
├── Ambient
│   ├── AMB_Wind
│   └── AMB_Weather
└── UI
    └── UI_Sounds

Output Format
## System: [Name]

### MetaSounds Patches
[JSON graph specs]

### Blueprint Logic
[Node descriptions / pseudo-code]

### Wwise Hierarchy
[Creation sequence with properties]

### Cross-Layer Wiring
[AudioLink + RTPC + event connections]

Source Files
Orchestrator: src/ue_audio_mcp/tools/systems.py
Templates: src/ue_audio_mcp/templates/ (22 JSON)
Wwise templates: src/ue_audio_mcp/tools/wwise_templates.py
Graph validator: src/ue_audio_mcp/knowledge/graph_schema.py

$ARGUMENTS

Weekly Installs
8
Repository
koshimazaki/ue-…o-skills
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass