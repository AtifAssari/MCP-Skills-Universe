---
rating: ⭐⭐
title: webperf-core-web-vitals
url: https://skills.sh/nucliweb/webperf-snippets/webperf-core-web-vitals
---

# webperf-core-web-vitals

skills/nucliweb/webperf-snippets/webperf-core-web-vitals
webperf-core-web-vitals
Installation
$ npx skills add https://github.com/nucliweb/webperf-snippets --skill webperf-core-web-vitals
SKILL.md
WebPerf: Core Web Vitals

JavaScript snippets for measuring web performance in Chrome DevTools. Execute with mcp__chrome-devtools__evaluate_script, capture output with mcp__chrome-devtools__get_console_message.

Scripts
scripts/CLS.js — Cumulative Layout Shift (CLS)
scripts/INP.js — Interaction to Next Paint (INP)
scripts/LCP-Image-Entropy.js — LCP Image Entropy
scripts/LCP-Subparts.js — LCP Subparts
scripts/LCP-Trail.js — LCP Trail
scripts/LCP-Video-Candidate.js — LCP Video Candidate
scripts/LCP.js — Largest Contentful Paint (LCP)
Common Workflows
Complete Core Web Vitals Audit

When the user asks for a comprehensive Core Web Vitals analysis or "audit CWV":

LCP.js - Measure Largest Contentful Paint
CLS.js - Measure Cumulative Layout Shift
INP.js - Measure Interaction to Next Paint
LCP-Subparts.js - Break down LCP timing phases
LCP-Trail.js - Track LCP candidate evolution
LCP Deep Dive

When LCP is slow or the user asks "debug LCP" or "why is LCP slow":

LCP.js - Establish baseline LCP value
LCP-Subparts.js - Break down into TTFB, resource load, render delay
LCP-Trail.js - Identify all LCP candidates and changes
LCP-Image-Entropy.js - Check if LCP image has visual complexity issues
LCP-Video-Candidate.js - Detect if LCP is a video (poster or video element)
CLS Investigation

When layout shifts are detected or the user asks "debug CLS" or "layout shift issues":

CLS.js - Measure overall CLS score
Layout-Shift-Loading-and-Interaction.js (pending — available in webperf-interaction skill)
Cross-reference with webperf-loading skill:
Find-Above-The-Fold-Lazy-Loaded-Images.js (lazy images causing shifts)
Fonts-Preloaded-Loaded-and-used-above-the-fold.js (font swap causing shifts)
INP Debugging

When interactions feel slow or the user asks "debug INP" or "slow interactions":

INP.js - Measure overall INP value; call getINP() after interactions, getINPDetails() for full list
Interactions.js (pending — available in webperf-interaction skill)
Input-Latency-Breakdown.js (pending — available in webperf-interaction skill)
Long-Animation-Frames.js (pending — available in webperf-interaction skill)
Long-Animation-Frames-Script-Attribution.js (pending — available in webperf-interaction skill)
Video as LCP Investigation

When LCP is a video element (detected by LCP-Video-Candidate.js):

LCP-Video-Candidate.js - Identify video as LCP candidate
Video-Element-Audit.js (from Media skill) - Audit video loading strategy
LCP-Subparts.js - Analyze video loading phases
Cross-reference with webperf-loading skill:
Resource-Hints-Validation.js (check for video preload)
Priority-Hints-Audit.js (check for fetchpriority on video)
Image as LCP Investigation

When LCP is an image (most common case):

LCP.js - Measure LCP timing
LCP-Subparts.js - Break down timing phases
LCP-Image-Entropy.js - Analyze image complexity
Cross-reference with webperf-media skill:
Image-Element-Audit.js (check format, dimensions, lazy loading)
Cross-reference with webperf-loading skill:
Find-Above-The-Fold-Lazy-Loaded-Images.js (check if incorrectly lazy)
Priority-Hints-Audit.js (check for fetchpriority="high")
Resource-Hints-Validation.js (check for preload)
Decision Tree

Use this decision tree to automatically run follow-up snippets based on results:

After LCP.js
If LCP > 2.5s → Run LCP-Subparts.js to diagnose which phase is slow
If LCP > 4.0s (poor) → Run full LCP deep dive workflow (5 snippets)
If LCP candidate is an image → Run LCP-Image-Entropy.js and webperf-media:Image-Element-Audit.js
If LCP candidate is a video → Run LCP-Video-Candidate.js and webperf-media:Video-Element-Audit.js
Always run → LCP-Trail.js to understand candidate evolution
After LCP-Subparts.js
If TTFB phase > 600ms → Switch to webperf-loading skill and run TTFB-Sub-Parts.js
If Resource Load Time > 1500ms → Run:
webperf-loading:Resource-Hints-Validation.js (check for preload/preconnect)
webperf-loading:Priority-Hints-Audit.js (check fetchpriority)
webperf-loading:Find-render-blocking-resources.js (competing resources)
If Render Delay > 200ms → Run:
webperf-loading:Find-render-blocking-resources.js (blocking CSS/JS)
webperf-loading:Script-Loading.js (parser-blocking scripts)
webperf-interaction:Long-Animation-Frames.js (main thread blocking)
After LCP-Trail.js
If many LCP candidate changes (>3) → This causes visual instability, investigate:
webperf-loading:Find-Above-The-Fold-Lazy-Loaded-Images.js (late-loading images)
webperf-loading:Fonts-Preloaded-Loaded-and-used-above-the-fold.js (font swaps)
CLS.js (layout shifts contributing to LCP changes)
If final LCP candidate appears late → Run webperf-loading:Resource-Hints-Validation.js
If early candidate was replaced → Understand why initial content was pushed down (likely CLS issue)
After LCP-Image-Entropy.js
If entropy is very high → Image is visually complex, recommend:
Modern formats (WebP, AVIF)
Appropriate compression
Potentially a placeholder strategy
If entropy is low → Image may be over-optimized or placeholder-like
If large file size detected → Run webperf-media:Image-Element-Audit.js for format/sizing analysis
After LCP-Video-Candidate.js
If video is LCP → Run:
webperf-media:Video-Element-Audit.js (check poster, preload, formats)
webperf-loading:Priority-Hints-Audit.js (check fetchpriority on poster)
LCP-Subparts.js (analyze video loading phases)
If poster image is LCP → Treat as image LCP (run image workflows)
After CLS.js
If CLS > 0.1 → Run webperf-interaction:Layout-Shift-Loading-and-Interaction.js (pending — available in webperf-interaction skill)
If CLS > 0.25 (poor) → Run comprehensive shift investigation:
webperf-loading:Find-Above-The-Fold-Lazy-Loaded-Images.js (images without dimensions)
webperf-loading:Fonts-Preloaded-Loaded-and-used-above-the-fold.js (font loading strategy)
webperf-loading:Critical-CSS-Detection.js (late-loading styles)
webperf-media:Image-Element-Audit.js (missing width/height)
If CLS = 0 → Confirm with multiple page loads (might be timing-dependent)
After INP.js
If INP > 200ms → Run webperf-interaction:Interactions.js to identify slow interactions
If INP > 500ms (poor) → Run full INP debugging workflow:
webperf-interaction:Interactions.js (list all interactions)
webperf-interaction:Input-Latency-Breakdown.js (phase breakdown)
webperf-interaction:Long-Animation-Frames.js (blocking frames)
webperf-interaction:Long-Animation-Frames-Script-Attribution.js (culprit scripts)
If specific interaction type is slow (e.g., keyboard) → Focus analysis on that interaction type
After INP data is collected → call getINPDetails() for the full sorted interaction list (useful for identifying patterns across multiple slow interactions)
Error Recovery
If any script returns status: "error" → Check if the page has finished loading:
If early in load: wait and re-run the script
If page is an SPA: user may need to navigate to the target route first
If LCP.js / LCP-Subparts.js returns status: "error" → Tell the user: "LCP data is not available yet. Please ensure the page has fully loaded, then run the analysis again."
If INP.js getINP() returns status: "error" → The getDataFn: "getINP" field signals the agent can retry after user interaction. Prompt the user to click, type, or scroll, then call getINP() again.
Cross-Skill Triggers

Context fork note: This skill runs with context: fork. Cross-skill triggers below are recommendations to report back to the parent agent, not direct calls this subagent can execute. When a cross-skill trigger fires, tell the user which skill and script to run next. Scripts marked (pending) are not yet available — skip them and note the limitation.

These triggers recommend using snippets from other skills:

From LCP to Loading Skill

If LCP > 2.5s and TTFB phase is dominant → Use webperf-loading skill:

TTFB.js, TTFB-Sub-Parts.js, Service-Worker-Analysis.js

If LCP image is lazy-loaded → Use webperf-loading skill:

Find-Above-The-Fold-Lazy-Loaded-Images.js

If LCP has no fetchpriority → Use webperf-loading skill:

Priority-Hints-Audit.js
From CLS to Loading Skill

If CLS caused by fonts → Use webperf-loading skill:

Fonts-Preloaded-Loaded-and-used-above-the-fold.js
Resource-Hints-Validation.js (for font preload)

If CLS caused by images → Use webperf-media skill:

Image-Element-Audit.js (check for width/height attributes)
From INP to Interaction Skill
If INP > 200ms → Use webperf-interaction skill for full debugging:
Interactions.js, Input-Latency-Breakdown.js
Long-Animation-Frames.js, Long-Animation-Frames-Script-Attribution.js
LongTask.js (if pre-interaction blocking suspected)
From LCP/INP to Interaction Skill
If render delay or interaction delay is high → Use webperf-interaction skill:
Long-Animation-Frames.js (main thread blocking)
LongTask.js (long tasks delaying rendering)
Multi-Metric Correlation

When multiple CWV metrics are poor, prioritize investigation:

If LCP > 2.5s AND CLS > 0.1 → Likely shared root cause:

Check for late-loading content pushing LCP element
Run LCP-Trail.js to see LCP candidate changes
Run Layout-Shift-Loading-and-Interaction.js to correlate timing

If LCP > 2.5s AND INP > 200ms → Main thread congestion:

Run Long-Animation-Frames.js
Run webperf-loading:Script-Loading.js
Run webperf-loading:JS-Execution-Time-Breakdown.js

If CLS > 0.1 AND INP > 200ms → Layout thrashing or interaction-triggered shifts:

Run Layout-Shift-Loading-and-Interaction.js
Run Interactions.js
Check if shifts occur during/after interactions
References
references/snippets.md — Descriptions and thresholds for each script
references/schema.md — Return value schema for interpreting script output
Weekly Installs
121
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