---
title: styling-nativewind-v4-expo
url: https://skills.sh/tristanmanchester/agent-skills/styling-nativewind-v4-expo
---

# styling-nativewind-v4-expo

skills/tristanmanchester/agent-skills/styling-nativewind-v4-expo
styling-nativewind-v4-expo
Installation
$ npx skills add https://github.com/tristanmanchester/agent-skills --skill styling-nativewind-v4-expo
SKILL.md
NativeWind v4 for Expo (React Native)
Non‑negotiables (v4)
Use Tailwind CSS v3 and include presets: [require("nativewind/preset")] in tailwind.config.js.
Keep exactly one Tailwind entry CSS file (commonly global.css) and keep its path consistent across:
metro.config.js → withNativeWind(..., { input: "./global.css" })
your app entry → import "./global.css" (or import "../global.css" from app/_layout.tsx)
Keep nativewind/babel in Babel presets and set jsxImportSource: "nativewind" on babel-preset-expo.
After any config change, restart Metro without cache: npx expo start --clear.
Quick start checklist

Copy/paste and tick off:

 Install deps (NativeWind + Tailwind + peers). See references/expo-setup.md.
 Create/verify tailwind.config.js (content globs + nativewind/preset).
 Create/verify global.css with Tailwind directives.
 Create/verify babel.config.js (jsxImportSource + nativewind/babel).
 Create/verify metro.config.js (wrap config with withNativeWind, set input).
 If targeting web, set app.json → expo.web.bundler = "metro".
 If TypeScript, add nativewind-env.d.ts with /// <reference types="nativewind/types" />.
 Start with cache cleared and validate on-device + web: npx expo start --clear.
 Validate with an obvious “smoke test” screen: background colour + centred text.
Project type selection
Expo Router: entry is usually app/_layout.tsx → import CSS there (relative path is typically ../global.css).
Classic: entry is usually App.tsx → import CSS there (./global.css).

If unsure, search package.json for "main": "expo-router/entry".

Implementation patterns
Build reusable components (recommended)

Accept className, merge defaults, and optionally use a class-variance helper.

Read: references/patterns.md

Style third‑party components (only when necessary)

Use remapProps (multiple style props) or cssInterop (map a class prop to a style prop).

Read: references/third-party-components.md

Dark mode + theming

Use useColorScheme / colorScheme.set() and CSS variables via vars().

Read: references/theming-dark-mode.md

Safe area utilities

On Expo Router, do not add your own SafeAreaProvider (Router already does). Use p-safe, pt-safe, etc.

If you are not using Expo Router, wrap the root with SafeAreaProvider.

Troubleshooting workflow (always in this order)
Start Expo without cache: npx expo start --clear.
Verify Tailwind CLI works by compiling your CSS entry file to an output file.
Confirm the “three paths” match:
CSS file exists
metro.config.js input points to it
your app imports it from the entry component
Confirm tailwind.config.js content globs include every directory that contains className strings.
Only then debug platform-specific behaviour (web bundler, Router, safe area, etc).

Read: references/troubleshooting.md

THE EXACT PROMPT — NativeWind v4 config audit

Use this prompt to perform a deterministic audit of an existing repo:

You are auditing an Expo React Native repo for NativeWind v4 correctness.

1) Identify whether the project uses Expo Router (app/ directory + package.json main = expo-router/entry) or classic App.tsx.
2) Check and report on:
   - tailwind.config.js: presets + content globs
   - global.css: Tailwind directives exist
   - babel.config.js: jsxImportSource nativewind + nativewind/babel in presets; preserve any existing required plugins
   - metro.config.js: withNativeWind wrapper; input path matches the CSS file
   - app.json: web bundler metro when web is used
   - TypeScript: nativewind-env.d.ts present and correctly named
3) For every issue, propose the minimal diff needed to fix it.
4) End by listing the exact commands to restart Metro and validate the fix.

Weekly Installs
195
Repository
tristanmanchest…t-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass