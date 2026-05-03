---
title: typo3-icon14
url: https://skills.sh/dirnbauer/webconsulting-skills/typo3-icon14
---

# typo3-icon14

skills/dirnbauer/webconsulting-skills/typo3-icon14
typo3-icon14
Installation
$ npx skills add https://github.com/dirnbauer/webconsulting-skills --skill typo3-icon14
SKILL.md
TYPO3 v14 Icon Modernizer

Prefer live TYPO3 v14 references over bundled snapshots. Use the official Icon API docs for registration rules and the TYPO3.Icons catalog for the current Core SVG language. Use the local reference files only to keep this skill concise.

What this skill is for

Use this skill to:

migrate legacy extension icons to TYPO3 v14
design new custom icons that fit the TYPO3 v14 backend
update Configuration/Icons.php and all icon consumers
keep module, plugin, record, action, and extension icons distinct

Do not invent a second icon system for the extension. Work with the icon identifiers, file names, and render contexts that already exist in the codebase.

Workflow
Inventory existing icon files and registrations.
Classify each icon by type and render context.
Infer the icon meaning from module names, TCA, plugin config, and current SVGs.
If the meaning is still unclear, ask one focused question: what should this icon communicate?
Load live TYPO3 v14 references for the matching icon family. See references/live-sources.md.
Redraw or modernize the SVG in the correct TYPO3 v14 style.
Update Configuration/Icons.php and every iconIdentifier / pluginIcon / typeicon_classes consumer.
Verify the icon in its real backend context and clear TYPO3 cache plus browser local storage if the old SVG still appears.
Start With Meaning, Not Shapes

When the user asks for new icons, first capture or infer:

which identifiers or files need to exist
what each icon represents
whether several icons should form a visual family
whether one icon is the parent and others are sub-variants

If the repository already makes the meaning obvious, proceed without stopping. If not, ask for a short mapping such as:

module-myext -> "main module for editorial planning"
record-myext-campaign -> "campaign record"
plugin-myext-list -> "frontend list plugin"

The user can describe usage, not geometry. Translate usage into icon semantics.

Source Of Truth

Use sources in this order:

Official TYPO3 Icon API docs for registration, providers, and migration: Icon API
Live TYPO3.Icons catalog for current Core SVG references: TYPO3.Icons
If the working TYPO3 instance has EXT:styleguide, inspect the real backend rendering there as a runtime check
Only fall back to local reference notes in this skill when live sources are unavailable

Prefer loading the current Core icons when needed. Do not ship copies of Core icons into an extension unless the user explicitly wants vendored assets or the environment is offline.

Respect The Icon Type
Type	Typical file	Render context	ViewBox	Where to look for references
Parent / submodule	module-*.svg	Backend navigation, module menu	0 0 64 64	module catalog
Extension icon	Extension.svg	Extension Manager and related backend views	0 0 64 64	module catalog
Plugin icon	plugin-*.svg	New content element wizard, list view, plugin selectors	usually 0 0 16 16	content, default, apps
Record icon	record-*.svg	TCA, page tree, list module	usually 0 0 16 16	default, apps, mimetypes, overlay, status
Action icon	actions-*.svg	Buttons, toolbars, controls	usually 0 0 16 16	actions

Always match the render size and visual density of the icon type you are editing. Do not force a 64x64 module composition into a 16x16 record or action icon.

Minimal TYPO3 v14 SVG Rules
transparent background only
primary geometry uses currentColor
accent geometry uses var(--icon-color-accent, #ff8700)
remove hardcoded white, black, gray, and legacy brand-color backgrounds
keep markup minimal: xmlns plus viewBox only unless a provider truly needs more
preserve the semantic shape from the existing icon whenever possible
for module-* and Extension.svg: prefer strong silhouettes, minimum 6-unit outline width, and .8 opacity for depth fills when needed
for 16x16 icons: reduce details aggressively; two clear ideas beat five tiny ones

See references/design-notes.md for the visual rules and anti-patterns.

Light And Dark Mode Are Non-Negotiable

TYPO3 v14 ships auto / light / dark color scheme switching in the backend (introduced as a Core feature in v13.3, carried into v14). Every custom icon must render correctly in both schemes. There is no separate "dark icon" file — the same SVG is used.

The two CSS tokens that the Core ships on :root (from TYPO3.Icons/assets/scss/icons.scss) are:

:root {
    --icon-color-primary: currentColor;
    --icon-color-accent: #ff8700;
}


How to stay compatible with both schemes:

Use currentColor (or var(--icon-color-primary, currentColor)) for the primary silhouette. It inherits the surrounding text color, which flips automatically when the user switches color scheme.
Use var(--icon-color-accent, #ff8700) for the accent. TYPO3 orange #ff8700 is the same fallback in both schemes because orange has sufficient contrast on both light and dark backend surfaces. Do not replace it with a scheme-specific hex — themes that want a different accent override the CSS variable, not the fallback.
Never hardcode fill="#000", fill="#333", fill="#fff", fill="white", or fill="black". Any one of these vanishes on one of the two backgrounds.
Never draw a solid background rectangle behind the icon. The backend surface color must show through so the scheme flip works.
Opacity-based depth (fill-opacity=".8" on top of currentColor) is safe because the base tone flips with the scheme.
Do not depend on prefers-color-scheme media queries inside the SVG. The Core drives the scheme via an attribute on the root element, and relying on prefers-color-scheme will miss manual switches from the User Settings dropdown.

Verify every icon in both schemes before shipping (see Verification below).

Registration Rules

Register icons in Configuration/Icons.php. TYPO3 v14 requires this and no longer allows registration in ext_localconf.php.

<?php

declare(strict_types=1);

use TYPO3\CMS\Core\Imaging\IconProvider\SvgIconProvider;

return [
    'module-myext' => [
        'provider' => SvgIconProvider::class,
        'source' => 'EXT:my_extension/Resources/Public/Icons/module-myext.svg',
    ],
    'record-myext-item' => [
        'provider' => SvgIconProvider::class,
        'source' => 'EXT:my_extension/Resources/Public/Icons/record-myext-item.svg',
    ],
];


Update every consumer after the SVG is in place:

Configuration/Backend/Modules.php -> iconIdentifier
Configuration/TCA/*.php -> typeicon_classes, iconIdentifier
Configuration/TCA/Overrides/*.php -> pluginIcon, page-type or folder icons

The official docs state that icons must be registered in the icon registry through Configuration/Icons.php, and that registration in ext_localconf.php is no longer possible in TYPO3 v14.

Migration Behavior

When legacy SVGs already exist:

keep the existing identifier unless a rename is required
modernize the current shape before replacing it with a completely new metaphor
keep file paths stable where possible to reduce config churn
verify every updated icon against the icon type it belongs to

Use references/migration-steps.md for the checklist.

Verification

Before finishing:

verify the file path matches the registered source
verify the icon type uses the correct viewBox
verify there is no solid background layer
verify all consumers point to the intended identifier
verify the icon remains readable at its real render size
verify the icon works in both light and dark backend schemes — switch via the user dropdown at the top right or User Settings, and check the icon in its real render context (module menu, content wizard, list module, TCA icons)
confirm no hardcoded #000, #333, #fff, white, or black fills remain
clear TYPO3 caches and browser local storage if rendering looks stale
References
references/live-sources.md: live TYPO3 v14 sources, catalog URLs, and fetch patterns
references/design-notes.md: visual rules, icon-family guidance, and common mistakes
references/migration-steps.md: migration checklist

Source: https://github.com/dirnbauer/webconsulting-skills

Weekly Installs
9
Repository
dirnbauer/webco…g-skills
GitHub Stars
27
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn