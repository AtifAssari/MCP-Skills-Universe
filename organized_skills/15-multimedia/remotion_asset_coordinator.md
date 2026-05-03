---
rating: ⭐⭐⭐⭐⭐
title: remotion-asset-coordinator
url: https://skills.sh/ncklrs/startup-os-skills/remotion-asset-coordinator
---

# remotion-asset-coordinator

skills/ncklrs/startup-os-skills/remotion-asset-coordinator
remotion-asset-coordinator
Installation
$ npx skills add https://github.com/ncklrs/startup-os-skills --skill remotion-asset-coordinator
SKILL.md
Remotion Asset Coordinator

Streamlines the asset preparation workflow from motion design specs to production-ready files. Identifies requirements, recommends sources, guides optimization, and generates proper import code.

What This Skill Does

Coordinates the complete asset lifecycle:

Requirement extraction — Parse specs for all asset needs
Source recommendations — Suggest free/paid asset sources
Format guidance — Recommend optimal formats for each asset type
Preparation workflows — Step-by-step asset prep instructions
Import code generation — Create validated staticFile imports
Quality validation — Verify assets meet production standards
Input/Output Formats
Input Format: VIDEO_SPEC.md OR CODE_SCAFFOLD.md

This skill accepts either:

Option 1: VIDEO_SPEC.md (from /motion-designer)

# Video Title

## Assets Required

### Images
- Logo (800x800, transparent background)
- Product photo (1920x1080)

### Audio
- Background music (full duration, 0.4 volume)
- Whoosh sound effect (5s mark, 0.6 volume)

### Fonts
- Inter (weights: 400, 600, 700)


Option 2: CODE_SCAFFOLD.md (from /remotion-spec-translator)

## TODO Markers

- [ ] **Assets Required**
  - [ ] Add `public/logo.png` (800x800)
  - [ ] Add `public/audio/background.mp3`
  - [ ] Add `public/audio/whoosh.mp3`

Output Format: ASSET_MANIFEST.md

Generates a comprehensive asset preparation manifest:

# Asset Manifest: [Video Title]

## Status Overview
- 🔴 Not Started: 3 assets
- 🟡 In Progress: 0 assets
- 🟢 Ready: 0 assets

**Progress:** 0/3 assets ready

## Required Assets

### Images (2 required)

#### 1. Logo
- **Status:** 🔴 Not Started
- **File Path:** `public/images/logo.png`
- **Specifications:**
  - Format: PNG (transparency required)
  - Dimensions: 800x800 pixels (2x for retina)
  - Display size: 400x400px
  - File size target: < 200KB

- **Source Recommendations:**
  - Option 1: Export from Figma/design tool
  - Option 2: Create in Photoshop/Illustrator
  - Optimization: Use pngquant or tinypng.com

- **Preparation Steps:**
  1. Export at 800x800 resolution
  2. Ensure transparent background
  3. Optimize with `pngquant --quality=80-95 logo.png`
  4. Verify file size < 200KB
  5. Save to `public/images/logo.png`

- **Import Code:**
  ```typescript
  import { Img, staticFile } from 'remotion';

  <Img
    src={staticFile('images/logo.png')}
    alt="Logo"
    style={{
      width: 400,
      height: 400,
    }}
  />

2. Product Photo

Status: 🔴 Not Started

File Path: public/images/product.jpg

Specifications:

Format: JPEG (no transparency needed)
Dimensions: 1920x1080 pixels
Quality: 85-90%
File size target: < 500KB

Source Recommendations:

Option 1: Unsplash (free, high-quality) - https://unsplash.com
Option 2: Pexels (free) - https://pexels.com
Option 3: Custom photography

Preparation Steps:

Download or shoot at 1920x1080+
Edit/crop to exact 1920x1080
Export as JPEG 85-90% quality
Verify file size < 500KB
Save to public/images/product.jpg

Import Code:

import { Img, staticFile } from 'remotion';

<Img
  src={staticFile('images/product.jpg')}
  style={{
    width: '100%',
    height: '100%',
    objectFit: 'cover',
  }}
/>

Audio (2 required)
3. Background Music

Status: 🔴 Not Started

File Path: public/audio/music/background.mp3

Specifications:

Format: MP3
Duration: 30 seconds
Bitrate: 192-256 kbps
Sample rate: 44.1 kHz or 48 kHz
Channels: Stereo

Source Recommendations:

Option 1: YouTube Audio Library (free) - https://studio.youtube.com
Option 2: Incompetech (free, attribution) - https://incompetech.com
Option 3: Epidemic Sound (paid) - https://epidemicsound.com

Preparation Steps:

Download/purchase 30s music track
Trim to exactly 30 seconds if needed
Convert to MP3 if needed: ffmpeg -i input.wav -b:a 192k output.mp3
Apply fade out at end if needed
Save to public/audio/music/background.mp3

Import Code:

import { Audio, staticFile, useVideoConfig } from 'remotion';

const { durationInFrames } = useVideoConfig();

<Audio
  src={staticFile('audio/music/background.mp3')}
  volume={0.4}
  startFrom={0}
  endAt={durationInFrames}
/>

4. Whoosh Sound Effect

Status: 🔴 Not Started

File Path: public/audio/sfx/whoosh.mp3

Specifications:

Format: MP3
Duration: 1-2 seconds
Bitrate: 192 kbps
Timing: Plays at 5s mark (frame 150 at 30fps)

Source Recommendations:

Option 1: Freesound (free, Creative Commons) - https://freesound.org
Option 2: Zapsplat (free, attribution) - https://zapsplat.com
Option 3: AudioJungle (paid) - https://audiojungle.net

Preparation Steps:

Download whoosh/transition sound effect
Trim to 1-2 seconds
Normalize volume if needed
Convert to MP3: ffmpeg -i input.wav -b:a 192k whoosh.mp3
Save to public/audio/sfx/whoosh.mp3

Import Code:

import { Audio, Sequence, staticFile } from 'remotion';

<Sequence from={150} durationInFrames={60}>
  <Audio
    src={staticFile('audio/sfx/whoosh.mp3')}
    volume={0.6}
  />
</Sequence>

Fonts (1 required)
5. Inter Font

Status: 🟢 Ready (Google Font)

Weights Needed: 400 (Regular), 600 (Semibold), 700 (Bold)

Source: Google Fonts via @remotion/google-fonts

Installation:

npm install @remotion/google-fonts


Import Code:

import { loadFont } from '@remotion/google-fonts/Inter';

const { fontFamily } = loadFont({
  weights: ['400', '600', '700'],
});

<div style={{
  fontFamily,
  fontWeight: 600,
}}>
  Text content
</div>

Directory Structure

Create this folder structure in your project:

public/
├── images/
│   ├── logo.png          # 🔴 Required
│   └── product.jpg       # 🔴 Required
└── audio/
    ├── music/
    │   └── background.mp3  # 🔴 Required
    └── sfx/
        └── whoosh.mp3      # 🔴 Required

Quick Reference: Optimization Commands
Images
# Optimize PNG
pngquant --quality=80-95 input.png -o output.png

# Convert to JPEG
magick input.png -quality 90 output.jpg

# Resize image
magick input.png -resize 1920x1080 output.png

Audio
# Convert to MP3
ffmpeg -i input.wav -b:a 192k output.mp3

# Trim audio
ffmpeg -i input.mp3 -ss 00:00:00 -t 00:00:30 -c copy output.mp3

# Normalize volume
ffmpeg -i input.mp3 -filter:a "volume=1.5" output.mp3

Quality Checklist

Before marking assets as ready:

 All files in correct directories
 File names match import paths exactly
 Image dimensions correct (2x for retina if needed)
 Image formats appropriate (PNG for transparency, JPEG for photos)
 Image file sizes optimized (< 500KB ideal)
 Audio files in MP3 format
 Audio durations correct
 Audio bitrates appropriate (192-256 kbps)
 Fonts installed and imported correctly
 All staticFile() paths tested
Next Steps
Gather assets using source recommendations above
Prepare assets following preparation steps for each
Validate quality using the checklist
Update status to 🟢 Ready as assets are completed
Implement code using provided import snippets
Run /remotion-video-reviewer to verify asset integration

**This document provides:**
- Complete asset inventory with specifications
- Source recommendations (free and paid)
- Step-by-step preparation workflows
- Ready-to-use import code snippets
- Quality validation checklist
- Progress tracking (🔴 🟡 🟢)

**Feeds into:** Developer implementation → `/remotion-video-reviewer` for quality check

## Asset Categories

### Images

**Types:**
- Product photos
- Background images
- Textures and patterns
- Icons and illustrations
- Logos and brand assets

**Optimal Formats:**
- **PNG**: Logos, icons, text overlays (transparency needed)
- **JPEG**: Photos, backgrounds (no transparency)
- **SVG**: Simple graphics, icons (scalable, small file size)
- **WebP**: Modern alternative, smaller file sizes

**Recommendations:**
```typescript
// Logo (transparency required)
Format: PNG
Resolution: 2x intended display size (retina)
Example: 400x400 element → 800x800 PNG

// Product photo
Format: JPEG (85-90% quality)
Resolution: Exact or slightly larger than display
Example: 1920x1080 display → 1920x1080 or 2560x1440 JPEG

// Icon
Format: SVG (preferred) or PNG
Resolution: 2x display size if PNG

Videos

Types:

Background footage
Product demos
Screen recordings
Transitions

Optimal Formats:

MP4 (H.264): Best compatibility
WebM: Modern, smaller files
ProRes: High quality source footage

Recommendations:

// Background video
Format: MP4 (H.264)
Codec: H.264, High profile
Resolution: Match composition (1920x1080)
Bitrate: 5-10 Mbps
Frame rate: Match composition (30fps)

// Product demo
Format: MP4 (H.264)
Resolution: 1920x1080 or 3840x2160 (4K)
Bitrate: 10-20 Mbps
Alpha channel: Use ProRes 4444 if transparency needed

Audio

Types:

Background music
Sound effects (SFX)
Voiceover
Ambient texture

Optimal Formats:

MP3: Compressed, good compatibility
WAV: Uncompressed, best quality
AAC: Modern, better compression than MP3

Recommendations:

// Background music
Format: MP3 or AAC
Bitrate: 192-320 kbps
Sample rate: 44.1 kHz or 48 kHz
Channels: Stereo

// Sound effects
Format: WAV (for editing) → MP3 (for production)
Bitrate: 192 kbps (MP3)
Sample rate: 44.1 kHz
Channels: Stereo or Mono
Duration: Trim to exact needed length

// Voiceover
Format: WAV or MP3
Bitrate: 256-320 kbps
Sample rate: 48 kHz
Channels: Mono (sufficient for voice)

Fonts

Types:

Google Fonts (free, web-safe)
Custom fonts (brand-specific)
System fonts (fallbacks)

Recommendations:

// Google Fonts (preferred)
Method: Import via @remotion/google-fonts
Weights: Only import needed weights
Example: 400 (regular), 600 (semibold), 700 (bold)

// Custom fonts
Format: WOFF2 (best), WOFF, TTF
Location: /public/fonts/
Import: Via CSS @font-face

Asset Source Recommendations
Free Sources

Images & Illustrations:

Unsplash — High-quality photos (free, no attribution required)
Pexels — Photos and videos (free)
Pixabay — Photos, vectors, videos (free)
unDraw — Customizable illustrations (free, SVG)
Heroicons — Beautiful hand-crafted SVG icons (free)

Audio:

Freesound — Sound effects library (Creative Commons)
YouTube Audio Library — Music and SFX (free for commercial use)
Incompetech — Royalty-free music (attribution required)
Zapsplat — Free sound effects (attribution)

Fonts:

Google Fonts — 1400+ free fonts (web-safe)
Font Squirrel — Free fonts for commercial use
Paid/Premium Sources

Images:

Adobe Stock — Professional quality
Shutterstock — Massive library
Getty Images — Premium content

Audio:

Epidemic Sound — High-quality music library
Artlist — Unlimited music licensing
AudioJungle — Individual tracks, affordable

Fonts:

Adobe Fonts — Included with Creative Cloud
MyFonts — Massive font marketplace
Asset Preparation Workflows
Image Preparation
# 1. Resize to appropriate dimensions
magick input.png -resize 1920x1080 output.png

# 2. Optimize PNG
pngquant --quality=80-95 input.png -o optimized.png

# 3. Convert to JPEG (if no transparency)
magick input.png -quality 90 output.jpg

# 4. Generate WebP (modern format)
magick input.png -quality 85 output.webp


Manual workflow:

Open in Photoshop/GIMP/Figma
Resize to exact or 2x display dimensions
Export at appropriate quality
Verify file size (< 1MB for most images)
Video Preparation
# Convert to H.264 MP4
ffmpeg -i input.mov -c:v libx264 -preset slow -crf 20 -c:a aac -b:a 192k output.mp4

# Resize video
ffmpeg -i input.mp4 -vf scale=1920:1080 -c:v libx264 -crf 20 output.mp4

# Extract clip segment
ffmpeg -i input.mp4 -ss 00:00:10 -t 00:00:05 -c copy output.mp4

# Compress video
ffmpeg -i input.mp4 -c:v libx264 -crf 28 -c:a aac -b:a 128k compressed.mp4

Audio Preparation
# Convert to MP3
ffmpeg -i input.wav -codec:a libmp3lame -b:a 192k output.mp3

# Trim audio
ffmpeg -i input.mp3 -ss 00:00:05 -t 00:00:10 -c copy trimmed.mp3

# Adjust volume
ffmpeg -i input.mp3 -filter:a "volume=1.5" louder.mp3

# Fade in/out
ffmpeg -i input.mp3 -af "afade=t=in:st=0:d=2,afade=t=out:st=28:d=2" faded.mp3

Import Code Generation
Images

Spec requirement: "Logo.png (800x800)"

Generated code:

import { Img, staticFile } from 'remotion';

// In component
<Img
  src={staticFile('logo.png')}
  alt="Logo"
  style={{
    width: 400,
    height: 400,
  }}
/>

Videos

Spec requirement: "Background video (1920x1080, 30fps)"

Generated code:

import { Video, staticFile } from 'remotion';

<Video
  src={staticFile('background-video.mp4')}
  style={{
    position: 'absolute',
    top: 0,
    left: 0,
    width: '100%',
    height: '100%',
    objectFit: 'cover',
  }}
/>

Audio

Spec requirement: "Background music (full duration)"

Generated code:

import { Audio, staticFile, useVideoConfig } from 'remotion';

// In component
const { durationInFrames } = useVideoConfig();

<Audio
  src={staticFile('background-music.mp3')}
  volume={0.5}
  startFrom={0}
  endAt={durationInFrames}
/>

Fonts

Spec requirement: "Inter font (400, 600, 700)"

Generated code:

import { loadFont } from '@remotion/google-fonts/Inter';

const { fontFamily } = loadFont({
  weights: ['400', '600', '700'],
});

// In component
<div style={{
  fontFamily,
  fontWeight: 700,
}}>
  Text content
</div>

Asset Organization
Directory Structure
project/
├── public/
│   ├── images/
│   │   ├── logo.png
│   │   ├── product.jpg
│   │   └── background.webp
│   ├── videos/
│   │   ├── intro.mp4
│   │   └── demo.mp4
│   ├── audio/
│   │   ├── music/
│   │   │   └── background.mp3
│   │   └── sfx/
│   │       ├── whoosh.mp3
│   │       ├── pop.mp3
│   │       └── ding.mp3
│   └── fonts/
│       └── CustomFont.woff2
└── src/
    └── remotion/
        └── compositions/

Naming Conventions
// Good naming
logo.png              // Clear, simple
product-hero.jpg      // Descriptive
background-gradient.webp
whoosh-transition.mp3
background-music.mp3

// Bad naming
IMG_1234.jpg         // Not descriptive
final-FINAL-v2.png   // Confusing versions
my image.png         // Spaces (use hyphens)

Quality Validation Checklist

Before using assets in production:

Images:

 Correct dimensions (2x for retina if needed)
 Appropriate format (PNG for transparency, JPEG for photos)
 Optimized file size (< 500KB ideal, < 1MB maximum)
 No artifacts or compression issues
 Transparent background if required

Videos:

 Correct resolution (matches composition)
 Correct frame rate (matches composition)
 Appropriate codec (H.264)
 Reasonable file size (< 50MB ideal)
 No dropped frames
 Audio included if needed

Audio:

 Correct format (MP3 or WAV)
 Appropriate bitrate (192-320 kbps)
 Trimmed to exact duration
 Normalized volume levels
 No clipping or distortion
 Fade in/out applied if needed

Fonts:

 Legal license for commercial use
 All required weights available
 Proper format (WOFF2 preferred)
 Loaded correctly in composition
Integration with Other Skills

Works with:

/motion-designer — Extracts asset requirements from specs
/remotion-spec-translator — Generates asset import code during translation
/remotion-video-reviewer — Validates asset quality during review
Rules Directory

For detailed asset guidance:

rules/image-assets.md — Image preparation and optimization
rules/video-assets.md — Video encoding and preparation
rules/audio-assets.md — Audio processing and integration
rules/font-assets.md — Font loading and management

This skill ensures all assets are properly sourced, prepared, and integrated for production-ready Remotion videos.

Weekly Installs
84
Repository
ncklrs/startup-os-skills
GitHub Stars
18
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass