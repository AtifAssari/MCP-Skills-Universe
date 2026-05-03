---
rating: ⭐⭐
title: mobile-app
url: https://skills.sh/nexu-io/open-design/mobile-app
---

# mobile-app

skills/nexu-io/open-design/mobile-app
mobile-app
Installation
$ npx skills add https://github.com/nexu-io/open-design --skill mobile-app
SKILL.md
Mobile App Skill

Produce a single mobile-app screen mockup, framed inside a real-feeling iPhone 15 Pro device.

Resource map
mobile-app/
├── SKILL.md                ← you're reading this
├── assets/
│   └── template.html       ← seed: device frame + screen primitives (READ FIRST)
└── references/
    ├── layouts.md          ← 6 screen archetypes (Feed / Detail / Onboarding / Profile / Checkout / Focus)
    └── checklist.md        ← P0/P1/P2 self-review (anti-fake-device)

Workflow
Step 0 — Pre-flight
Read assets/template.html end-to-end through the <style> block. The Dynamic Island, status bar SVG icons, home indicator, side rails, and tab bar are all already drawn in HTML/SVG — do not re-implement them inline on each screen.
Read references/layouts.md so you know which 6 archetypes exist.
Read the active DESIGN.md — map its tokens to the six :root variables in the seed.
Step 1 — Copy the seed

Copy assets/template.html to the project root as index.html. Replace the six :root variables with the active design system's tokens. Replace the page <title> and the caption above the device.

Step 2 — Pick exactly one archetype
Brief language	Use
feed, inbox, timeline, list, messages, notifications	A — Feed
article, post, item, recipe, song, product, song detail	B — Detail
sign-up, welcome, intro, walkthrough, tour	C — Onboarding
profile, account, user page, someone's bio	D — Profile
checkout, payment, order, form, settings step	E — Checkout
timer, map, dashboard widget, single big number	F — Focus / hero card

A mobile screen does one job. If the brief seems to combine two, ship one screen and offer the other as a follow-up.

Step 3 — Paste and fill

Copy the archetype block from layouts.md into <main class="content">, replacing the placeholder card. Fill bracketed text with real, specific copy from the brief. Drop the <nav class="tabbar"> block entirely for archetypes that don't show one (B, C, E).

Step 4 — Self-check

Run through references/checklist.md. Pay extra attention to:

Frame still has the Dynamic Island, status bar SVGs, and home indicator
Tap targets ≥ 44px
One accent, used ≤ 2× on the screen
Display headings still use var(--font-display) (serif)
Step 5 — Emit the artifact
<artifact identifier="mobile-slug" type="text/html" title="Mobile — Screen Name">
<!doctype html>
<html>...</html>
</artifact>


One sentence before describing what's there. Stop after </artifact>.

Hard rules
The phone is real. Dynamic Island gap, SVG status icons, home indicator. The seed protects all three — don't rewrite the frame.
Single screen, single job. No multi-tab tours, no spliced flows.
Accent budget = 2. One active tab + one primary action is the default.
Numerics in mono via .num class.
Display in serif via var(--font-display).
No external images — use .ph-img placeholders.
Weekly Installs
68
Repository
nexu-io/open-design
GitHub Stars
14.2K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass