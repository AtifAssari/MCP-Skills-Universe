---
rating: ⭐⭐
title: ui-useframe
url: https://skills.sh/verekia/r3f-gamedev/ui-useframe
---

# ui-useframe

skills/verekia/r3f-gamedev/ui-useframe
ui-useframe
Installation
$ npx skills add https://github.com/verekia/r3f-gamedev --skill ui-useframe
SKILL.md
UI useFrame

Sync UI elements outside the Canvas with the render loop using R3F v10's external useFrame.

Technique

Since React Three Fiber v10, useFrame can be used outside of the Canvas component. This allows updating DOM elements in sync with the 3D scene without using Drei's Html component.

Key Concepts
useFrame works outside <Canvas> in R3F v10+
Use refs to manipulate DOM elements directly for performance
Throttle with { fps: N } option since DOM manipulation is expensive
Useful for HUDs, debug info, and UI that doesn't need to be in 3D space
Usage
const Ui = () => {
  const ref = useRef<HTMLDivElement>(null)

  useFrame(() => {
    ref.current.innerText = `${position.x.toFixed(2)}, ${position.y.toFixed(2)}`
  }, { fps: 10 })

  return <div ref={ref} className="fixed top-4 right-4" />
}

// Place outside Canvas
<Canvas>
  <Scene />
</Canvas>
<Ui />


This skill is part of verekia's r3f-gamedev.

Weekly Installs
8
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