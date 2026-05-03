---
title: page-transitions
url: https://skills.sh/dylantarre/animation-principles/page-transitions
---

# page-transitions

skills/dylantarre/animation-principles/page-transitions
page-transitions
Installation
$ npx skills add https://github.com/dylantarre/animation-principles --skill page-transitions
SKILL.md
Page Transition Animation

Apply Disney's 12 animation principles to route changes, view transitions, and navigation patterns.

Quick Reference
Principle	Page Transition Implementation
Squash & Stretch	Entering page elastic effect
Anticipation	Exit animation before enter
Staging	Hero elements bridge views
Straight Ahead / Pose to Pose	Shared element vs crossfade
Follow Through / Overlapping	Content settles after nav
Slow In / Slow Out	Asymmetric enter/exit easing
Arc	Slide transitions with curve
Secondary Action	Background, nav state changes
Timing	200-500ms total transition
Exaggeration	Reserved for emphasis moments
Solid Drawing	Consistent spatial model
Appeal	Smooth, oriented navigation
Principle Applications

Squash & Stretch: Incoming pages can have subtle elastic settle. Modal sheets bounce slightly on full open. Pull-to-navigate stretches before triggering.

Anticipation: Current page begins exit before new page enters. Slight fade or scale prepares for change. Navigation indicator updates before page swaps.

Staging: Shared/hero elements maintain context across views. Common elements (nav, footer) stay stable. New content area receives transition focus.

Straight Ahead vs Pose to Pose: Shared element transitions morph continuously (straight ahead). Crossfades swap between discrete states (pose to pose). Choose based on content relationship.

Follow Through & Overlapping: Page content settles after initial position. Staggered content entry—header, then body, then footer. Images load with subtle fade after container.

Slow In / Slow Out: Exit: ease-in (accelerate away). Enter: ease-out (decelerate in). Combined: ease-in-out for shared elements. Never linear—feels broken.

Arc: Slide transitions can curve slightly. Stack navigation implies z-depth. Circular reveals expand from trigger point.

Secondary Action: Header updates title during transition. Bottom nav indicator moves. Background color shifts. Scroll position resets with transition.

Timing: Quick transitions: 200-300ms. Standard: 300-400ms. Complex: 400-500ms. Modal/sheet: 250-350ms. Back navigation often faster than forward.

Exaggeration: Save exaggeration for key moments—onboarding, achievement. Regular navigation should be smooth, not theatrical. Users navigate frequently.

Solid Drawing: Maintain consistent spatial metaphor. If pages stack, maintain z-order. If pages slide, direction should be consistent. Users build mental model from transitions.

Appeal: Transitions should feel helpful, not impressive. Fast, smooth, oriented. Users should understand where they came from and went to.

Transition Patterns
Crossfade (Default)
.page-exit {
    opacity: 1;
}
.page-exit-active {
    opacity: 0;
    transition: opacity 200ms ease-in;
}
.page-enter {
    opacity: 0;
}
.page-enter-active {
    opacity: 1;
    transition: opacity 200ms ease-out;
}

Slide (Hierarchical)
/* Forward navigation */
.page-enter {
    transform: translateX(100%);
}
.page-enter-active {
    transform: translateX(0);
    transition: transform 300ms ease-out;
}
.page-exit-active {
    transform: translateX(-30%);
    transition: transform 300ms ease-in;
}

/* Back navigation - reversed */
.page-enter {
    transform: translateX(-30%);
}
.page-exit-active {
    transform: translateX(100%);
}

Shared Element (Hero)
// View Transitions API
document.startViewTransition(() => {
    updateDOM();
});

// CSS for specific element
.hero-image {
    view-transition-name: hero;
}
::view-transition-old(hero),
::view-transition-new(hero) {
    animation-duration: 300ms;
}

Timing Reference
Transition Type	Duration	Exit	Enter
Crossfade	200-300ms	ease-in	ease-out
Slide forward	300-400ms	ease-in	ease-out
Slide back	250-350ms	ease-in	ease-out
Modal open	250-350ms	—	ease-out
Modal close	200-300ms	ease-in	—
Shared element	300-400ms	n/a	ease-in-out
Tab switch	150-200ms	instant	ease-out
Navigation Patterns
Pattern	Transition	Direction
Drill-down (list→detail)	Slide left / shared element	Right = forward
Tab bar	Fade / slide	Horizontal
Bottom sheet	Slide up	Vertical
Modal	Scale + fade	Z-axis
Back button	Reverse of forward	Left = back
Performance
Use transform and opacity only
Hardware acceleration: will-change: transform
Reduce motion: instant transitions
Test on slow devices—transitions must not block
View Transitions API: native performance
Weekly Installs
141
Repository
dylantarre/anim…inciples
GitHub Stars
35
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass