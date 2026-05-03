---
title: swiftui-liquid-glass
url: https://skills.sh/dimillian/skills/swiftui-liquid-glass
---

# swiftui-liquid-glass

skills/dimillian/skills/swiftui-liquid-glass
swiftui-liquid-glass
Originally fromopenai/plugins
Installation
$ npx skills add https://github.com/dimillian/skills --skill swiftui-liquid-glass
Summary

Build and review SwiftUI features using the iOS 26+ Liquid Glass API with native modifiers and Apple design guidance.

Supports three workflows: reviewing existing features for correct Liquid Glass usage, improving features by refactoring to glass components, and implementing new glass-based UI from scratch
Provides native API patterns including glassEffect(), GlassEffectContainer for grouped elements, and .buttonStyle(.glass) / .buttonStyle(.glassProminent) for actions
Includes availability gating with #available(iOS 26, *) and fallback strategies using ultraThinMaterial for earlier iOS versions
Covers modifier ordering, interactivity handling with .interactive(), shape consistency, and morphing transitions with glassEffectID and @Namespace
SKILL.md
SwiftUI Liquid Glass
Overview

Use this skill to build or review SwiftUI features that fully align with the iOS 26+ Liquid Glass API. Prioritize native APIs (glassEffect, GlassEffectContainer, glass button styles) and Apple design guidance. Keep usage consistent, interactive where needed, and performance aware.

Workflow Decision Tree

Choose the path that matches the request:

1) Review an existing feature
Inspect where Liquid Glass should be used and where it should not.
Verify correct modifier order, shape usage, and container placement.
Check for iOS 26+ availability handling and sensible fallbacks.
2) Improve a feature using Liquid Glass
Identify target components for glass treatment (surfaces, chips, buttons, cards).
Refactor to use GlassEffectContainer where multiple glass elements appear.
Introduce interactive glass only for tappable or focusable elements.
3) Implement a new feature using Liquid Glass
Design the glass surfaces and interactions first (shape, prominence, grouping).
Add glass modifiers after layout/appearance modifiers.
Add morphing transitions only when the view hierarchy changes with animation.
Core Guidelines
Prefer native Liquid Glass APIs over custom blurs.
Use GlassEffectContainer when multiple glass elements coexist.
Apply .glassEffect(...) after layout and visual modifiers.
Use .interactive() for elements that respond to touch/pointer.
Keep shapes consistent across related elements for a cohesive look.
Gate with #available(iOS 26, *) and provide a non-glass fallback.
Review Checklist
Availability: #available(iOS 26, *) present with fallback UI.
Composition: Multiple glass views wrapped in GlassEffectContainer.
Modifier order: glassEffect applied after layout/appearance modifiers.
Interactivity: interactive() only where user interaction exists.
Transitions: glassEffectID used with @Namespace for morphing.
Consistency: Shapes, tinting, and spacing align across the feature.
Implementation Checklist
Define target elements and desired glass prominence.
Wrap grouped glass elements in GlassEffectContainer and tune spacing.
Use .glassEffect(.regular.tint(...).interactive(), in: .rect(cornerRadius: ...)) as needed.
Use .buttonStyle(.glass) / .buttonStyle(.glassProminent) for actions.
Add morphing transitions with glassEffectID when hierarchy changes.
Provide fallback materials and visuals for earlier iOS versions.
Quick Snippets

Use these patterns directly and tailor shapes/tints/spacing.

if #available(iOS 26, *) {
    Text("Hello")
        .padding()
        .glassEffect(.regular.interactive(), in: .rect(cornerRadius: 16))
} else {
    Text("Hello")
        .padding()
        .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
}

GlassEffectContainer(spacing: 24) {
    HStack(spacing: 24) {
        Image(systemName: "scribble.variable")
            .frame(width: 72, height: 72)
            .font(.system(size: 32))
            .glassEffect()
        Image(systemName: "eraser.fill")
            .frame(width: 72, height: 72)
            .font(.system(size: 32))
            .glassEffect()
    }
}

Button("Confirm") { }
    .buttonStyle(.glassProminent)

Resources
Reference guide: references/liquid-glass.md
Prefer Apple docs for up-to-date API details.
Weekly Installs
2.8K
Repository
dimillian/skills
GitHub Stars
3.4K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass