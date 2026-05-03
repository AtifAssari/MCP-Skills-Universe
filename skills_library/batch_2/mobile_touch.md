---
title: mobile-touch
url: https://skills.sh/dylantarre/animation-principles/mobile-touch
---

# mobile-touch

skills/dylantarre/animation-principles/mobile-touch
mobile-touch
Installation
$ npx skills add https://github.com/dylantarre/animation-principles --skill mobile-touch
Summary

Disney's 12 animation principles applied to iOS and Android gestures, haptics, and native motion design.

Covers all 12 principles with mobile-specific implementations: squash & stretch via rubber-banding, anticipation through long-press previews, staging with sheet presentations, and arc-based swipe-to-dismiss curves
Provides platform-specific code examples for iOS spring animations and Android Material spring physics, plus haptic feedback pairing guidelines
Establishes timing targets: touch response under 100ms, transitions 250-350ms, and 60fps minimum (120fps on ProMotion displays)
Emphasizes gesture-driven animation must feel connected to finger input, respect safe areas and notches, and pair haptics with visual feedback for secondary actions
SKILL.md
Mobile Touch Animation

Apply Disney's 12 animation principles to mobile gestures, haptics, and native app motion.

Quick Reference
Principle	Mobile Implementation
Squash & Stretch	Rubber-banding, bounce on scroll limits
Anticipation	Peek before reveal, long-press preview
Staging	Sheet presentations, focus states
Straight Ahead / Pose to Pose	Gesture-driven vs preset transitions
Follow Through / Overlapping	Momentum scrolling, trailing elements
Slow In / Slow Out	iOS spring animations, Material easing
Arc	Swipe-to-dismiss curves, card throws
Secondary Action	Haptic pulse with visual feedback
Timing	Touch response <100ms, transitions 250-350ms
Exaggeration	Bounce amplitude, haptic intensity
Solid Drawing	Respect safe areas, consistent anchors
Appeal	60fps minimum, gesture continuity
Principle Applications

Squash & Stretch: Implement rubber-band effect at scroll boundaries. Pull-to-refresh should stretch content naturally. Buttons compress on touch.

Anticipation: Long-press shows preview before full action. Drag threshold provides visual hint before item lifts. Swipe shows edge of destination content.

Staging: Use sheet presentations to maintain context. Dim and scale background during modal focus. Hero transitions connect views meaningfully.

Straight Ahead vs Pose to Pose: Gesture-following animations (drag, pinch) are straight ahead—driven by touch input. System transitions (push, present) are pose to pose—predefined keyframes.

Follow Through & Overlapping: Content continues moving after finger lifts (momentum). Navigation bar elements animate slightly after main content. Lists items settle with stagger.

Slow In / Slow Out: iOS uses spring physics—configure mass, stiffness, damping. Android Material uses standard easing: FastOutSlowIn. Never use linear for user-initiated motion.

Arc: Thrown cards follow parabolic arcs. Swipe-to-dismiss curves based on velocity vector. FAB expand/collapse follows natural arc path.

Secondary Action: Pair haptic feedback with visual response. Button ripple accompanies press. Success checkmark triggers light haptic.

Timing: Touch acknowledgment: <100ms. Quick actions: 150-250ms. View transitions: 250-350ms. Complex animations: 350-500ms. Haptic should sync precisely with visual.

Exaggeration: Pull-to-refresh stretches beyond natural—makes feedback clear. Error shake is pronounced. Success animations celebrate appropriately.

Solid Drawing: Respect device safe areas during animation. Maintain consistent transform origins. Account for notch/dynamic island in motion paths.

Appeal: Minimum 60fps, target 120fps on ProMotion displays. Gesture-driven animation must feel connected to finger. Interruptible animations essential.

Platform Patterns
iOS
// Spring animation with follow-through
UIView.animate(withDuration: 0.5,
               delay: 0,
               usingSpringWithDamping: 0.7,
               initialSpringVelocity: 0.5,
               options: .curveEaseOut)

// Haptic pairing
let feedback = UIImpactFeedbackGenerator(style: .medium)
feedback.impactOccurred()

Android
// Material spring animation
SpringAnimation(view, DynamicAnimation.TRANSLATION_Y)
    .setSpring(SpringForce()
        .setStiffness(SpringForce.STIFFNESS_MEDIUM)
        .setDampingRatio(SpringForce.DAMPING_RATIO_MEDIUM_BOUNCY))
    .start()

Haptic Guidelines
Action	iOS	Android
Selection	.selection	EFFECT_TICK
Success	.success	EFFECT_CLICK
Warning	.warning	EFFECT_DOUBLE_CLICK
Error	.error	EFFECT_HEAVY_CLICK

Haptics are secondary action—always pair with visual confirmation.

Weekly Installs
1.6K
Repository
dylantarre/anim…inciples
GitHub Stars
35
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass