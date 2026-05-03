---
title: front-end-skill
url: https://skills.sh/0xgeorgemathew/splithub/front-end-skill
---

# front-end-skill

skills/0xgeorgemathew/splithub/front-end-skill
front-end-skill
Installation
$ npx skills add https://github.com/0xgeorgemathew/splithub --skill front-end-skill
SKILL.md
Next.js Frontend Development
When to Use This Skill

Activate this skill when working on frontend tasks in packages/nextjs/:

Creating or modifying React components
Styling with Tailwind CSS
Building new pages or layouts
Implementing animations and interactions
Working with UI/UX improvements
Project Context

SplitHub is a tap-to-pay bill splitting app. The frontend should feel:

Instant & Responsive — NFC tap interactions need snappy feedback
Trustworthy — Financial app requires clean, confident design
Effortless — Hide complexity, make payments feel magical
Aesthetic Guidelines
Avoid "AI Slop"

Generic AI-generated designs are immediately recognizable. Avoid:

Overused fonts: Inter, Roboto, Open Sans, Lato, system fonts
Cliché color schemes: purple gradients on white backgrounds
Predictable layouts and cookie-cutter component patterns
Space Grotesk (overused in AI outputs)

Make creative, distinctive choices that surprise and delight.

Typography

Typography signals quality instantly. Use distinctive fonts from Google Fonts.

Good choices:

Code aesthetic: JetBrains Mono, Fira Code
Editorial: Playfair Display, Crimson Pro
Technical: IBM Plex family, Source Sans 3
Distinctive: Bricolage Grotesque, Newsreader, Syne, Outfit, Archivo

Pairing principles:

High contrast = interesting (display + monospace, serif + geometric sans)
Use weight extremes: 100/200 vs 800/900, not 400 vs 600
Size jumps of 3x+, not 1.5x

Load fonts via next/font/google in layout files.

Color & Theme
Commit to a cohesive aesthetic with CSS variables
Dominant colors with sharp accents > timid, evenly-distributed palettes
Draw inspiration from IDE themes, cultural aesthetics, or unexpected sources
Dark themes work well for financial/tech apps
Motion & Animation
Use framer-motion (available as motion in this project) for React animations
Focus on high-impact moments: orchestrated page loads with staggered reveals
One well-designed animation-delay sequence > scattered micro-interactions
CSS transitions for simple hover/focus states
Provide tactile feedback for NFC tap interactions
Backgrounds & Depth

Create atmosphere rather than defaulting to solid colors:

Layer CSS gradients
Subtle geometric patterns
Contextual effects matching the aesthetic
Use opacity and blur for depth
Technical Stack
Framework: Next.js 15 with App Router
Styling: Tailwind CSS
Animation: Framer Motion (motion)
Fonts: next/font/google
Path alias: ~~/* resolves to packages/nextjs/
Component Locations
packages/nextjs/
├── app/                    # Pages (App Router)
├── components/
│   ├── settle/            # Payment flow UI
│   ├── credits/           # POS terminal UI
│   ├── activity/          # Activity/receipt UI
│   ├── expense/           # Expense forms
│   ├── home/              # Dashboard components
│   └── scaffold-eth/      # Wallet components
├── hooks/                  # Custom React hooks
└── services/              # API/data services

Implementation Checklist

When creating frontend components:

 Check existing components in packages/nextjs/components/ for patterns
 Use distinctive typography (never Inter/Roboto)
 Apply consistent color theme via CSS variables or Tailwind config
 Add purposeful animations for key interactions
 Ensure mobile-first responsive design
 Provide loading/error states with visual feedback
 Test NFC-related flows feel instant and satisfying
Weekly Installs
11
Repository
0xgeorgemathew/splithub
GitHub Stars
2
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn