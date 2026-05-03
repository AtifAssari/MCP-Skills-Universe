---
rating: ⭐⭐
title: liquid-glass
url: https://skills.sh/casper-studios/casper-marketplace/liquid-glass
---

# liquid-glass

skills/casper-studios/casper-marketplace/liquid-glass
liquid-glass
Installation
$ npx skills add https://github.com/casper-studios/casper-marketplace --skill liquid-glass
SKILL.md
Liquid Glass Design

Build native macOS/iOS applications with Apple's Liquid Glass design and HIG.

Core Rules
Three-Layer Model
┌─────────────────────────────────────────┐
│     GLASS LAYER (Navigation/Controls)   │  ← Glass here ONLY
├─────────────────────────────────────────┤
│         CONTENT LAYER (Your App)        │  ← Never glass here
└─────────────────────────────────────────┘


Glass is ONLY for navigation floating above content. Never on content itself.

Five Principles
Content First - Glass floats above, content shines through
Depth Through Light - Lensing creates hierarchy, not opacity
Adaptive Tinting - Colors respond to background dynamically
Semantic Emphasis - Tint primary actions only
Accessibility Built-In - System handles adaptations automatically
Materials (macOS 14+ / Pre-iOS 26)
// Card with material
.padding(24)
.background(.regularMaterial, in: RoundedRectangle(cornerRadius: 16, style: .continuous))

// Material options (lightest → heaviest):
// .ultraThinMaterial, .thinMaterial, .regularMaterial (default), .thickMaterial, .ultraThickMaterial

Liquid Glass API (iOS 26+ / macOS Tahoe)
// Basic
Button("Action") { }.glassEffect()

// Variants
.glassEffect(.regular)   // Standard UI
.glassEffect(.clear)     // Media backgrounds only
.glassEffect(.identity)  // Disabled

// Interactive (adds bounce/shimmer)
Button("Tap") { }.glassEffect(.regular.interactive())

// Multiple glass elements - MUST wrap in container
GlassEffectContainer(spacing: 30) {
    HStack {
        Button("A") { }.glassEffect()
        Button("B") { }.glassEffect()
    }
}

// Button styles
Button("Cancel") { }.buttonStyle(.glass)           // Secondary
Button("Save") { }.buttonStyle(.glassProminent).tint(.blue)  // Primary

Essential Patterns
Card
VStack(alignment: .leading, spacing: 12) {
    HStack {
        ZStack {
            Circle().fill(color.opacity(0.15)).frame(width: 36, height: 36)
            Image(systemName: icon).foregroundStyle(color)
        }
        Spacer()
    }
    Text(value).font(.system(size: 28, weight: .bold, design: .rounded))
    Text(label).font(.caption).foregroundStyle(.secondary)
}
.padding(20)
.background(.regularMaterial, in: RoundedRectangle(cornerRadius: 16, style: .continuous))

Row with Hover
HStack { content }
.padding(16)
.background(isHovering ? Color.primary.opacity(0.04) : .clear)
.background(.quaternary.opacity(0.5), in: RoundedRectangle(cornerRadius: 12, style: .continuous))
.onHover { withAnimation(.easeInOut(duration: 0.15)) { isHovering = $0 } }

Badge
HStack(spacing: 8) {
    Circle().fill(isActive ? .green : .orange).frame(width: 8, height: 8)
    Text(status).font(.caption).fontWeight(.medium)
}
.padding(.horizontal, 12).padding(.vertical, 8)
.background(.regularMaterial, in: Capsule())

Icon with Tinted Background
ZStack {
    Circle().fill(color.opacity(0.15)).frame(width: 32, height: 32)
    Image(systemName: icon).font(.system(size: 14, weight: .semibold)).foregroundStyle(color)
}

Shapes
// Always use .continuous
RoundedRectangle(cornerRadius: 16, style: .continuous)  // Cards
RoundedRectangle(cornerRadius: 12, style: .continuous)  // Rows
RoundedRectangle(cornerRadius: 8, style: .continuous)   // Small elements
Capsule()  // Pills, badges
Circle()   // Icons

Colors
// Semantic foreground
.foregroundStyle(.primary)    // Main content
.foregroundStyle(.secondary)  // Subtitles
.foregroundStyle(.tertiary)   // Timestamps

// Backgrounds
.background(.quaternary)
.background(.quaternary.opacity(0.5))

// Accent meanings
Color.blue    // Primary actions, selection
Color.green   // Success, active
Color.orange  // Warning, loading
Color.red     // Destructive, error
Color.purple  // Premium, AI
Color.cyan    // Security

// Tinted backgrounds: always 15% opacity
.fill(color.opacity(0.15))

Typography
.font(.largeTitle).fontWeight(.bold)      // Page titles
.font(.headline).fontWeight(.semibold)    // Section headers
.font(.subheadline).fontWeight(.medium)   // Row titles
.font(.body)                               // Content (17pt default)
.font(.caption)                            // Metadata
.font(.caption2)                           // Timestamps
.font(.system(size: 28, weight: .bold, design: .rounded))  // Stats


Rules: Min 11pt. Avoid Ultralight/Thin/Light. Use system fonts for Dynamic Type.

Spacing (8pt Grid)
// Standard values: 4, 8, 12, 16, 20, 24, 32, 40, 48

.padding(24)                    // Cards
.padding(16)                    // Rows
.padding(.horizontal, 12).padding(.vertical, 8)  // Badges

// Rule: external spacing ≥ internal spacing
VStack(spacing: 24) { CardView().padding(20) }  // Correct

SF Symbols
// Preferred: hierarchical for depth
Image(systemName: icon).symbolRenderingMode(.hierarchical).foregroundStyle(color)

// Match weight to nearby text
Image(systemName: "gear").font(.system(size: 14, weight: .semibold))

Hit Targets
// MINIMUM: 44pt × 44pt
Button { } label: { Image(systemName: "gear") }
    .frame(minWidth: 44, minHeight: 44)

Animations
// Hover
.onHover { withAnimation(.easeInOut(duration: 0.15)) { isHovering = $0 } }

// Spring
withAnimation(.spring(response: 0.3)) { }
withAnimation(.bouncy) { }

// Entry
.opacity(appeared ? 1 : 0).offset(y: appeared ? 0 : 10)
.onAppear { withAnimation(.spring(response: 0.5, dampingFraction: 0.8)) { appeared = true } }

Do's and Don'ts

DO:

Use .regularMaterial for cards/toolbars
Use .continuous on ALL rounded rectangles
Use 15% opacity for icon backgrounds
Wrap multiple glass in GlassEffectContainer
Use 44pt minimum hit targets
Use 8pt grid spacing
Use SF Symbols with .hierarchical

DON'T:

Apply glass to content (lists, tables)
Stack glass on glass without container
Use sharp corners
Go below 11pt text
Create touch targets < 44pt
Use full-color images on glass
Accessibility

System handles automatically:

Reduce Transparency → opaquer glass
Increase Contrast → visible borders
Reduce Motion → no bouncy effects
Dynamic Type → text scales

Manual override if needed:

@Environment(\.accessibilityReduceTransparency) var reduceTransparency
.glassEffect(reduceTransparency ? .identity : .regular)

References

For detailed patterns and examples, see:

references/components.md - Full component implementations
references/apple-hig.md - Complete Apple HIG guidelines
Weekly Installs
194
Repository
casper-studios/…ketplace
GitHub Stars
11
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass