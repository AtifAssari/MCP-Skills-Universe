---
rating: ⭐⭐⭐
title: vvvv-patching
url: https://skills.sh/tebjan/vvvv-skills/vvvv-patching
---

# vvvv-patching

skills/tebjan/vvvv-skills/vvvv-patching
vvvv-patching
Installation
$ npx skills add https://github.com/tebjan/vvvv-skills --skill vvvv-patching
SKILL.md
vvvv Patching Patterns
Dataflow Basics
Left-to-right, top-to-bottom execution order
Links carry data between pads (input/output connection points)
Spreading — connecting a Spread<T> to a single-value input auto-iterates the node
Every frame, the entire connected graph evaluates; disconnected subgraphs are skipped

Both visual patches and C# source projects operate in a live environment — edits take effect immediately while the program runs. Patch changes preserve node state; C# code changes trigger a node restart (Dispose → Constructor). You can adjust parameters, add connections, and restructure patches while seeing results in real-time.

When to Patch vs Write C#
Patch	Code (C#)
Data flow routing, visual connections	Performance-critical algorithms
Prototyping and parameter tweaking	Complex state machines
UI composition and layout	.NET library interop
Simple transformations	Native resource management

As a rule: patch the data flow, code the algorithms.

Regions

Regions are visual constructs that control execution flow:

Region	Purpose	C# Equivalent
ForEach	Iterate over Spread elements	foreach loop
If	Conditional execution	if/else
Switch	Multi-branch selection	switch
Repeat	Loop N times	for loop
Accumulator	Running aggregation	Aggregate/Fold
Process Nodes in Patches

Process nodes are the primary way to add state to patches:

They have a Create region (runs once) and an Update region (runs each frame)
Internal state persists between frames
Can contain sub-patches for complex logic
Channels — Reactive Data Flow

Channels provide two-way data binding:

IChannel<T> — observable value container
.Value — read or write the current value
Channels persist state across sessions
Connect channels between nodes for reactive updates without explicit links
Event Handling
Bang — a one-frame true pulse (trigger)
Toggle — alternates between true and false
FrameDelay — delays a value by one frame (breaks circular dependencies)
Use Changed node to detect when a value changes between frames
Patch Organization
Naming Conventions
Use PascalCase for patch names and node names
Group related operations under a common category
Use descriptive names that indicate the operation (verb + noun)
Structure
Keep patches focused — one purpose per patch
Extract reusable logic into sub-patches
Use IOBox nodes for exposing parameters
Add Pad nodes to create input/output pins on the patch boundary
Common Anti-Patterns
Circular dependencies — use FrameDelay to break cycles
Too many nodes in one patch — extract sub-patches
Polling instead of reacting — use Channels for reactive updates
Ignoring Nil — always handle null/empty Spread inputs gracefully

For common patterns reference, see patterns.md.

Weekly Installs
45
Repository
tebjan/vvvv-skills
GitHub Stars
23
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass