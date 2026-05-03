---
title: visionos-immersive-media-developer
url: https://skills.sh/tomkrikorian/visionosagents/visionos-immersive-media-developer
---

# visionos-immersive-media-developer

skills/tomkrikorian/visionosagents/visionos-immersive-media-developer
visionos-immersive-media-developer
Installation
$ npx skills add https://github.com/tomkrikorian/visionosagents --skill visionos-immersive-media-developer
SKILL.md
visionOS Immersive Media Developer
Quick Start

Decide first whether the app should use the system AVKit experience or a custom RealityKit playback surface.

Clarify the media shape: surface video, portal, progressive immersive, full immersive, spatial video, or Apple Immersive Video.
Load only the matching reference files.
Treat playback-mode changes as both media and scene-orchestration work.
Load References When
Reference	When to Use
playback-decision-tree.md	Decision tree: window vs portal vs progressive vs full immersive playback.
avexperiencecontroller.md	When AVKit AVExperienceController is the right surface for the product.
videoplayercomponent-basics.md	When you need to set up VideoPlayerComponent + AVPlayer correctly.
apmp-and-spatial-video.md	When the content is spatial video, APMP, or Apple Immersive Video.
immersive-viewing-modes.md	When implementing portal, progressive, or full modes and related scene transitions.
events-and-transitions.md	When responding to VideoPlayerEvents and managing UI during transitions.
comfort-mitigation.md	When handling comfort violations and mitigation strategies on visionOS 26+.
apple-immersive-video-authoring.md	When you need Apple Immersive Video authoring or packaging references.
Workflow
Choose the playback architecture.
Load the references for that surface and media type.
Implement playback and viewing-mode transitions.
Add event handling and comfort mitigation where relevant.
Summarize the playback path, transition model, and remaining validation work.
Guardrails
Start with AVKit AVExperienceController when the system player experience fits the product.
Use RealityKit VideoPlayerComponent when the video must live in a custom scene graph.
Do not treat immersive-mode transitions as a simple property flip when the app also needs scene changes.
Make sure the user has a clear exit path from immersive playback.
Output Expectations

Provide:

the chosen playback architecture
the media type and viewing mode
which references were used
the transition or event model involved
the next validation step
Weekly Installs
15
Repository
tomkrikorian/vi…osagents
GitHub Stars
49
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass