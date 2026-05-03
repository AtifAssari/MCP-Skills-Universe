---
title: audit-speed
url: https://skills.sh/calm-north/seojuice-skills/audit-speed
---

# audit-speed

skills/calm-north/seojuice-skills/audit-speed
audit-speed
Installation
$ npx skills add https://github.com/calm-north/seojuice-skills --skill audit-speed
Summary

Comprehensive Core Web Vitals audit with root-cause diagnosis and resource optimization guidance.

Covers five key metrics (LCP, CLS, INP, FCP, TTFB) with diagnostic trees that pinpoint specific causes like slow servers, missing image dimensions, font loading issues, and main-thread blocking
Includes structured resource analysis breaking down HTML, CSS, JavaScript, images, fonts, and third-party script sizes against industry benchmarks
Provides prioritized fix recommendations ordered by impact, plus quick-win optimizations that require minimal effort
Designed for page speed investigations, Lighthouse score improvement, and performance bottleneck identification across different tech stacks
SKILL.md
Audit Speed

Deep Core Web Vitals audit with root-cause analysis trees and resource optimization recommendations.

Core Web Vitals Thresholds
Metric	Good	Needs Improvement	Poor
LCP (Largest Contentful Paint)	< 2.5s	2.5s - 4.0s	> 4.0s
CLS (Cumulative Layout Shift)	< 0.1	0.1 - 0.25	> 0.25
INP (Interaction to Next Paint)	< 200ms	200ms - 500ms	> 500ms
FCP (First Contentful Paint)	< 1.8s	1.8s - 3.0s	> 3.0s
TTFB (Time to First Byte)	< 800ms	800ms - 1800ms	> 1800ms
Before You Start

Gather this context:

Which pages? Homepage, key landing pages, or specific slow pages.
Current scores. If the user has Lighthouse or PageSpeed Insights data, start there.
Tech stack. CMS, framework, hosting — this determines which optimizations are available.
Known constraints. Third-party scripts they can't remove, design requirements that limit optimization.

If no data is available, suggest running Google PageSpeed Insights on the key URLs.

LCP Root-Cause Tree

LCP measures when the largest visible element finishes rendering. Diagnose:

Is TTFB slow (> 800ms)?

→ Server response time issue
Check: hosting quality, CDN configuration, database queries, server-side rendering time
Fix: upgrade hosting, add CDN, optimize server-side code, enable caching

Is the LCP element an image?

→ Image optimization issue
Check: image format (use WebP/AVIF), image size (serve responsive sizes), lazy loading on LCP image (should NOT be lazy loaded)
Fix: convert to modern formats, add width/height attributes, use fetchpriority="high" on LCP image, preload the LCP image

Is the LCP element text?

→ Font loading issue
Check: custom fonts blocking render, font file size, font-display strategy
Fix: use font-display: swap or optional, preload critical fonts, subset fonts to used characters

Is render-blocking CSS/JS delaying the LCP?

Check: large CSS files in <head>, synchronous JS before content
Fix: inline critical CSS, defer non-critical CSS, async/defer JS
CLS Root-Cause Tree

CLS measures unexpected layout shifts. Diagnose:

Do images/videos lack dimensions?

→ Browser can't reserve space before loading
Fix: add width and height attributes to all <img> and <video> elements, use CSS aspect-ratio

Do ads or embeds inject content?

→ Dynamic content pushing existing content down
Fix: reserve space for ad slots with min-height, use contain-intrinsic-size for lazy content

Do fonts cause text reflow?

→ FOUT (Flash of Unstyled Text) causes layout shift when custom font loads
Fix: use font-display: optional (no swap = no shift), or match fallback font metrics

Does dynamic content insert above the fold?

→ Banners, cookie notices, notifications pushing content
Fix: use overlays instead of inline insertions, or reserve space with fixed-height containers
INP Root-Cause Tree

INP measures responsiveness to user interactions. Diagnose:

Is the main thread blocked by long tasks?

Check: JavaScript execution time, third-party scripts, large DOM
Fix: break long tasks with requestIdleCallback or setTimeout, code-split heavy modules

Do event handlers do heavy synchronous work?

Check: click handlers that trigger large DOM updates, form validation on every keystroke
Fix: debounce inputs, use requestAnimationFrame for visual updates, offload work to web workers

Are third-party scripts competing for the main thread?

Check: analytics, chat widgets, A/B testing tools, social embeds
Fix: defer loading until after interaction, use loading="lazy" for embeds, consider removing low-value scripts
Resource Analysis

Break down the total page weight:

Resource Type	Size	Assessment	Action
HTML	[x] KB	[ok/large]	Compress, reduce inline styles/scripts
CSS	[x] KB	[ok/large]	Remove unused CSS, minify, critical CSS extraction
JavaScript	[x] KB	[ok/large]	Code-split, tree-shake, defer non-critical
Images	[x] KB	[ok/large]	Modern formats, responsive sizes, lazy load below fold
Fonts	[x] KB	[ok/large]	Subset, limit families/weights, preload critical
Third-party	[x] KB	[ok/large]	Audit necessity, defer, self-host if possible

Benchmarks:

Total page weight under 1.5 MB is good
JavaScript under 300 KB (compressed) for most sites
CSS under 100 KB (compressed)
First-party fonts under 100 KB
Output Format
Speed Audit: [URL or domain]

Core Web Vitals

Metric	Value	Rating	Root Cause
LCP	[value]	Good / Needs Improvement / Poor	[identified cause]
CLS	[value]	...	...
INP	[value]	...	...
FCP	[value]	...	...
TTFB	[value]	...	...

Resource Breakdown [Table from Resource Analysis]

Priority Fixes

For each failing metric, ordered by impact:

[Metric]: [Root cause]

Current: [value]
Target: [threshold]
Fix: [specific action]
Estimated impact: [high/medium/low]

...

Quick Wins List optimizations that require minimal effort:

 Add width/height to images
 Set fetchpriority="high" on LCP image
 Defer non-critical JavaScript
 ...

Pro Tip: Use the free CWV Impact Calculator to estimate the traffic impact of fixing Core Web Vitals, and the Critical CSS Generator to extract above-the-fold CSS. SEOJuice MCP users can run /seojuice:page-audit [domain] [url] for instant CWV scores, Lighthouse data, and resource breakdowns.

Weekly Installs
1.7K
Repository
calm-north/seoj…e-skills
GitHub Stars
7
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass