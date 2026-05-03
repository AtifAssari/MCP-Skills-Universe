---
rating: ⭐⭐
title: realitykit-visionos-developer
url: https://skills.sh/tomkrikorian/visionosagents/realitykit-visionos-developer
---

# realitykit-visionos-developer

skills/tomkrikorian/visionosagents/realitykit-visionos-developer
realitykit-visionos-developer
Installation
$ npx skills add https://github.com/tomkrikorian/visionosagents --skill realitykit-visionos-developer
SKILL.md
RealityKit visionOS Developer
Quick Start
Decide whether the task is component selection, scene setup, animation, physics, audio, input, or ECS debugging.
Load only the component, category, or custom-system references that match the task instead of reading the whole catalog.
Use RealityView as the SwiftUI bridge and keep all content mutation inside documented RealityKit entry points.
Register custom components before use, then keep per-frame behavior in systems instead of ad hoc view logic.
Route app launch, simulator flow, or build-debug plumbing to build-run-debug.
Load References When
Reference	When to Use
references/component-index.md	When you need the RealityKit category map and guidance on which component reference to open next.
references/systemandcomponentcreation.md	When you need a complete custom ECS registration, query, and update-order pattern.
references/modelcomponent.md	When rendering meshes and materials.
references/inputtargetcomponent.md	When making entities interactive.
references/anchoringcomponent.md	When anchoring content to planes, hands, images, or world targets.
references/spatialaudiocomponent.md	When placing audio in 3D space.
references/collisioncomponent.md	When defining collision shapes or hit testing.
references/viewattachmentcomponent.md	When embedding SwiftUI into 3D space.
references/synchronizationcomponent.md	When synchronizing entity state across a session.
references/custom-components.md	When defining custom per-entity state.
references/custom-systems.md	When implementing custom systems or per-frame behavior.
Workflow
Classify the task by scene, component, or system responsibility.
Load the narrowest matching reference files.
Implement or inspect the smallest RealityKit slice that answers the question.
Keep mutation inside RealityView, event handlers, or systems.
Summarize the chosen component or system path and the next validation step.
Guardrails
Always load assets asynchronously; avoid blocking the main actor.
On visionOS, ARView is not available. Use RealityView.
Keep RealityView update logic and ECS mutation out of SwiftUI body code.
Register custom components and systems once during app startup before scenes or assets that depend on them are loaded.
Prefer ManipulationComponent.configureEntity(...) when built-in interaction fits the need.
Prefer a custom System when behavior spans multiple entities or needs continuous updates.
Output Expectations

Provide:

the RealityKit task category
which references were used
the component, attachment, or system path chosen
the main constraint or pitfall
routing back to SwiftUI, architecture, or build-debug if needed
Weekly Installs
61
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