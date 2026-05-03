---
title: spatial-swiftui-developer
url: https://skills.sh/tomkrikorian/visionosagents/spatial-swiftui-developer
---

# spatial-swiftui-developer

skills/tomkrikorian/visionosagents/spatial-swiftui-developer
spatial-swiftui-developer
Installation
$ npx skills add https://github.com/tomkrikorian/visionosagents --skill spatial-swiftui-developer
SKILL.md
Spatial SwiftUI Developer
Quick Start
If the task is really about surface choice, scene ownership, or file structure, switch to spatial-app-architecture first.
Pick the rendering track: Model3D for simple asset display, RealityView for custom entity graphs and attachments.
Load only the matching reference files.
Keep loading async and keep RealityKit mutations inside its intended entry points.
Route build, launch, simulator, and test problems to build-run-debug.
Load References When
Reference	When to Use
swiftui-spatial-overview.md	When you need the general feature map, examples, and routing guidance for this skill.
model3d.md	When using Model3D for async model loading, assets, animation, or manipulation.
realityview.md	When setting up RealityView, attachments, or RealityKit integration patterns.
interaction.md	When implementing gestures or manipulation patterns for spatial input.
buttons-and-controls.md	When implementing visible SwiftUI buttons, links styled as buttons, toolbars, forms, or control surfaces.
windowing-immersion.md	When managing windows, volumetric surfaces, or immersive space transitions.
spatial-layout.md	When using SwiftUI spatial layout APIs, sizing, or debug tools.
charts-3d.md	When implementing Chart3D or other spatial data-visualization patterns.
Workflow
Confirm the architecture and scene ownership are already settled.
Choose the rendering surface: Model3D, RealityView, window, volume, or immersive scene.
Load only the matching reference files.
Implement the smallest viable scene and keep mutations in the right layer.
Summarize the chosen SwiftUI-to-RealityKit integration path.
Guardrails
Keep RealityKit loads async; do not block the main actor with asset or entity loading.
Mutate RealityKit content in RealityView make or update closures or in a system, not in SwiftUI body code.
Use Model3D only when you need simple display and layout, not a custom ECS graph.
Treat ImmersiveSpace as a separate scene with its own lifecycle and environment actions.
Use defaultSize as an initial hint only; the system can clamp or restore geometry.
Switch to build-run-debug when the question is about launch, build, simulator, codesign, or debugging workflow.
Use spatial-app-architecture when the question is about scene boundaries, ownership, or feature decomposition rather than API usage.
Output Expectations

Provide:

the chosen rendering and scene path
which references were used
the API surface involved (Model3D, RealityView, windowing, interaction, layout, or charts)
the main implementation constraint or pitfall
routing back to architecture or build/debug if needed
Weekly Installs
46
Repository
tomkrikorian/vi…osagents
GitHub Stars
49
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass