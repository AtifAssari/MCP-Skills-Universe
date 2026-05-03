---
title: image editing
url: https://skills.sh/ljt-520/openclaw-backup/image-editing
---

# image editing

skills/ljt-520/openclaw-backup/Image Editing
Image Editing
Installation
$ npx skills add https://github.com/ljt-520/openclaw-backup --skill 'Image Editing'
SKILL.md
AI Image Editing

Help users edit and enhance images with AI tools.

Rules:

Ask what edit they need: remove objects, extend canvas, upscale, fix faces, change background
Check technique files: inpainting.md, outpainting.md, background-removal.md, upscaling.md, restoration.md, style-transfer.md
Check tools.md for provider-specific setup
Always preserve original file before editing
Edit Type Selection
Task	Technique	Best Tools
Remove objects/people	Inpainting	DALL-E, SD Inpaint, IOPaint
Extend image borders	Outpainting	DALL-E, SD Outpaint, Photoshop AI
Remove background	Segmentation	remove.bg, ClipDrop, Photoroom
Increase resolution	Upscaling	Real-ESRGAN, Topaz, Magnific
Fix blurry faces	Restoration	GFPGAN, CodeFormer
Change style	Style Transfer	SD img2img, ControlNet
Relight scene	Relighting	ClipDrop, IC-Light
Workflow Principles
Non-destructive editing — keep originals, save edits as new files
Work in layers — combine multiple edits sequentially
Match resolution — edit at original resolution, upscale last
Mask precision matters — better masks = better results
Iterate on masks — refine edges for seamless blends
Masking Basics

Masks define edit regions:

White = edit this area
Black = preserve this area
Gray = partial blend (feathering)

Mask creation methods:

Manual brush in editor
SAM (Segment Anything) for auto-selection
Color/luminance keying
Edge detection
Common Workflows
Object Removal
Create mask over unwanted object
Run inpainting with context prompt (optional)
Blend edges if needed
Touch up artifacts
Background Replacement
Remove background (get transparent PNG)
Place on new background
Match lighting/color
Add shadows for realism
Enhancement Pipeline
Restore faces (if present)
Remove artifacts/noise
Color correct
Upscale to final resolution
Quality Tips
Feather masks — hard edges look artificial
Context prompts help — describe what should fill the area
Multiple passes — large edits may need iterative refinement
Check edges — zoom in to verify blend quality
Match grain/noise — add film grain to match original
Current Setup
Projects
Preferences

Check technique files for detailed workflows.

Weekly Installs
–
Repository
ljt-520/openclaw-backup
GitHub Stars
1
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass