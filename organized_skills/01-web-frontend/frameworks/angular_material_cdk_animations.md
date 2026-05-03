---
rating: ⭐⭐
title: angular-material-cdk-animations
url: https://skills.sh/7spade/black-tortoise/angular-material-cdk-animations
---

# angular-material-cdk-animations

skills/7spade/black-tortoise/angular-material-cdk-animations
angular-material-cdk-animations
Installation
$ npx skills add https://github.com/7spade/black-tortoise --skill angular-material-cdk-animations
SKILL.md
SKILL: Angular Material + CDK + Animations
Use when
Adding or refactoring UI that uses @angular/material, @angular/cdk, or @angular/animations.
Building overlays, drag-drop, virtual scroll, focus management, or motion/transition behaviors.
Workflow
Start from the simplest Material component that fits; only drop to CDK primitives when needed.
Keep inputs/outputs signal-first; avoid component-internal RxJS state.
If using CDK overlays/focus traps/observers, define ownership and dispose on destroy.
If adding motion:
CSS transitions for small state changes
@angular/animations only for coordinated/complex transitions
always respect prefers-reduced-motion
Validate a11y: labels, focus order, keyboard operation, and visible focus.
Checklist (PR-ready)
Uses M3 tokens (no raw hex/px).
Overlays/listeners/observers cleaned up.
Reduced-motion path exists.
No “cute” drag/animation that adds complexity without user value.
References
.github/instructions/62-angular-core-ui-copilot-instructions.md
.github/instructions/71-angular-material-cdk-animations-copilot-instructions.md
.github/skills/material-design-3/skill.md
.github/skills/angular-ecosystem/skill.md
Weekly Installs
10
Repository
7spade/black-tortoise
First Seen
Feb 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass