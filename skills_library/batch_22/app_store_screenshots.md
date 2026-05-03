---
title: app-store-screenshots
url: https://skills.sh/boraoztunc/skills/app-store-screenshots
---

# app-store-screenshots

skills/boraoztunc/skills/app-store-screenshots
app-store-screenshots
Installation
$ npx skills add https://github.com/boraoztunc/skills --skill app-store-screenshots
SKILL.md
App Store Screenshots Generator
Overview

Build a Next.js page that renders iOS App Store screenshots as advertisements (not UI showcases) and exports them via html-to-image at Apple's required resolutions. Screenshots are the single most important conversion asset on the App Store.

Core Principle

Screenshots are advertisements, not documentation. Every screenshot sells one idea. If you're showing UI, you're doing it wrong — you're selling a feeling, an outcome, or killing a pain point.

Step 1: Ask the User These Questions

Before writing ANY code, ask the user all of these. Do not proceed until you have answers:

Required
App screenshots — "Where are your app screenshots? (PNG files of actual device captures)"
App icon — "Where is your app icon PNG?"
Brand colors — "What are your brand colors? (accent color, text color, background preference)"
Font — "What font does your app use? (or what font do you want for the screenshots?)"
Feature list — "List your app's features in priority order. What's the #1 thing your app does?"
Number of slides — "How many screenshots do you want? (Apple allows up to 10)"
Style direction — "What style do you want? Examples: warm/organic, dark/moody, clean/minimal, bold/colorful, gradient-heavy, flat. Share App Store screenshot references if you have any."
Optional
iPad screenshots — "Do you also have iPad screenshots? If so, we'll generate iPad App Store screenshots too (recommended for universal apps)."
Component assets — "Do you have any UI element PNGs (cards, widgets, etc.) you want as floating decorations? If not, that's fine — we'll skip them."
Localized screenshots — "Do you want screenshots in multiple languages? This helps your listing rank in regional App Stores even if your app is English-only. If yes: which languages? (e.g. en, de, es, pt, ja, ar, he)"
Theme preset system — "Do you want one art direction, or reusable visual themes (for example: clean-light, dark-bold, warm-editorial) so you can swap screenshot looks quickly?"
Additional instructions — "Any specific requirements, constraints, or preferences?"
Derived from answers (do NOT ask — decide yourself)

Based on the user's style direction, brand colors, and app aesthetic, decide:

Background style: gradient direction, colors, whether light or dark base
Decorative elements: blobs, glows, geometric shapes, or none — match the style
Dark vs light slides: how many of each, which features suit dark treatment
Typography treatment: weight, tracking, line height — match the brand personality
Color palette: derive text colors, secondary colors, shadow tints from the brand colors
Theme preset names: turn vague style requests into reusable theme ids the user can switch between
RTL behavior: if any locale is RTL (ar, he, fa, ur), mirror layout intentionally instead of just translating the text

IMPORTANT: If the user gives additional instructions at any point during the process, follow them. User instructions always override skill defaults.

Step 2: Set Up the Project
Detect Package Manager

Check what's available, use this priority: bun > pnpm > yarn > npm

# Check in order
which bun && echo "use bun" || which pnpm && echo "use pnpm" || which yarn && echo "use yarn" || echo "use npm"

Scaffold (if no existing Next.js project)
# With bun:
bunx create-next-app@latest . --typescript --tailwind --app --src-dir --no-eslint --import-alias "@/*"
bun add html-to-image

# With pnpm:
pnpx create-next-app@latest . --typescript --tailwind --app --src-dir --no-eslint --import-alias "@/*"
pnpm add html-to-image

# With yarn:
yarn create next-app . --typescript --tailwind --app --src-dir --no-eslint --import-alias "@/*"
yarn add html-to-image

# With npm:
npx create-next-app@latest . --typescript --tailwind --app --src-dir --no-eslint --import-alias "@/*"
npm install html-to-image

Copy the Phone Mockup

The skill includes a pre-measured iPhone mockup at mockup.png (co-located with this SKILL.md). Copy it to the project's public/ directory. The mockup file is in the same directory as this skill file. No iPad mockup is needed — the iPad frame is CSS-only.

File Structure
project/
├── public/
│   ├── mockup.png              # iPhone frame (included with skill)
│   ├── app-icon.png            # User's app icon
│   ├── screenshots/            # iPhone app screenshots
│   │   ├── home.png
│   │   ├── feature-1.png
│   │   └── ...
│   └── screenshots-ipad/       # iPad app screenshots (optional)
│       ├── home.png
│       ├── feature-1.png
│       └── ...
├── src/app/
│   ├── layout.tsx              # Font setup
│   └── page.tsx                # The screenshot generator (single file)
└── package.json


Note: No iPad mockup PNG is needed — the iPad frame is rendered with CSS (see iPad Mockup Component below).

Multi-language: nest screenshots under a locale folder per language. The generator switches the base path; all slide image srcs stay identical.

└── screenshots/
    ├── en/
    │   ├── home.png
    │   ├── feature-1.png
    │   └── ...
    ├── de/
    │   └── ...
    └── {locale}/


If iPad screenshots are localized too, mirror the same locale structure:

└── screenshots-ipad/
    ├── en/
    ├── de/
    └── {locale}/


The entire generator is a single page.tsx file. No routing, no extra layouts, no API routes.

Multi-language: Locale Tabs

Add a LOCALES array and locale tabs to the toolbar. Every slide src uses base — no hardcoded paths:

const LOCALES = ["en", "de", "es"] as const; // use whatever langs were defined
type Locale = typeof LOCALES[number];

// In ScreenshotsPage:
const [locale, setLocale] = useState<Locale>("en");
const base = `/screenshots/${locale}`;

// Toolbar tabs:
{LOCALES.map(l => (
  <button key={l} onClick={() => setLocale(l)}
    style={{ fontWeight: locale === l ? 700 : 400 }}>
    {l.toUpperCase()}
  </button>
))}

// In every slide — unchanged between single and multi-language:
<Phone src={`${base}/home.png`} alt="Home" />

Theme Presets + Locale Metadata

Add a small config layer so the user can switch theme and locale without rewriting slide components:

const LOCALES = ["en", "de", "ar"] as const;
type Locale = typeof LOCALES[number];

const RTL_LOCALES = new Set<Locale>(["ar"]);

const THEMES = {
  "clean-light": {
    bg: "#F6F1EA",
    fg: "#171717",
    accent: "#5B7CFA",
    muted: "#6B7280",
  },
  "dark-bold": {
    bg: "#0B1020",
    fg: "#F8FAFC",
    accent: "#8B5CF6",
    muted: "#94A3B8",
  },
  "warm-editorial": {
    bg: "#F7E8DA",
    fg: "#2B1D17",
    accent: "#D97706",
    muted: "#7C5A47",
  },
} as const;

type ThemeId = keyof typeof THEMES;

const COPY_BY_LOCALE = {
  en: { hero: "Build better habits" },
  de: { hero: "Baue bessere Gewohnheiten auf" },
  ar: { hero: "ابنِ عادات أفضل" },
} satisfies Record<Locale, { hero: string }>;

const [themeId, setThemeId] = useState<ThemeId>("clean-light");
const [locale, setLocale] = useState<Locale>("en");

const theme = THEMES[themeId];
const copy = COPY_BY_LOCALE[locale];
const isRtl = RTL_LOCALES.has(locale);


Use theme tokens everywhere instead of hardcoding colors. For RTL locales, set dir={isRtl ? "rtl" : "ltr"} on the screenshot canvas and mirror asymmetric layouts intentionally.

Support query params for automation:

// ?locale=de&theme=dark-bold&device=ipad

Font Setup
// src/app/layout.tsx
import { YourFont } from "next/font/google"; // Use whatever font the user specified
const font = YourFont({ subsets: ["latin"] });

export default function Layout({ children }: { children: React.ReactNode }) {
  return <html><body className={font.className}>{children}</body></html>;
}

Step 3: Plan the Slides
Screenshot Framework (Narrative Arc)

Adapt this framework to the user's requested slide count. Not all slots are required — pick what fits:

Slot	Purpose	Notes
#1	Hero / Main Benefit	App icon + tagline + home screen. This is the ONLY one most people see.
#2	Differentiator	What makes this app unique vs competitors
#3	Ecosystem	Widgets, extensions, watch — beyond the main app. Skip if N/A.
#4+	Core Features	One feature per slide, most important first
2nd to last	Trust Signal	Identity/craft — "made for people who [X]"
Last	More Features	Pills listing extras + coming soon. Skip if few features.

Rules:

Each slide sells ONE idea. Never two features on one slide.
Vary layouts across slides — never repeat the same template structure.
Include 1-2 contrast slides (inverted bg) for visual rhythm.
Step 4: Write Copy FIRST

Get all headlines approved before building layouts. Bad copy ruins good design.

The Iron Rules
One idea per headline. Never join two things with "and."
Short, common words. 1-2 syllables. No jargon unless it's domain-specific.
3-5 words per line. Must be readable at thumbnail size in the App Store.
Line breaks are intentional. Control where lines break with <br />.
Three Approaches (pick one per slide)
Type	What it does	Example
Paint a moment	You picture yourself doing it	"Check your coffee without opening the app."
State an outcome	What your life looks like after	"A home for every coffee you buy."
Kill a pain	Name a problem and destroy it	"Never waste a great bag of coffee."
What NEVER Works
Feature lists as headlines: "Log every item with tags, categories, and notes"
Two ideas joined by "and": "Track X and never miss Y"
Compound clauses: "Save and customize X for every Y you own"
Vague aspirational: "Every item, tracked"
Marketing buzzwords: "AI-powered tips" (unless it's actually AI)
Bad-to-Better Headline Examples

Use these patterns to rewrite weak copy before building any layout:

Weak	Better	Why it wins
Track habits and stay motivated	Keep your streak alive	one idea, faster to parse
Organize tasks with AI summaries and smart sorting	Turn notes into next steps	outcome-first, less jargon
Save recipes with tags, filters, and favorites	Find dinner fast	sells the user benefit, not the UI
Manage budgets and never miss payments	See where money goes	cleaner promise, no dual claim
AI-powered wellness support	Feel calmer tonight	concrete emotional outcome
Copy Process
Write 3 options per slide using the three approaches
Read each at arm's length — if you can't parse it in 1 second, it's too complex
Check: does each line have 3-5 words? If not, adjust line breaks
Present options to the user with reasoning for each
Example Prompt Shapes

If the user gives a weak or underspecified request, reshape it internally into something like:

Build App Store screenshots for my habit tracker.
The app helps people stay consistent with simple daily routines.
I want 6 slides, clean/minimal style, warm neutrals, and a calm premium feel.

Generate App Store screenshots for my personal finance app.
The app's main strengths are fast expense capture, clear monthly trends, and shared budgets.
I want a sharp, modern style with high contrast and 7 slides.

Create exportable App Store screenshots for my AI note-taking app.
The core value is turning messy voice notes into clean summaries and action items.
I want bold copy, dark backgrounds, and a polished tech-forward look.


The pattern is:

app category + core outcome
top features in priority order
desired slide count
style direction
Localization Rules
Do not literally translate headlines if the result becomes long or awkward.
Re-write copy for the target market while keeping the same selling idea.
Re-check line breaks per locale; German, French, and Portuguese often need shorter claims.
For RTL languages, also reverse badge alignment, supporting decorations, and phone offsets when the composition depends on left/right weight.
Reference Apps for Copy Style
Raycast — specific, descriptive, one concrete value per slide
Turf — ultra-simple action verbs, conversational
Mela / Notion — warm, minimal, elegant
Step 5: Build the Page
Architecture
page.tsx
├── Constants (IPHONE_W/H, IPAD_W/H, SIZES, design tokens)
├── LOCALES / RTL_LOCALES / THEMES / COPY_BY_LOCALE
├── Phone component (mockup PNG with screen overlay)
├── IPad component (CSS-only frame with screen overlay)
├── Caption component (label + headline, accepts canvasW for scaling)
├── Decorative components (blobs, glows, shapes — based on style direction)
├── iPhoneSlide1..N components (one per slide)
├── iPadSlide1..N components (same designs, adjusted for iPad proportions)
├── IPHONE_SCREENSHOTS / IPAD_SCREENSHOTS arrays (registries)
├── ScreenshotPreview (ResizeObserver scaling + hover export)
└── ScreenshotsPage (grid + locale tabs + theme tabs + device toggle + export logic)

Export Sizes (Apple Required, portrait)
iPhone
const IPHONE_SIZES = [
  { label: '6.9"', w: 1320, h: 2868 },
  { label: '6.5"', w: 1284, h: 2778 },
  { label: '6.3"', w: 1206, h: 2622 },
  { label: '6.1"', w: 1125, h: 2436 },
] as const;


Design at the LARGEST size (1320x2868) and scale down for export.

iPad (Optional)

If the user provides iPad screenshots, also generate iPad App Store screenshots:

const IPAD_SIZES = [
  { label: '13" iPad', w: 2064, h: 2752 },
  { label: '12.9" iPad Pro', w: 2048, h: 2732 },
] as const;


Design iPad slides at 2064x2752 and scale down. iPad screenshots are optional but recommended — they're required for iPad-only apps and improve listing quality for universal apps.

Device Toggle

When supporting both devices, add a toggle (iPhone / iPad) in the toolbar next to the size dropdown. The size dropdown should switch between iPhone and iPad sizes based on the selected device. Support a ?device=ipad URL parameter for headless/automated capture workflows.

Theme + Locale Toggles

Place locale and theme selectors in the same toolbar as device + size. This turns the generator into a small control panel instead of a one-off page.

locale switches screenshot folders and copy dictionaries
theme switches design tokens only
device switches iPhone/iPad slide registries
size switches export resolution only
Rendering Strategy

Each screenshot is designed at full resolution (1320x2868px). Two copies exist:

Preview: CSS transform: scale() via ResizeObserver to fit a grid card
Export: Offscreen at position: absolute; left: -9999px at true resolution
Phone Mockup Component

The included mockup.png has these pre-measured values:

const MK_W = 1022;  // mockup image width
const MK_H = 2082;  // mockup image height
const SC_L = (52 / MK_W) * 100;   // screen left offset %
const SC_T = (46 / MK_H) * 100;   // screen top offset %
const SC_W = (918 / MK_W) * 100;  // screen width %
const SC_H = (1990 / MK_H) * 100; // screen height %
const SC_RX = (126 / 918) * 100;  // border-radius x %
const SC_RY = (126 / 1990) * 100; // border-radius y %

function Phone({ src, alt, style, className = "" }: {
  src: string; alt: string; style?: React.CSSProperties; className?: string;
}) {
  return (
    <div className={`relative ${className}`}
      style={{ aspectRatio: `${MK_W}/${MK_H}`, ...style }}>
      <img src="/mockup.png" alt=""
        className="block w-full h-full" draggable={false} />
      <div className="absolute z-10 overflow-hidden"
        style={{
          left: `${SC_L}%`, top: `${SC_T}%`,
          width: `${SC_W}%`, height: `${SC_H}%`,
          borderRadius: `${SC_RX}% / ${SC_RY}%`,
        }}>
        <img src={src} alt={alt}
          className="block w-full h-full object-cover object-top"
          draggable={false} />
      </div>
    </div>
  );
}

iPad Mockup Component (CSS-Only)

Unlike the iPhone mockup which uses a pre-measured PNG frame, the iPad uses a CSS-only frame. This avoids needing a separate mockup asset and looks clean at any resolution.

Critical dimension: The frame aspect ratio must be 770/1000 so the inner screen area (92% width × 94.4% height) matches the 3:4 aspect ratio of iPad screenshots. Using incorrect proportions causes black bars or stretched screenshots.

function IPad({ src, alt, style, className = "" }: {
  src: string; alt: string; style?: React.CSSProperties; className?: string;
}) {
  return (
    <div className={`relative ${className}`}
      style={{ aspectRatio: "770/1000", ...style }}>
      <div style={{
        width: "100%", height: "100%", borderRadius: "5% / 3.6%",
        background: "linear-gradient(180deg, #2C2C2E 0%, #1C1C1E 100%)",
        position: "relative", overflow: "hidden",
        boxShadow: "inset 0 0 0 1px rgba(255,255,255,0.1), 0 8px 40px rgba(0,0,0,0.6)",
      }}>
        {/* Front camera dot */}
        <div style={{
          position: "absolute", top: "1.2%", left: "50%",
          transform: "translateX(-50%)", width: "0.9%", height: "0.65%",
          borderRadius: "50%", background: "#111113",
          border: "1px solid rgba(255,255,255,0.08)", zIndex: 20,
        }} />
        {/* Bezel edge highlight */}
        <div style={{
          position: "absolute", inset: 0, borderRadius: "5% / 3.6%",
          border: "1px solid rgba(255,255,255,0.06)",
          pointerEvents: "none", zIndex: 15,
        }} />
        {/* Screen area */}
        <div style={{
          position: "absolute", left: "4%", top: "2.8%",
          width: "92%", height: "94.4%",
          borderRadius: "2.2% / 1.6%", overflow: "hidden", background: "#000",
        }}>
          <img src={src} alt={alt}
            style={{ display: "block", width: "100%", height: "100%",
              objectFit: "cover", objectPosition: "top" }}
            draggable={false} />
        </div>
      </div>
    </div>
  );
}


iPad layout adjustments vs iPhone:

Use width: "65-70%" for iPad mockups (vs 82-86% for iPhone) — iPad is wider relative to its height
Two-iPad layouts work the same as two-phone layouts but with adjusted widths
Caption font sizes should scale from canvasW (which is 2064 for iPad vs 1320 for iPhone)
Same slide designs/copy can be reused — just swap the Phone component for IPad and adjust positioning
Typography (Resolution-Independent)

All sizing relative to canvas width W:

Element	Size	Weight	Line Height
Category label	W * 0.028	600 (semibold)	default
Headline	W * 0.09 to W * 0.1	700 (bold)	1.0
Hero headline	W * 0.1	700 (bold)	0.92
Phone Placement Patterns

Vary across slides — NEVER use the same layout twice in a row:

Centered phone (hero, single-feature):

bottom: 0, width: "82-86%", translateX(-50%) translateY(12-14%)


Two phones layered (comparison):

Back: left: "-8%", width: "65%", rotate(-4deg), opacity: 0.55
Front: right: "-4%", width: "82%", translateY(10%)


Phone + floating elements (only if user provided component PNGs):

Cards should NOT block the phone's main content.
Position at edges, slight rotation (2-5deg), drop shadows.
If distracting, push partially off-screen or make smaller.

"More Features" Slide (Optional)

Dark/contrast background with app icon, headline ("And so much more."), and feature pills. Can include a "Coming Soon" section with dimmer pills.

Step 6: Export
Why html-to-image, NOT html2canvas

html2canvas breaks on CSS filters, gradients, drop-shadow, backdrop-filter, and complex clipping. html-to-image uses native browser SVG serialization — handles all CSS faithfully.

Export Implementation
import { toPng } from "html-to-image";

// Before capture: move element on-screen
el.style.left = "0px";
el.style.opacity = "1";
el.style.zIndex = "-1";

const opts = { width: W, height: H, pixelRatio: 1, cacheBust: true };

// CRITICAL: Double-call trick — first warms up fonts/images, second produces clean output
await toPng(el, opts);
const dataUrl = await toPng(el, opts);

// After capture: move back off-screen
el.style.left = "-9999px";
el.style.opacity = "";
el.style.zIndex = "";

Export Matrix

If the project supports multiple locales and themes, add bulk export helpers so the user can export everything in one pass:

const jobs = LOCALES.flatMap(locale =>
  ACTIVE_THEME_IDS.flatMap(themeId =>
    ACTIVE_DEVICES.flatMap(device =>
      getSlidesFor(device).map((slide, index) => ({
        locale,
        themeId,
        device,
        index,
        slide,
      })),
    ),
  ),
);


Name files so they sort cleanly and preserve metadata:

01-hero-en-clean-light-iphone-1320x2868.png
01-hero-ar-dark-bold-ipad-2064x2752.png


At minimum, support:

export current slide
export all slides for current locale/device/theme
export all locales for current theme
export full matrix when the user explicitly asks for it
Key Rules
Double-call trick: First toPng() loads fonts/images lazily. Second produces clean output. Without this, exports are blank.
On-screen for capture: Temporarily move to left: 0 before calling toPng.
Offscreen container: Use position: absolute; left: -9999px (not fixed).
Resizing: Load data URL into Image, draw onto canvas at target size.
300ms delay between sequential exports.
Set fontFamily on the offscreen container.
Numbered filenames: Prefix exports with zero-padded index so they sort correctly: 01-hero-1320x2868.png, 02-freshness-1320x2868.png, etc. Use String(index + 1).padStart(2, "0").
Step 7: Final QA Gate

Before handing the page back to the user, review every slide against this checklist:

Message Quality
One idea per slide: if a headline sells two ideas, split it or simplify it
First slide is strongest: the hero slide should communicate the main benefit immediately
Readable in one second: if you cannot parse it instantly at arm's length, rewrite it
Visual Quality
No repeated layouts in sequence: adjacent slides should not feel templated
Decorative elements support the story: they should add energy without covering the app UI
Visual rhythm exists: include at least one contrast slide when the set is long enough
Export Quality
No clipped text or assets after scaling to the selected export size
Screenshots are correctly aligned inside the phone or iPad frame
Filenames sort correctly with zero-padded numeric prefixes
Theme tokens are applied consistently across all slides in the same preset
Localized copy still fits after translation, especially on long-word languages
RTL slides feel designed, not just flipped
Hand-off Behavior

When you present the finished work:

briefly explain the narrative arc across the slides
mention any slides that intentionally use contrast or different layout treatment
call out any assumptions you made about brand tone, copy, or missing assets
Common Mistakes
Mistake	Fix
All slides look the same	Vary phone position (center, left, right, two-phone, no-phone)
Decorative elements invisible	Increase size and opacity — better too visible than invisible
Copy is too complex	"One second at arm's length" test
Floating elements block the phone	Move off-screen edges or above the phone
Plain white/black background	Use gradients — even subtle ones add depth
Too cluttered	Remove floating elements, simplify to phone + caption
Too simple/empty	Add larger decorative elements, floating items at edges
Headlines use "and"	Split into two slides or pick one idea
No visual contrast across slides	Mix light and dark backgrounds
Export is blank	Use double-call trick; move element on-screen before capture
Weekly Installs
22
Repository
boraoztunc/skills
GitHub Stars
15
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass