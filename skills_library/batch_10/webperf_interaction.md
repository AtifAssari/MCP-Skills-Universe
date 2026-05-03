---
title: webperf-interaction
url: https://skills.sh/nucliweb/webperf-snippets/webperf-interaction
---

# webperf-interaction

skills/nucliweb/webperf-snippets/webperf-interaction
webperf-interaction
Installation
$ npx skills add https://github.com/nucliweb/webperf-snippets --skill webperf-interaction
SKILL.md
WebPerf: Interaction & Animation

JavaScript snippets for measuring web performance in Chrome DevTools. Execute with mcp__chrome-devtools__evaluate_script, capture output with mcp__chrome-devtools__get_console_message.

Scripts
scripts/Input-Latency-Breakdown.js — Input Latency Breakdown
scripts/Interactions.js — Interactions
scripts/Layout-Shift-Loading-and-Interaction.js — Layout Shift Tracking
scripts/Long-Animation-Frames-Helpers.js — LoAF Helpers
scripts/Long-Animation-Frames-Script-Attribution.js — Long Animation Frames Script Attribution
scripts/Long-Animation-Frames.js — Long Animation Frames (LoAF)
scripts/LongTask.js — Long Tasks
scripts/Scroll-Performance.js — Scroll Performance Analysis
Common Workflows
Complete Interaction Performance Audit

When the user asks for interaction analysis or "audit responsiveness":

Interactions.js - List all user interactions with timing
Input-Latency-Breakdown.js - Break down interaction phases
Long-Animation-Frames.js - Detect blocking animation frames
LongTask.js - Identify long tasks blocking the main thread
Scroll-Performance.js - Measure scroll smoothness
INP Deep Dive

When INP is slow (>200ms) or the user asks "debug INP" or "slow interactions":

Interactions.js - Identify which interactions are slow
Input-Latency-Breakdown.js - Break down into input delay, processing time, presentation delay
Long-Animation-Frames.js - Find animation frames >50ms that block interactions
Long-Animation-Frames-Script-Attribution.js - Identify scripts causing the blocking
Long-Animation-Frames-Helpers.js - Get detailed timing and attribution helpers
Scroll Jank Investigation

When the user reports "scroll jank", "choppy scrolling", or "scroll performance issues":

Scroll-Performance.js - Measure scroll smoothness and frame drops
Long-Animation-Frames.js - Detect frames causing jank (>50ms)
Layout-Shift-Loading-and-Interaction.js - Check for layout shifts during scroll
Long-Animation-Frames-Script-Attribution.js - Find scripts running during scroll
Main Thread Blocking Analysis

When the page feels unresponsive or the user asks "why is the page frozen":

LongTask.js - List all tasks >50ms blocking the main thread
Long-Animation-Frames.js - Correlate with animation frame timing
Long-Animation-Frames-Script-Attribution.js - Attribute blocking to specific scripts
Cross-reference with webperf-loading skill:
JS-Execution-Time-Breakdown.js (script parsing/execution time)
First-And-Third-Party-Script-Info.js (identify third-party blockers)
Layout Shift During Interaction

When the user reports "things move when I click" or CLS issues during interaction:

Layout-Shift-Loading-and-Interaction.js - Separate loading vs interaction shifts
Interactions.js - Correlate shifts with specific interactions
CLS.js (from Core Web Vitals skill) - Measure total CLS
Cross-reference with webperf-media skill:
Image-Element-Audit.js (images without dimensions causing shifts)
Animation Performance Analysis

When animations feel sluggish or the user asks "debug animation performance":

Long-Animation-Frames.js - Identify frames taking too long to render
Long-Animation-Frames-Helpers.js - Detailed frame timing analysis
Long-Animation-Frames-Script-Attribution.js - Find scripts delaying frames
Scroll-Performance.js - If scroll animations are involved
Third-Party Script Impact on Interactions

When interactions are slow and third-party scripts are suspected:

Long-Animation-Frames-Script-Attribution.js - Identify third-party scripts in long frames
LongTask.js - Measure long task frequency
Cross-reference with webperf-loading skill:
First-And-Third-Party-Script-Info.js (list all third-party scripts)
First-And-Third-Party-Script-Timings.js (measure script loading impact)
Script-Loading.js (check for blocking scripts)
Decision Tree

Use this decision tree to automatically run follow-up snippets based on results:

After Interactions.js
If any interaction > 200ms → Run Input-Latency-Breakdown.js on slow interactions; also run webperf-core-web-vitals:INP.js for official INP measurement
If many interactions > 200ms → Main thread congestion, run:
Long-Animation-Frames.js (blocking frames)
LongTask.js (long tasks)
Long-Animation-Frames-Script-Attribution.js (culprit scripts)
If specific interaction types are slow (e.g., click vs keyboard) → Focus on that interaction type
If interactions occur during page load → Cross-check with webperf-loading:JS-Execution-Time-Breakdown.js
After Input-Latency-Breakdown.js
If Input Delay > 50ms → Main thread was busy, run:
Long-Animation-Frames.js (what was blocking)
LongTask.js (long task before interaction)
If Processing Time > 100ms → Heavy event handlers, run:
Long-Animation-Frames-Script-Attribution.js (which scripts)
webperf-loading:First-And-Third-Party-Script-Info.js (third-party involvement)
If Presentation Delay > 50ms → Rendering bottleneck, run:
Long-Animation-Frames.js (frame rendering time)
Layout-Shift-Loading-and-Interaction.js (check for layout work)
After Long-Animation-Frames.js
If many frames > 50ms → Run Long-Animation-Frames-Script-Attribution.js to identify causes
If frames > 100ms → Critical blocking, run:
Long-Animation-Frames-Script-Attribution.js (detailed attribution)
LongTask.js (related long tasks)
webperf-loading:JS-Execution-Time-Breakdown.js (script execution cost)
If frames occur during scroll → Run Scroll-Performance.js to measure impact
If frames occur during page load → Cross-check with webperf-loading:Event-Processing-Time.js
After Long-Animation-Frames-Script-Attribution.js
If third-party scripts are causing long frames → Run:
webperf-loading:First-And-Third-Party-Script-Info.js (list all third-party scripts)
webperf-loading:Script-Loading.js (check loading strategy)
Recommend deferring or removing problematic scripts
If first-party scripts are causing long frames → Recommend:
Code splitting
Debouncing/throttling event handlers
Web Workers for heavy computation
If forced reflow/layout detected → Analyze DOM manipulation patterns
After LongTask.js
If many long tasks (>5) → Main thread is congested, run:
Long-Animation-Frames-Script-Attribution.js (detailed attribution)
webperf-loading:JS-Execution-Time-Breakdown.js (script execution analysis)
webperf-loading:First-And-Third-Party-Script-Info.js (identify heavy scripts)
If long tasks > 500ms → Critical blocking, investigate:
Synchronous third-party scripts
Heavy computation without Web Workers
Excessive DOM manipulation
If long tasks correlate with interactions → Run Interactions.js to see impact
After Scroll-Performance.js
If scroll FPS < 30 → Severe jank, run:
Long-Animation-Frames.js (blocking frames during scroll)
Long-Animation-Frames-Script-Attribution.js (scripts running on scroll)
Layout-Shift-Loading-and-Interaction.js (layout work during scroll)
If scroll FPS 30-50 → Noticeable jank, investigate:
Scroll event handlers
Passive event listeners
CSS will-change properties
If scroll FPS > 50 → Good, but check for layout shifts during scroll
After Layout-Shift-Loading-and-Interaction.js
If shifts occur during page load → Cross-reference with webperf-core-web-vitals:CLS.js
If shifts occur during interaction → This impacts INP and UX, investigate:
Dynamic content insertion
Images/ads loading without dimensions
Font swaps (run webperf-loading:Fonts-Preloaded-Loaded-and-used-above-the-fold.js)
If shifts occur during scroll → Run Scroll-Performance.js to measure impact
After Long-Animation-Frames-Helpers.js

This is a utility snippet, use results to:

Understand frame timing in detail
Identify precise script attribution
Measure style/layout/paint phases
No automatic follow-up, use data to inform next steps
Performance Budget Thresholds

Use these thresholds to automatically trigger follow-up analysis:

INP Thresholds:

Good: ≤ 200ms → Monitor, no action needed
Needs Improvement: 200-500ms → Run Input-Latency-Breakdown.js
Poor: > 500ms → Run full INP debugging workflow (5 snippets)

Long Animation Frames:

Warning: > 50ms → Run Long-Animation-Frames-Script-Attribution.js
Critical: > 100ms → Run full main thread blocking workflow

Long Tasks:

Warning: > 50ms → Monitor frequency
Critical: > 200ms or >5 tasks per second → Run attribution and script analysis

Scroll Performance:

Good: ≥ 50 FPS → Monitor
Needs Improvement: 30-50 FPS → Run Long-Animation-Frames.js
Poor: < 30 FPS → Run full scroll jank workflow

Interaction Frequency:

If >10 interactions/second → User is actively interacting, prioritize INP optimization
If <1 interaction/5 seconds → Interactions are rare, focus on first interaction responsiveness
Multi-Metric Correlation

When multiple interaction metrics are poor:

If Long Tasks AND Long Animation Frames both detected → Shared root cause:

Run Long-Animation-Frames-Script-Attribution.js
Likely heavy JavaScript execution
Consider code splitting or Web Workers

If INP slow AND CLS high → Interaction-triggered layout shifts:

Run Layout-Shift-Loading-and-Interaction.js
Correlate shift timing with interaction timing
Check for dynamic content insertion

If Scroll jank AND Long Animation Frames → Scroll handlers blocking main thread:

Run Long-Animation-Frames-Script-Attribution.js during scroll
Check for non-passive scroll listeners
Audit scroll-triggered animations
References
references/snippets.md — Descriptions and thresholds for each script
references/schema.md — Return value schema for interpreting script output
Weekly Installs
102
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