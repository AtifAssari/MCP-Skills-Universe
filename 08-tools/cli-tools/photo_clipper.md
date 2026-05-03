---
title: photo-clipper
url: https://skills.sh/ppx123-web/claude-config/photo-clipper
---

# photo-clipper

skills/ppx123-web/claude-config/photo-clipper
photo-clipper
Installation
$ npx skills add https://github.com/ppx123-web/claude-config --skill photo-clipper
SKILL.md
Photo Clipper
When to Use

Use this skill when the user asks to:

Crop or trim a photo
Remove parts of an image (e.g., "remove 20% from top")
Focus on a specific subject or area
Improve composition (e.g., "apply rule of thirds")
Remove distractions from edges
Adjust framing or aspect ratio
Instructions

This skill uses GPT-5 vision API to analyze photos and suggest intelligent cropping. Always:

Validate input - Ensure photo exists and is JPG/PNG format
Call GPT-5 - Get clipping suggestions based on user's natural language prompt
Validate safety - Ensure clipping doesn't remove more than 50% per dimension
Apply clipping - Crop the photo and save to new file (never overwrite original)
Report results - Show what was removed and GPT-5's reasoning
Usage
from photo_clipper import main

result = main(
    photo_path="photo.jpg",
    prompt="Remove 20% from top to reduce empty sky"
)
# Returns: "photo-clipped.jpg"

Command Line
python photo_clipper.py <photo_path> "<prompt>" [output_path]

Examples

Remove empty sky:

Remove 30% from top to reduce empty sky


Focus on subject:

Crop to focus on the person's face in the center


Remove distractions:

Remove the partial tree on the left edge


Improve composition:

Apply rule of thirds to balance the composition


Trim specific amount:

Remove 10% from all edges for a cleaner frame

Output
Returns path to clipped photo
Never overwrites original
Format: {original_name}-clipped.{ext}
Displays GPT-5's confidence score and reasoning
Error Handling
Falls back to safe defaults (no clipping) if GPT-5 unavailable
Validates parameters (max 50% removal per dimension)
Clear error messages for missing files or invalid formats
Requirements
OPENROUTER_API_KEY environment variable must be set
Photo must be JPG or PNG format
Photo under 50MB recommended
Technical Implementation

See references/implementation.md for:

GPT-5 vision API integration
Cropping algorithm details
Error handling strategy
Performance optimization
Examples

See examples/common-use-cases.md for:

Remove empty sky
Focus on subject
Remove distractions
Improve composition
Error handling scenarios
Weekly Installs
15
Repository
ppx123-web/claude-config
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn