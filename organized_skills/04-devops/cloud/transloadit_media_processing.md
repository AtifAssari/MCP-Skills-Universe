---
rating: ⭐⭐
title: transloadit-media-processing
url: https://skills.sh/github/awesome-copilot/transloadit-media-processing
---

# transloadit-media-processing

skills/github/awesome-copilot/transloadit-media-processing
transloadit-media-processing
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill transloadit-media-processing
Summary

Cloud-based media processing for video, audio, images, and documents using 86+ specialized robots.

Supports video encoding (HLS, MP4, WebM), thumbnail generation, image resizing/watermarking, audio transcoding, document OCR, and speech-to-text via chainable processing steps
Access via MCP server (recommended for IDE integration) or CLI; requires free Transloadit account with API credentials
Build multi-step pipelines by chaining robot operations together using the "use" field; reuse pipelines as templates with dynamic variables
Includes preset configurations for common formats (HLS-1080p, MP3, WebP) and batch processing via HTTP import from URLs, S3, GCS, or other cloud storage
SKILL.md
Transloadit Media Processing

Process, transform, and encode media files using Transloadit's cloud infrastructure. Supports video, audio, images, and documents with 86+ specialized processing robots.

When to Use This Skill

Use this skill when you need to:

Encode video to HLS, MP4, WebM, or other formats
Generate thumbnails or animated GIFs from video
Resize, crop, watermark, or optimize images
Convert between image formats (JPEG, PNG, WebP, AVIF, HEIF)
Extract or transcode audio (MP3, AAC, FLAC, WAV)
Concatenate video or audio clips
Add subtitles or overlay text on video
OCR documents (PDF, scanned images)
Run speech-to-text or text-to-speech
Apply AI-based content moderation or object detection
Build multi-step media pipelines that chain operations together
Setup
Option A: MCP Server (recommended for Copilot)

Add the Transloadit MCP server to your IDE config. This gives the agent direct access to Transloadit tools (create_template, create_assembly, list_assembly_notifications, etc.).

VS Code / GitHub Copilot (.vscode/mcp.json or user settings):

{
  "servers": {
    "transloadit": {
      "command": "npx",
      "args": ["-y", "@transloadit/mcp-server", "stdio"],
      "env": {
        "TRANSLOADIT_KEY": "YOUR_AUTH_KEY",
        "TRANSLOADIT_SECRET": "YOUR_AUTH_SECRET"
      }
    }
  }
}


Get your API credentials at https://transloadit.com/c/-/api-credentials

Option B: CLI

If you prefer running commands directly:

npx -y @transloadit/node assemblies create \
  --steps '{"encoded": {"robot": "/video/encode", "use": ":original", "preset": "hls-1080p"}}' \
  --wait \
  --input ./my-video.mp4

Core Workflows
Encode Video to HLS (Adaptive Streaming)
{
  "steps": {
    "encoded": {
      "robot": "/video/encode",
      "use": ":original",
      "preset": "hls-1080p"
    }
  }
}

Generate Thumbnails from Video
{
  "steps": {
    "thumbnails": {
      "robot": "/video/thumbs",
      "use": ":original",
      "count": 8,
      "width": 320,
      "height": 240
    }
  }
}

Resize and Watermark Images
{
  "steps": {
    "resized": {
      "robot": "/image/resize",
      "use": ":original",
      "width": 1200,
      "height": 800,
      "resize_strategy": "fit"
    },
    "watermarked": {
      "robot": "/image/resize",
      "use": "resized",
      "watermark_url": "https://example.com/logo.png",
      "watermark_position": "bottom-right",
      "watermark_size": "15%"
    }
  }
}

OCR a Document
{
  "steps": {
    "recognized": {
      "robot": "/document/ocr",
      "use": ":original",
      "provider": "aws",
      "format": "text"
    }
  }
}

Concatenate Audio Clips
{
  "steps": {
    "imported": {
      "robot": "/http/import",
      "url": ["https://example.com/clip1.mp3", "https://example.com/clip2.mp3"]
    },
    "concatenated": {
      "robot": "/audio/concat",
      "use": "imported",
      "preset": "mp3"
    }
  }
}

Multi-Step Pipelines

Steps can be chained using the "use" field. Each step references a previous step's output:

{
  "steps": {
    "resized": {
      "robot": "/image/resize",
      "use": ":original",
      "width": 1920
    },
    "optimized": {
      "robot": "/image/optimize",
      "use": "resized"
    },
    "exported": {
      "robot": "/s3/store",
      "use": "optimized",
      "bucket": "my-bucket",
      "path": "processed/${file.name}"
    }
  }
}

Key Concepts
Assembly: A single processing job. Created via create_assembly (MCP) or assemblies create (CLI).
Template: A reusable set of steps stored on Transloadit. Created via create_template (MCP) or templates create (CLI).
Robot: A processing unit (e.g., /video/encode, /image/resize). See full list at https://transloadit.com/docs/transcoding/
Steps: JSON object defining the pipeline. Each key is a step name, each value configures a robot.
:original: Refers to the uploaded input file.
Tips
Use --wait with the CLI to block until processing completes.
Use preset values (e.g., "hls-1080p", "mp3", "webp") for common format targets instead of specifying every parameter.
Chain "use": "step_name" to build multi-step pipelines without intermediate downloads.
For batch processing, use /http/import to pull files from URLs, S3, GCS, Azure, FTP, or Dropbox.
Templates can include ${variables} for dynamic values passed at assembly creation time.
Weekly Installs
8.4K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn