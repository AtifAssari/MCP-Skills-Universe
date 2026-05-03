---
title: design-principles
url: https://skills.sh/srbhr/resume-matcher/design-principles
---

# design-principles

skills/srbhr/resume-matcher/design-principles
design-principles
Installation
$ npx skills add https://github.com/srbhr/resume-matcher --skill design-principles
SKILL.md
Swiss International Style Design

Invoke when: Creating new components, modifying styles, or building new pages. Skip when: Backend work, API changes, logic-only changes.

Before Designing

Read the full design specs in docs/agent/design/:

style-guide.md - Core rules, colors, typography, components
design-system.md - Extended tokens, spacing, shadows
swiss-design-system-prompt.md - AI prompt for Swiss UI
Colors
Name	Hex	Usage
Canvas	#F0F0E8	Background
Ink	#000000	Text, borders
Hyper Blue	#1D4ED8	Primary actions
Signal Green	#15803D	Success
Alert Orange	#F97316	Warning
Alert Red	#DC2626	Danger
Steel Grey	#4B5563	Secondary text
Typography
font-serif  → Headers
font-mono   → Labels, metadata (uppercase, tracking-wider)
font-sans   → Body text

Component Patterns
// Button: Square corners, hard shadow, press effect
<button className="rounded-none border-2 border-black shadow-[2px_2px_0px_0px_#000000] hover:translate-y-[1px] hover:translate-x-[1px] hover:shadow-none">

// Card: Hard shadow, no rounded corners
<div className="bg-white border-2 border-black shadow-[4px_4px_0px_0px_#000000]">

// Label: Mono, uppercase
<label className="font-mono text-sm uppercase tracking-wider">

Status Indicators
<div className="w-3 h-3 bg-green-700" />  // Ready
<div className="w-3 h-3 bg-amber-500" />  // Warning
<div className="w-3 h-3 bg-red-600" />    // Error
<div className="w-3 h-3 bg-blue-700" />   // Active

Anti-Patterns (NEVER)
rounded-* (except rounded-none)
Gradients or blur shadows
Custom colors outside palette
Pastel or soft colors
Decorative icons without function
Retro Terminal Elements

For dashboard/settings/empty states ONLY:

<span className="font-mono text-xs uppercase">[ STATUS: READY ]</span>


DO NOT use retro elements on resume components.

Checklist
 rounded-none on all components
 Hard shadows (shadow-[Xpx_Xpx_0px_0px_#000000])
 Correct typography (serif headers, mono labels, sans body)
 Colors from palette only
 No gradients or blur effects
Weekly Installs
93
Repository
srbhr/resume-matcher
GitHub Stars
26.5K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass