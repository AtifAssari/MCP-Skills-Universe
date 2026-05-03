---
rating: ⭐⭐
title: shadergraph-editor
url: https://skills.sh/tomkrikorian/visionosagents/shadergraph-editor
---

# shadergraph-editor

skills/tomkrikorian/visionosagents/shadergraph-editor
shadergraph-editor
Installation
$ npx skills add https://github.com/tomkrikorian/visionosagents --skill shadergraph-editor
SKILL.md
ShaderGraph Editor
Quick Start

Default to Reality Composer Pro. Use raw USD or MaterialX inspection only when debugging exports or interoperability.

Decide whether the task is node selection, runtime parameter control, export debugging, or sample selection.
Load only the matching reference files.
Route text-level USD structure edits to usd-editor.
Load References When
Reference	When to Use
references/shadergraph-node-reference.md	When choosing RealityKit Shader Graph nodes by category.
references/runtime-api.md	When loading ShaderGraphMaterial, working with promoted inputs, or updating parameters at runtime.
references/export-debug.md	When inspecting exported USD or MaterialX, or when a graph fails to load or render as expected.
references/samples.md	When selecting the closest repo sample before authoring a new effect from scratch.
Workflow
Start from the closest existing sample when possible.
Author or refine the graph in Reality Composer Pro.
Promote the inputs that need runtime control.
Load and update the material through the runtime API.
Inspect exports only when the normal authoring path stops explaining the failure.
When To Switch Skills
Switch to usd-editor when the task is really about prim paths, composition, or text-level USD authoring.
Switch to realitykit-visionos-developer when the blocker is entity setup, material application, or scene integration rather than graph authoring.
Guardrails
Treat Reality Composer Pro as the default authoring surface.
Do not treat exported info:id strings or raw graph layout as stable public API unless Apple documents them directly.
Output Expectations

Provide:

the selected effect or sample starting point
which references were used
how the material is authored or loaded
whether the issue is a graph problem, runtime problem, or export problem
explicit routing to usd-editor or RealityKit work if needed
Weekly Installs
26
Repository
tomkrikorian/vi…osagents
GitHub Stars
49
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass