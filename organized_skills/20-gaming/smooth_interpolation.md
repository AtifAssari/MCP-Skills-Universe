---
rating: ⭐⭐
title: smooth-interpolation
url: https://skills.sh/verekia/r3f-gamedev/smooth-interpolation
---

# smooth-interpolation

skills/verekia/r3f-gamedev/smooth-interpolation
smooth-interpolation
Installation
$ npx skills add https://github.com/verekia/r3f-gamedev --skill smooth-interpolation
SKILL.md
Smooth Interpolation

Animate values smoothly using exponential decay instead of linear interpolation.

Technique

Use exponential smoothing formulas to interpolate between current and target values. This creates a natural easing effect that's frame-rate independent.

Key Concepts
Exponential smoothing: (target - current) * (1 - Math.exp(-speed * dt))
Exponential decay: target + (current - target) * Math.exp(-decay * dt)
Both formulas produce the same result with different parameters
Speed/decay values from 1-25 work well
Frame-rate independent due to delta time usage
Usage
const addSmoothExp = (current: number, target: number, speed: number, dt: number) =>
  (target - current) * (1 - Math.exp(-speed * dt))

const expDecay = (current: number, target: number, decay: number, dt: number) =>
  target + (current - target) * Math.exp(-decay * dt)

useFrame((_, delta) => {
  mesh.position.x += addSmoothExp(mesh.position.x, targetX, 3, delta)
  // or
  mesh.position.x = expDecay(mesh.position.x, targetX, 3, delta)
})

References
Exponential Smoothing
Lerp Smoothing is Broken

This skill is part of verekia's r3f-gamedev.

Weekly Installs
12
Repository
verekia/r3f-gamedev
GitHub Stars
29
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass