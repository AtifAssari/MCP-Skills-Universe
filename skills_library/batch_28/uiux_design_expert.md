---
title: uiux-design-expert
url: https://skills.sh/0xkynz/codekit/uiux-design-expert
---

# uiux-design-expert

skills/0xkynz/codekit/uiux-design-expert
uiux-design-expert
Installation
$ npx skills add https://github.com/0xkynz/codekit --skill uiux-design-expert
SKILL.md
UI/UX Design Expert

Expert in modern UI/UX design patterns, visual styles, design systems, accessibility standards, and CSS implementation across all major frameworks.

When Invoked
Identify the design context (web app, mobile, dashboard, marketing)
Detect existing design system or framework (Tailwind, CSS Modules, styled-components)
Recommend appropriate visual style based on brand/audience
Implement with accessibility and performance in mind
Design Style Reference
1. Minimalism & Swiss Design

Philosophy: Less is more. Focus on content, clarity, and functionality.

Prompt Keywords: minimalist landing page, white space, geometric layouts, sans-serif fonts, high contrast, grid-based structure, essential elements only

CSS Implementation:

.swiss-layout {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

.swiss-card {
  background: #FFFFFF;
  color: #000000;
  border: none;
  box-shadow: none;
  padding: 2rem;
}


Design Tokens:

--spacing: 2rem
--border-radius: 0px
--font-weight: 400-700
--shadow: none
--accent-color: single primary only

Checklist: Grid 12-16 columns, Typography hierarchy, No decorations, WCAG AAA contrast, Mobile responsive

2. Neumorphism (Soft UI)

Philosophy: Soft, extruded plastic appearance with subtle depth.

Prompt Keywords: neumorphic UI, soft 3D effects, light pastels, rounded corners, soft shadows, monochromatic, embossed/debossed

CSS Implementation:

.neu-card {
  background: #E8E8E8;
  border-radius: 16px;
  box-shadow:
    8px 8px 16px rgba(0, 0, 0, 0.15),
    -8px -8px 16px rgba(255, 255, 255, 0.9);
}

.neu-button {
  background: linear-gradient(145deg, #F0F0F0, #D8D8D8);
  border-radius: 12px;
  box-shadow:
    5px 5px 10px rgba(0, 0, 0, 0.1),
    -5px -5px 10px rgba(255, 255, 255, 0.8);
  transition: transform 150ms ease;
}

.neu-button:active {
  transform: scale(0.98);
  box-shadow: inset 3px 3px 6px rgba(0, 0, 0, 0.1);
}


Design Tokens:

--border-radius: 14px
--shadow-light: -8px -8px 16px rgba(255,255,255,0.9)
--shadow-dark: 8px 8px 16px rgba(0,0,0,0.15)
--color-base: #E8E8E8

Checklist: Rounded corners 12-16px, Multiple shadow layers, Pastel colors, Press animation 150ms

3. Glassmorphism

Philosophy: Frosted glass effect with depth and translucency.

Prompt Keywords: glassmorphic interface, frosted glass effect, backdrop blur, translucent overlays, vibrant backgrounds, layered depth

CSS Implementation:

.glass-card {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.glass-container {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
}


Design Tokens:

--blur-amount: 16px
--glass-opacity: 0.15
--border-color: rgba(255,255,255,0.2)
--background: vibrant gradient

Checklist: Backdrop-filter 10-20px, Translucent 15-30% opacity, Subtle border, Vibrant background, Text contrast 4.5:1

4. Brutalism

Philosophy: Raw, unpolished, intentionally stark and aggressive.

Prompt Keywords: brutalist design, raw aesthetic, pure primary colors, no smooth transitions, sharp corners, bold large typography, visible grid, intentional broken elements

CSS Implementation:

.brutal-layout {
  font-family: 'Courier New', monospace;
  background: #FFFFFF;
  color: #000000;
}

.brutal-card {
  border: 4px solid #000000;
  border-radius: 0;
  background: #FFFF00;
  padding: 2rem;
  transition: none;
}

.brutal-button {
  background: #FF0000;
  color: #FFFFFF;
  border: 3px solid #000000;
  font-weight: 900;
  text-transform: uppercase;
  padding: 1rem 2rem;
}

.brutal-button:hover {
  background: #0000FF;
  /* No transition - instant change */
}


Design Tokens:

--border-radius: 0px
--transition-duration: 0s
--font-weight: 700-900
--colors: #FF0000, #0000FF, #FFFF00, #000000, #FFFFFF

Checklist: No border-radius, No transitions, Bold typography 700+, Pure primary colors, Visible borders

5. Neubrutalism

Philosophy: Evolved brutalism with playful, modern twist.

Prompt Keywords: neubrutalist interface, high contrast, hard black borders, bright pop colors, hard shadows, bold typography, raw but functional

CSS Implementation:

.neubrutalist-card {
  background: #FFDB58;
  border: 3px solid #000000;
  border-radius: 8px;
  box-shadow: 6px 6px 0px #000000;
  padding: 1.5rem;
}

.neubrutalist-button {
  background: #FF6B6B;
  color: #000000;
  border: 2px solid #000000;
  border-radius: 4px;
  box-shadow: 4px 4px 0px #000000;
  font-weight: 700;
  transition: transform 100ms, box-shadow 100ms;
}

.neubrutalist-button:hover {
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0px #000000;
}

.neubrutalist-button:active {
  transform: translate(2px, 2px);
  box-shadow: 2px 2px 0px #000000;
}


Design Tokens:

--border-width: 2-4px
--shadow-offset: 4-6px
--shadow-color: #000000
--colors: #FFDB58, #FF6B6B, #4ECDC4, #9B5DE5

Checklist: Hard borders 2-4px, Hard offset shadows, High saturation colors, Bold typography, No blurs

6. Bento Grid Layout

Philosophy: Apple-inspired modular grid with varied card sizes.

Prompt Keywords: Bento Grid layout, modular grid system, rounded corners, different card sizes, card-based hierarchy, soft backgrounds, Apple-style aesthetic

CSS Implementation:

.bento-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 200px;
  gap: 20px;
  padding: 20px;
  background: #F5F5F7;
}

.bento-card {
  background: #FFFFFF;
  border-radius: 24px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.bento-card--large {
  grid-column: span 2;
  grid-row: span 2;
}

.bento-card--wide {
  grid-column: span 2;
}

.bento-card--tall {
  grid-row: span 2;
}

@media (max-width: 768px) {
  .bento-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}


Design Tokens:

--grid-gap: 20px
--card-radius: 24px
--card-bg: #FFFFFF
--page-bg: #F5F5F7
--shadow: 0 2px 8px rgba(0,0,0,0.04)

Checklist: CSS Grid layout, Rounded corners 16-24px, Varied card spans, Responsive reflow

7. Dark Mode (OLED Optimized)

Philosophy: True black for OLED power saving with vibrant accents.

Prompt Keywords: OLED-optimized dark interface, deep black, dark grey, midnight blue, neon accents, high contrast text, eye comfort

CSS Implementation:

:root[data-theme="dark"] {
  --bg-primary: #000000;
  --bg-secondary: #0D0D0D;
  --bg-elevated: #1A1A1A;
  --text-primary: #FFFFFF;
  --text-secondary: #A0A0A0;
  --accent-neon: #00D4FF;
  --accent-success: #00FF85;
  --accent-warning: #FFB800;
}

.dark-card {
  background: var(--bg-elevated);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
}

.dark-glow-text {
  color: var(--accent-neon);
  text-shadow: 0 0 20px rgba(0, 212, 255, 0.4);
}


Design Tokens:

--bg-black: #000000
--bg-elevated: #1A1A1A
--text-primary: #FFFFFF
--accent-neon: cyan, green, gold, purple
--glow-effect: minimal

Checklist: Deep black #000000, Vibrant neon accents, Text contrast 7:1+, Minimal glow, OLED optimized

8. Aurora UI (Gradient Mesh)

Philosophy: Northern Lights inspired flowing gradients.

Prompt Keywords: vibrant gradient interface, Northern Lights, mesh gradients, smooth color blends, flowing animations, iridescent effects

CSS Implementation:

.aurora-background {
  background: linear-gradient(
    125deg,
    #667eea 0%,
    #764ba2 25%,
    #f093fb 50%,
    #f5576c 75%,
    #667eea 100%
  );
  background-size: 400% 400%;
  animation: aurora-shift 12s ease infinite;
}

@keyframes aurora-shift {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.aurora-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}


Design Tokens:

--gradient-colors: complementary pairs
--animation-duration: 8-12s
--blend-mode: screen
--color-saturation: 1.2

Checklist: Mesh/flowing gradients, 8-12s animation loop, Complementary colors, Smooth transitions

9. Claymorphism

Philosophy: Playful, toy-like 3D with soft chunky elements.

Prompt Keywords: playful toy-like interface, soft 3D, chunky elements, bubbly aesthetic, rounded edges, thick borders, double shadows, pastel colors

CSS Implementation:

.clay-card {
  background: linear-gradient(145deg, #FFE5E5, #FFC4C4);
  border: 3px solid #FF9999;
  border-radius: 24px;
  box-shadow:
    inset -3px -3px 8px rgba(255, 255, 255, 0.6),
    6px 6px 16px rgba(255, 100, 100, 0.2);
}

.clay-button {
  background: linear-gradient(145deg, #C4E5FF, #94D0FF);
  border: 3px solid #5BB5FF;
  border-radius: 20px;
  padding: 16px 32px;
  font-weight: 700;
  animation: clay-bounce 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

@keyframes clay-bounce {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}


Design Tokens:

--border-radius: 20-24px
--border-width: 3-4px
--shadow-inner: inset -3px -3px 8px
--shadow-outer: 6px 6px 16px
--color-palette: pastels

Checklist: Border-radius 16-24px, Thick borders 3-4px, Double shadows, Pastel colors, Bounce animations

10. Retro-Futurism (Cyberpunk/Vaporwave)

Philosophy: 80s sci-fi meets neon future.

Prompt Keywords: retro-futuristic cyberpunk vaporwave, neon colors, deep black, 80s aesthetic, CRT scanlines, glitch effects, neon glow, monospace fonts

CSS Implementation:

.retro-container {
  background: #0A0A14;
  font-family: 'Share Tech Mono', monospace;
  color: #00FFFF;
}

.retro-card {
  background: rgba(0, 255, 255, 0.05);
  border: 1px solid rgba(0, 255, 255, 0.3);
  box-shadow:
    0 0 20px rgba(0, 255, 255, 0.2),
    inset 0 0 20px rgba(0, 255, 255, 0.05);
}

.neon-text {
  color: #FF006E;
  text-shadow:
    0 0 10px #FF006E,
    0 0 20px #FF006E,
    0 0 40px #FF006E;
}

.scanlines::after {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    0deg,
    rgba(0, 0, 0, 0.1) 0px,
    rgba(0, 0, 0, 0.1) 1px,
    transparent 1px,
    transparent 2px
  );
  pointer-events: none;
}

@keyframes glitch {
  0%, 100% { transform: translate(0); }
  20% { transform: translate(-2px, 2px); }
  40% { transform: translate(2px, -2px); }
  60% { transform: translate(-1px, -1px); }
  80% { transform: translate(1px, 1px); }
}


Design Tokens:

--neon-cyan: #00FFFF
--neon-pink: #FF006E
--neon-blue: #0080FF
--background: #0A0A14
--font-family: monospace

Checklist: Neon colors, CRT scanlines, Glitch animations, Monospace font, Deep black background

11. HUD / Sci-Fi FUI

Philosophy: Futuristic heads-up display with technical aesthetics.

Prompt Keywords: futuristic HUD FUI, thin lines, neon cyan on black, technical markers, decorative brackets, data visualization, monospaced tech fonts, holographic

CSS Implementation:

.hud-container {
  background: rgba(0, 10, 20, 0.95);
  font-family: 'Orbitron', monospace;
  color: #00FFFF;
}

.hud-panel {
  border: 1px solid rgba(0, 255, 255, 0.4);
  background: transparent;
  position: relative;
}

.hud-panel::before,
.hud-panel::after {
  content: '';
  position: absolute;
  width: 20px;
  height: 20px;
  border-color: #00FFFF;
  border-style: solid;
}

.hud-panel::before {
  top: -1px;
  left: -1px;
  border-width: 2px 0 0 2px;
}

.hud-panel::after {
  bottom: -1px;
  right: -1px;
  border-width: 0 2px 2px 0;
}

.hud-text {
  text-shadow: 0 0 8px rgba(0, 255, 255, 0.6);
  letter-spacing: 2px;
  text-transform: uppercase;
}


Design Tokens:

--hud-color: #00FFFF
--bg-color: rgba(0,10,20,0.95)
--line-width: 1px
--glow: 0 0 8px
--font: monospace/tech

Checklist: Fine lines 1px, Neon glow, Monospaced font, Transparent BG, Tech markers, Holographic feel

12. Liquid Glass (Premium)

Philosophy: Fluid, morphing, premium glass effects.

Prompt Keywords: liquid glass effect, morphing shapes, flowing animations, chromatic aberration, iridescent gradients, smooth transitions, fluid premium feel

CSS Implementation:

.liquid-glass {
  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.4) 0%,
    rgba(255, 255, 255, 0.1) 100%
  );
  backdrop-filter: blur(20px) saturate(1.5);
  border-radius: 32px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  transition: all 500ms cubic-bezier(0.4, 0, 0.2, 1);
}

.liquid-morph {
  animation: morph 8s ease-in-out infinite;
}

@keyframes morph {
  0%, 100% { border-radius: 32px 64px 32px 64px; }
  25% { border-radius: 64px 32px 64px 32px; }
  50% { border-radius: 32px 64px 64px 32px; }
  75% { border-radius: 64px 32px 32px 64px; }
}

.chromatic {
  filter:
    drop-shadow(-2px 0 0 rgba(255, 0, 0, 0.3))
    drop-shadow(2px 0 0 rgba(0, 255, 255, 0.3));
}


Design Tokens:

--morph-duration: 400-600ms
--blur-amount: 20px
--chromatic-aberration: true
--iridescent: true
--saturation: 1.5

Checklist: Morphing animations, Chromatic aberration, Dynamic blur, Iridescent gradients, Premium feel

13. Skeuomorphism (Realistic)

Philosophy: Real-world textures and tactile depth.

Prompt Keywords: realistic textured interface, 3D depth, real-world metaphors, complex gradients, realistic shadows, grain texture, tactile animations, premium luxury

CSS Implementation:

.skeu-button {
  background: linear-gradient(
    180deg,
    #FFFFFF 0%,
    #F5F5F5 10%,
    #E8E8E8 50%,
    #D0D0D0 90%,
    #C0C0C0 100%
  );
  border: 1px solid #A0A0A0;
  border-radius: 8px;
  box-shadow:
    0 1px 2px rgba(255, 255, 255, 0.9) inset,
    0 -1px 2px rgba(0, 0, 0, 0.1) inset,
    0 4px 8px rgba(0, 0, 0, 0.2);
  transition: transform 300ms ease;
}

.skeu-button:active {
  transform: scale(0.98);
  box-shadow:
    0 1px 2px rgba(0, 0, 0, 0.1) inset,
    0 -1px 2px rgba(255, 255, 255, 0.9) inset;
}

.texture-grain {
  background-image: url("data:image/svg+xml,..."); /* noise pattern */
  opacity: 0.05;
}


Design Tokens:

--gradient-stops: 8-12
--texture-overlay: noise+grain
--shadow-layers: 3+
--animation-duration: 300-500ms

Checklist: Realistic textures, Complex gradients, Multi-layer shadows, Texture overlays, Tactile animations

14. Flat Design 2.0

Philosophy: Clean, simple, with subtle depth cues.

Prompt Keywords: flat 2D interface, bold colors, no gradients, clean lines, simple shapes, icon-heavy, typography-focused, minimal ornamentation

CSS Implementation:

.flat-card {
  background: #FFFFFF;
  border: none;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
  border-radius: 4px;
}

.flat-button {
  background: #2196F3;
  color: #FFFFFF;
  border: none;
  border-radius: 4px;
  font-weight: 600;
  transition: background 150ms ease;
}

.flat-button:hover {
  background: #1976D2;
}

.flat-icon {
  fill: currentColor;
  stroke: none;
}


Design Tokens:

--shadow: minimal or none
--color-palette: 4-6 solid colors
--border-radius: 2-4px
--gradient: none
--animation: 150-200ms

Checklist: No heavy shadows, 4-6 solid colors max, Clean lines, Simple shapes, Fast loading

15. Pixel Art (8-bit)

Philosophy: Retro gaming nostalgia with blocky aesthetics.

Prompt Keywords: pixel art interface, 8-bit 16-bit aesthetic, pixelated fonts, sharp edges, limited color palette, blocky UI, retro gaming feel

CSS Implementation:

.pixel-container {
  font-family: 'Press Start 2P', cursive;
  image-rendering: pixelated;
  image-rendering: crisp-edges;
}

.pixel-button {
  background: #5C94FC;
  color: #FFFFFF;
  border: 4px solid;
  border-color: #9CBAFC #1C3CBC #1C3CBC #9CBAFC;
  padding: 8px 16px;
  font-size: 12px;
  cursor: pointer;
}

.pixel-button:active {
  border-color: #1C3CBC #9CBAFC #9CBAFC #1C3CBC;
}

.pixel-sprite {
  width: 32px;
  height: 32px;
  image-rendering: pixelated;
}


Design Tokens:

--pixel-size: 4px
--color-palette: 16 colors max
--font: pixel font
--image-rendering: pixelated

Checklist: Pixelated fonts, Sharp edges, Limited palette, Blocky elements, Retro feel

Accessibility Standards (WCAG)
Universal Requirements
/* Focus states - always visible */
:focus-visible {
  outline: 3px solid var(--focus-color);
  outline-offset: 2px;
}

/* Touch targets - minimum 44x44px */
.touch-target {
  min-width: 44px;
  min-height: 44px;
  padding: 12px;
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}

/* High contrast mode */
@media (prefers-contrast: high) {
  :root {
    --text-color: #000000;
    --bg-color: #FFFFFF;
    --border-color: #000000;
  }
}

Contrast Ratios
Level	Normal Text	Large Text	UI Components
AA	4.5:1	3:1	3:1
AAA	7:1	4.5:1	4.5:1
Checklist for All Designs
 Color contrast 4.5:1+ (AA) or 7:1+ (AAA)
 Focus states visible (3px ring)
 Touch targets 44x44px minimum
 Keyboard navigation works
 Screen reader tested
 No color-only indicators
 Reduced motion supported
 Semantic HTML used
 ARIA labels where needed
Animation Guidelines
Performance-Optimized Properties
/* GPU-accelerated (prefer these) */
transform: translate, scale, rotate;
opacity: 0-1;

/* Avoid animating (triggers layout) */
width, height, top, left, margin, padding;

Timing Functions
/* Natural motion */
--ease-out: cubic-bezier(0.0, 0.0, 0.2, 1);
--ease-in-out: cubic-bezier(0.4, 0.0, 0.2, 1);
--bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
--spring: cubic-bezier(0.68, -0.55, 0.265, 1.55);

Duration Guidelines
Interaction	Duration
Micro-interaction	50-100ms
Button press	100-150ms
Page transition	200-400ms
Complex animation	400-600ms
Background loop	8-12s
Color Palette Generation
Complementary Schemes
/* Blue-Orange */
--primary: #2563EB;
--secondary: #EA580C;

/* Purple-Yellow */
--primary: #7C3AED;
--secondary: #EAB308;

/* Cyan-Red */
--primary: #06B6D4;
--secondary: #DC2626;

Neutral Scales
/* Light mode neutrals */
--gray-50: #F9FAFB;
--gray-100: #F3F4F6;
--gray-200: #E5E7EB;
--gray-300: #D1D5DB;
--gray-400: #9CA3AF;
--gray-500: #6B7280;
--gray-600: #4B5563;
--gray-700: #374151;
--gray-800: #1F2937;
--gray-900: #111827;

/* Dark mode neutrals */
--dark-50: #18181B;
--dark-100: #27272A;
--dark-200: #3F3F46;
--dark-300: #52525B;
--dark-400: #71717A;
--dark-500: #A1A1AA;

Implementation Workflow
Identify Context: What's the product? Who's the audience?
Choose Style: Match visual style to brand/audience
Set Tokens: Define CSS custom properties
Build Components: Create reusable component library
Test Accessibility: Verify WCAG compliance
Optimize Performance: Check animation performance
Responsive Check: Test all breakpoints
Best Practices
Start with tokens - Define colors, spacing, typography first
Mobile-first - Design for smallest screens first
Test early - Accessibility testing from day one
Performance budget - Keep animations under 16ms/frame
Document everything - Create a living style guide
Weekly Installs
15
Repository
0xkynz/codekit
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass