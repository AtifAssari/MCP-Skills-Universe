---
rating: ⭐⭐⭐
title: screenshot-compression
url: https://skills.sh/zc277584121/marketing-skills/screenshot-compression
---

# screenshot-compression

skills/zc277584121/marketing-skills/screenshot-compression
screenshot-compression
Installation
$ npx skills add https://github.com/zc277584121/marketing-skills --skill screenshot-compression
SKILL.md
Skill: Screenshot Compression

Compress screenshot images (PNG/JPEG) in place while keeping the original format. Uses pngquant for PNG and jpegoptim for JPEG — both are highly effective for screenshot content (UI elements, text, flat colors).

Prerequisites: pngquant and jpegoptim must be installed on the system. The script will not install them automatically — it checks for their presence and prints install instructions if missing.

When to Use

The user has screenshot files that are too large and wants to reduce file size without changing format. Common scenarios:

Preparing images for GitHub READMEs, blog posts, or documentation
Reducing image sizes before committing to a repository
Batch compressing a directory of screenshots
Why Keep Original Format (Not WebP)

WebP has better compression, but poor compatibility in some contexts:

Context	WebP Support
Browsers (Chrome/Firefox/Safari/Edge)	Yes
GitHub Issues/PRs	Yes
WeChat editor	No
Word / PowerPoint	No
Some forums/blog backends	Varies

Keeping PNG/JPEG ensures the compressed images work everywhere.

Default Workflow
python /path/to/skills/screenshot-compression/scripts/compress_screenshots.py <files-or-directories>


The script will:

Check that pngquant and jpegoptim are installed — if not, print install instructions and exit
Auto-detect file format by extension
Compress each file in place (overwrites the original)
Print per-file and total compression summary
Dependency Check

The script requires two system tools. If either is missing, it exits with install instructions instead of proceeding. Do not install them on behalf of the user — just relay the error message so the user can install them.

Install commands:

# macOS
brew install pngquant jpegoptim

# Ubuntu / Debian
sudo apt install pngquant jpegoptim

# CentOS / RHEL
sudo yum install pngquant jpegoptim

Script Options
Flag	Default	Description
paths (positional)	required	Image files or directories to compress
-r, --recursive	off	Recursively process directories
--png-quality	80-95	pngquant quality range (min-max, 0-100)
--jpeg-quality	85	jpegoptim max quality (0-100)
Examples
# Compress a single file
python .../compress_screenshots.py screenshot.png

# Compress all images in a directory
python .../compress_screenshots.py ./images/

# Recursive directory scan
python .../compress_screenshots.py ./docs/ --recursive

# High quality for code screenshots
python .../compress_screenshots.py *.png --png-quality 90-100

# Aggressive compression for thumbnails
python .../compress_screenshots.py *.jpg --jpeg-quality 70

Quality Tuning Guide
Scenario	--png-quality	--jpeg-quality
General screenshots (docs, web pages)	80-95	85
Code screenshots (need sharp text)	90-100	90
Thumbnails / previews (size priority)	60-80	70
How It Works
PNG (pngquant)
Quantizes 24-bit true color (16M colors) down to an 8-bit palette (256 colors)
Uses Floyd-Steinberg dithering for smooth gradients
Screenshots are ideal candidates — UI colors are typically well under 256 unique values
Typical reduction: 60-80%
JPEG (jpegoptim)
Re-encodes at the specified quality level
Strips metadata (EXIF, ICC profiles, thumbnails) via --strip-all
Optimizes Huffman tables
Typical reduction: 20-50%
Important Notes
Files are compressed in place — the original is overwritten. Back up files first if needed.
Only .png, .jpg, and .jpeg files are processed. Other formats are silently skipped.
The script never installs dependencies. If tools are missing, it prints install instructions and exits.
Weekly Installs
476
Repository
zc277584121/mar…g-skills
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass