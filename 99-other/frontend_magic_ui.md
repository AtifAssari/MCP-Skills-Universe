---
title: frontend-magic-ui
url: https://skills.sh/petbrains/mvp-builder/frontend-magic-ui
---

# frontend-magic-ui

skills/petbrains/mvp-builder/frontend-magic-ui
frontend-magic-ui
Installation
$ npx skills add https://github.com/petbrains/mvp-builder --skill frontend-magic-ui
SKILL.md
Magic UI

150+ animated components for SaaS landing pages. Professional polish, production-ready.

When to Use
Number/stat animations (tickers, counters)
Logo walls (marquee)
Bento grid layouts
Device mockups (iPhone, Safari)
Text animations (typing, word rotate)
Shimmer/rainbow buttons
When NOT to Use
Basic UI → shadcn/ui
Dramatic hero effects → Aceternity
State-driven animations → Rive
Process

NEED → ADD → CUSTOMIZE

Identify component type
Install: npx magicui-cli@latest add [component]
Customize props/styles
Dependencies
npm install framer-motion clsx tailwind-merge

Component Categories
Text:       number-ticker, typing-animation, word-rotate, flip-text, morphing-text
Buttons:    shimmer-button, rainbow-button, pulsating-button, shiny-button
Patterns:   dot-pattern, grid-pattern, retro-grid, particles, meteors
Mockups:    iphone-15-pro, safari, android
Layout:     bento-grid, marquee, dock, animated-list, file-tree
Effects:    orbiting-circles, animated-beam, border-beam, confetti, globe

Decision Tree
Need animated component?
  ├─ Stats/numbers → number-ticker
  ├─ Logo carousel → marquee
  ├─ Feature grid → bento-grid
  ├─ CTA button → shimmer-button, rainbow-button
  ├─ App screenshot → safari, iphone-15-pro
  ├─ Dynamic headline → word-rotate, typing-animation
  └─ Integration diagram → orbiting-circles, animated-beam

Quick Patterns
// Number Ticker
<div className="flex gap-12">
  <NumberTicker value={10000} className="text-4xl font-bold" />
  <span className="text-4xl">+</span>
</div>

// Marquee (logo wall)
<Marquee pauseOnHover className="[--duration:20s]">
  {logos.map(logo => <img key={logo.name} src={logo.img} />)}
</Marquee>

// Word Rotate
<h1>Build <WordRotate words={["faster", "better"]} /> apps</h1>

// Safari Mockup
<Safari url="yourapp.com" src="/screenshot.png" />

Customization
// Speed via CSS variables
<Marquee className="[--duration:40s]">...</Marquee>
<NumberTicker className="[--duration:3s]" value={1000} />

// Colors
<ShimmerButton
  shimmerColor="#a855f7"
  background="linear-gradient(to right, #6366f1, #8b5cf6)"
>
  Custom
</ShimmerButton>

// Marquee gap
<Marquee className="[--gap:2rem]">...</Marquee>

SSR & Hydration
// Always 'use client'
'use client'

// Heavy components: dynamic import
import dynamic from 'next/dynamic'
const Globe = dynamic(() => import('@/components/magicui/globe'), { ssr: false })

// Mounted check pattern
const [mounted, setMounted] = useState(false)
useEffect(() => setMounted(true), [])
if (!mounted) return <Skeleton />

Magic UI vs Aceternity
Use Case	Magic UI	Aceternity
Number animation	✓ NumberTicker	✗
Logo carousel	✓ Marquee	✓ InfiniteMovingCards
Hero spotlight	✗	✓ Spotlight
Device mockup	✓ Safari/iPhone	✗
3D card tilt	✗	✓ 3D Card

Rule: Magic UI = polished SaaS, Aceternity = dramatic effects

Troubleshooting
"Component not found":
  → npx magicui-cli@latest add [name]
  → Check components/magicui/[name].tsx

"Animation not playing":
  → Add 'use client'
  → Check framer-motion installed

"Hydration mismatch":
  → dynamic(() => ..., { ssr: false })

"Marquee stuttering":
  → Increase [--duration:Xs]
  → Use pauseOnHover

References
components.md — Full component API with all props
External Resources
https://magicui.design/docs — Documentation
For latest API → use context7 skill
Weekly Installs
81
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