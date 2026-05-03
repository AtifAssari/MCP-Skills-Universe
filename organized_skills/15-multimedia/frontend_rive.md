---
rating: ⭐⭐⭐
title: frontend-rive
url: https://skills.sh/petbrains/mvp-builder/frontend-rive
---

# frontend-rive

skills/petbrains/mvp-builder/frontend-rive
frontend-rive
Installation
$ npx skills add https://github.com/petbrains/mvp-builder --skill frontend-rive
SKILL.md
Rive

Interactive animations with built-in state machines. Animation logic inside the .riv file.

When to Use
Animations that REACT to input (hover, click, data)
Animated buttons, toggles, checkboxes
Progress indicators driven by values
Multi-state characters/icons
Complex state transitions
When NOT to Use
Simple decorative loops → Lottie
Static illustrations → SVG
Quick spinners → CSS/Lottie
Key Concept: State Machines
┌─────────────────────────────────┐
│         Rive State Machine      │
│   ┌──────┐  hover  ┌───────┐    │
│   │ Idle │ ──────► │ Hover │    │
│   └──────┘         └───────┘    │
│       ▲    click       │        │
│       └──────────── ◄──┘        │
│                                 │
│   Inputs: hover (bool), click   │
└─────────────────────────────────┘
You control inputs → Rive handles animations

Process

SETUP → CONNECT → CONTROL

Install: npm install @rive-app/react-canvas
Load .riv file with state machine
Get inputs via useStateMachineInput
Connect to UI events
Quick Start
import { useRive, useStateMachineInput } from '@rive-app/react-canvas';

function InteractiveButton() {
  const { rive, RiveComponent } = useRive({
    src: '/button.riv',
    stateMachines: 'ButtonState',
    autoplay: true,
  });

  const hover = useStateMachineInput(rive, 'ButtonState', 'hover');
  const press = useStateMachineInput(rive, 'ButtonState', 'pressed');

  return (
    <RiveComponent
      onMouseEnter={() => hover && (hover.value = true)}
      onMouseLeave={() => hover && (hover.value = false)}
      onMouseDown={() => press && (press.value = true)}
      onMouseUp={() => press && (press.value = false)}
    />
  );
}

Input Types
Boolean:  input.value = true/false     # hover, isActive
Number:   input.value = 75             # progress (0-100)
Trigger:  input.fire()                 # onClick, onComplete

Common Patterns
Toggle:
  - Boolean input "isOn"
  - onClick: toggle value

Progress:
  - Number input "progress" (0-100)
  - useEffect: sync with prop

Notification Bell:
  - Number input "count"
  - Trigger input "ring"
  - onClick: fire() trigger

Decision: Rive vs Lottie
Need	Use
Just plays/loops	Lottie
Reacts to hover	Rive
Controlled by data	Rive
Multiple states	Rive
Simple loader	Lottie
Layout & Sizing
// Container controls size
<div className="w-64 h-64">
  <RiveComponent />
</div>

// Responsive with aspect ratio
<div className="w-full aspect-video max-w-2xl">
  <RiveComponent />
</div>

SSR & Hydration
// Always 'use client'
'use client'

// Dynamic import for heavy animations
const Animation = dynamic(() => import('./RiveAnimation'), { ssr: false })

// Or mounted check
const [mounted, setMounted] = useState(false)
useEffect(() => setMounted(true), [])
if (!mounted) return <Skeleton />

Performance
// Lazy load
const Rive = dynamic(() => import('./RiveComponent'), { ssr: false })

// Pause when not visible
const { ref, inView } = useInView()
useEffect(() => { inView ? rive?.play() : rive?.pause() }, [inView])

Troubleshooting
"Animation not playing":
  → Check autoplay: true
  → Check stateMachines name (case-sensitive)
  → Check .riv path in public/

"Inputs undefined":
  → Always check: if (input) input.value = x
  → Verify input names match Rive editor

"Hydration mismatch":
  → Add 'use client'
  → Use dynamic(() => ..., { ssr: false })

"Wrong size":
  → Container needs explicit width/height
  → Use aspect-ratio utilities

References
patterns.md — Toggle, Checkbox, Progress, Like button, Form integration
External Resources
https://rive.app/docs/runtimes/react — React runtime docs
https://rive.app/community — Free .riv files
For latest API → use context7 skill
Weekly Installs
8
Repository
petbrains/mvp-builder
GitHub Stars
10
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass