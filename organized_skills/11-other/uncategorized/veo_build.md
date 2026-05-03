---
rating: ⭐⭐
title: veo-build
url: https://skills.sh/cnemri/google-genai-skills/veo-build
---

# veo-build

skills/cnemri/google-genai-skills/veo-build
veo-build
Installation
$ npx skills add https://github.com/cnemri/google-genai-skills --skill veo-build
SKILL.md
Veo Video Generation and Editing

This skill provides comprehensive workflows for using Google's Veo models (Veo 2 and Veo 3) via the google-genai Python SDK.

Quick Start Setup

All Veo operations require the google-genai library and an authenticated client with Vertex AI enabled.

from google import genai
from google.genai import types
import os

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_REGION", "us-central1")

client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)

Reference Materials
Generation (Veo 3): Text-to-Video, Image-to-Video.
Editing (Veo 2): Inpainting, Masking.
Advanced Controls: Frame Interpolation, Video Extension, Reference Images.
Prompting Guide: Camera angles, visual styles, and best practices.
Source Code: Deep inspection of SDK internals (models.py, types.py).
Available Workflows
1. Video Generation (Veo 3)

Create new videos from text or image prompts.

Text-to-Video: Create videos from detailed text descriptions.
Image-to-Video: Animate static images.
Prompt Engineering: Optimization keywords for camera, lighting, and style.
2. Video Editing (Veo 2)

Modify existing videos using masks (Inpainting).

Remove Objects: Erase dynamic or static objects.
Insert Objects: Add new elements into a scene.
3. Advanced Controls (Veo 3)

Specialized generation tasks for precise control.

Frame Interpolation: Generate video bridging two images (first & last frame).
Video Extension: Extend the duration of an existing video clip.
Reference-to-Video: Use specific asset images (subjects, products) to guide generation.
Weekly Installs
60
Repository
cnemri/google-g…i-skills
GitHub Stars
119
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn