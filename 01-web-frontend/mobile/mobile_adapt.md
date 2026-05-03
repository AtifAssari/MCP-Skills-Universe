---
rating: ⭐⭐⭐
title: mobile-adapt
url: https://skills.sh/s0up4200/skills/mobile-adapt
---

# mobile-adapt

skills/s0up4200/skills/mobile-adapt
mobile-adapt
Installation
$ npx skills add https://github.com/s0up4200/skills --skill mobile-adapt
SKILL.md
Mobile Adapt
Goal

Adapt existing interfaces to work well on phones without removing core functionality. Prioritize iPhone-class mobile web unless the user names another target.

Default target

If the user does not specify a device or browser, optimize first for:

iPhone Pro Max class in portrait and landscape
iOS Safari
compact touch screens around 390-440 CSS px wide
keyboard-open use, large text, safe areas, and reduced motion
When to research

This skill depends on current platform behavior.

Browse official sources when the user asks for the latest/current guidance, iPhone-specific behavior, Safari/WebKit quirks, safe-area behavior, PWA/home-screen behavior, or direct citations.
Prefer Apple Developer, WebKit, W3C/WCAG, MDN, Android Developers, and web.dev.
Use absolute dates when citing recent platform changes.

For the current high-signal rules and sources, read references/mobile-ui-2026.md.

Core rules

Keep compact phones single-pane. Do not switch to desktop IA just because a landscape phone crosses a generic breakpoint. A phone rotated sideways is still held in two hands at arm's length — the user's mental model is "phone," not "tablet." Breaking into a multi-pane layout creates a disorienting experience where nothing is big enough to use comfortably.

Use bottom-first mobile navigation for true top-level sections only. Keep it to 3-5 primary destinations; move overflow to More, a sheet, or secondary flows. The bottom of the screen is the thumb's natural resting zone — putting primary nav there means the most common actions require the least effort. More than 5 items shrink tap targets below usable size and overwhelm scanning.

Every interactive target should be at least 44x44 CSS px in both dimensions. This includes secondary elements that are easy to overlook: inline action buttons (edit, delete, view), expand/collapse toggles, filter chips, icon buttons in toolbars, close buttons on sheets, and checkbox/radio rows (use the <label> as the full tap target, not the input alone). Capacitive touchscreens register the center of a finger's contact patch at roughly 44pt — smaller targets cause mispress frustration, especially in motion. Common Tailwind classes that fall short: h-8 (32px), h-9 (36px), p-1 on an icon (~24px), p-1.5 (~28px), p-2 (~32px). Use h-11 (44px), min-h-[44px], or equivalent as the baseline for every tappable element. This aligns with Apple HIG and exceeds WCAG 2.2's 24px minimum.

Do not rely on hover, tiny icon taps, or hidden row actions. There is no hover state on touch — anything that requires hover to discover is invisible. Use visible controls, swipe actions with a visual hint, or a contextual sheet/menu.

Avoid horizontal page scroll. One-handed phone use is vertical thumb scrolling. Horizontal scroll breaks the user's spatial model and hides content off-screen with no visible affordance. Reflow, stack, paginate, or locally scroll tables and charts instead of the whole page.

Use viewport-fit=cover, env(safe-area-inset-*), and min-height: 100dvh. Modern iPhones have rounded corners, the Dynamic Island, and the home indicator — all of which eat into the rectangular viewport. Without explicit safe-area handling, content gets clipped behind hardware chrome. dvh accounts for the collapsing Safari toolbar that old vh does not.

Keep primary actions clear of browser bars, the home indicator, rounded corners, and the on-screen keyboard. A "Submit" button hidden behind the keyboard or overlapping the home indicator is functionally broken — the user either can't see it or can't tap it without triggering a system gesture.

Prefer one main scroll container for form-heavy or keyboard-heavy flows. Nested scroll regions on iOS Safari create scroll-trapping: the user's thumb scrolls the inner container when they intended to scroll the page, or vice versa. WebKit has had persistent bugs here (see reference file). Use nested scroll only when there's no alternative.

Use semantic mobile inputs. Labels above fields (not beside — there's no horizontal space), correct type, inputmode, autocomplete, and enterkeyhint. These attributes control which keyboard appears — inputmode="decimal" shows the number pad for currency, enterkeyhint="next" lets users tab through a form without dismissing the keyboard.

Treat large text as real layout input. iOS users can set system-wide larger text, and many do. Wrap and reflow — do not hide key meaning behind truncation. If a truncated label makes the user guess whether they're looking at "Savings Account" or "Salary Account," the layout has failed.

On phones, charts support the story; they are not the whole story. A phone screen can render maybe 5-6 legible bars or one donut. That's not enough data density for the chart to be self-explanatory. Lead with the headline number and a text summary; use the chart as visual reinforcement.

Preserve the product's existing brand and design system unless the user asks for a broader redesign. Mobile adaptation is about layout and interaction, not reskinning.

Examples
Desktop sidebar nav → mobile bottom tab bar

Apple HIG (confirmed current as of WWDC 2024/2025) recommends 3–5 tabs on iPhone, bottom-positioned, with glyph icons and required labels. The bottom bar remains the standard on iPhone — the floating top-bar redesign in iPadOS 18 is iPad-only and not applicable to mobile web.

Before — a sidebar that works on desktop but steals half the phone screen:

<aside className="w-64 fixed left-0 top-0 h-full border-r">
  <nav className="flex flex-col gap-2 p-4">
    <Link href="/dashboard">Dashboard</Link>
    <Link href="/transactions">Transaksjoner</Link>
    <Link href="/accounts">Kontoer</Link>
    <Link href="/categories">Kategorier</Link>
    <Link href="/settings">Innstillinger</Link>
  </nav>
</aside>


After — bottom tab bar with safe-area padding and 44x44 tap targets (WCAG 2.5.5 AAA, Apple HIG minimum). The env(safe-area-inset-bottom) value is ~34px on Face ID iPhones for the home indicator, but returns 0 without viewport-fit=cover in the viewport meta tag. Each NavTab renders at least h-14 (56px) to clear the 44px minimum with comfortable padding:

<nav className="fixed bottom-0 left-0 right-0 z-50 border-t bg-white
                pb-[env(safe-area-inset-bottom)] md:hidden">
  <div className="flex items-center justify-around h-14">
    <NavTab href="/dashboard" icon={HomeIcon} label="Hjem" />
    <NavTab href="/transactions" icon={ListIcon} label="Transaksjoner" />
    <NavTab href="/accounts" icon={WalletIcon} label="Kontoer" />
    <NavTab href="/categories" icon={TagIcon} label="Kategorier" />
  </div>
</nav>
{/* Main content gets bottom padding to clear tab bar + safe area */}
<main className="pb-20 md:pb-0 md:ml-64">...</main>

Dense data table → card list on phones

When a 5-column table renders on a 390px screen, columns get squeezed below readable width or force horizontal document scroll. The card pattern preserves all data while using vertical space, which phones have in abundance.

Before — a multi-column table that forces horizontal scroll:

<table className="w-full">
  <thead><tr>
    <th>Dato</th><th>Beskrivelse</th><th>Kategori</th><th>Belop</th><th>Konto</th>
  </tr></thead>
  <tbody>{rows.map(r => (
    <tr><td>{r.date}</td><td>{r.desc}</td><td>{r.cat}</td><td>{r.amount}</td><td>{r.account}</td></tr>
  ))}</tbody>
</table>


After — stacked cards that use vertical space and remain scannable. The amount gets tabular-nums and whitespace-nowrap so financial figures stay aligned and never break mid-number. If the original table must remain for accessibility (e.g., screen reader users who benefit from row/column association), keep it in the DOM and toggle visibility at the breakpoint rather than removing it:

<ul className="divide-y md:hidden" role="list">
  {rows.map(r => (
    <li key={r.id} className="flex items-start justify-between gap-3 px-4 py-3
                               min-h-[44px]" role="listitem">
      <div className="min-w-0 flex-1">
        <p className="font-medium truncate">{r.desc}</p>
        <p className="text-sm text-muted">{r.date} · {r.cat}</p>
      </div>
      <span className="tabular-nums font-medium whitespace-nowrap">
        {formatNOK(r.amount)}
      </span>
    </li>
  ))}
</ul>

Form with keyboard-aware submit

On iOS Safari, when the keyboard opens the Layout Viewport stays the same size but the Visual Viewport shrinks. Elements with position: fixed; bottom: 0 stay anchored to the Layout Viewport and disappear behind the keyboard (WebKit bug #202120 confirms position: sticky; bottom: 0 also fails to pin when the keyboard is open). The safest pattern is to let the submit button scroll naturally within the form flow, or use position: sticky with a visualViewport resize listener as a fallback.

Use inputmode="decimal" instead of type="number" for currency — it shows the decimal keyboard without the spinner arrows, which are a mobile UX antipattern for money fields. Chain enterkeyhint="next" on intermediate fields so users can advance without dismissing the keyboard, and enterkeyhint="done" on the last field.

Before — submit button at the bottom of a long form, hidden when the keyboard opens:

<form className="space-y-4 p-4">
  <Input label="Belop" type="number" />
  <Input label="Beskrivelse" />
  <Select label="Kategori" options={categories} />
  <Button type="submit">Lagre</Button>
</form>


After — inline submit that scrolls with form content, staying naturally reachable. The outer container uses min-h-[100dvh] (dvh tracks the visual viewport including keyboard, unlike old vh):

<form className="flex flex-col min-h-[100dvh]">
  <div className="flex-1 space-y-4 p-4">
    <Input label="Belop" type="text" inputMode="decimal"
           enterKeyHint="next" autoComplete="off" />
    <Input label="Beskrivelse" enterKeyHint="next" autoComplete="off" />
    <Select label="Kategori" options={categories} />
  </div>
  <div className="sticky bottom-0 p-4 border-t bg-white
                  pb-[max(1rem,env(safe-area-inset-bottom))]">
    <Button type="submit" className="w-full h-12">Lagre</Button>
  </div>
</form>

Workflow
Lock target context.
device, browser, orientation, usage context
default to iPhone Pro Max + iOS Safari if unspecified
Audit the shell first.
navigation mode
safe areas
sticky/fixed bars
landscape behavior
keyboard behavior
Audit each screen or component.
lists and rows
forms
tables
charts
empty/error/loading states
Choose the hard cutover.
what becomes single-column
what becomes cards
what moves into a sheet/drawer
what becomes secondary under More
Implement mobile-first adaptations.
prefer container queries for component internals
prefer viewport queries for shell/layout mode changes
do not keep old half-desktop/half-mobile behavior unless explicitly required
Verify on compact portrait and compact landscape.
Safari/WebKit first
then Chromium
Report the highest-risk issues first, then the concrete changes and any remaining gaps.
Screen Checklist
Shell and navigation
Keep landscape phones in the phone shell.
Avoid hard md => desktop sidebar switches for devices that are still phones.
Pad bottom UI with env(safe-area-inset-bottom).
Make sticky actions sit above bottom nav.
Keep mobile labels short.
Lists and rows
Let titles, metadata, and amounts wrap into two rows when needed.
Reserve stable space for prices, balances, and totals.
Prefer stacked metadata over squeezed inline metadata.
Expose actions with visible controls or a sheet/menu, not hover.
Size row action buttons (edit, delete, view, expand) to at least 44x44 CSS px — not just primary nav and toolbar buttons.
Forms
Use one column on compact phones.
Keep submit visible above the keyboard.
Use a clear full-width primary CTA.
Break long flows into steps or progressive disclosure.
Avoid type="number" for currency if formatting or precision matters.
Tables and import/review flows
Convert dense editable tables to cards/lists on phones.
If a true table must remain, isolate horizontal scroll to the table only.
Keep sticky headers and toolbars from obscuring focused inputs.
Charts and stats
Lead with the key number and short narrative.
Add compact legends and text fallback.
Prefer horizontal scroll or paged comparisons over unreadable dense bars.
Avoid tiny pies/donuts on compact screens.
Verification

For each check below, confirm the specific pass condition and use the suggested tooling. Real device testing is the gold standard — simulators are useful for iteration but cannot fully reproduce keyboard timing, scroll inertia, or touch precision.

Portrait and landscape — Phone stays in the mobile shell in both orientations. No layout breakage, no content overflow, no sudden switch to a desktop sidebar or multi-pane view. Test at 390px (iPhone Pro) and 430px (iPhone Pro Max) portrait, and their landscape equivalents. Use Chrome DevTools device toolbar or Xcode Simulator.

iOS Safari safe areas — Content is not clipped by the Dynamic Island, rounded corners, or home indicator. Bottom-fixed elements have visible env(safe-area-inset-bottom) padding (~34px on Face ID iPhones). Verify that viewport-fit=cover is set in the viewport meta tag — without it, all env(safe-area-inset-*) values return 0. Best tested in Xcode Simulator (accurate per-device insets) or Polypane 26+ (desktop browser with real safe-area inset presets). Chrome DevTools 135+ supports Emulation.setSafeAreaInsetsOverride but requires manual configuration.

Keyboard-open form flow — Focus each input in sequence and verify: (1) the focused field scrolls into view, (2) the submit action is visible and tappable, (3) sticky headers don't obscure the focused field. Be aware that position: fixed; bottom: 0 elements hide behind the iOS keyboard (the Layout Viewport doesn't shrink), and position: sticky; bottom: 0 also fails to pin during keyboard display (WebKit bug #202120). Playwright and Cypress cannot trigger real on-screen keyboards — this requires real device testing or Xcode Simulator with Safari Web Inspector.

Large text / display zoom — WCAG 1.4.4 (AA) requires text resizable to 200% without loss of content. WCAG 1.4.10 (AA) requires reflow at 400% zoom (equivalent to 320px-wide viewport) without horizontal scroll. Test by: (1) setting browser zoom to 200% and verifying no truncation or overlap, (2) setting viewport to 1280px and zooming to 400% to simulate the 320px reflow requirement, (3) enabling iOS Settings > Accessibility > Display & Text Size > Larger Text at maximum. Verify the viewport meta tag does not set user-scalable=no or maximum-scale below 2.0.

Reduced motion — Animations respect prefers-reduced-motion: reduce. Transitions still communicate state changes but use crossfades or opacity rather than motion. iOS Safari does not automatically suppress web animations when Reduce Motion is on — the developer must handle it. Test via: Chrome DevTools Rendering tab > "Emulate prefers-reduced-motion", Safari Web Inspector preference overrides (available since late 2022), or Playwright's page.emulateMedia({ reducedMotion: 'reduce' }).

Empty/error/loading states — These states render properly on the compact screen. Loading skeletons match the mobile layout, not the desktop one. Error messages are readable without scrolling.

Standalone/PWA mode (when relevant) — If the app supports display: standalone, verify that the status bar area, home indicator, and gesture regions are handled. svh and dvh resolve to the same value in standalone mode since there's no collapsible toolbar (WebKit bug #261185). WebKit bug #254868 can cause incorrect height values. WebKit bug #265578 causes visual viewport height to update late when Safari UI animates back into view.

No horizontal document scroll — Swipe left/right on the page body produces no movement. Any horizontal scroll is isolated to a specific container (table, carousel) with visible overflow affordance and overscroll-behavior: contain to prevent triggering Safari UI shifts (WebKit bug #240861). For automated verification in Playwright:

const hasOverflow = await page.evaluate(() =>
  document.documentElement.scrollWidth > document.documentElement.clientWidth
);
expect(hasOverflow).toBe(false);

Deliverable

When using this skill, produce:

a short mobile adaptation plan
the highest-risk issues first
concrete per-screen changes
verification performed
any remaining device/browser uncertainty
Weekly Installs
12
Repository
s0up4200/skills
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass