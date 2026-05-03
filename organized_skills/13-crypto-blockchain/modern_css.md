---
rating: ⭐⭐⭐
title: modern-css
url: https://skills.sh/caidanw/skills/modern-css
---

# modern-css

skills/caidanw/skills/modern-css
modern-css
Installation
$ npx skills add https://github.com/caidanw/skills --skill modern-css
SKILL.md
Modern CSS

The CSS spec has evolved dramatically. Many old hacks — absolute-position centering, padding-top aspect ratios, JS scroll listeners, Sass color functions — now have clean, native replacements. This skill ensures you always reach for the modern approach first.

Reference: modern-css.com — all techniques sourced from this site. Visit individual pages for live demos and deeper explanations.

Support data: Browser support percentages represent global user coverage from caniuse.com, last updated February 2026. These numbers shift as browsers release updates — verify on caniuse if precision matters for a project.

How to Use This Skill

When writing or reviewing CSS:

Always use techniques in the Widely Available tier (90%+ support) without asking. If you spot legacy patterns, refactor them to the modern equivalent.
Suggest techniques in the Newly Available tier (80–90% support). Mention they are newly available and let the user decide. Offer a fallback if relevant.
Ask first before using Limited Availability techniques (<80% support). Warn about browser support and suggest a progressive-enhancement approach or fallback.
If the user has legacy browser requirements (e.g. older Safari, corporate browsers), ask before using any technique — even Widely Available ones — since support percentages assume modern browser versions. Use @supports to provide fallbacks.

When you see old CSS patterns in existing code, point them out and suggest the modern replacement with a brief explanation of why it's better.

Widely Available (90%+ support) — Always Use

These techniques are well-established and work across all modern browsers. Use them without hesitation.

Layout
Centering elements — place-items: center
/* OLD: absolute + transform hack (5 declarations, 2 selectors) */
.parent { position: relative; }
.child {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
}

/* MODERN: grid centering (2 declarations, 1 selector) */
.parent {
  display: grid;
  place-items: center;
}


Reference →

Spacing elements — gap
/* OLD: margin hacks with :last-child override */
.grid > * { margin-right: 16px; }
.grid > *:last-child { margin-right: 0; }

/* MODERN: gap on the container */
.grid {
  display: flex;
  gap: 16px;
}


Reference →

Aspect ratios — aspect-ratio
/* OLD: padding-top percentage hack */
.wrapper { padding-top: 56.25%; position: relative; }
.inner { position: absolute; inset: 0; }

/* MODERN: aspect-ratio property */
.video-wrapper {
  aspect-ratio: 16 / 9;
}


Reference →

Positioning shorthand — inset
/* OLD: four separate properties */
.overlay { top: 0; right: 0; bottom: 0; left: 0; }

/* MODERN: inset shorthand */
.overlay {
  position: absolute;
  inset: 0;
}


Reference →

Sticky headers — position: sticky
/* OLD: JS scroll listener + getBoundingClientRect */
// add/remove .fixed class based on scroll position

/* MODERN: sticky positioning */
.header {
  position: sticky;
  top: 0;
}


Reference →

Responsive images — object-fit
/* OLD: background-image with background-size */
.card-image {
  background-image: url(...);
  background-size: cover;
  background-position: center;
}

/* MODERN: object-fit on an img element */
img {
  object-fit: cover;
  width: 100%;
  height: 200px;
}


Reference →

Filling available space — stretch
/* OLD: calc workaround */
.full { width: calc(100% - 40px); }

/* MODERN: stretch keyword */
.full { width: stretch; }
/* fills container, respects margins */


Reference →

Preventing scroll chaining — overscroll-behavior
/* OLD: JS wheel event preventDefault */
// modal.addEventListener('wheel', e => e.preventDefault(), { passive: false })

/* MODERN: overscroll-behavior */
.modal-content {
  overflow-y: auto;
  overscroll-behavior: contain;
}


Reference →

Preventing scrollbar layout shift — scrollbar-gutter
/* OLD: force scrollbar or hardcode padding */
body { overflow-y: scroll; }

/* MODERN: reserve scrollbar space */
body { scrollbar-gutter: stable; }


Reference →

Grid template areas — named areas
/* OLD: grid line numbers or floats */
.item { grid-column: 1 / 3; grid-row: 2; }

/* MODERN: named grid areas */
.layout {
  display: grid;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
}
.header { grid-area: header; }


Reference →

Modal dialogs — <dialog> element
/* OLD: fixed overlay + JS open/close/ESC/focus-trap */
.overlay { position: fixed; z-index: 999; }

/* MODERN: native dialog with ::backdrop */
dialog { padding: 1rem; }
dialog::backdrop { background: rgb(0 0 0 / .5); }
/* JS: dialog.showModal() / dialog.close() */


Reference →

Direction-aware layouts — logical properties
/* OLD: physical properties + RTL overrides */
margin-left: 1rem;
padding-right: 1rem;
[dir="rtl"] .box { margin-right: 1rem; }

/* MODERN: logical properties */
margin-inline-start: 1rem;
padding-inline-end: 1rem;
border-block-start: 1px solid;


Reference →

Responsive components — @container
/* OLD: viewport-based media queries */
@media (min-width: 768px) {
  .card { grid-template-columns: auto 1fr; }
}

/* MODERN: container queries */
.wrapper { container-type: inline-size; }
@container (width > 400px) {
  .card { grid-template-columns: auto 1fr; }
}


Reference →

Scroll snapping — scroll-snap
/* OLD: Slick/Swiper carousel or touch handlers */
// $('.carousel').slick({ ... })

/* MODERN: CSS scroll snap */
.carousel {
  scroll-snap-type: x mandatory;
  overflow-x: auto;
}
.carousel > * { scroll-snap-align: start; }


Reference →

Selectors
Parent selection — :has()
/* OLD: JavaScript el.closest('.parent').classList.add(...) */

/* MODERN: :has() parent selector */
.card:has(img) {
  grid-template-rows: auto 1fr;
}


Reference →

Grouping selectors — :is()
/* OLD: repeat the full selector for each match */
.card h1, .card h2, .card h3, .card h4 { margin-bottom: 0.5em; }

/* MODERN: :is() grouping */
.card :is(h1, h2, h3, h4) { margin-bottom: 0.5em; }


Reference →

Low-specificity resets — :where()
/* OLD: class-based resets with specificity issues */
.reset ul, .reset ol { margin: 0; }

/* MODERN: :where() has zero specificity */
:where(ul, ol) {
  margin: 0;
  padding-inline-start: 1.5rem;
}


Reference →

Keyboard-only focus — :focus-visible
/* OLD: :focus fires on mouse click too, so people remove outlines (a11y fail) */
:focus { outline: 2px solid blue; }

/* MODERN: :focus-visible only shows for keyboard navigation */
:focus-visible {
  outline: 2px solid var(--focus-color);
}


Reference →

Color
Styling form controls — accent-color
/* OLD: appearance: none + rebuild the entire control */
input[type="checkbox"] { appearance: none; /* 20+ lines of custom styles */ }

/* MODERN: accent-color */
input[type="checkbox"],
input[type="radio"] {
  accent-color: #7c3aed;
}


Reference →

Perceptually uniform colors — oklch()
/* OLD: hex/rgb with guess-and-check for each shade */
--brand: #4f46e5;
--brand-light: #818cf8;
--brand-dark: #3730a3;

/* MODERN: oklch — adjust lightness, keep perceived hue */
--brand: oklch(0.55 0.2 264);
--brand-light: oklch(0.75 0.2 264);
--brand-dark: oklch(0.35 0.2 264);


Reference →

Wide-gamut colors — display-p3 / oklch
/* OLD: sRGB only — washed out on P3 displays */
.hero { color: rgb(200, 80, 50); }

/* MODERN: oklch or display-p3 for vivid colors */
.hero { color: oklch(0.7 0.25 29); }
/* or: color(display-p3 1 0.2 0.1) */


Reference →

Frosted glass — backdrop-filter
/* OLD: pseudo-element with blurred background image */
.card::before { content: ''; background-image: url(bg.jpg); filter: blur(12px); z-index: -1; }

/* MODERN: backdrop-filter */
.glass {
  backdrop-filter: blur(12px);
  background: rgba(255, 255, 255, .1);
}


Reference →

Typography
Fluid typography — clamp()
/* OLD: multiple media queries for each breakpoint */
h1 { font-size: 1rem; }
@media (min-width: 600px) { h1 { font-size: 1.5rem; } }
@media (min-width: 900px) { h1 { font-size: 2rem; } }

/* MODERN: clamp for fluid scaling */
h1 { font-size: clamp(1rem, 2.5vw, 2rem); }


Reference →

Multiline text truncation — line-clamp
/* OLD: JS to slice text by chars/words and add "..." */

/* MODERN: line-clamp */
.card-title {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3;
}


Reference →

Drop caps — initial-letter
/* OLD: float hack with manual line-height */
.drop-cap::first-letter { float: left; font-size: 3em; line-height: 1; }

/* MODERN: initial-letter */
.drop-cap::first-letter { initial-letter: 3; }


Reference →

Font loading — font-display: swap
/* OLD: invisible text until font loads (FOIT) */
@font-face { font-family: "MyFont"; src: url(...); }

/* MODERN: font-display swap shows fallback immediately */
@font-face {
  font-family: "MyFont";
  src: url("MyFont.woff2");
  font-display: swap;
}


Reference →

Variable fonts — single file, all weights
/* OLD: separate @font-face for each weight */
@font-face { font-weight: 400; src: url("Regular.woff2"); }
@font-face { font-weight: 700; src: url("Bold.woff2"); }

/* MODERN: one variable font file */
@font-face {
  font-family: "MyVar";
  src: url("MyVar.woff2");
  font-weight: 100 900;
}


Reference →

Animation
Independent transforms
/* OLD: rewrite entire transform shorthand to change one value */
.icon { transform: translateX(10px) rotate(45deg) scale(1.2); }

/* MODERN: individual transform properties */
.icon {
  translate: 10px 0;
  rotate: 45deg;
  scale: 1.2;
}
/* animate any one without touching the rest */


Reference →

Typed custom properties — @property
/* OLD: custom properties are strings, can't animate */
:root { --hue: 0; }
.wheel { transition: --hue .3s; } /* ignored */

/* MODERN: @property makes them animatable */
@property --hue {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}
.wheel {
  background: hsl(var(--hue), 80%, 50%);
  transition: --hue .3s;
}


Reference →

Responsive clip paths — shape()
/* OLD: clip-path: path() uses fixed px coordinates */
.shape { clip-path: path('M0 200 L100 0...'); }

/* MODERN: shape() uses responsive units */
.shape { clip-path: shape(from 0% 100%, ...); }


Reference →

Workflow
CSS nesting — no preprocessor needed
/* OLD: requires Sass/Less compiler */
// .nav { & a { color: #888; } }

/* MODERN: native CSS nesting */
.nav {
  & a { color: #888; }
}
/* plain .css file, no build step */


Reference →

Cascade layers — @layer
/* OLD: specificity wars and !important */
.page .card .title.special { color: red !important; }

/* MODERN: cascade layers control order */
@layer base, components, utilities;
@layer utilities {
  .mt-4 { margin-top: 1rem; }
}


Reference →

Theme variables — custom properties
/* OLD: Sass variables compile to static values */
$primary: #7c3aed;
.btn { background: $primary; }

/* MODERN: CSS custom properties update at runtime */
:root { --primary: #7c3aed; }
.btn { background: var(--primary); }


Reference →

Dark mode defaults — color-scheme
/* OLD: manually restyle every form control for dark mode */
@media (prefers-color-scheme: dark) { input, select, textarea { ... } }

/* MODERN: color-scheme tells the browser to handle it */
:root { color-scheme: light dark; }


Reference →

Lazy rendering — content-visibility
/* OLD: IntersectionObserver to defer rendering */
// new IntersectionObserver((entries) => { /* render */ }).observe(el)

/* MODERN: content-visibility auto */
.section {
  content-visibility: auto;
  contain-intrinsic-size: auto 500px;
}


Reference →

Newly Available (80–90% support) — Suggest to User

These techniques are newly available across major browsers. Suggest them to the user, mention the support level, and offer a fallback if needed.

Layout
Dropdown menus — [popover] (86%)
/* OLD: display:none + JS toggle + click-outside + ESC */
.menu { display: none; }
.menu.open { display: block; }

/* MODERN: popover attribute */
/* <button popovertarget="menu">Toggle</button> */
/* <div id="menu" popover>...</div> */
#menu[popover] { position: absolute; }


Reference →

Subgrid — align nested grids to parent tracks (88%)
/* OLD: duplicate parent track definitions in child */
.child-grid { grid-template-columns: 1fr 1fr 1fr; }

/* MODERN: subgrid inherits parent tracks */
.child-grid {
  display: grid;
  grid-template-columns: subgrid;
}


Reference →

Customizable selects — appearance: base-select (86%)
/* OLD: Select2 or Choices.js replacing native select */

/* MODERN: base-select unlocks full styling */
select, select ::picker(select) {
  appearance: base-select;
}


Note: support is expanding rapidly — verify current status on caniuse. Reference →

Hover tooltips — popover=hint + interestfor (86%)
<!-- OLD: JS mouseenter/mouseleave + focus/blur + positioning -->

<!-- MODERN: declarative hover trigger -->
<button interestfor="tip">Hover me</button>
<div id="tip" popover=hint>Tooltip content</div>


Reference →

Animation
Entry animations — @starting-style (85%)
/* OLD: requestAnimationFrame to add class after paint */
// requestAnimationFrame(() => el.classList.add('visible'))

/* MODERN: @starting-style defines entry state */
.card {
  transition: opacity .3s, transform .3s;
  @starting-style {
    opacity: 0;
    transform: translateY(10px);
  }
}


Reference →

Animating display: none — transition-behavior: allow-discrete (85%)
/* OLD: wait for transitionend, use visibility + opacity + pointer-events */

/* MODERN: allow-discrete enables display transitions */
.panel {
  transition: opacity .2s, display .2s;
  transition-behavior: allow-discrete;
}
.panel.hidden { opacity: 0; display: none; }


Reference →

Page transitions — View Transitions API (89%)
/* OLD: Barba.js or React Transition Group */

/* MODERN: View Transitions API */
/* JS: document.startViewTransition(() => updateDOM()); */
.hero { view-transition-name: hero; }
/* Style with ::view-transition-old(hero) / ::view-transition-new(hero) */


Reference →

Color
Color mixing — color-mix() (89%)
/* OLD: Sass mix($blue, $pink, 60%) */

/* MODERN: color-mix in CSS */
background: color-mix(in oklch, #3b82f6, #ec4899);


Reference →

Color variants — relative color syntax (87%)
/* OLD: Sass lighten($brand, 20%) — compile-time only */

/* MODERN: relative color syntax — runtime */
.btn {
  background: oklch(from var(--brand) calc(l + 0.2) c h);
}
/* change --brand and all derivatives update */


Reference →

Dark mode colors — light-dark() (83%)
/* OLD: duplicate values in prefers-color-scheme media query */
@media (prefers-color-scheme: dark) { color: #eee; }

/* MODERN: light-dark() function */
color: light-dark(#111, #eee);
color-scheme: light dark;


Reference →

Selectors
Form validation — :user-invalid / :user-valid (85%)
/* OLD: JS blur listener to add .touched class */
// el.addEventListener('blur', () => el.classList.add('touched'))

/* MODERN: :user-invalid only fires after interaction */
input:user-invalid { border-color: red; }
input:user-valid { border-color: green; }


Reference →

Workflow
Scoped styles — @scope (84%)
/* OLD: BEM naming (.card__title) or CSS Modules */

/* MODERN: @scope limits selectors to a root */
@scope (.card) {
  .title { font-size: 1.25rem; }
  .body { color: #444; }
}
/* .title only matches inside .card */


Reference →

Range style queries (88%)
/* OLD: multiple style() blocks for each value */
@container style(--p: 51%) {}
@container style(--p: 52%) {}

/* MODERN: range comparisons */
@container style(--progress > 50%) {
  .bar { ... }
}


Reference →

Typography
Balanced headlines — text-wrap: balance (87%)
/* OLD: manual <br> tags or Balance-Text.js */

/* MODERN: text-wrap balance */
h1, h2 { text-wrap: balance; }


Reference →

Limited Availability (<80% support) — Ask Before Using

These are cutting-edge CSS features. Always ask the user before using them, warn about browser support, and suggest fallbacks or progressive enhancement strategies.

Layout
Modal controls — commandfor (72%)
<!-- OLD: onclick handler to call showModal() -->
<button onclick="document.querySelector('#dlg').showModal()">Open</button>

<!-- MODERN: declarative command -->
<button commandfor="dlg" command="show-modal">Open</button>
<dialog id="dlg">...</dialog>


Fallback: use a small JS onclick handler to call dialog.showModal(). Reference →

Dialog light dismiss — closedby="any" (72%)
<!-- OLD: JS click listener checking click bounds -->

<!-- MODERN: closedby attribute -->
<dialog closedby="any">Click outside to close</dialog>


Fallback: add a click listener on ::backdrop to call dialog.close(). Reference →

Anchor positioning — position-anchor + anchor() (77%)
/* OLD: Popper.js / Floating UI for tooltip positioning */

/* MODERN: CSS anchor positioning */
.trigger { anchor-name: --tip; }
.tooltip {
  position-anchor: --tip;
  top: anchor(bottom);
}


Fallback: use Floating UI or absolute positioning with JS. Reference →

Carousel controls — ::scroll-button / ::scroll-marker (72%)
/* OLD: Swiper.js or Slick carousel */

/* MODERN: native scroll markers and buttons */
.carousel::scroll-button(right) { content: "→"; }
.carousel li::scroll-marker { content: ''; }


Fallback: use CSS scroll-snap with custom buttons via JS. Reference →

Corner shapes — corner-shape: squircle (67%)
/* OLD: clip-path polygon with 20+ points */

/* MODERN: corner-shape property */
.card {
  border-radius: 2em;
  corner-shape: squircle;
}


Fallback: use standard border-radius or SVG clip-path. Reference →

Animation
Scroll-driven animations — animation-timeline: view() (78%)
/* OLD: IntersectionObserver + GSAP or AOS.js */

/* MODERN: CSS scroll-driven animations */
@keyframes reveal {
  from { opacity: 0; translate: 0 40px; }
  to   { opacity: 1; translate: 0 0; }
}
.reveal {
  animation: reveal linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 100%;
}


Fallback: use IntersectionObserver with a .visible class toggle. Polyfill: scroll-timeline Reference →

Height auto animations — interpolate-size: allow-keywords (69%)
/* OLD: JS to measure scrollHeight, set px, then transition */

/* MODERN: interpolate-size enables height:auto transitions */
:root { interpolate-size: allow-keywords; }
.accordion { height: 0; overflow: hidden; transition: height .3s ease; }
.accordion.open { height: auto; }


Fallback: use max-height with a large value, or JS measurement. Reference →

Staggered animations — sibling-index() (72%)
/* OLD: nth-child custom property for each item */
li:nth-child(1) { --i: 0; }
li:nth-child(2) { --i: 1; }

/* MODERN: sibling-index() function */
li {
  transition-delay: calc(0.1s * (sibling-index() - 1));
}


Fallback: use nth-child with CSS custom properties. Reference →

Sticky/snapped element styling — scroll-state container queries (50%)
/* OLD: JS scroll listener checking element position */

/* MODERN: @container scroll-state() */
@container scroll-state(stuck: top) {
  .header { box-shadow: 0 2px 8px rgb(0 0 0 / .1); }
}


Fallback: use IntersectionObserver to toggle a class. Reference →

Typography
Vertical text centering — text-box (79%)
/* OLD: uneven padding hacks for optical centering */
.btn { padding: 10px 20px; padding-top: 8px; /* hack */ }

/* MODERN: text-box trims leading/trailing space */
h1, button {
  text-box: trim-both cap alphabetic;
}


Fallback: use manual padding adjustments. Reference →

Auto-growing textarea — field-sizing: content (73%)
/* OLD: JS input listener resizing on every keystroke */

/* MODERN: field-sizing */
textarea {
  field-sizing: content;
  min-height: 3lh;
}


Fallback: use a JS auto-resize handler. Reference →

Selectors
Scroll spy — :target-current (48%)
/* OLD: IntersectionObserver with 15+ lines of JS */

/* MODERN: :target-current pseudo-class */
nav a:target-current {
  color: var(--accent);
}


Fallback: use IntersectionObserver to toggle an .active class. Reference →

Workflow
CSS functions — @function (67%)
/* OLD: Sass @function */
// @function fluid($min, $max) { @return clamp(...); }

/* MODERN: native CSS @function */
@function --fluid(--min, --max) {
  @return clamp(...);
}


Fallback: use Sass functions or repeated clamp() expressions. Reference →

Typed attribute values — attr() with type (42%)
/* OLD: JS reading dataset to set styles */
// el.style.width = el.dataset.pct + '%';

/* MODERN: attr() with type() */
.bar { width: attr(data-pct type(<percentage>)); }


Fallback: use JS to read data attributes and set inline styles. Reference →

Inline conditionals — if() (35%)
/* OLD: JS classList toggle */
// el.classList.toggle('primary', isPrimary)

/* MODERN: CSS if() function */
.btn {
  background: if(style(--variant: primary): blue; else: gray);
}


Fallback: use CSS custom properties with class toggles. Reference →

Core Principles

When writing any CSS, follow these guiding principles:

Native CSS over JavaScript — If CSS can do it, don't use JS. Scroll snap over carousel libraries. Popover over toggle scripts. Dialog over modal libraries.
Logical properties over physical — Use inline/block instead of left/right/ top/bottom. Your layout will work in any writing direction.
Intrinsic sizing over fixed breakpoints — Use clamp(), min(), max(), container queries, and flex/grid auto-sizing. Let content determine layout.
Custom properties over preprocessor variables — CSS custom properties update at runtime, work with JS, and cascade. Sass variables compile away.
Cascade layers over specificity hacks — Use @layer to organize your cascade. Stop using !important or deep nesting to win specificity battles.
Progressive enhancement — Use modern features with fallbacks. Use @supports to gate Newly Available and Limited features behind capability checks:
/* fallback for older browsers */
.card { display: flex; flex-wrap: wrap; }

/* modern upgrade */
@supports (container-type: inline-size) {
  .wrapper { container-type: inline-size; }
  @container (width > 400px) { .card { flex-direction: row; } }
}

Quick Decision Guide
You want to...	Use this
Center something	display: grid; place-items: center
Space children evenly	gap on flex/grid
Maintain aspect ratio	aspect-ratio: 16 / 9
Pin a header on scroll	position: sticky; top: 0
Responsive component	@container query
Create a modal	<dialog> element
Create a dropdown	[popover] attribute 🟡
Select parent based on child	:has() selector
Style keyboard focus only	:focus-visible
Fluid font size	clamp(min, preferred, max)
Truncate multiline text	line-clamp: N
Balance headline wrapping	text-wrap: balance 🟡
Animate on scroll	animation-timeline: view() ⚠️
Page transitions	View Transitions API 🟡
Animate into view	@starting-style 🟡
Create color palette from one color	oklch() with adjusted lightness
Mix two colors	color-mix(in oklch, ...) 🟡
Dark mode colors	light-dark() + color-scheme 🟡
Scope styles to a component	@scope (.component) 🟡
Control cascade order	@layer
Nest selectors	Native CSS nesting & selector
Type a custom property	@property
Position a tooltip	CSS anchor positioning ⚠️

No marker = Widely Available (90%+, always use). 🟡 = Newly Available (80–90%, suggest to user). ⚠️ = Limited (<80%, ask first).

Weekly Installs
46
Repository
caidanw/skills
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass