---
title: elite-accessibility
url: https://skills.sh/rshvr/elite-web-design/elite-accessibility
---

# elite-accessibility

skills/rshvr/elite-web-design/elite-accessibility
elite-accessibility
Installation
$ npx skills add https://github.com/rshvr/elite-web-design --skill elite-accessibility
SKILL.md
Elite Accessibility

Making motion-rich websites accessible to everyone.

Quick Reference
Topic	Reference File
Reduced motion	reduced-motion.md
WCAG contrast	wcag-contrast.md
Focus & keyboard	focus-keyboard.md
Inclusive aesthetics	inclusive-aesthetics.md
Touch interaction	touch-interaction.md
Why This Matters

Motion can cause real harm:

Vestibular disorders affect ~35% of adults over 40
Motion sensitivity can trigger nausea, dizziness, migraines
Cognitive overload - animations can distract users with ADHD or anxiety
Seizure risk - flashing content can trigger photosensitive epilepsy

Accessibility isn't optional - it's a design requirement.

The Golden Rule

Every animation MUST have a prefers-reduced-motion alternative.

This is non-negotiable for elite web design.

Quick Implementation
CSS Approach
/* Global reduced motion */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

GSAP Approach
// ALWAYS use gsap.matchMedia() for motion preferences
const mm = gsap.matchMedia();

mm.add('(prefers-reduced-motion: no-preference)', () => {
  // Full animations for users who want them
  gsap.from('.hero-content', {
    opacity: 0,
    y: 50,
    duration: 1,
    stagger: 0.2
  });
});

mm.add('(prefers-reduced-motion: reduce)', () => {
  // Instant state for users who prefer reduced motion
  gsap.set('.hero-content', { opacity: 1, y: 0 });
});

CSS Scroll-Driven Animations
/* Only enable scroll animations if motion is OK */
@media (prefers-reduced-motion: no-preference) {
  .scroll-animated {
    animation: reveal linear;
    animation-timeline: scroll();
  }
}

/* Fallback: just show the content */
@media (prefers-reduced-motion: reduce) {
  .scroll-animated {
    opacity: 1;
    transform: none;
  }
}

What to Provide Instead

Don't just disable animations - provide alternatives:

Full Animation	Reduced Motion Alternative
Slide in from side	Instant appear or fade only
Parallax scrolling	Static positioning
Scroll-triggered reveals	Content visible by default
Bouncing/pulsing	Static or subtle opacity change
Page transitions	Instant navigation
Auto-playing carousels	Static slide, manual controls
Example: Reveal Animation
const mm = gsap.matchMedia();

// Full experience
mm.add('(prefers-reduced-motion: no-preference)', () => {
  gsap.from('.card', {
    opacity: 0,
    y: 30,
    duration: 0.6,
    stagger: 0.1,
    scrollTrigger: {
      trigger: '.cards-section',
      start: 'top 80%'
    }
  });
});

// Reduced motion: simple fade, no movement
mm.add('(prefers-reduced-motion: reduce)', () => {
  gsap.from('.card', {
    opacity: 0,
    duration: 0.3,  // Shorter
    stagger: 0.05,  // Faster stagger
    scrollTrigger: {
      trigger: '.cards-section',
      start: 'top 80%'
    }
  });
});

Animation Guidelines
Safe Animations (Usually OK)
Opacity changes (fade in/out)
Small scale changes (0.95 → 1)
Color transitions
Short durations (< 300ms)
Problematic Animations (Need Alternatives)
Large movements (sliding, flying)
Parallax effects
Zooming (in/out)
Rotation
Bouncing/pulsing
Infinite loops
Dangerous (Avoid or Gate Heavily)
Flashing/strobing (can cause seizures)
Rapid movement
Auto-playing video with motion
Spinning elements
Testing Reduced Motion
macOS

System Preferences → Accessibility → Display → Reduce motion

Windows

Settings → Ease of Access → Display → Show animations in Windows (off)

iOS

Settings → Accessibility → Motion → Reduce Motion

Chrome DevTools
Open DevTools (F12)
Cmd/Ctrl + Shift + P → "Render"
Find "Emulate CSS media feature prefers-reduced-motion"
Contrast Quick Reference
WCAG Requirements
Content	AA (Minimum)	AAA (Enhanced)
Normal text	4.5:1	7:1
Large text (18px+)	3:1	4.5:1
UI components	3:1	3:1
Focus indicators	3:1	3:1
Quick Test

Use browser extensions:

axe DevTools
WAVE
Stark

See wcag-contrast.md for detailed guidance.

Focus States

Every interactive element needs visible focus:

/* Base focus style */
:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
}

/* Remove default, add custom */
button:focus {
  outline: none;
}

button:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
  box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.2);
}


See focus-keyboard.md for keyboard navigation patterns.

Screen Reader Considerations
Hide Decorative Animations
<!-- Decorative animation should be hidden -->
<div class="animated-background" aria-hidden="true"></div>

<!-- Content animations: ensure content is accessible -->
<div class="animated-card" role="article">
  <!-- Content here is accessible -->
</div>

Announce Dynamic Content
<!-- Live region for content that updates -->
<div aria-live="polite" aria-atomic="true">
  <p>Loading complete. Showing 12 results.</p>
</div>

Implementation Checklist
Every Animation Must:
 Check prefers-reduced-motion
 Provide reduced/no-motion alternative
 Not flash more than 3 times per second
 Not auto-play infinitely without user control
 Not cause layout shift that disrupts reading
Every Page Must:
 Pass WCAG AA contrast (4.5:1 for text)
 Have visible focus states
 Be keyboard navigable
 Work without JavaScript animations
 Have skip links for keyboard users
Resources
MDN: prefers-reduced-motion
WCAG 2.1 Guidelines
A11y Project
Inclusive Design Principles
Weekly Installs
20
Repository
rshvr/elite-web-design
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass