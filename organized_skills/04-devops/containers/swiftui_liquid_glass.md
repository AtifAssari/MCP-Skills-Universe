---
rating: ⭐⭐⭐
title: swiftui-liquid-glass
url: https://skills.sh/dpearson2699/swift-ios-skills/swiftui-liquid-glass
---

# swiftui-liquid-glass

skills/dpearson2699/swift-ios-skills/swiftui-liquid-glass
swiftui-liquid-glass
Originally fromopenai/plugins
Installation
$ npx skills add https://github.com/dpearson2699/swift-ios-skills --skill swiftui-liquid-glass
Summary

SwiftUI Liquid Glass effects for iOS 26+ with interactive glass containers, morphing transitions, and button styles.

Provides .glassEffect() modifier for applying translucent Liquid Glass material to custom views, with support for tinting, interactivity, and custom shapes
Includes GlassEffectContainer for grouping and blending multiple glass elements, plus glassEffectID and glassEffectUnion for morphing animations during view hierarchy changes
Offers pre-built button styles (.glass, .glassProminent), scroll edge effects, and toolbar utilities like ToolbarSpacer for iOS 26 design patterns
Requires availability gating with if #available(iOS 26, *) and fallback UI for earlier versions; emphasizes correct modifier ordering and avoiding overuse of glass effects
SKILL.md
SwiftUI Liquid Glass

Liquid Glass is the dynamic translucent material introduced in iOS 26 (and iPadOS 26, macOS 26, tvOS 26, watchOS 26). It blurs content behind it, reflects surrounding color and light, and reacts to touch and pointer interactions. Standard SwiftUI components (tab bars, toolbars, navigation bars, sheets) adopt Liquid Glass automatically when built with the iOS 26 SDK. Use the APIs below for custom views and controls.

See references/liquid-glass.md for the full API reference with additional examples.

Contents
Workflow
Core API Summary
Code Examples
Common Mistakes
Review Checklist
References
Workflow

Choose the path that matches the request:

1. Implement a new feature with Liquid Glass
Identify target surfaces (cards, chips, floating controls, custom bars).
Decide shape, prominence, and whether each element needs interactivity.
Wrap grouped glass elements in a GlassEffectContainer.
Apply .glassEffect() after layout and appearance modifiers.
Add .interactive() only to tappable/focusable elements.
Add morphing transitions with glassEffectID(_:in:) where the view hierarchy changes with animation.
Gate with if #available(iOS 26, *) and provide a fallback for earlier versions.
2. Improve an existing feature with Liquid Glass
Find custom blur/material backgrounds that can be replaced with .glassEffect().
Wrap sibling glass elements in GlassEffectContainer for blending and performance.
Replace custom glass-like buttons with .buttonStyle(.glass) or .buttonStyle(.glassProminent).
Add morphing transitions where animated insertion/removal occurs.
3. Review existing Liquid Glass usage

Run through the Review Checklist below and verify each item.

Core API Summary
glassEffect(_:in:)

Applies Liquid Glass behind a view. Default: .regular variant in a Capsule shape.

nonisolated func glassEffect(
    _ glass: Glass = .regular,
    in shape: some Shape = DefaultGlassEffectShape()
) -> some View

Glass struct
Property / Method	Purpose
.regular	Standard glass material
.clear	Clear variant (minimal tint)
.identity	No visual effect (pass-through)
.tint(_:)	Add a color tint for prominence
.interactive(_:)	React to touch and pointer interactions

Chain them: .regular.tint(.blue).interactive()

GlassEffectContainer

Wraps multiple glass views for shared rendering, blending, and morphing.

GlassEffectContainer(spacing: 24) {
    // child views with .glassEffect()
}


The spacing controls when nearby glass shapes begin to blend. Match or exceed the interior layout spacing so shapes merge during animated transitions but remain separate at rest.

Morphing & Transitions
Modifier	Purpose
glassEffectID(_:in:)	Stable identity for morphing during view hierarchy changes
glassEffectUnion(id:namespace:)	Merge multiple views into one glass shape
glassEffectTransition(_:)	Control how glass appears/disappears

Transition types: .matchedGeometry (default when within spacing), .materialize (fade content + animate glass in/out), .identity (no transition).

Button Styles
Button("Action") { }
    .buttonStyle(.glass)           // standard glass button

Button("Primary") { }
    .buttonStyle(.glassProminent)  // prominent glass button

Scroll Edge Effects and Background Extension (iOS 26+)

These complement Liquid Glass when building custom toolbars and scroll views:

ScrollView {
    content
}
.scrollEdgeEffectStyle(.soft, for: .top)  // Configures edge effect at scroll boundaries

// Duplicate view into mirrored copies at safe area edges with blur (e.g., under sidebars)
content
    .backgroundExtensionEffect()

ToolbarSpacer (iOS 26+)

Creates a visual break between items in toolbars:

.toolbar {
    ToolbarItem { Button("Edit") { } }
    ToolbarSpacer(.fixed)
    ToolbarItem { Button("Share") { } }
}

Code Examples
Basic glass effect with availability gate
if #available(iOS 26, *) {
    Text("Status")
        .padding()
        .glassEffect(.regular.interactive(), in: .rect(cornerRadius: 16))
} else {
    Text("Status")
        .padding()
        .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
}

Grouped glass elements in a container
GlassEffectContainer(spacing: 24) {
    HStack(spacing: 24) {
        ForEach(tools) { tool in
            Image(systemName: tool.icon)
                .frame(width: 56, height: 56)
                .glassEffect(.regular.interactive())
        }
    }
}

Morphing transition
@State private var isExpanded = false
@Namespace private var ns

var body: some View {
    GlassEffectContainer(spacing: 40) {
        HStack(spacing: 40) {
            Image(systemName: "pencil")
                .frame(width: 80, height: 80)
                .glassEffect()
                .glassEffectID("pencil", in: ns)

            if isExpanded {
                Image(systemName: "eraser.fill")
                    .frame(width: 80, height: 80)
                    .glassEffect()
                    .glassEffectID("eraser", in: ns)
            }
        }
    }

    Button("Toggle") {
        withAnimation { isExpanded.toggle() }
    }
    .buttonStyle(.glass)
}

Unioning views into a single glass shape
@Namespace private var ns

GlassEffectContainer(spacing: 20) {
    HStack(spacing: 20) {
        ForEach(items.indices, id: \.self) { i in
            Image(systemName: items[i])
                .frame(width: 80, height: 80)
                .glassEffect()
                .glassEffectUnion(id: i < 2 ? "group1" : "group2", namespace: ns)
        }
    }
}

Tinted glass badge
struct GlassBadge: View {
    let icon: String
    let tint: Color

    var body: some View {
        Image(systemName: icon)
            .font(.title2)
            .padding()
            .glassEffect(.regular.tint(tint), in: .rect(cornerRadius: 12))
    }
}

Common Mistakes
DON'T: Apply Liquid Glass to every surface

Overuse distracts from content. Glass should emphasize key interactive elements, not decorate everything.

// WRONG: Glass on everything
VStack {
    Text("Title").glassEffect()
    Text("Subtitle").glassEffect()
    Divider().glassEffect()
    Text("Body").glassEffect()
}

// CORRECT: Glass on primary interactive elements only
VStack {
    Text("Title").font(.title)
    Text("Subtitle").font(.subheadline)
    Divider()
    Text("Body")
}
.padding()
.glassEffect()

DON'T: Nest GlassEffectContainer inside another

Nested containers cause undefined rendering behavior.

// WRONG
GlassEffectContainer {
    GlassEffectContainer {
        content.glassEffect()
    }
}

// CORRECT: Single container wrapping all glass views
GlassEffectContainer {
    content.glassEffect()
}

DON'T: Add .interactive() to non-interactive elements

.interactive() adds visual affordance suggesting tappability. Using it on decorative glass misleads users.

DON'T: Apply .glassEffect() before layout modifiers

Glass calculates its shape from the final frame. Applying it before padding/frame produces incorrect bounds.

// WRONG: Glass applied before padding
Text("Label").glassEffect().padding()

// CORRECT: Glass applied after layout
Text("Label").padding().glassEffect()

DON'T: Forget accessibility testing

Always test with Reduce Transparency and Reduce Motion enabled. Glass degrades gracefully but verify content remains readable.

DON'T: Skip availability checks

Liquid Glass requires iOS 26+. Gate with if #available(iOS 26, *) and provide a fallback.

Review Checklist
 Availability: if #available(iOS 26, *) present with fallback UI.
 Container: Multiple glass views wrapped in GlassEffectContainer.
 Modifier order: .glassEffect() applied after layout/appearance modifiers.
 Interactivity: .interactive() used only where user interaction exists.
 Transitions: glassEffectID used with @Namespace for morphing animations.
 Transition type: .matchedGeometry for nearby effects; .materialize for distant ones.
 Consistency: Shapes, tints, and spacing are uniform across related elements.
 Performance: Glass effects are limited in number; container used for grouping.
 Accessibility: Tested with Reduce Transparency and Reduce Motion enabled.
 Button styles: Standard .glass / .glassProminent used for buttons.
 Ensure types driving Liquid Glass effects are Sendable; apply glass effects on @MainActor context
References
Full API guide: references/liquid-glass.md
Apple docs: Applying Liquid Glass to custom views
Apple docs: Adopting Liquid Glass
Weekly Installs
1.2K
Repository
dpearson2699/sw…s-skills
GitHub Stars
512
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass