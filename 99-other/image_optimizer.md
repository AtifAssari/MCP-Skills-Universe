---
title: image-optimizer
url: https://skills.sh/insight68/skills/image-optimizer
---

# image-optimizer

skills/insight68/skills/image-optimizer
image-optimizer
Installation
$ npx skills add https://github.com/insight68/skills --skill image-optimizer
SKILL.md
Image Optimizer

Image optimization toolkit using Sharp for high-performance WebP conversion, thumbnail generation, and intelligent background removal.

Quick Start

All scripts are in scripts/. Use pnpm to run them:

# Basic WebP conversion (large images)
node scripts/optimize-images.js

# Small images (higher quality)
node scripts/optimize-small-images.js

# Advanced with custom config
node scripts/optimize-images-advanced.js

Thumbnail Generation

Generate thumbnails with specific dimensions or aspect ratios:

# Square thumbnails (128x128)
pnpm optimize:128

# Square thumbnails (256x256)
pnpm optimize:256

# 16:9 aspect ratio (640x360 default)
pnpm optimize:16-9

# Process specific files
pnpm optimize:128 public/image.png public/logo.png

# Custom options
node scripts/optimize-thumbnails.js --size=128 --dir=public/icons

Aspect Ratio Thumbnails

Generate thumbnails with preset aspect ratios:

# 16:9 (widescreen, YouTube)
pnpm optimize:16-9 --size=small    # 640x360
pnpm optimize:16-9 --size=medium   # 800x450
pnpm optimize:16-9 --size=large    # 1920x1080

# 4:3 (traditional, iPad)
pnpm optimize:4-3 --size=medium    # 800x600

# 1:1 (square, Instagram)
pnpm optimize:1-1 --size=large     # 1080x1080

# Custom dimensions
node scripts/optimize-aspect-ratio.js --width=1280 --height=720

Background Removal

Remove white backgrounds with smart edge smoothing:

# Basic white to transparent
pnpm optimize:128 public/product.png --transparency=white-to-transparent

# High quality for product photos
pnpm optimize:256 public/product.jpg \
  --transparency=white-to-transparent \
  --threshold=250 \
  --quality=90

# Custom threshold for off-white backgrounds
pnpm optimize:128 public/icon.png --transparency=white-to-transparent --threshold=230

Configuration
WebP Quality
85-90: Product photos, high-quality images
75-85: Standard web images (default)
60-75: Thumbnails, non-critical images
Fit Strategies
cover: Fill entire area (recommended, exact dimensions)
inside: Maintain aspect ratio, may not fill completely
fill: Force stretch (distorts, not recommended)
Crop Position
entropy: Smart crop, keeps subject (recommended)
center: Center crop
attention: AI attention-based (requires Sharp 0.29+)
top, bottom, left, right: Edge-aligned
Transparency Modes
auto: Auto-detect based on input (PNG/WebP preserve, others remove)
preserve: Keep existing transparency
remove: Remove transparency, fill with background color
white-to-transparent: Smart white background removal
add: Add transparency with alpha level
Background Removal Options
--threshold: White threshold (0-255, default 240). Use 230-245 for off-white, 250-255 for pure white
--smooth-edges: Enable edge smoothing (default true)
--supersample: 2x supersampling for smooth edges (default true)
--gaussian-smoothing: Use 5x5 Gaussian kernel (default true, false=3x3 simple)
--smoothing-iterations: Edge smoothing passes (default 1, max 2)
Common Use Cases
E-commerce Product Photos
# Remove white background, high quality
pnpm optimize:256 public/products/*.jpg \
  --transparency=white-to-transparent \
  --threshold=250 \
  --quality=90 \
  --supersample=true \
  --gaussian-smoothing=true

Blog Thumbnails (16:9)
# Generate 16:9 thumbnails for blog posts
pnpm optimize:16-9 --size=medium --dir=public/blog-images

Social Media Avatars (1:1)
# Square thumbnails for profiles
pnpm optimize:1-1 --size=large --dir=public/avatars

Icon Optimization (128x128)
# Small square icons
pnpm optimize:128 public/icons/logo.png --transparency=preserve

Processing Directories

Batch process entire directories:

# Process all images in a directory
node scripts/optimize-thumbnails.js \
  --dir=public/uploads \
  --size=256 \
  --output=public/thumbnails

# With background removal
node scripts/optimize-thumbnails.js \
  --dir=public/products \
  --size=512 \
  --transparency=white-to-transparent \
  --threshold=245

Tips
Use supersampling for product photos to eliminate jagged edges
Higher quality (90+) for images that will be further edited
Standard quality (75) for final web images
Entropy position preserves important image content
Test thresholds on sample images before batch processing
Lower threshold (230-240) for off-white backgrounds
Higher threshold (250-255) for pure white backgrounds
Dependencies

All scripts require:

pnpm add sharp


Sharp is a high-performance Node.js image processing library.

Weekly Installs
19
Repository
insight68/skills
GitHub Stars
4
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass