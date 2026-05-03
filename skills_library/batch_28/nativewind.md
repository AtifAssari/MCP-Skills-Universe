---
title: nativewind
url: https://skills.sh/hairyf/skills/nativewind
---

# nativewind

skills/hairyf/skills/nativewind
nativewind
Installation
$ npx skills add https://github.com/hairyf/skills --skill nativewind
SKILL.md

Skill is based on NativeWind v5 (Tailwind CSS v4), generated at 2026-02-26.

NativeWind compiles Tailwind CSS for React Native: className on components, StyleSheet.create on native and reuse of the Tailwind stylesheet on web. It supports media/container queries, pseudo-classes (hover, focus, active), platform variants (ios:, android:, native:, web:), dark mode, and custom theme/utilities via CSS-first config.

Core References
Topic	Description	Reference
Setup	CSS file, Metro withNativewind, PostCSS, app entry, optional lightningcss pin	core-setup
Configuration	CSS-first config, @theme, @source, nativewind/theme, custom utilities/variants	core-config
v5 Tailwind foundation	Built on Tailwind v4, CSS-first, web vs native support	core-v5-tailwind-foundation
v5 Units	px, %, vw/vh, rem, em on native; dp vs px; rem sizing	core-v5-units
v5 Functions & directives	@import, @theme, @utility; var(), calc(), env(), color-mix(); RN functions	core-v5-functions-directives
v5 Style specificity	Order of precedence, !important, merging className and style	core-v5-style-specificity
Features
Topic	Description	Reference
Styling components	className usage, custom vs third-party, styled() / cssInterop / remapProps, nativeStyleToProp	features-styling
Platform & responsive	Platform variants, units, breakpoints, safe-area utilities	features-platform
v5 Responsive	Breakpoints on native, media queries, platform media, reactive updates	features-v5-responsive
States & dark mode	hover/focus/active, disabled/empty, group modifiers, dark:, data attributes	features-states
v5 States & pseudo-classes	Detailed pseudo-class table, selection/placeholder, group, ltr/rtl	features-v5-states-pseudo
v5 Third-party guide	When className isn't passed, multiple style props, dynamic mapping @prop	features-v5-third-party-guide
Theming & colors	@theme tokens, vars() for runtime CSS variables, color behavior	advanced-theme
API (v5)
Topic	Description	Reference
withNativewind	Metro wrapper options (globalClassNamePolyfill, typescriptEnvPath)	api-with-nativewind
styled	Third-party components, nativeStyleToProp, multiple className props	api-styled
vars & runtime variables	vars(), VariableContextProvider, useUnstableNativeVariable	api-vars-runtime
cssInterop / remapProps	Legacy API (deprecated; use styled) — migration reference	api-css-interop-remap
Advanced
Topic	Description	Reference
Migrate v4 → v5	Steps, breaking changes, deprecations	advanced-migrate-v4
Best Practices
Topic	Description	Reference
Correctness & debugging	Explicit light/dark, colors on Text not View, cache, DEBUG, verifyInstallation	best-practices-performance
v5 Deprecations	useColorScheme → RN, cssInterop/remapProps → styled, @prop modifier	best-practices-v5-deprecations
Weekly Installs
93
Repository
hairyf/skills
GitHub Stars
15
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass