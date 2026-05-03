---
rating: ⭐⭐
title: nano-banana-build
url: https://skills.sh/cnemri/google-genai-skills/nano-banana-build
---

# nano-banana-build

skills/cnemri/google-genai-skills/nano-banana-build
nano-banana-build
Installation
$ npx skills add https://github.com/cnemri/google-genai-skills --skill nano-banana-build
SKILL.md
Nano Banana Image Generation Skill

Use this skill to generate and edit images using the google-genai Python SDK with Gemini's specialized image models (Nano Banana).

Quick Start Setup
from google import genai
from google.genai import types
from PIL import Image
import io

client = genai.Client()

Reference Materials
Model Capabilities: Comparison of Gemini 2.5 vs 3 Pro, resolutions, and token costs.
Image Generation: Text-to-Image, Interleaved Text/Image.
Image Editing: Subject Customization, Style Transfer, Multi-turn Editing.
Thinking Process: Understanding thoughts and signatures (Gemini 3 Pro).
Recipes: Extensive collection of examples (Logos, Stickers, Mockups, Comics, etc.).
Source Code: Deep inspection of SDK internals.
Available Models
gemini-2.5-flash-image (Nano Banana): Fast, high-quality generation and editing. Best for most use cases.
gemini-3-pro-image-preview (Nano Banana Pro): Highest fidelity, supports 2K and 4K resolution, complex prompt adherence, and grounding.
Common Workflows
1. Fast Generation
response = client.models.generate_content(
    model='gemini-2.5-flash-image',
    contents='A cute robot eating a banana',
    config=types.GenerateContentConfig(
        response_modalities=['IMAGE']
    )
)

2. High-Quality Editing
response = client.models.generate_content(
    model='gemini-3-pro-image-preview',
    contents=[
        types.Part.from_uri(file_uri='gs://.../shoe.jpg', mime_type='image/jpeg'),
        "Change the color of the shoe to neon green."
    ],
    config=types.GenerateContentConfig(response_modalities=['IMAGE'])
)

Weekly Installs
46
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