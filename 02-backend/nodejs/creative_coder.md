---
title: creative-coder
url: https://skills.sh/mae616/design-skills/creative-coder
---

# creative-coder

skills/mae616/design-skills/creative-coder
creative-coder
Installation
$ npx skills add https://github.com/mae616/design-skills --skill creative-coder
SKILL.md
Creative Coder Skill
When to Apply

Apply this skill when the request involves:

Animation, interaction, motion design, transitions, scroll effects, micro-UX, immersive experience
アニメーション、インタラクション、表現、演出、マイクロUX、没入感、スクロール、トランジション
Any visual expression or timing-based UI behavior
Core Principles
Experience is state transitions and timing, not just visuals. Design how things change over time.
Constraints first. Respect accessibility (prefers-reduced-motion) and performance (GPU load, INP/LCP).
Start minimal. Prototype small, keep only animations that add value.
Design Philosophy (Decision Rules)
Motion is information, but can also be noise. Articulate the purpose: visual guidance, state change comprehension, or delight.
Don't animate everything. Only animate important moments (create contrast).
Never break a11y. Support reduced motion, maintain contrast, preserve focus and operability.
Performance IS the experience. Avoid layout thrashing; prefer lightweight techniques.
Make it reversible. Implement animations as toggleable features.
Initial Questions to Clarify
What should users understand from this motion? (Purpose)
What environment is expected? (Mobile / low-spec / slow network)
What triggers this? (Hover / click / scroll / route change)
Is reduced motion support required? (If yes, it's mandatory)
Output Format (Follow This Order)
Purpose (what experience goal to achieve)
Specification (trigger, states, duration, easing, stop conditions)
Implementation approach (start minimal → enhance if needed)
Accessibility considerations (reduced motion, focus, operability)
Performance considerations (measurement points)
Next actions (prototype → integration)
Checklist
 Can you explain the motion's purpose? (Not just "looks cool")
 Does it respect prefers-reduced-motion?
 Are keyboard/focus operations unobstructed?
 Does it avoid layout recalculations? (Prefer transform/opacity)
 No negative impact on INP/LCP?
Common Pitfalls
Over-animating everything, reducing information density
Ignoring reduced motion, causing discomfort or danger
Heavy implementations (scroll handler abuse) degrading INP
Weekly Installs
63
Repository
mae616/design-skills
GitHub Stars
8
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass