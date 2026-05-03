---
rating: ⭐⭐
title: haptics
url: https://skills.sh/johnrogers/claude-swift-engineering/haptics
---

# haptics

skills/johnrogers/claude-swift-engineering/haptics
haptics
Installation
$ npx skills add https://github.com/johnrogers/claude-swift-engineering --skill haptics
SKILL.md
Haptics

Haptic feedback provides tactile confirmation of user actions and system events. When designed thoughtfully, haptics transform interfaces from functional to delightful.

Overview

Haptics should enhance interactions, not dominate them. The core principle: haptic feedback is like sound design—every haptic should have purpose (confirmation, error, warning), timing (immediate or delayed), and restraint (less is more).

Reference Loading Guide

ALWAYS load reference files if there is even a small chance the content may be required. It's better to have the context than to miss a pattern or make a mistake.

Reference	Load When
UIFeedbackGenerator	Using simple impact/selection/notification haptics
Core Haptics	Creating custom patterns with CHHapticEngine
AHAP Patterns	Working with Apple Haptic Audio Pattern files
Design Principles	Applying Causality, Harmony, Utility framework
Core Workflow
Choose complexity level: Simple (UIFeedbackGenerator) vs Custom (Core Haptics)
For simple haptics: Use UIImpactFeedbackGenerator, UISelectionFeedbackGenerator, or UINotificationFeedbackGenerator
For custom patterns: Create CHHapticEngine, define CHHapticEvents, build CHHapticPattern
Prepare before triggering: Call prepare() to reduce latency
Apply design principles: Ensure Causality (timing), Harmony (multimodal), Utility (meaningful)
System Requirements
iOS 10+ for UIFeedbackGenerator
iOS 13+ for Core Haptics (CHHapticEngine)
iPhone 8+ for Core Haptics hardware support
Physical device required - haptics cannot be tested in Simulator
Common Mistakes

Haptic feedback on every action — Every button doesn't need haptics. Reserve haptics for critical confirmations (purchase, delete, settings change). Over-haptics are annoying and drain battery.

Triggering haptics on main thread blocks — Long haptic patterns can freeze UI briefly. Use background threads or async for Core Haptics prepare() calls to prevent jank.

Haptic without audio/visual feedback — Relying ONLY on haptics means deaf or deaf-blind users miss feedback. Always pair haptics with sound or visual response.

Ignoring haptic settings — Some users disable haptics system-wide. Check UIFeedbackGenerator.isHapticFeedbackEnabled before triggering. Graceful degradation is required.

AHAP file errors silently — Invalid AHAP files fail silently without errors. Test with Xcode's haptic designer and validate file syntax before shipping.

Forgetting battery impact — Continuous haptic patterns (progress bars, loading states) drain battery fast. Use haptics for state changes only, not ongoing feedback.

Weekly Installs
105
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