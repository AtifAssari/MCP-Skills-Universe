---
title: ios-hig
url: https://skills.sh/johnrogers/claude-swift-engineering/ios-hig
---

# ios-hig

skills/johnrogers/claude-swift-engineering/ios-hig
ios-hig
Installation
$ npx skills add https://github.com/johnrogers/claude-swift-engineering --skill ios-hig
SKILL.md
iOS Human Interface Guidelines

Apple's Human Interface Guidelines define the visual language, interaction patterns, and accessibility standards that make iOS apps feel native and intuitive. The core principle: clarity and consistency through thoughtful design.

Reference Loading Guide

ALWAYS load reference files if there is even a small chance the content may be required. It's better to have the context than to miss a pattern or make a mistake.

Reference	Load When
Interaction	Touch targets, navigation, layout, hierarchy, or gesture patterns
Content	Empty states, writing copy, typography, or placeholder text
Visual Design	Colors, materials, contrast, dark mode, or SF Symbols
Accessibility	VoiceOver, Dynamic Type, Reduce Motion, or accessibility labels
Feedback	Animations, haptics, loading states, or error messages
Performance	Responsiveness, system components, or app launch
Privacy	Permission requests, data handling, or privacy-sensitive APIs
Common Mistakes

Touch targets smaller than 44x44 points — Buttons and interactive elements must be at least 44x44 points (iOS) to accommodate thumbs. Smaller targets cause frustrated users and accessibility failures.

Ignoring Dynamic Type constraints — Text with fixed sizes doesn't respect user accessibility settings. Use Dynamic Type sizes, test with Large or Extra Large settings, and avoid hardcoded font sizes.

Insufficient color contrast in dark mode — Colors that work in light mode may fail accessibility in dark mode. Test with Reduce Contrast accessibility setting enabled for both modes.

Over-animating transitions — Animations that feel smooth at 60fps can trigger motion sickness in users with vestibular issues. Respect Reduce Motion settings and keep animations under 300ms.

Missing VoiceOver labels on custom controls — Custom buttons, toggles, or interactive views need .accessibilityLabel() and .accessibilityHint() or they're completely unusable to screen reader users.

Haptic overuse — Every action does NOT need haptic feedback. Reserve haptics for confirmations (purchase, critical action) and errors. Excessive haptics are annoying and drain battery.

Weekly Installs
196
Repository
johnrogers/clau…ineering
GitHub Stars
201
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass