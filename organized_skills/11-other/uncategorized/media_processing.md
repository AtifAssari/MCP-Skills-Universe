---
rating: ⭐⭐⭐
title: media-processing
url: https://skills.sh/mrgoonie/claudekit-skills/media-processing
---

# media-processing

skills/mrgoonie/claudekit-skills/media-processing
media-processing
Installation
$ npx skills add https://github.com/mrgoonie/claudekit-skills --skill media-processing
SKILL.md
Media Processing Skill

Process video, audio, and images using FFmpeg and ImageMagick command-line tools for conversion, optimization, streaming, and manipulation tasks.

When to Use This Skill

Use when:

Converting media formats (video, audio, images)
Encoding video with codecs (H.264, H.265, VP9, AV1)
Processing images (resize, crop, effects, watermarks)
Extracting audio from video
Creating streaming manifests (HLS/DASH)
Generating thumbnails and previews
Batch processing media files
Optimizing file sizes and quality
Applying filters and effects
Creating composite images or videos
Tool Selection Guide
FFmpeg: Video/Audio Processing

Use FFmpeg for:

Video encoding, conversion, transcoding
Audio extraction, conversion, mixing
Live streaming (RTMP, HLS, DASH)
Video filters (scale, crop, rotate, overlay)
Hardware-accelerated encoding
Media file inspection (ffprobe)
Frame extraction, concatenation
Codec selection and optimization
ImageMagick: Image Processing

Use ImageMagick for:

Image format conversion (PNG, JPEG, WebP, GIF)
Resizing, cropping, transformations
Batch image processing (mogrify)
Visual effects (blur, sharpen, sepia)
Text overlays and watermarks
Image composition and montages
Color adjustments, filters
Thumbnail generation
Decision Matrix
Task	Tool	Why
Video encoding	FFmpeg	Native video codec support
Audio extraction	FFmpeg	Direct stream manipulation
Image resize	ImageMagick	Optimized for still images
Batch images	ImageMagick	mogrify for in-place edits
Video thumbnails	FFmpeg	Frame extraction built-in
GIF creation	FFmpeg or ImageMagick	FFmpeg for video source, ImageMagick for images
Streaming	FFmpeg	Live streaming protocols
Image effects	ImageMagick	Rich filter library
Installation
macOS
brew install ffmpeg imagemagick

Ubuntu/Debian
sudo apt-get install ffmpeg imagemagick

Windows
# Using winget
winget install ffmpeg
winget install ImageMagick.ImageMagick

# Or download binaries
# FFmpeg: https://ffmpeg.org/download.html
# ImageMagick: https://imagemagick.org/script/download.php

Verify Installation
ffmpeg -version
ffprobe -version
magick -version
# or
convert -version

Quick Start Examples
Video Conversion
# Convert format (copy streams, fast)
ffmpeg -i input.mkv -c copy output.mp4

# Re-encode with H.264
ffmpeg -i input.avi -c:v libx264 -crf 22 -c:a aac output.mp4

# Resize video to 720p
ffmpeg -i input.mp4 -vf scale=-1:720 -c:a copy output.mp4

Audio Extraction
# Extract audio (no re-encoding)
ffmpeg -i video.mp4 -vn -c:a copy audio.m4a

# Convert to MP3
ffmpeg -i video.mp4 -vn -q:a 0 audio.mp3

Image Processing
# Convert format
magick input.png output.jpg

# Resize maintaining aspect ratio
magick input.jpg -resize 800x600 output.jpg

# Create square thumbnail
magick input.jpg -resize 200x200^ -gravity center -extent 200x200 thumb.jpg

Batch Image Resize
# Resize all JPEGs to 800px width
mogrify -resize 800x -quality 85 *.jpg

# Output to separate directory
mogrify -path ./output -resize 800x600 *.jpg

Video Thumbnail
# Extract frame at 5 seconds
ffmpeg -ss 00:00:05 -i video.mp4 -vframes 1 -vf scale=320:-1 thumb.jpg

HLS Streaming
# Generate HLS playlist
ffmpeg -i input.mp4 \
  -c:v libx264 -preset fast -crf 22 -g 48 \
  -c:a aac -b:a 128k \
  -f hls -hls_time 6 -hls_playlist_type vod \
  playlist.m3u8

Image Watermark
# Add watermark to corner
magick input.jpg watermark.png -gravity southeast \
  -geometry +10+10 -composite output.jpg

Common Workflows
Optimize Video for Web
# H.264 with good compression
ffmpeg -i input.mp4 \
  -c:v libx264 -preset slow -crf 23 \
  -c:a aac -b:a 128k \
  -movflags +faststart \
  output.mp4

Create Responsive Images
# Generate multiple sizes
for size in 320 640 1024 1920; do
  magick input.jpg -resize ${size}x -quality 85 "output-${size}w.jpg"
done

Extract Video Segment
# From 1:30 to 3:00 (re-encode for precision)
ffmpeg -i input.mp4 -ss 00:01:30 -to 00:03:00 \
  -c:v libx264 -c:a aac output.mp4

Batch Image Optimization
# Convert PNG to optimized JPEG
mogrify -path ./optimized -format jpg -quality 85 -strip *.png

Video GIF Creation
# High quality GIF with palette
ffmpeg -i input.mp4 -vf "fps=15,scale=640:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" output.gif

Image Blur Effect
# Gaussian blur
magick input.jpg -gaussian-blur 0x8 output.jpg

Advanced Techniques
Multi-Pass Video Encoding
# Pass 1 (analysis)
ffmpeg -y -i input.mkv -c:v libx264 -b:v 2600k -pass 1 -an -f null /dev/null

# Pass 2 (encoding)
ffmpeg -i input.mkv -c:v libx264 -b:v 2600k -pass 2 -c:a aac output.mp4

Hardware-Accelerated Encoding
# NVIDIA NVENC
ffmpeg -hwaccel cuda -i input.mp4 -c:v h264_nvenc -preset fast -crf 22 output.mp4

# Intel QuickSync
ffmpeg -hwaccel qsv -c:v h264_qsv -i input.mp4 -c:v h264_qsv output.mp4

Complex Image Pipeline
# Resize, crop, border, adjust
magick input.jpg \
  -resize 1000x1000^ \
  -gravity center \
  -crop 1000x1000+0+0 +repage \
  -bordercolor black -border 5x5 \
  -brightness-contrast 5x10 \
  -quality 90 \
  output.jpg

Video Filter Chains
# Scale, denoise, watermark
ffmpeg -i video.mp4 -i logo.png \
  -filter_complex "[0:v]scale=1280:720,hqdn3d[v];[v][1:v]overlay=10:10" \
  -c:a copy output.mp4

Animated GIF from Images
# Create with delay
magick -delay 100 -loop 0 frame*.png animated.gif

# Optimize size
magick animated.gif -fuzz 5% -layers Optimize optimized.gif

Media Analysis
Inspect Video Properties
# Detailed JSON output
ffprobe -v quiet -print_format json -show_format -show_streams input.mp4

# Get resolution
ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height \
  -of csv=s=x:p=0 input.mp4

Image Information
# Basic info
identify image.jpg

# Detailed format
identify -verbose image.jpg

# Custom format
identify -format "%f: %wx%h %b\n" image.jpg

Performance Tips
Use CRF for quality control - Better than bitrate for video
Copy streams when possible - Avoid re-encoding with -c copy
Hardware acceleration - GPU encoding 5-10x faster
Appropriate presets - Balance speed vs compression
Batch with mogrify - In-place image processing
Strip metadata - Reduce file size with -strip
Progressive JPEG - Better web loading with -interlace Plane
Limit memory - Prevent crashes on large batches
Test on samples - Verify settings before batch
Parallel processing - Use GNU Parallel for multiple files
Reference Documentation

Detailed guides in references/:

ffmpeg-encoding.md - Video/audio codecs, quality optimization, hardware acceleration
ffmpeg-streaming.md - HLS/DASH, live streaming, adaptive bitrate
ffmpeg-filters.md - Video/audio filters, complex filtergraphs
imagemagick-editing.md - Format conversion, effects, transformations
imagemagick-batch.md - Batch processing, mogrify, parallel operations
format-compatibility.md - Format support, codec recommendations
Common Parameters
FFmpeg Video
-c:v - Video codec (libx264, libx265, libvpx-vp9)
-crf - Quality (0-51, lower=better, 23=default)
-preset - Speed/compression (ultrafast to veryslow)
-b:v - Video bitrate (e.g., 2M, 2500k)
-vf - Video filters
FFmpeg Audio
-c:a - Audio codec (aac, mp3, opus)
-b:a - Audio bitrate (e.g., 128k, 192k)
-ar - Sample rate (44100, 48000)
ImageMagick Geometry
800x600 - Fit within (maintains aspect)
800x600! - Force exact size
800x600^ - Fill (may crop)
800x - Width only
x600 - Height only
50% - Scale percentage
Troubleshooting

FFmpeg "Unknown encoder"

# Check available encoders
ffmpeg -encoders | grep h264

# Install codec libraries
sudo apt-get install libx264-dev libx265-dev


ImageMagick "not authorized"

# Edit policy file
sudo nano /etc/ImageMagick-7/policy.xml
# Change <policy domain="coder" rights="none" pattern="PDF" />
# to <policy domain="coder" rights="read|write" pattern="PDF" />


Memory errors

# Limit memory usage
ffmpeg -threads 4 input.mp4 output.mp4
magick -limit memory 2GB -limit map 4GB input.jpg output.jpg

Resources
FFmpeg: https://ffmpeg.org/documentation.html
FFmpeg Wiki: https://trac.ffmpeg.org/
ImageMagick: https://imagemagick.org/
ImageMagick Usage: https://imagemagick.org/Usage/
Weekly Installs
376
Repository
mrgoonie/claude…t-skills
GitHub Stars
2.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn