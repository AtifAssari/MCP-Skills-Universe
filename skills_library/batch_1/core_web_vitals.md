---
title: core-web-vitals
url: https://skills.sh/addyosmani/web-quality-skills/core-web-vitals
---

# core-web-vitals

skills/addyosmani/web-quality-skills/core-web-vitals
core-web-vitals
Installation
$ npx skills add https://github.com/addyosmani/web-quality-skills --skill core-web-vitals
Summary

Diagnose and fix the three Core Web Vitals metrics that impact search ranking and user experience.

Covers LCP (Largest Contentful Paint), INP (Interaction to Next Paint), and CLS (Cumulative Layout Shift) with specific thresholds and optimization strategies for each
Includes common causes, code examples, and debugging scripts for identifying bottlenecks in loading, interactivity, and visual stability
Provides framework-specific quick fixes for Next.js, React, and Vue/Nuxt, plus measurement tools for both lab testing and real-user field data
Optimization checklists for each metric help prioritize fixes to meet Google's 75th percentile performance requirements
SKILL.md
Core Web Vitals optimization

Targeted optimization for the three Core Web Vitals metrics that affect Google Search ranking and user experience.

The three metrics
Metric	Measures	Good	Needs work	Poor
LCP	Loading	≤ 2.5s	2.5s – 4s	> 4s
INP	Interactivity	≤ 200ms	200ms – 500ms	> 500ms
CLS	Visual Stability	≤ 0.1	0.1 – 0.25	> 0.25

Google measures at the 75th percentile — 75% of page visits must meet "Good" thresholds.

LCP: Largest Contentful Paint

LCP measures when the largest visible content element renders. Usually this is:

Hero image or video
Large text block
Background image
<svg> element
Common LCP issues

1. Slow server response (TTFB > 800ms)

Fix: CDN, caching, optimized backend, edge rendering


2. Render-blocking resources

<!-- ❌ Blocks rendering -->
<link rel="stylesheet" href="/all-styles.css">

<!-- ✅ Critical CSS inlined, rest deferred -->
<style>/* Critical above-fold CSS */</style>
<link rel="preload" href="/styles.css" as="style" 
      onload="this.onload=null;this.rel='stylesheet'">


3. Slow resource load times

<!-- ❌ No hints, discovered late -->
<img src="/hero.jpg" alt="Hero">

<!-- ✅ Preloaded with high priority -->
<link rel="preload" href="/hero.webp" as="image" fetchpriority="high">
<img src="/hero.webp" alt="Hero" fetchpriority="high">


4. Client-side rendering delays

// ❌ Content loads after JavaScript
useEffect(() => {
  fetch('/api/hero-text').then(r => r.json()).then(setHeroText);
}, []);

// ✅ Server-side or static rendering
// Use SSR, SSG, or streaming to send HTML with content
export async function getServerSideProps() {
  const heroText = await fetchHeroText();
  return { props: { heroText } };
}

LCP optimization checklist
- [ ] TTFB < 800ms (use CDN, edge caching)
- [ ] LCP image preloaded with fetchpriority="high"
- [ ] LCP image optimized (WebP/AVIF, correct size)
- [ ] Critical CSS inlined (< 14KB)
- [ ] No render-blocking JavaScript in <head>
- [ ] Fonts don't block text rendering (font-display: swap)
- [ ] LCP element in initial HTML (not JS-rendered)

LCP element identification
// Find your LCP element
new PerformanceObserver((list) => {
  const entries = list.getEntries();
  const lastEntry = entries[entries.length - 1];
  console.log('LCP element:', lastEntry.element);
  console.log('LCP time:', lastEntry.startTime);
}).observe({ type: 'largest-contentful-paint', buffered: true });

INP: Interaction to Next Paint

INP measures responsiveness across ALL interactions (clicks, taps, key presses) during a page visit. It reports the worst interaction (at 98th percentile for high-traffic pages).

INP breakdown

Total INP = Input Delay + Processing Time + Presentation Delay

Phase	Target	Optimization
Input Delay	< 50ms	Reduce main thread blocking
Processing	< 100ms	Optimize event handlers
Presentation	< 50ms	Minimize rendering work
Common INP issues

1. Long tasks blocking main thread

// ❌ Long synchronous task
function processLargeArray(items) {
  items.forEach(item => expensiveOperation(item));
}

// ✅ Break into chunks with yielding
async function processLargeArray(items) {
  const CHUNK_SIZE = 100;
  for (let i = 0; i < items.length; i += CHUNK_SIZE) {
    const chunk = items.slice(i, i + CHUNK_SIZE);
    chunk.forEach(item => expensiveOperation(item));
    
    // Yield to main thread
    await new Promise(r => setTimeout(r, 0));
    // Or use scheduler.yield() when available
  }
}


2. Heavy event handlers

// ❌ All work in handler
button.addEventListener('click', () => {
  // Heavy computation
  const result = calculateComplexThing();
  // DOM updates
  updateUI(result);
  // Analytics
  trackEvent('click');
});

// ✅ Prioritize visual feedback
button.addEventListener('click', () => {
  // Immediate visual feedback
  button.classList.add('loading');
  
  // Defer non-critical work
  requestAnimationFrame(() => {
    const result = calculateComplexThing();
    updateUI(result);
  });
  
  // Use requestIdleCallback for analytics
  requestIdleCallback(() => trackEvent('click'));
});


3. Third-party scripts

// ❌ Eagerly loaded, blocks interactions
<script src="https://heavy-widget.com/widget.js"></script>

// ✅ Lazy loaded on interaction or visibility
const loadWidget = () => {
  import('https://heavy-widget.com/widget.js')
    .then(widget => widget.init());
};
button.addEventListener('click', loadWidget, { once: true });


4. Excessive re-renders (React/Vue)

// ❌ Re-renders entire tree
function App() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <Counter count={count} />
      <ExpensiveComponent /> {/* Re-renders on every count change */}
    </div>
  );
}

// ✅ Memoized expensive components
const MemoizedExpensive = React.memo(ExpensiveComponent);

function App() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <Counter count={count} />
      <MemoizedExpensive />
    </div>
  );
}

INP optimization checklist
- [ ] No tasks > 50ms on main thread
- [ ] Event handlers complete quickly (< 100ms)
- [ ] Visual feedback provided immediately
- [ ] Heavy work deferred with requestIdleCallback
- [ ] Third-party scripts don't block interactions
- [ ] Debounced input handlers where appropriate
- [ ] Web Workers for CPU-intensive operations

INP debugging
// Identify slow interactions
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (entry.duration > 200) {
      console.warn('Slow interaction:', {
        type: entry.name,
        duration: entry.duration,
        processingStart: entry.processingStart,
        processingEnd: entry.processingEnd,
        target: entry.target
      });
    }
  }
}).observe({ type: 'event', buffered: true, durationThreshold: 16 });

CLS: Cumulative Layout Shift

CLS measures unexpected layout shifts. A shift occurs when a visible element changes position between frames without user interaction.

CLS Formula: impact fraction × distance fraction

Common CLS causes

1. Images without dimensions

<!-- ❌ Causes layout shift when loaded -->
<img src="photo.jpg" alt="Photo">

<!-- ✅ Space reserved -->
<img src="photo.jpg" alt="Photo" width="800" height="600">

<!-- ✅ Or use aspect-ratio -->
<img src="photo.jpg" alt="Photo" style="aspect-ratio: 4/3; width: 100%;">


2. Ads, embeds, and iframes

<!-- ❌ Unknown size until loaded -->
<iframe src="https://ad-network.com/ad"></iframe>

<!-- ✅ Reserve space with min-height -->
<div style="min-height: 250px;">
  <iframe src="https://ad-network.com/ad" height="250"></iframe>
</div>

<!-- ✅ Or use aspect-ratio container -->
<div style="aspect-ratio: 16/9;">
  <iframe src="https://youtube.com/embed/..." 
          style="width: 100%; height: 100%;"></iframe>
</div>


3. Dynamically injected content

// ❌ Inserts content above viewport
notifications.prepend(newNotification);

// ✅ Insert below viewport or use transform
const insertBelow = viewport.bottom < newNotification.top;
if (insertBelow) {
  notifications.prepend(newNotification);
} else {
  // Animate in without shifting
  newNotification.style.transform = 'translateY(-100%)';
  notifications.prepend(newNotification);
  requestAnimationFrame(() => {
    newNotification.style.transform = '';
  });
}


4. Web fonts causing FOUT

/* ❌ Font swap shifts text */
@font-face {
  font-family: 'Custom';
  src: url('custom.woff2') format('woff2');
}

/* ✅ Optional font (no shift if slow) */
@font-face {
  font-family: 'Custom';
  src: url('custom.woff2') format('woff2');
  font-display: optional;
}

/* ✅ Or match fallback metrics */
@font-face {
  font-family: 'Custom';
  src: url('custom.woff2') format('woff2');
  font-display: swap;
  size-adjust: 105%; /* Match fallback size */
  ascent-override: 95%;
  descent-override: 20%;
}


5. Animations triggering layout

/* ❌ Animates layout properties */
.animate {
  transition: height 0.3s, width 0.3s;
}

/* ✅ Use transform instead */
.animate {
  transition: transform 0.3s;
}
.animate.expanded {
  transform: scale(1.2);
}

CLS optimization checklist
- [ ] All images have width/height or aspect-ratio
- [ ] All videos/embeds have reserved space
- [ ] Ads have min-height containers
- [ ] Fonts use font-display: optional or matched metrics
- [ ] Dynamic content inserted below viewport
- [ ] Animations use transform/opacity only
- [ ] No content injected above existing content

CLS debugging
// Track layout shifts
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (!entry.hadRecentInput) {
      console.log('Layout shift:', entry.value);
      entry.sources?.forEach(source => {
        console.log('  Shifted element:', source.node);
        console.log('  Previous rect:', source.previousRect);
        console.log('  Current rect:', source.currentRect);
      });
    }
  }
}).observe({ type: 'layout-shift', buffered: true });

Measurement tools
Lab testing
Chrome DevTools → Performance panel, Lighthouse
WebPageTest → Detailed waterfall, filmstrip
Lighthouse CLI → npx lighthouse <url>
Field data (real users)
Chrome User Experience Report (CrUX) → BigQuery or API
Search Console → Core Web Vitals report
web-vitals library → Send to your analytics
import {onLCP, onINP, onCLS} from 'web-vitals';

function sendToAnalytics({name, value, rating}) {
  gtag('event', name, {
    event_category: 'Web Vitals',
    value: Math.round(name === 'CLS' ? value * 1000 : value),
    event_label: rating
  });
}

onLCP(sendToAnalytics);
onINP(sendToAnalytics);
onCLS(sendToAnalytics);

Framework quick fixes
Next.js
// LCP: Use next/image with priority
import Image from 'next/image';
<Image src="/hero.jpg" priority fill alt="Hero" />

// INP: Use dynamic imports
const HeavyComponent = dynamic(() => import('./Heavy'), { ssr: false });

// CLS: Image component handles dimensions automatically

React
// LCP: Preload in head
<link rel="preload" href="/hero.jpg" as="image" fetchpriority="high" />

// INP: Memoize and useTransition
const [isPending, startTransition] = useTransition();
startTransition(() => setExpensiveState(newValue));

// CLS: Always specify dimensions in img tags

Vue/Nuxt
<!-- LCP: Use nuxt/image with preload -->
<NuxtImg src="/hero.jpg" preload loading="eager" />

<!-- INP: Use async components -->
<component :is="() => import('./Heavy.vue')" />

<!-- CLS: Use aspect-ratio CSS -->
<img :style="{ aspectRatio: '16/9' }" />

References
web.dev LCP
web.dev INP
web.dev CLS
Performance skill
Weekly Installs
5.7K
Repository
addyosmani/web-…y-skills
GitHub Stars
1.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass