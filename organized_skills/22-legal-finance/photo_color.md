---
rating: ⭐⭐
title: photo-color
url: https://skills.sh/ppx123-web/claude-config/photo-color
---

# photo-color

skills/ppx123-web/claude-config/photo-color
photo-color
Installation
$ npx skills add https://github.com/ppx123-web/claude-config --skill photo-color
SKILL.md
Photo Color
When to Use

Use this skill when the user asks to:

Adjust brightness (e.g., "make it brighter", "darken the photo")
Change contrast (e.g., "increase contrast", "make it more dramatic")
Modify saturation (e.g., "make colors more vibrant", "desaturate")
Apply a specific style (e.g., "cinematic look", "natural enhancement")
Fix photo issues (e.g., "fix washed out colors", "add warmth")
Instructions

This skill uses GPT-5 text API to interpret natural language and calculate color adjustments. Always:

Validate input - Ensure photo exists and is JPG/PNG format
Analyze photo - Calculate current brightness, contrast, saturation scores
Call GPT-5 - Get enhancement suggestions based on user's prompt and photo analysis
Select best match - Choose suggestion that best matches prompt keywords (vivid/natural/dramatic)
Apply enhancements - Adjust colors and save to new file (never overwrite original)
Report results - Show multipliers applied and GPT-5's reasoning
Usage
from photo_color import main

result = main(
    photo_path="photo.jpg",
    prompt="Make the colors more vibrant and warm"
)
# Returns: "photo-enhanced.jpg"

Command Line
python photo_color.py <photo_path> "<prompt>" [output_path]

Examples

Vivid colors:

Make the colors much more vibrant and vivid
Increase saturation by 50%
Make colors pop


Natural enhancement:

Apply a subtle natural enhancement
Keep it looking natural and soft


Cinematic/dramatic:

Create a dramatic cinematic look with high contrast
Make it bold and intense


Fix issues:

Fix the washed out appearance
Increase saturation to make colors more realistic
Add warmth to the photo


Specific adjustments:

Brighten and increase contrast
Make it darker and more moody

Output
Returns path to enhanced photo
Never overwrites original
Format: {original_name}-enhanced.{ext}
Multipliers in safe range (0.5-2.0)
Displays style name and GPT-5's reasoning
Enhancement Styles

GPT-5 suggests these style categories:

Vivid: High saturation (1.3-1.5), increased brightness and contrast
Natural: Subtle adjustments (1.05-1.2), minimal changes
Dramatic: High contrast (1.5-1.8), bold adjustments
Custom: Tailored to specific prompt requirements
Error Handling
Falls back to safe defaults (×1.2 saturation, ×1.1 brightness, ×1.1 contrast) if GPT-5 unavailable
Validates multipliers (0.5-2.0 range)
Clear error messages for missing files or invalid formats
Requirements
OPENROUTER_API_KEY environment variable must be set
Photo must be JPG or PNG format
Photo under 50MB recommended
Technical Implementation

See references/implementation.md for:

GPT-5 text API integration
Photo analysis algorithms
Color enhancement styles
Prompt matching strategy
Examples

See examples/common-use-cases.md for:

Vivid color enhancement
Natural subtle adjustment
Dramatic cinematic look
Fix washed out photos
Add warmth
Before/after comparisons
Weekly Installs
17
Repository
ppx123-web/claude-config
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass