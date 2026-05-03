---
rating: ⭐⭐
title: frontend-aceternity
url: https://skills.sh/petbrains/mvp-builder/frontend-aceternity
---

# frontend-aceternity

skills/petbrains/mvp-builder/frontend-aceternity
frontend-aceternity
Installation
$ npx skills add https://github.com/petbrains/mvp-builder --skill frontend-aceternity
SKILL.md
Aceternity UI

Copy-paste animated effects for stunning landing pages. Built on Framer Motion + Tailwind.

When to Use
Hero sections with spotlight/aurora effects
3D card hover effects
Text reveal animations
Animated backgrounds (beams, stars, meteors)
User asks for "cool effects", "wow factor"
When NOT to Use
Basic UI components → shadcn/ui
SaaS stats/marquees → Magic UI
State-driven animations → Rive
Process

IDENTIFY → INSTALL → CUSTOMIZE

Identify effect type needed
Install: npx aceternity-ui@latest add [component]
Customize colors/timing
Dependencies
npm install framer-motion clsx tailwind-merge

Component Categories
Backgrounds:  spotlight, aurora-background, background-beams, wavy-background, meteors, sparkles
Cards:        3d-card, evervault-card, focus-cards, infinite-moving-cards, wobble-card
Text:         text-generate-effect, flip-words, typewriter-effect, hero-highlight
Navigation:   floating-navbar, floating-dock, navbar-menu
Special:      lamp, tracing-beam, parallax-scroll, globe, timeline
Buttons:      moving-border, hover-border-gradient

Decision Tree
Need dramatic effect?
  ├─ Hero background → spotlight, aurora-background, background-beams
  ├─ Feature cards → 3d-card, focus-cards
  ├─ Testimonials → infinite-moving-cards
  ├─ Headlines → text-generate-effect, flip-words
  └─ Section divider → lamp, tracing-beam

Quick Patterns
// Spotlight Hero
<div className="relative h-screen bg-black">
  <Spotlight className="absolute top-0 left-0" fill="white" />
  <div className="relative z-10">
    <h1>Content</h1>
  </div>
</div>

// 3D Card
<CardContainer>
  <CardBody className="bg-gray-50 rounded-xl p-6">
    <CardItem translateZ="50">Title</CardItem>
    <CardItem translateZ="100"><img src="..." /></CardItem>
  </CardBody>
</CardContainer>

// Flip Words
<h1>Build <FlipWords words={["faster", "better", "smarter"]} /> apps</h1>

SSR & Hydration
// ALL components require 'use client'
'use client'

// Heavy components: dynamic import
import dynamic from 'next/dynamic'
const Globe = dynamic(() => import('@/components/ui/globe'), { ssr: false })

// Hydration fix pattern
const [mounted, setMounted] = useState(false)
useEffect(() => setMounted(true), [])
if (!mounted) return null

Performance Tips
// Reduce particles on mobile
const count = isMobile ? 20 : 100

// Respect reduced motion
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches

References
components.md — Full component API with all props and patterns
External Resources
https://ui.aceternity.com/components
For latest API → use context7 skill
Weekly Installs
10
Repository
petbrains/mvp-builder
GitHub Stars
10
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass