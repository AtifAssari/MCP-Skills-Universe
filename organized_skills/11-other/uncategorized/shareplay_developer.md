---
rating: ⭐⭐
title: shareplay-developer
url: https://skills.sh/tomkrikorian/visionosagents/shareplay-developer
---

# shareplay-developer

skills/tomkrikorian/visionosagents/shareplay-developer
shareplay-developer
Installation
$ npx skills add https://github.com/tomkrikorian/visionosagents --skill shareplay-developer
SKILL.md
SharePlay Developer
Quick Start
Decide whether this experience is launch-only co-location or shared state sync.
Add the Group Activities capability and required entitlement before building SharePlay UI.
Define one GroupActivity per experience and keep the payload minimal and Codable.
Load the right reference only after you know the workflow.
Configure SystemCoordinator before joining whenever spatial personas or immersive spaces are involved.
Load References When
Reference	When to Use
activation-ui.md	When wiring the SharePlay entry point or start button flow.
activity-definition.md	When defining the GroupActivity payload, metadata, or transfer representation.
group-session-lifecycle.md	When joining, leaving, observing, or presenting a GroupSession.
messaging-journal.md	When using GroupSessionMessenger, GroupSessionJournal, or late-joiner sync.
spatial-coordination.md	When configuring SystemCoordinator, spatial templates, or group immersive-space behavior.
visionos-immersive-space.md	When implementing launch-only SharePlay for a visionOS immersive space.
groupactivities-patterns.md	When you need broader GroupActivities patterns or sample-backed examples.
Workflow
Define the activity and choose the activation surface.
Observe and configure the session before joining.
Add messaging or journal synchronization only if shared state is required.
Configure spatial coordination when the experience shares an immersive space.
Summarize the session lifecycle, sync model, and launch surface clearly.
When To Switch Skills
Switch to build-run-debug when the blocker is app launch, simulator state, or runtime debugging rather than SharePlay behavior.
Switch to signing-entitlements when the issue is capabilities, entitlements, or privacy gating.
Switch to telemetry when proof of event ordering or session state changes matters more than API design.
Guardrails
Keep GroupActivity data small and Codable.
Store strong references to GroupSession, GroupSessionMessenger, and GroupSessionJournal.
Configure SystemCoordinator before join() when using spatial coordination.
Do not treat .immersiveEnvironmentBehavior(.coexist) as the coordination API.
Join only after the UI and local state are ready.
Output Expectations

Provide:

the activity type and activation surface
the chosen session and sync model
which references were used
the coordination model if immersive space is involved
the next skill to use if the blocker is execution, signing, or testing
Weekly Installs
22
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