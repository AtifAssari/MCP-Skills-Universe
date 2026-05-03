---
title: 12-principles-of-animation
url: https://skills.sh/raphaelsalaja/userinterface-wiki/12-principles-of-animation
---

# 12-principles-of-animation

skills/raphaelsalaja/userinterface-wiki/12-principles-of-animation
12-principles-of-animation
Installation
$ npx skills add https://github.com/raphaelsalaja/userinterface-wiki --skill 12-principles-of-animation
SKILL.md
12 Principles of Animation

Review animation code for compliance with Disney's 12 principles adapted for web interfaces.

How It Works
Read the specified files (or prompt user for files/pattern)
Check against all rules below
Output findings in file:line format
Rule Categories
Priority	Category	Prefix
1	Timing	timing-
2	Easing	easing-
3	Physics	physics-
4	Staging	staging-
Rules
Timing Rules
timing-under-300ms

User-initiated animations must complete within 300ms.

Fail:

.button { transition: transform 400ms; }


Pass:

.button { transition: transform 200ms; }

timing-consistent

Similar elements must use identical timing values.

Fail:

.button-primary { transition: 200ms; }
.button-secondary { transition: 150ms; }


Pass:

.button-primary { transition: 200ms; }
.button-secondary { transition: 200ms; }

timing-no-entrance-context-menu

Context menus should not animate on entrance (exit only).

Fail:

<motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} />


Pass:

<motion.div exit={{ opacity: 0 }} />

Easing Rules
easing-entrance-ease-out

Entrances must use ease-out (arrive fast, settle gently).

Fail:

.modal-enter { animation-timing-function: ease-in; }


Pass:

.modal-enter { animation-timing-function: ease-out; }

easing-exit-ease-in

Exits must use ease-in (build momentum before departure).

Fail:

.modal-exit { animation-timing-function: ease-out; }


Pass:

.modal-exit { animation-timing-function: ease-in; }

easing-no-linear-motion

Linear easing should only be used for progress indicators, not motion.

Fail:

.card { transition: transform 200ms linear; }


Pass:

.progress-bar { transition: width 100ms linear; }

easing-natural-decay

Use exponential ramps, not linear, for natural decay.

Fail:

gain.gain.linearRampToValueAtTime(0, t + 0.05);


Pass:

gain.gain.exponentialRampToValueAtTime(0.001, t + 0.05);

Physics Rules
physics-active-state

Interactive elements must have active/pressed state with scale transform.

Fail:

.button:hover { background: var(--gray-3); }
/* Missing :active state */


Pass:

.button:active { transform: scale(0.98); }

physics-subtle-deformation

Squash/stretch deformation must be subtle (0.95-1.05 range).

Fail:

<motion.div whileTap={{ scale: 0.8 }} />


Pass:

<motion.div whileTap={{ scale: 0.98 }} />

physics-spring-for-overshoot

Use springs (not easing) when overshoot-and-settle is needed.

Fail:

<motion.div transition={{ duration: 0.3, ease: "easeOut" }} />
// When element should bounce/settle


Pass:

<motion.div transition={{ type: "spring", stiffness: 500, damping: 30 }} />

physics-no-excessive-stagger

Stagger delays must not exceed 50ms per item.

Fail:

transition={{ staggerChildren: 0.15 }}


Pass:

transition={{ staggerChildren: 0.03 }}

Staging Rules
staging-one-focal-point

Only one element should animate prominently at a time.

Fail:

// Multiple elements with competing entrance animations
<motion.div animate={{ scale: 1.1 }} />
<motion.div animate={{ scale: 1.1 }} />

staging-dim-background

Modal/dialog backgrounds should dim to direct focus.

Fail:

.overlay { background: transparent; }


Pass:

.overlay { background: var(--black-a6); }

staging-z-index-hierarchy

Animated elements must respect z-index layering.

Fail:

.tooltip { /* No z-index, may render behind other elements */ }


Pass:

.tooltip { z-index: 50; }

Output Format

When reviewing files, output findings as:

file:line - [rule-id] description of issue

Example:
components/modal/index.tsx:45 - [timing-under-300ms] Exit animation 400ms exceeds 300ms limit
components/button/styles.module.css:12 - [physics-active-state] Missing :active transform

Summary Table

After findings, output a summary:

Rule	Count	Severity
timing-under-300ms	2	HIGH
physics-active-state	3	MEDIUM
easing-entrance-ease-out	1	MEDIUM
References
The Illusion of Life: Disney Animation
Apple WWDC23: Animate with Springs
Weekly Installs
282
Repository
raphaelsalaja/u…ace-wiki
GitHub Stars
722
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass