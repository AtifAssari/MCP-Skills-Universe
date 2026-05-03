---
title: tooyoung:neoblo-landing-page
url: https://skills.sh/shiqkuangsan/oh-my-daily-skills/tooyoung:neoblo-landing-page
---

# tooyoung:neoblo-landing-page

skills/shiqkuangsan/oh-my-daily-skills/tooyoung:neoblo-landing-page
tooyoung:neoblo-landing-page
Installation
$ npx skills add https://github.com/shiqkuangsan/oh-my-daily-skills --skill tooyoung:neoblo-landing-page
SKILL.md
Neoblo Landing Page

Build static landing pages using the Neoblo design system: Neobrutalism visuals + Blobity cursor effects. Pure HTML/CSS/JS, zero build tools, zero dependencies (Blobity loaded via ESM CDN).

Battle-tested across two production projects (UnClosed, Recopy) with consistent patterns for theme switching, i18n, 3D card interactions, and responsive design.

For detailed Blobity cursor configuration, see tooyoung:blobity-cursor skill.

Design Tokens

All visual properties are controlled through CSS custom properties. Override the color slots to create any brand palette.

Core Variables
:root {
  /* Layout */
  --border-width: 3px;
  --radius: 12px;

  /* Shadows — always consistent direction (bottom-right) */
  --shadow: 6px 6px 0 #0a0a0a;
  --shadow-hover: 10px 10px 0 #0a0a0a;

  /* Typography */
  --font: "Space Grotesk", system-ui, sans-serif;
  --font-mono: "Space Mono", monospace;

  /* Color Slots */
  --bg: #fafaf9;
  --surface: #ffffff;
  --text: #0a0a0a;
  --text-secondary: #525252;
  --primary: #6366f1; /* Nav bg, badges, CTA bg */
  --primary-hover: #4f46e5;
  --accent: #059669; /* Primary buttons, success */
  --accent-hover: #047857;
  --border: #0a0a0a; /* All borders and shadows */
}

Dark Theme Override
[data-theme="dark"] {
  --bg: #1a1a2e;
  --surface: #16213e;
  --text: #f5f5f5;
  --text-secondary: #a3a3a3;
  --border: #e5e5e5;
  --shadow: 6px 6px 0 #e5e5e5;
  --shadow-hover: 10px 10px 0 #e5e5e5;
}

Feature Card Color Cycling

Cards use alternating background colors via nth-child. Define color slots for both themes:

:root {
  --card-lime: #6ee7b7;
  --card-amber: #fcd34d;
  --card-pink: #fb7185;
  --card-cyan: #67e8f9;
  --card-orange: #fdba74;
  --card-purple: #c4b5fd;
}

[data-theme="dark"] {
  --card-lime: #365314;
  --card-amber: #854d0e;
  --card-pink: #9f1239;
  --card-cyan: #155e75;
  --card-orange: #9a3412;
  --card-purple: #4c1d95;
}

.feature-card:nth-child(1) {
  background: var(--card-lime);
}
.feature-card:nth-child(2) {
  background: var(--card-amber);
}
.feature-card:nth-child(3) {
  background: var(--card-pink);
}
/* ... continue for each card */

Example Palettes
Slot	Indigo (UnClosed)	Amber (Recopy)
--primary	#6366f1 (indigo-500)	#f59e0b (amber-500)
--accent	#059669 (emerald-600)	#059669 (emerald-600)
--bg	#fafaf9 (warm gray)	#fafaf9 (warm gray)
--surface	#ffffff	#ffffff
Nav bg	Uses --accent (emerald)	Uses --primary (amber)
Badge bg	Uses --primary (indigo)	Uses --accent (emerald)
Quick Start

Minimal working page with nav + hero + 1 card + footer:

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Landing Page</title>
    <link
      href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap"
      rel="stylesheet"
    />
    <script>
      /* FOUC prevention — must be in <head> before content renders */
      (function () {
        const saved = localStorage.getItem("theme");
        const theme =
          saved === "system" || !saved
            ? matchMedia("(prefers-color-scheme: dark)").matches
              ? "dark"
              : "light"
            : saved;
        document.documentElement.setAttribute("data-theme", theme);
      })();
    </script>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <nav class="nav">
      <div class="nav-inner">
        <a href="/" class="nav-logo">MyApp</a>
        <div class="nav-actions">
          <button class="btn btn-sm" onclick="toggleTheme()">theme</button>
        </div>
      </div>
    </nav>

    <section class="hero">
      <div class="container">
        <div class="hero-badge">Open Source</div>
        <h1 class="hero-title">Your headline here.</h1>
        <p class="hero-desc">One-sentence description.</p>
        <div class="hero-actions">
          <a href="#" class="btn btn-primary">Get Started</a>
          <a href="#" class="btn btn-outline">Source Code</a>
        </div>
      </div>
    </section>

    <footer class="footer">
      <div class="container footer-inner">
        <span>2026 MyApp</span>
        <div class="footer-links"><a href="#">GitHub</a></div>
      </div>
    </footer>

    <script src="script.js"></script>
  </body>
</html>


For the full copy-paste template, see references/page-template.md.

Page Structure

Standard section order for a Neoblo landing page:

nav         — Sticky top bar: logo + links + theme toggle + lang toggle + CTA
hero        — Badge + title + subtitle + dual action buttons
demo        — Browser window mockup with screenshot/GIF
features    — 3x2 or 4x2 grid of colorful cards with icons
cta         — Full-width call to action with accent background
footer      — Copyright + links


Optional sections (insert between features and CTA):

comparison  — Two-column good/bad table (Recopy pattern)
timeline    — Horizontal numbered steps with connector line
shortcuts   — Keyboard shortcut showcase with <kbd> elements
screenshots — 2-column gallery grid

Section Borders

Sections alternate between --bg and --surface backgrounds. Use top/bottom borders to create visual separation:

.features {
  background: var(--surface);
  border-top: var(--border-width) solid var(--border);
  border-bottom: var(--border-width) solid var(--border);
}
.cta {
  background: var(--primary);
  border-top: var(--border-width) solid var(--border);
  border-bottom: var(--border-width) solid var(--border);
}

Component Patterns
Buttons

All buttons share a base .btn class with shadow animation on hover/active:

.btn:hover {
  transform: translate(-3px, -3px);
  box-shadow: var(--shadow-hover);
}
.btn:active {
  transform: translate(3px, 3px);
  box-shadow: 2px 2px 0 var(--border);
}


Variants: .btn-primary (filled accent), .btn-outline (surface bg), .btn-sm (smaller padding/shadow), .btn-lg (larger).

Feature Cards

Cards use nth-child color cycling, contain an icon container + title + description:

<div class="feature-card" data-blobity>
  <div class="feature-icon">
    <svg
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2.5"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <!-- Feather-style icon path -->
    </svg>
  </div>
  <h3>Feature Title</h3>
  <p>Feature description text.</p>
</div>


Icon style: Feather icons (stroke-based, no fill), inherits currentColor.

Nav

Sticky top with colored background. Links hidden on mobile via display: none at 768px breakpoint.

.nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--primary);
}

Hero Badge

Pill-shaped tag above the title:

.hero-badge {
  display: inline-block;
  padding: 6px 18px;
  font-family: var(--font-mono);
  background: var(--primary);
  border: var(--border-width) solid var(--border);
  border-radius: 999px;
  box-shadow: 4px 4px 0 var(--border);
  text-transform: uppercase;
  letter-spacing: 1px;
}

Demo Window

Browser window mockup with macOS traffic light dots:

<div class="demo-window">
  <div class="demo-titlebar">
    <span class="demo-dot" style="background:#ff5f57"></span>
    <span class="demo-dot" style="background:#febc2e"></span>
    <span class="demo-dot" style="background:#28c840"></span>
    <span class="demo-titlebar-text">App Name</span>
  </div>
  <img src="demo.gif" alt="Demo" class="demo-img" loading="lazy" />
</div>


For full component CSS and all variants, see references/component-catalog.md.

Blobity Integration

Add data-blobity to interactive elements for cursor expansion. Blobity is loaded via ESM CDN and skips touch devices automatically.

<div class="feature-card" data-blobity>...</div>
<a href="#" class="btn btn-primary" data-blobity-tooltip="Install now">...</a>


Key integration points:

focusableElements: 'a, button, [data-blobity]' — CSS selector for cursor expansion
invert: true — uses mix-blend-mode: difference for color inversion
Theme sync — call blobity.updateOptions({ color, dotColor }) when theme changes
Hide default cursor with body.blobity-active { cursor: none !important; }

For complete Blobity configuration, theming, tooltip mode, and framework adapters, see tooyoung:blobity-cursor.

Responsive Design
Breakpoints
Breakpoint	Grid Change	Notes
> 1024px	3-4 column features	Full layout
768-1024px	2 column features	Tablet
< 768px	1 column everything	Stack all, hide nav links
Touch Devices
Skip 3D card tilt on touch (e.pointerType === 'touch' guard)
Skip Blobity initialization ('ontouchstart' in window check)
Hover effects degrade gracefully (no jitter on tap)
Mobile Adjustments
@media (max-width: 768px) {
  .features-grid {
    grid-template-columns: 1fr;
  }
  .hero {
    padding: 48px 0 40px;
  }
  .hero-title {
    font-size: 32px;
    letter-spacing: -1px;
  }
  .section-title {
    font-size: 28px;
  }
  .nav-link {
    display: none;
  }
  .footer-inner {
    flex-direction: column;
    gap: 12px;
    text-align: center;
  }
}

Common Pitfalls

Shadow direction inconsistency — All shadows must go bottom-right. If a card tilts via 3D transform, dynamically mirror the shadow: box-shadow: ${-rotateY}px ${rotateX}px 0 var(--border).

Missing box-sizing: border-box — The thick borders (3px) will break layouts without it. Always include the universal reset: *, *::before, *::after { box-sizing: border-box; }.

Theme not persisting across reloads — The FOUC prevention script MUST be in <head> before any CSS loads. It reads localStorage and sets data-theme before the first paint.

CJK text overflow — Chinese/Japanese text doesn't break at word boundaries. Add word-break: break-word on description text inside cards and hero sections.

3D tilt jitter at card edges — When the card rotates, its bounding rect shifts, causing rapid pointerleave/pointerenter events. Solution: defer pointerleave by one animation frame and verify the pointer is truly outside the original rect.

Font loading flash — Load Google Fonts with &display=swap to show fallback immediately. The design still works without Space Grotesk since system-ui is the fallback.

Hardcoded colors — Never use raw hex values in component CSS. Always reference var(--token). This ensures theme switching and palette customization work correctly.

References
File	Content
page-template.md	Complete copy-paste HTML template with all sections
interactive-behaviors.md	3D card tilt, theme toggle, i18n — full JS implementation
component-catalog.md	All components: buttons, cards, nav, hero, footer + optional sections
Customization Guide
Changing the Color Palette
Pick a primary color (nav/CTA background) and an accent color (buttons/badges)
Override the 4 main slots in :root: --primary, --primary-hover, --accent, --accent-hover
Generate matching dark theme values (darken by ~40-50% for card backgrounds)
Update Blobity color and dotColor to match (remember: invert: true means colors appear as their complement)
Adding a New Section
Create a <section class="my-section"> with a .container wrapper inside
Choose background: var(--bg) or var(--surface) (alternate with adjacent sections)
Add top/bottom borders if using --surface background
Use .section-title for the heading
Follow the existing spacing pattern: padding: 80px 0
Extending Interactions

The 3D tilt system can be applied to any card-like element:

Add perspective: 800px to the parent grid
Add transform-style: preserve-3d to the card
Use the initCardTilt() function targeting your card selector
Inject .card-spotlight overlay for the radial gradient highlight
i18n for Additional Languages

The data-{lang} attribute pattern extends to any language:

<h1 data-en="Hello" data-zh="你好" data-ja="こんにちは">Hello</h1>


Update the toggle function to cycle through your supported languages and call el.getAttribute('data-' + lang).

Weekly Installs
14
Repository
shiqkuangsan/oh…y-skills
GitHub Stars
15
First Seen
Mar 4, 2026