---
title: webperf-resources
url: https://skills.sh/nucliweb/webperf-snippets/webperf-resources
---

# webperf-resources

skills/nucliweb/webperf-snippets/webperf-resources
webperf-resources
Installation
$ npx skills add https://github.com/nucliweb/webperf-snippets --skill webperf-resources
SKILL.md
WebPerf: Resources & Network

JavaScript snippets for measuring web performance in Chrome DevTools. Execute with mcp__chrome-devtools__evaluate_script, capture output with mcp__chrome-devtools__get_console_message.

Scripts
scripts/Network-Bandwidth-Connection-Quality.js — Network Bandwidth & Connection Quality
Common Workflows
Network Quality Assessment

When the user asks about network performance, connection quality, or adaptive loading:

Network-Bandwidth-Connection-Quality.js - Analyze network bandwidth, effective connection type, RTT, downlink, save-data mode
Adaptive Loading Strategy

When implementing adaptive loading or the user asks "how to optimize for slow connections":

Network-Bandwidth-Connection-Quality.js - Detect connection quality
Cross-reference with webperf-loading skill:
TTFB.js (measure server response on slow connections)
Find-render-blocking-resources.js (identify heavy resources to defer)
Resource-Hints-Validation.js (optimize preconnect for slow networks)
Cross-reference with webperf-media skill:
Image-Element-Audit.js (implement responsive images based on connection)
Video-Element-Audit.js (adjust video quality based on connection)
Save-Data Mode Detection

When the user asks about save-data or data-saving features:

Network-Bandwidth-Connection-Quality.js - Check if save-data is enabled
If save-data is enabled, recommend:
Reducing image quality
Disabling autoplay videos
Deferring non-critical resources
Using low-res thumbnails
Mobile/Slow Connection Optimization

When the user asks "optimize for mobile" or "slow connection users":

Network-Bandwidth-Connection-Quality.js - Assess connection type
Cross-reference with webperf-loading skill:
TTFB.js (critical for slow connections)
Find-render-blocking-resources.js (minimize blocking on slow networks)
Critical-CSS-Detection.js (inline critical CSS to reduce RTT)
Prefetch-Resource-Validation.js (avoid excessive prefetch on slow connections)
Decision Tree

Use this decision tree to automatically run follow-up snippets based on results:

After Network-Bandwidth-Connection-Quality.js

If effectiveType is "slow-2g" or "2g" → Very slow connection, recommend:

Run webperf-loading:Critical-CSS-Detection.js (inline critical CSS)
Run webperf-media:Image-Element-Audit.js (implement aggressive lazy loading)
Run webperf-loading:Prefetch-Resource-Validation.js (remove prefetch to save bandwidth)
Run webperf-core-web-vitals:LCP.js (LCP is heavily impacted by slow connections)
Recommend minimal resource strategy

If effectiveType is "3g" → Moderate connection, recommend:

Run webperf-loading:Find-render-blocking-resources.js (minimize blocking)
Run webperf-media:Image-Element-Audit.js (responsive images)
Run webperf-loading:Resource-Hints-Validation.js (optimize preconnect)
Run webperf-core-web-vitals:INP.js (high latency can impact interaction responsiveness)
Implement adaptive image quality

If effectiveType is "4g" or better → Good connection, recommend:

Standard optimization practices
Consider strategic prefetch for navigation
Higher quality media is acceptable

If save-data is enabled → User explicitly wants to save data, recommend:

Reduce image quality aggressively
Disable autoplay videos
Defer non-critical resources
Remove prefetch/preload hints
Show "high quality" toggle option

If RTT > 300ms → High latency, recommend:

Run webperf-loading:TTFB.js (latency impacts TTFB)
Run webperf-loading:TTFB-Sub-Parts.js (break down latency components)
Run webperf-loading:Resource-Hints-Validation.js (preconnect critical for high RTT)
Run webperf-loading:Service-Worker-Analysis.js (caching is critical for high latency)
Minimize number of origins
Use HTTP/2 or HTTP/3 for multiplexing

If downlink < 1 Mbps → Very limited bandwidth, recommend:

Run webperf-media:Image-Element-Audit.js (aggressive compression)
Run webperf-media:Video-Element-Audit.js (disable autoplay)
Run webperf-loading:Prefetch-Resource-Validation.js (remove prefetch)
Implement bandwidth-aware loading

If downlink > 10 Mbps → Good bandwidth, consider:

Higher quality media
Strategic prefetch
Preloading next-page resources
Adaptive Loading Implementation Guide

Based on Network Information API results, implement these strategies:

For slow-2g / 2g (< 50 Kbps): (effectiveType: "slow-2g" or "2g")

Serve low-res images (quality: 30-40)
Disable autoplay videos
Remove all prefetch hints
Inline all critical CSS
Defer all non-critical JavaScript
Use system fonts (no webfonts)
Aggressive lazy loading (load on scroll + buffer)

For 3g (50-700 Kbps): (effectiveType: "3g")

Serve medium-res images (quality: 60-70)
Disable autoplay videos
Limited prefetch (critical only)
Inline critical CSS only
Defer non-critical JavaScript
Preload 1-2 critical fonts
Standard lazy loading

For 4g+ (> 700 Kbps): (effectiveType: "4g")

Serve high-res images (quality: 80-90)
Allow autoplay videos (muted)
Strategic prefetch for navigation
Standard CSS loading and JavaScript loading
Preload critical fonts
Standard lazy loading

For save-data mode: (navigator.connection.saveData === true)

Override connection type, treat as worse than actual
Show "Load high quality" toggle
Disable autoplay entirely
Minimal images, minimal quality
No prefetch, no preload (except critical)
Performance Budget by Connection Type

Adjust performance budgets based on connection quality:

slow-2g / 2g:

Total page weight: < 500KB
Images: < 200KB total
JavaScript: < 100KB total
No videos

3g:

Total page weight: < 1.5MB
Images: < 800KB total
JavaScript: < 300KB total
Videos: < 3MB (only if critical)

4g+:

Total page weight: < 3MB
Images: < 2MB total
JavaScript: < 1MB total
Videos: < 10MB
Network Information API Limitations

Be aware of API limitations and fallbacks:

API not available:

Safari does not support Network Information API
Fallback: Use TTFB as proxy for connection quality
Fallback: Device detection (mobile = assume slow)
Fallback: User preference toggle

API values are estimates:

effectiveType is based on recent observations
Values can change during session
Re-check periodically for long sessions

Privacy considerations:

Some browsers limit precision for privacy
Values may be rounded or capped
Consider user privacy when making decisions
References
references/snippets.md — Descriptions and thresholds for each script
references/schema.md — Return value schema for interpreting script output
Weekly Installs
104
Repository
nucliweb/webper…snippets
GitHub Stars
1.4K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn