---
title: web-haptics
url: https://skills.sh/lochie/web-haptics/web-haptics
---

# web-haptics

skills/lochie/web-haptics/web-haptics
web-haptics
Installation
$ npx skills add https://github.com/lochie/web-haptics --skill web-haptics
Summary

Tactile feedback for web apps using the Web Vibration API across React, Vue, Svelte, and vanilla JavaScript.

Four trigger categories: notifications (success, warning, error), impacts (light, medium, heavy), selection (picker/slider detents), and extra presets (soft, rigid, nudge, buzz)
Framework-specific hooks and composables for React, Vue, Svelte; vanilla JS class; automatic SSR handling in Nuxt and SvelteKit
Zero dependencies, silent no-op on unsupported platforms (desktop), no feature detection required
Apple HIG design rules built in: haptics supplement visual feedback, match intensity to interaction significance, synchronize with state changes, and avoid overuse to prevent fatigue
SKILL.md

Install web-haptics (npm i web-haptics) and add haptic feedback to the app following these rules:

Package: web-haptics

Repository: https://github.com/lochie/web-haptics | License: MIT | Zero dependencies Uses the Web Vibration API. Silently no-ops on unsupported platforms (desktop). No error handling or feature detection needed.

Trigger Types

trigger() accepts one of these strings (empty value defaults to a sensible "medium" impact):

Notification (task outcomes):

"success" -- form saved, payment confirmed, upload complete
"warning" -- destructive action ahead, approaching limit, irreversible step
"error" -- validation failure, network error, permission denied

Impact (physical collisions):

"light" -- small toggle, subtle tap, minor interaction
"medium" -- button press, card snap-to-position, drop into place
"heavy" -- major state change, heavy element landed, force press

Selection (discrete stepping):

"selection" -- picker scroll, stepper increment, slider detent, segment switch
Framework Imports

React:

import { useWebHaptics } from "web-haptics/react";

const haptic = useWebHaptics();

<button onClick={() => haptic.trigger()}>Tap me</button>;


Vue:

<script setup>
import { useWebHaptics } from "web-haptics/vue";
const haptic = useWebHaptics();
</script>

<template>
  <button @click="haptic.trigger()">Tap me</button>
</template>


Svelte:

<script>
  import { createWebHaptics } from "web-haptics/svelte";
  import { onDestroy } from "svelte";
  const haptic = createWebHaptics();
  onDestroy(() => haptic.destroy());
</script>

<button on:click={() => haptic.trigger()}>Tap me</button>


Vanilla JS:

import { WebHaptics } from "web-haptics";

const haptics = new WebHaptics();
haptics.trigger(); // medium impact
haptics.trigger("success");


Next.js: add "use client" to any component using useWebHaptics(). Nuxt/SvelteKit: works directly, library handles SSR.

Trigger Presets & defaultPatterns

All named string presets have a corresponding object in defaultPatterns. Use when you need to pass a preset as a value rather than a string literal:

import { WebHaptics, defaultPatterns } from 'web-haptics'

const haptics = new WebHaptics()
haptics.trigger(defaultPatterns.light)


Extra presets not listed above: "soft", "rigid", "nudge", "buzz". See defaultPatterns for all available values.

Apple HIG Design Rules -- FOLLOW THESE
Haptics supplement, never replace. Always pair with visual feedback. UI must work fully without haptics.
Build causal relationships. The haptic must feel like a direct physical consequence of the user action.
Match intensity to significance. Light interactions = light/selection. Standard = medium/success. Major = heavy/error/warning.
Do not overuse. If every tap vibrates, nothing feels special. Reserve for meaningful moments only.
Synchronize perfectly. Fire haptic at the exact instant the visual change occurs.
Respect conventions. success=positive, error=negative, warning=cautionary, selection=discrete ticks only.
For async ops, trigger when the RESULT arrives, synced with the visual state change:
try {
  await submit();
  haptic.trigger("success");
} catch {
  haptic.trigger("error");
}

Interaction to Type Quick Reference

Primary button tap = "medium" | Secondary button = "light" Form success = "success" | Validation error = "error" | Network error = "error" Toggle switch = "light" | Delete before confirm = "warning" Picker/wheel = "selection" | Slider detents = "selection" | Tab switch = "selection" Drag-drop snap = "medium" | Long press = "heavy" | Modal appear = "medium" Pull-to-refresh threshold = "light" | Swipe dismiss threshold = "light" Payment confirmed = "success"

Anti-Patterns -- AVOID
Haptic on every tap (fatigue)
"error" for non-errors (breaks conventions)
Haptic without visual feedback (some devices cannot vibrate)
Haptic on page load or passive scroll (invasive)
"heavy" for minor interactions (jarring)
Long continuous vibrations (web haptics = brief transient pulses)
Before implementing, confirm with the user:
Which interactive elements to target
Whether to add at shared component level or individual call sites
Weekly Installs
542
Repository
lochie/web-haptics
GitHub Stars
2.5K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass