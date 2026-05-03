---
rating: ⭐⭐
title: image-optimization
url: https://skills.sh/aj-geddes/useful-ai-prompts/image-optimization
---

# image-optimization

skills/aj-geddes/useful-ai-prompts/image-optimization
image-optimization
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill image-optimization
SKILL.md
Image Optimization
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Images typically comprise 50% of page weight. Optimization dramatically improves performance, especially on mobile networks.

When to Use
Website optimization
Responsive image implementation
Performance improvement
Mobile experience enhancement
Before deployment
Quick Start

Minimal working example:

Format Selection:

JPEG:
  Best for: Photographs, complex images
  Compression: Lossy (quality 70-85)
  Size: ~50-70% reduction
  Tools: ImageMagick, TinyJPEG
  Command: convert image.jpg -quality 75 optimized.jpg

PNG:
  Best for: Icons, screenshots, transparent images
  Compression: Lossless
  Size: 10-30% reduction
  Tools: PNGQuant, OptiPNG
  Command: optipng -o3 image.png

WebP:
  Best for: Modern browsers (90% support)
  Compression: 25-35% better than JPEG/PNG
  Fallback: Use <picture> element
  Tools: cwebp
  Command: cwebp -q 75 image.jpg -o image.webp

SVG:
  Best for: Icons, logos, simple graphics
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Image Compression & Formats	Image Compression & Formats
Responsive Images	Responsive Images
Optimization Process	Optimization Process
Monitoring & Best Practices	Monitoring & Best Practices
Best Practices
✅ DO
Follow established patterns and conventions
Write clean, maintainable code
Add appropriate documentation
Test thoroughly before deploying
❌ DON'T
Skip testing or validation
Ignore error handling
Hard-code configuration values
Weekly Installs
390
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass