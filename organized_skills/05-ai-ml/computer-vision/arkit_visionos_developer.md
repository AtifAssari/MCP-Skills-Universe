---
rating: ⭐⭐
title: arkit-visionos-developer
url: https://skills.sh/tomkrikorian/visionosagents/arkit-visionos-developer
---

# arkit-visionos-developer

skills/tomkrikorian/visionosagents/arkit-visionos-developer
arkit-visionos-developer
Installation
$ npx skills add https://github.com/tomkrikorian/visionosagents --skill arkit-visionos-developer
SKILL.md
ARKit visionOS Developer
Quick Start
Identify the provider set first: world tracking, hand tracking, plane detection, scene reconstruction, or another specialized provider.
Add only the usage strings required by the providers you actually use.
Create a long-lived ARKitSession and request authorization before running it.
Load the shared session, anchor, or bridge references first, then load only the provider files you actually need.
Keep anchor state in a model layer, and bridge into RealityKit only when you have a rendering target.
If the issue is app launch, test flow, simulator behavior, or signing, switch to build-run-debug or signing-entitlements.
Load References When
Reference	When to Use
references/provider-index.md	When you need the provider map and routing guidance.
references/session-basics.md	When setting up ARKitSession, authorization, or shared lifecycle rules.
references/anchor-processing.md	When reconciling anchorUpdates, IDs, and model-layer state.
references/realitykit-bridge.md	When ARKit data needs to become visible RealityKit scene content.
references/world-tracking-provider.md	When tracking device pose or world anchors.
references/hand-tracking-provider.md	When tracking hands and joints.
references/plane-detection-provider.md	When detecting horizontal or vertical planes.
references/scene-reconstruction-provider.md	When consuming mesh reconstruction.
references/image-tracking-provider.md	When tracking known 2D images.
references/object-tracking-provider.md	When tracking 3D objects.
references/room-tracking-provider.md	When tracking room boundaries and room-scale features.
references/accessory-tracking-provider.md	When tracking supported accessories.
references/barcode-detection-provider.md	When detecting and reading barcodes.
references/camera-frame-provider.md	When accessing raw camera frames.
references/camera-region-provider.md	When reading region-scoped camera content.
references/environment-light-estimation-provider.md	When estimating ambient lighting.
references/shared-coordinate-space-provider.md	When sharing coordinate spaces across participants or sessions.
references/stereo-properties-provider.md	When working with stereo camera properties.
Workflow
Choose the provider set.
Load the shared session and lifecycle guidance first.
Add only the provider references that match the task.
Keep anchor reconciliation in a model layer.
Bridge into RealityKit only after the model layer has stable state.
Guardrails
Keep a strong reference to ARKitSession for the full lifetime of the experience.
Request authorization before running providers that need it.
Do not block the main actor while awaiting provider updates.
Do not assume every provider has the same presentation requirements.
Route launch, build, simulator, and codesign problems out to the execution skills instead of expanding this skill with run-loop detail.
Output Expectations

Provide:

the chosen provider set
which shared and provider references were used
the session and anchor-processing model
the RealityKit bridge plan if applicable
the next skill to use if the blocker is execution, signing, or scene work
Weekly Installs
53
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