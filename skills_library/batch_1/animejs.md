---
title: animejs
url: https://skills.sh/heygen-com/hyperframes/animejs
---

# animejs

skills/heygen-com/hyperframes/animejs
animejs
Installation
$ npx skills add https://github.com/heygen-com/hyperframes --skill animejs
SKILL.md
Anime.js for HyperFrames

HyperFrames can seek Anime.js instances through its animejs runtime adapter. The composition owns the animation objects; HyperFrames owns the clock.

Contract
Create animations or timelines synchronously during composition initialization.
Set autoplay: false so Anime.js does not advance on its own clock.
Register every returned animation or timeline on window.__hfAnime.
Use finite durations and loop counts.
Avoid callbacks that mutate DOM based on wall-clock time, network state, or unseeded randomness.

The adapter seeks every registered instance with instance.seek(timeMs), where timeMs is HyperFrames time in milliseconds.

Basic Pattern
<script src="https://cdn.jsdelivr.net/npm/animejs@4.0.2/lib/anime.iife.min.js"></script>
<script>
  const anim = anime({
    targets: ".mark",
    translateX: 280,
    rotate: "1turn",
    opacity: [0, 1],
    duration: 1200,
    easing: "easeOutExpo",
    autoplay: false,
  });

  window.__hfAnime = window.__hfAnime || [];
  window.__hfAnime.push(anim);
</script>

Timeline Pattern
<script>
  const tl = anime.timeline({
    autoplay: false,
    easing: "easeOutCubic",
  });

  tl.add({
    targets: ".title",
    translateY: [40, 0],
    opacity: [0, 1],
    duration: 650,
  }).add(
    {
      targets: ".accent",
      scaleX: [0, 1],
      duration: 450,
    },
    250,
  );

  window.__hfAnime = window.__hfAnime || [];
  window.__hfAnime.push(tl);
</script>

Module Builds

If you use an ES module build, the adapter does not care how the instance was created. It only needs the returned object to expose seek(), pause(), and preferably play():

<script type="module">
  import { animate } from "https://cdn.jsdelivr.net/npm/animejs/+esm";

  const anim = animate(".chip", {
    x: "18rem",
    duration: 900,
    autoplay: false,
  });

  window.__hfAnime = window.__hfAnime || [];
  window.__hfAnime.push(anim);
</script>

Good Uses
Small SVG and DOM flourishes where Anime.js syntax is compact.
Imported Anime.js examples that can be made seek-driven.
Multiple independent micro-animations pushed into the same registry.

Use GSAP for complex scene sequencing unless the user specifically asks for Anime.js. GSAP is still the primary HyperFrames authoring path.

Avoid
Leaving autoplay at the Anime.js default.
Depending on anime.running auto-discovery instead of explicit window.__hfAnime.push(...).
Infinite loops. Compute a finite repeat count from the composition duration.
Building animations in timers, promises, event handlers, or after async asset loads.
Validation

After editing a composition that uses Anime.js:

npx hyperframes lint
npx hyperframes validate

Credits And References
HyperFrames adapter source: packages/core/src/runtime/adapters/animejs.ts.
Anime.js documentation for autoplay, pause(), and seek(): https://animejs.com/documentation/
Weekly Installs
2.4K
Repository
heygen-com/hyperframes
GitHub Stars
13.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn