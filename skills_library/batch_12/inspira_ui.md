---
title: inspira-ui
url: https://skills.sh/secondsky/claude-skills/inspira-ui
---

# inspira-ui

skills/secondsky/claude-skills/inspira-ui
inspira-ui
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill inspira-ui
SKILL.md
Inspira UI - Animated Vue/Nuxt Component Library

Inspira UI is a collection of 120+ reusable, animated components powered by TailwindCSS v4, motion-v, GSAP, and Three.js — crafted to help ship beautiful Vue and Nuxt applications faster.

Table of Contents
When to Use
Quick Start
Component Selection
Core Patterns
Critical Pitfalls
Detailed References
When to Use This Skill

Use Inspira UI when building:

Animated landing pages with hero sections, testimonials, and effects
Modern web applications requiring 3D visualizations and interactive elements
Marketing sites with eye-catching backgrounds and text animations
Portfolio sites with image galleries, carousels, and showcase effects
Interactive experiences with custom cursors, special effects, and particle systems
Vue 3 or Nuxt 4 projects requiring production-ready animated components

Key Benefits:

120+ copy-paste components (not a traditional npm library)
Full TypeScript support with Vue 3 Composition API
TailwindCSS v4 with OkLch color space
Responsive and mobile-optimized
Free and open source (MIT license)
Quick Start
1. Install Core Dependencies
# Required for all components
bun add -d clsx tailwind-merge class-variance-authority tw-animate-css
bun add @vueuse/core motion-v

# Optional: For 3D components (Globe, Cosmic Portal, etc.)
bun add three @types/three

# Optional: For WebGL components (Fluid Cursor, Neural Background, etc.)
bun add ogl

2. Setup CN Utility

Create lib/utils.ts:

import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

3. Configure CSS Variables

Add to your main.css. See references/SETUP.md for complete CSS configuration with OkLch colors.

4. Verify Setup
./scripts/verify-setup.sh

5. Copy Components

Browse inspira-ui.com/components, copy what you need into components/ui/.

Component Selection Workflow

What type of effect do you need?

Background Effects → Aurora, Cosmic Portal, Particles, Neural Background

See: references/components-list.md#backgrounds

Text Animations → Morphing Text, Glitch, Hyper Text, Sparkles Text

See: references/components-list.md#text-animations

3D Visualizations → Globe, 3D Carousel, Icon Cloud, World Map

Dependencies: bun add three @types/three
See: references/components-list.md#visualization

Interactive Cursors → Fluid Cursor, Tailed Cursor, Smooth Cursor

Dependencies: bun add ogl (for WebGL cursors)
See: references/components-list.md#cursors

Animated Buttons → Shimmer, Ripple, Rainbow, Gradient

No extra dependencies
See: references/components-list.md#buttons

Special Effects → Confetti, Meteors, Neon Border, Glow Border

See: references/components-list.md#special-effects

For complete implementation details (props, full code, installation): Fetch https://inspira-ui.com/docs/llms-full.txt - LLM-optimized documentation with structured props tables and working code examples.

Core Usage Patterns
Pattern 1: Animated Landing Page
<template>
  <AuroraBackground>
    <Motion
      :initial="{ opacity: 0, y: 40, filter: 'blur(10px)' }"
      :while-in-view="{ opacity: 1, y: 0, filter: 'blur(0px)' }"
      :transition="{ delay: 0.3, duration: 0.8, ease: 'easeInOut' }"
      class="relative flex flex-col items-center gap-4 px-4"
    >
      <div class="text-center text-3xl font-bold md:text-7xl">
        Your amazing headline
      </div>
      <ShimmerButton>Get Started</ShimmerButton>
    </Motion>
  </AuroraBackground>
</template>

<script setup lang="ts">
import { Motion } from "motion-v";
import AuroraBackground from "~/components/ui/AuroraBackground.vue";
import ShimmerButton from "~/components/ui/ShimmerButton.vue";
</script>

Pattern 2: Props with TypeScript Interfaces
<script setup lang="ts">
// ALWAYS use interface-based props
interface Props {
  title: string;
  count?: number;
  variant?: "primary" | "secondary";
}

const props = withDefaults(defineProps<Props>(), {
  count: 0,
  variant: "primary",
});
</script>

Pattern 3: Explicit Imports (Critical for Vue.js Compatibility)
<script setup lang="ts">
// ALWAYS include explicit imports even with Nuxt auto-imports
import { ref, onMounted, computed } from "vue";
import { useWindowSize } from "@vueuse/core";

const { width } = useWindowSize();
</script>

Pattern 4: WebGL Component Cleanup
<script setup lang="ts">
import { onUnmounted } from "vue";

let animationFrame: number;
let renderer: any;

onUnmounted(() => {
  // CRITICAL: Clean up WebGL resources to prevent memory leaks
  if (animationFrame) cancelAnimationFrame(animationFrame);
  if (renderer) renderer.dispose();
});
</script>

Pattern 5: Client-Only Wrapper (Nuxt)
<template>
  <ClientOnly>
    <FluidCursor />
  </ClientOnly>
</template>

Critical Pitfalls to Avoid
1. Accessibility Bug (CRITICAL)

The original Inspira UI docs have --destructive-foreground set to the same color as --destructive, making text invisible. Use the corrected value:

:root {
  --destructive: oklch(0.577 0.245 27.325);
  --destructive-foreground: oklch(0.985 0 0); /* CORRECTED */
}

2. Missing CSS Imports
/* REQUIRED in main.css */
@import "tailwindcss";
@import "tw-animate-css";  /* Often forgotten! */

3. Wrong Props Syntax
// DON'T: Object syntax
const props = defineProps({ title: { type: String } });

// DO: Interface syntax
interface Props { title: string; }
const props = defineProps<Props>();

4. Three.js Without ClientOnly (Nuxt)
<!-- WRONG: Will fail during SSR -->
<GithubGlobe :markers="markers" />

<!-- CORRECT -->
<ClientOnly>
  <GithubGlobe :markers="markers" />
</ClientOnly>

5. Using Enums Instead of as const
// DON'T: TypeScript enums
enum ButtonVariant { Primary = "primary" }

// DO: as const objects
const ButtonVariants = { Primary: "primary" } as const;

Token Efficiency

Average Token Savings: ~65%

Without skill: ~15k tokens (trial-and-error with setup)
With skill: ~5k tokens (direct implementation)

Errors Prevented: 13+ common issues including:

Critical accessibility bug (destructive-foreground)
TailwindCSS v4 CSS variables misconfiguration
Missing @import "tw-animate-css"
Motion-V setup issues
Three.js/OGL without ClientOnly
Props typed with object syntax instead of interfaces
Missing explicit imports
Detailed Documentation

For complete setup with all CSS variables: references/SETUP.md

For all 120+ components with dependencies: references/components-list.md

For troubleshooting common issues: references/TROUBLESHOOTING.md

For TypeScript patterns and conventions: references/CODE_PATTERNS.md

Keywords

Frameworks: Vue, Vue 3, Nuxt, Nuxt 4, Composition API, script setup

Styling: TailwindCSS v4, OkLch, CSS variables, dark mode

Animation: motion-v, GSAP, Three.js, WebGL, OGL, canvas

Components: aurora background, shimmer button, morphing text, 3D globe, fluid cursor, confetti, neon border, icon cloud, flip card, particles

Use Cases: landing pages, hero sections, animated backgrounds, interactive UI, marketing sites, portfolios, 3D websites

Problems Solved: Vue animations, Nuxt animations, animated components, 3D effects, particle effects, modern UI effects

Resources
Official Documentation: https://inspira-ui.com/docs
LLM-Optimized Docs: https://inspira-ui.com/docs/llms-full.txt (complete props, code examples, installation)
Component Gallery: https://inspira-ui.com/components
GitHub Repository: https://github.com/unovue/inspira-ui
Discord Community: https://discord.gg/Xbh5DwJRc9

Production Status: ✅ Production-Ready Token Efficiency: ✅ ~65% savings Error Prevention: ✅ 13+ common issues prevented Last Updated: 2025-11-12

Weekly Installs
263
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn