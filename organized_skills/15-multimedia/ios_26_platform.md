---
rating: ⭐⭐
title: ios-26-platform
url: https://skills.sh/johnrogers/claude-swift-engineering/ios-26-platform
---

# ios-26-platform

skills/johnrogers/claude-swift-engineering/ios-26-platform
ios-26-platform
Installation
$ npx skills add https://github.com/johnrogers/claude-swift-engineering --skill ios-26-platform
SKILL.md
iOS 26 Platform

iOS 26 introduces Liquid Glass, Apple's next-generation material design system that dynamically bends light, moves organically, and adapts automatically across all platforms.

Overview

iOS 26 modernizes UI with new materials (Liquid Glass), SwiftUI APIs (WebView, Chart3D, @Animatable), and advanced features (@BackoffAnimation, free-form windows). The core principle: modern UI gets updated automatically at compile time; most Liquid Glass benefits are "free" from recompiling with Xcode 26.

Reference Loading Guide

ALWAYS load reference files if there is even a small chance the content may be required. It's better to have the context than to miss a pattern or make a mistake.

Reference	Load When
Liquid Glass	Implementing glass effects, choosing Regular vs Clear variants, or understanding visual properties
Automatic Adoption	Understanding what iOS 26 changes automatically vs what requires code
SwiftUI APIs	Using WebView, Chart3D, @Animatable, AttributedString, or new view modifiers
Toolbar & Navigation	Customizing toolbars with spacers, morphing, glass button styles, or search
Backward Compatibility	Supporting iOS 17/18 alongside iOS 26, or using UIDesignRequiresCompatibility
Core Workflow
Check deployment target — iOS 26+ required for Liquid Glass
Recompile with Xcode 26 — Standard controls get glass automatically
Identify navigation layer — Apply glass to tab bars, toolbars, navigation (not content)
Choose variant — Regular (95% of cases) or Clear (media-rich backgrounds only)
Add @available guards — For backward compatibility with iOS 17/18
Test accessibility — Verify Reduce Transparency, Increase Contrast, Reduce Motion
Common Mistakes

Ignoring backward compatibility — Targeting iOS 26+ without @available guards breaks iOS 17/18 support. Always use if #available(iOS 26, *) for Liquid Glass or new APIs.

Over-using glass effect — Applying glass to content areas, not just navigation, creates visual noise. Glass works for: tab bars, toolbars, sheets, navigation. NOT for content areas.

Animation performance issues — Liquid Glass animations can be expensive. Respect Reduce Motion accessibility setting and profile with Instruments 26 before shipping.

Assuming Clear variant looks good — Clear is for media-rich backgrounds only (photos, video). Regular variant is correct 95% of the time. Only use Clear if you explicitly need the ultra-transparency.

Not testing on actual devices — Simulator rendering differs from hardware. Test glass effects on iPhone 15 Pro, iPad, and Mac to verify visual quality.

Using old UIView patterns with new glass — Mixing UIView-based navigation with iOS 26 glass creates inconsistent appearances. Migrate fully to SwiftUI or wrap carefully with UIViewRepresentable.

Weekly Installs
161
Repository
johnrogers/clau…ineering
GitHub Stars
201
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn