---
rating: ⭐⭐
title: tvos
url: https://skills.sh/fusengine/agents/tvos
---

# tvos

skills/fusengine/agents/tvos
tvos
Installation
$ npx skills add https://github.com/fusengine/agents --skill tvos
SKILL.md
tvOS Platform

tvOS-specific development for Apple TV living room experiences.

Agent Workflow (MANDATORY)

Before ANY implementation, use TeamCreate to spawn 3 agents:

fuse-ai-pilot:explore-codebase - Analyze existing tvOS patterns
fuse-ai-pilot:research-expert - Verify latest tvOS 26 docs via Context7/Exa
mcp__apple-docs__search_apple_docs - Check tvOS patterns

After implementation, run fuse-ai-pilot:sniper for validation.

Overview
When to Use
Building Apple TV applications
Video and audio streaming
Focus-based navigation
Siri Remote interactions
Multi-user experiences
Game controller support
Why tvOS Skill
Feature	Benefit
Focus system	Large screen navigation
Liquid Glass	Modern TV UI (tvOS 26)
Media playback	AVKit integration
Remote control	Siri Remote gestures
tvOS 26 Features
Liquid Glass on TV
Button("Watch Now") { }
    .buttonStyle(.bordered)
    .glassEffect(.regular)  // Glass effect on focus

TabView {
    // Tab bar with Liquid Glass
}

Focus System
struct ContentView: View {
    @FocusState private var focused: Bool

    var body: some View {
        Button("Play") { }
            .focused($focused)
            .scaleEffect(focused ? 1.1 : 1.0)
    }
}

Reference Guide
Need	Reference
Focus, selection states	focus-system.md
AVKit, video playback	media-playback.md
Siri Remote, gestures	remote-control.md
Best Practices
Large UI elements - Readable from 10 feet
Focus feedback - Clear visual indication
Simple navigation - Minimal depth
Remote-friendly - Siri Remote gestures
Media-first - Optimize for video/audio
Multi-user - Support user switching
Weekly Installs
22
Repository
fusengine/agents
GitHub Stars
11
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass