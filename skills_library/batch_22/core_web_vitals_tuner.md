---
title: core-web-vitals-tuner
url: https://skills.sh/patricio0312rev/skills/core-web-vitals-tuner
---

# core-web-vitals-tuner

skills/patricio0312rev/skills/core-web-vitals-tuner
core-web-vitals-tuner
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill core-web-vitals-tuner
SKILL.md
Core Web Vitals Tuner

Improve LCP, INP, and CLS systematically.

LCP Optimization (<2.5s)

Prioritized Fixes:

Optimize images (Biggest impact)

<!-- Before -->
<img src="hero.jpg" />

<!-- After -->
<img
  src="hero.jpg"
  srcset="hero-400.webp 400w, hero-800.webp 800w, hero-1200.webp 1200w"
  sizes="(max-width: 600px) 400px, (max-width: 1200px) 800px, 1200px"
  loading="eager"
  fetchpriority="high"
/>


Preload LCP resource

<link rel="preload" as="image" href="/hero.webp" fetchpriority="high" />


Inline critical CSS

<style>
  /* Above-the-fold styles */
  .hero {
    display: flex;
    height: 100vh;
  }
</style>


Use CDN

Serve images from CloudFront/Cloudflare
Enable HTTP/2 or HTTP/3
INP Optimization (<200ms)

Fixes:

Debounce expensive interactions

import { debounce } from "lodash";

const handleSearch = debounce((query) => {
  fetchResults(query);
}, 300);


Use Web Workers for heavy tasks

const worker = new Worker("processor.js");
worker.postMessage(largeData);
worker.onmessage = (e) => console.log(e.data);


Code splitting

const HeavyComponent = lazy(() => import("./HeavyComponent"));

CLS Optimization (<0.1)

Fixes:

Reserve space for images/ads

<img src="banner.jpg" width="1200" height="600" />


Use CSS aspect-ratio

.video-container {
  aspect-ratio: 16 / 9;
}


Avoid injecting content above existing

.notification {
  position: fixed;
  top: 0;
}

Verification
# Lighthouse CI
npm run lighthouse -- --url=https://example.com

# Web Vitals in production
import { getCLS, getFID, getLCP } from 'web-vitals';

getCLS(console.log);
getFID(console.log);
getLCP(console.log);

Output Checklist
 LCP optimized (<2.5s)
 INP optimized (<200ms)
 CLS optimized (<0.1)
 Monitoring in place
 Performance regression tests ENDFILE
Weekly Installs
110
Repository
patricio0312rev/skills
GitHub Stars
35
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass