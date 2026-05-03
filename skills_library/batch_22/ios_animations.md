---
title: ios-animations
url: https://skills.sh/pproenca/dot-skills/ios-animations
---

# ios-animations

skills/pproenca/dot-skills/ios-animations
ios-animations
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill ios-animations
SKILL.md
dot-skills — Airbnb iOS SwiftUI Animations Best Practices

Opinionated, strict animation craft guide for SwiftUI iOS 26 / Swift 6.2 apps. Contains 50 rules across 8 categories, prioritized by impact. Derived from Airbnb Engineering motion patterns, Apple WWDC sessions, and Apple Human Interface Guidelines. Mandates @Equatable on every animated view, motion tokens for all spring/timing values, and design system tokens for layout.

Mandated Architecture Alignment

This skill is designed to work alongside swift-ui-architect and ios-design-system. All code examples follow the same non-negotiable constraints:

@Equatable macro on every view (Airbnb measured 15% scroll hitch reduction)
@Observable for complex animation state that involves business logic triggers
@State for view-owned animation state (toggle booleans, drag offsets)
Design system tokens: Spacing.xs/sm/md/lg, Radius.sm/md/lg — zero hardcoded layout numbers
Motion tokens: Motion.standard/responsive/playful — zero scattered spring literals
Semantic colors: .backgroundSurface, .accentPrimary — no raw Color literals in views
Feature animations remain presentation-only; data/network concerns stay in Data package
Scope & Relationship to Sibling Skills

This skill is the motion layer — it teaches how to BUILD fluid, performant animations. When loaded alongside sibling skills:

Sibling Skill	Its Focus	This Skill's Focus
swift-ui-architect	Architecture (modular MVVM-C, route shells, protocol boundaries)	Animation architecture (motion tokens, spring selection, orchestration)
ios-design-system	Design system infrastructure (tokens, styles, governance)	Motion tokens and animated component patterns
ios-hig	HIG compliance patterns	Motion-specific HIG (reduce motion, spatial continuity)

Out of scope: Designer-authored vector animations (use Lottie for After Effects exports). Complex UIKit transition controllers (see Airbnb's declarative transition framework). This skill covers programmatic SwiftUI animations only.

Clinic Architecture Contract (iOS 26 / Swift 6.2)

All guidance in this skill assumes the clinic modular MVVM-C architecture:

Feature modules import Domain + DesignSystem only (never Data, never sibling features)
App target is the convergence point and owns DependencyContainer, concrete coordinators, and Route Shell wiring
Domain stays pure Swift and defines models plus repository, *Coordinating, ErrorRouting, and AppError contracts
Data owns SwiftData/network/sync/retry/background I/O and implements Domain protocols
Read/write flow defaults to stale-while-revalidate reads and optimistic queued writes
ViewModels call repository protocols directly (no default use-case/interactor layer)
When to Apply

Reference these guidelines when:

Adding animations to SwiftUI views or transitions
Building gesture-driven interactions (drag, swipe, pan)
Connecting views with spatial transitions (expand/collapse, navigation morphs)
Designing micro-interactions (button press, toggle, loading states)
Making content changes feel physical (number rolls, symbol replacements)
Choreographing multi-element animation sequences (KeyframeAnimator, PhaseAnimator)
Defining motion tokens for a design system
Reviewing animation code for performance, accessibility, and architecture compliance
Rule Categories by Priority
Priority	Category	Impact	Prefix	Rules
1	Spring Physics	CRITICAL	spring-	8
2	Timing & Feel	CRITICAL	feel-	6
3	Gesture Continuity	HIGH	gesture-	7
4	Spatial Transitions	HIGH	spatial-	6
5	Micro-interactions	HIGH	micro-	6
6	Orchestration	HIGH	orch-	5
7	Craft & Polish	HIGH	craft-	5
8	Content Motion	MEDIUM-HIGH	content-	5
Quick Reference
1. Spring Physics (CRITICAL)
spring-motion-tokens — Define motion tokens as a caseless enum for all spring presets
spring-smooth-default — Default to .smooth spring for all UI transitions
spring-snappy-responsive — Use .snappy spring for responsive interactions
spring-bouncy-celebration — Use .bouncy spring for playful and celebratory moments
spring-custom-parameters — Tune custom springs with response and dampingFraction
spring-velocity-preservation — Springs preserve velocity on interruption
spring-never-linear — Never use linear or easeInOut for interactive UI
spring-completion-chaining — Use withAnimation completion for chained sequences
2. Timing & Feel (CRITICAL)
feel-250ms-max — Keep UI animations under 250ms
feel-faster-better — Faster animations almost always feel better
feel-asymmetric-enter-exit — Use asymmetric timing for enter and exit
feel-distance-proportional — Match duration to distance traveled
feel-haptic-sync — Sync haptic feedback to visual animation keyframes
feel-stagger-timing — Stagger reveals at 30-50ms intervals
3. Gesture Continuity (HIGH)
gesture-rubber-band — Rubber band at drag boundaries
gesture-momentum-dismiss — Dismiss on velocity OR distance threshold
gesture-snap-points — Use velocity-aware snap points
gesture-interruptible — Make all gesture animations interruptible
gesture-scroll-drag-conflict — Resolve scroll and drag gesture conflicts
gesture-state-transient — Use GestureState for transient drag state
gesture-projected-landing — Project gesture velocity for natural landing position
4. Spatial Transitions (HIGH)
spatial-matched-geometry — Use matchedGeometryEffect for expand/collapse morphs
spatial-zoom-navigation — Use zoom navigation transition for collection detail (iOS 18)
spatial-transition-origin — Anchor transitions to their trigger location
spatial-hero-shared-element — Share multiple element IDs for rich hero animations
spatial-sheet-morph — Use matchedGeometryEffect for sheet presentations
spatial-tab-continuity — Maintain spatial direction in tab transitions
5. Micro-interactions (HIGH)
micro-button-press-scale — Scale buttons to 0.97 on press for tactile feedback
micro-haptic-pairing — Pair every visual state change with haptic feedback
micro-symbol-effect — Use symbolEffect for SF Symbol animations
micro-toggle-bounce — Add bounce to toggle state changes
micro-long-press-fill — Animate progressive fill for long press actions
micro-loading-phase — Use repeating spring for organic loading states
6. Orchestration (HIGH)
orch-phase-animator — Use PhaseAnimator for multi-step sequences
orch-keyframe-animator — Use KeyframeAnimator for timeline-precise motion
orch-stagger-children — Stagger child elements for orchestrated reveals
orch-coordinated-entrance — Coordinate multi-element entrances with shared trigger
orch-timeline-view — Use TimelineView for continuous repeating animations
7. Craft & Polish (HIGH)
craft-reduce-motion — Respect accessibilityReduceMotion with crossfade fallback
craft-blur-bridge — Use blur to bridge imperfect transition states
craft-drawing-group — Use drawingGroup() for Metal-backed complex animations
craft-geometry-group — Use geometryGroup() to isolate layout animation propagation
craft-transaction-debug — Use Transaction to debug and override animation behavior
8. Content Motion (MEDIUM-HIGH)
content-numeric-text — Use contentTransition(.numericText) for number changes
content-scroll-transition — Use scrollTransition for scroll-position effects
content-visual-effect — Use visualEffect for position-aware animations
content-symbol-replace — Animate symbol replacement with contentTransition
content-text-renderer — Use Text Renderer for character-level animation (iOS 18)
How to Use

Read individual reference files for detailed explanations with incorrect/correct code examples:

Section definitions — Category structure and impact levels
Rule template — Template for adding new rules
Reference Files
File	Description
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
155
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass