---
rating: ⭐⭐
title: webperf-media
url: https://skills.sh/nucliweb/webperf-snippets/webperf-media
---

# webperf-media

skills/nucliweb/webperf-snippets/webperf-media
webperf-media
Installation
$ npx skills add https://github.com/nucliweb/webperf-snippets --skill webperf-media
SKILL.md
WebPerf: Media Performance

JavaScript snippets for measuring web performance in Chrome DevTools. Execute with mcp__chrome-devtools__evaluate_script, capture output with mcp__chrome-devtools__get_console_message.

Scripts
scripts/Image-Element-Audit.js — Image Element Audit
scripts/SVG-Embedded-Bitmap-Analysis.js — SVG Embedded Bitmap Analysis
scripts/Video-Element-Audit.js — Video Element Audit
Common Workflows
Complete Media Audit

When the user asks for media optimization or "audit images and videos":

Image-Element-Audit.js - Analyze all images (format, lazy loading, sizing, fetchpriority)
Video-Element-Audit.js - Analyze all videos (poster, preload, formats, autoplay)
SVG-Embedded-Bitmap-Analysis.js - Detect inefficient bitmap images embedded in SVGs
Image Optimization Workflow

When the user asks "optimize images" or "check image performance":

Image-Element-Audit.js - Full image audit
Cross-reference with webperf-loading skill:
Find-Above-The-Fold-Lazy-Loaded-Images.js (incorrectly lazy-loaded images)
Find-non-Lazy-Loaded-Images-outside-of-the-viewport.js (missing lazy loading)
Find-Images-With-Lazy-and-Fetchpriority.js (contradictory attributes)
Priority-Hints-Audit.js (LCP image should have fetchpriority="high")
Video Performance Audit

When the user asks "optimize videos" or "check video performance":

Video-Element-Audit.js - Full video audit
Cross-reference with webperf-core-web-vitals skill:
LCP-Video-Candidate.js (check if video/poster is LCP)
Cross-reference with webperf-loading skill:
Priority-Hints-Audit.js (video poster priority)
Resource-Hints-Validation.js (video preload)
LCP Image Investigation

When LCP is an image and needs optimization:

Cross-reference with webperf-core-web-vitals skill:
LCP.js (measure LCP)
LCP-Image-Entropy.js (analyze image complexity)
Image-Element-Audit.js - Check format, dimensions, lazy loading
Cross-reference with webperf-loading skill:
Find-Above-The-Fold-Lazy-Loaded-Images.js (should NOT be lazy)
Priority-Hints-Audit.js (should have fetchpriority="high")
Resource-Hints-Validation.js (consider preload)
Layout Shift from Images

When CLS is caused by images without dimensions:

Image-Element-Audit.js - Check for missing width/height attributes
Cross-reference with webperf-core-web-vitals skill:
CLS.js (measure total CLS)
Cross-reference with webperf-interaction skill:
Layout-Shift-Loading-and-Interaction.js (when shifts occur)
SVG Optimization Audit

When the user asks about SVG performance or file sizes are large:

SVG-Embedded-Bitmap-Analysis.js - Detect raster images embedded in vector SVGs
Recommend SVGO optimization for SVGs without embedded bitmaps
Recommend extracting bitmaps to separate image files with proper formats
Decision Tree

Use this decision tree to automatically run follow-up snippets based on results:

After Image-Element-Audit.js

If images missing width/height attributes → Layout shift risk, run:

webperf-core-web-vitals:CLS.js (measure CLS impact)
webperf-interaction:Layout-Shift-Loading-and-Interaction.js (timing of shifts)
Recommend adding explicit dimensions to all images

If images using wrong format (JPEG for graphics, PNG for photos) → Recommend:

Modern formats: WebP, AVIF
Appropriate format for content type
Format-specific compression settings

If images much larger than display size → Recommend:

Responsive images with srcset
Appropriate image CDN sizing
srcset with multiple sizes for different viewports

If above-the-fold images are lazy-loaded → Run:

webperf-loading:Find-Above-The-Fold-Lazy-Loaded-Images.js (confirm)
webperf-core-web-vitals:LCP.js (measure LCP impact)
Recommend removing loading="lazy" from above-fold images

If LCP image lacks fetchpriority="high" → Run:

webperf-core-web-vitals:LCP.js (measure current LCP)
webperf-loading:Priority-Hints-Audit.js (full priority audit)
Recommend adding fetchpriority="high" to LCP image

If below-the-fold images are NOT lazy-loaded → Run:

webperf-loading:Find-non-Lazy-Loaded-Images-outside-of-the-viewport.js (confirm)
Recommend adding loading="lazy" to offscreen images

If images have both loading="lazy" AND fetchpriority="high" → Run:

webperf-loading:Find-Images-With-Lazy-and-Fetchpriority.js (confirm contradiction)
Recommend removing one of the conflicting attributes

If images competing with critical resources → Run:

webperf-loading:Find-render-blocking-resources.js (resource priority conflicts)
webperf-loading:TTFB-Resources.js (identify slow image CDN)

If images missing alt text → Accessibility issue, recommend adding descriptive alt text

After Video-Element-Audit.js

If video is LCP candidate → Run:

webperf-core-web-vitals:LCP-Video-Candidate.js (confirm)
webperf-core-web-vitals:LCP.js (measure LCP)
webperf-core-web-vitals:LCP-Sub-Parts.js (break down timing)
Optimize video poster image or consider image alternative

If video missing poster → Recommend:

Adding poster image for better perceived performance
Using first frame or custom thumbnail
Optimizing poster as you would an image

If video uses preload="auto" → Bandwidth concern, evaluate:

Is video above-the-fold? Keep preload="auto"
Is video below-the-fold? Change to preload="metadata" or "none"
Is autoplay intended? Verify preload matches intent

If autoplay video without muted → Browser will block, recommend:

Adding muted attribute
Or removing autoplay

If video missing multiple formats → Recommend:

WebM for Chrome/Firefox
MP4 as fallback for Safari
Order sources by efficiency (WebM first)

If large video files (>5MB) → Recommend:

Compression/transcoding
Adaptive bitrate streaming (HLS, DASH)
Loading strategy optimization
After SVG-Embedded-Bitmap-Analysis.js

If bitmap images found in SVGs → Recommend:

Extract bitmaps to separate files
Use WebP/AVIF format for extracted images
Reference images from SVG with element
Or convert to pure vector if possible

If large embedded bitmaps (>100KB) → Critical inefficiency:

SVG parsing overhead + large bitmap = worst of both worlds
Urgently recommend extraction

If multiple small bitmaps in SVG → Consider:

CSS sprites for small icons
SVG symbols for reusable graphics
Extracting to individual optimized images
Performance Budget Thresholds

Use these thresholds to trigger recommendations:

Image File Sizes:

Warning: Individual image > 500KB → Check format and compression
Critical: Individual image > 1MB → Urgent optimization needed
Total images: > 5MB on initial load → Implement lazy loading

Image Formats:

JPEG for graphics/icons → Recommend PNG or SVG
PNG for photos → Recommend JPEG, WebP, or AVIF
GIF for animations → Recommend video (MP4/WebM) or animated WebP
No modern formats (WebP/AVIF) → Recommend upgrading

Image Dimensions:

Intrinsic size > 2x display size → Recommend responsive images
Intrinsic size < display size → Upscaling = blurry, provide larger source

Video File Sizes:

Warning: Video > 10MB → Consider compression or streaming
Critical: Video > 50MB → Urgent optimization or streaming needed

Lazy Loading:

Above-fold images lazy-loaded → Critical LCP impact, fix immediately
Below-fold images NOT lazy-loaded → Wasted bandwidth, implement lazy loading
>10 images eager-loaded → Excessive, implement lazy loading

Priority Hints:

LCP image without fetchpriority="high" → Add for 10-30% LCP improvement
Non-LCP images with fetchpriority="high" → Remove, wasting browser hints
Lazy + fetchpriority="high" conflict → Fix contradiction
References
references/snippets.md — Descriptions and thresholds for each script
references/schema.md — Return value schema for interpreting script output
Weekly Installs
106
Repository
nucliweb/webper…snippets
GitHub Stars
1.4K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass