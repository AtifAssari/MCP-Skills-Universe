---
rating: ⭐⭐
title: crop-tool
url: https://skills.sh/jdluther2020/ai-claude-code-talk/crop-tool
---

# crop-tool

skills/jdluther2020/ai-claude-code-talk/crop-tool
crop-tool
Installation
$ npx skills add https://github.com/jdluther2020/ai-claude-code-talk --skill crop-tool
SKILL.md
Crop Tool
When to Use
Reading small text, legends, or axis labels in charts
Extracting values from dense tables or diagrams
Any region where initial analysis feels uncertain
How to Use

Simply ask naturally about the image. Claude decides which regions to examine and handles the cropping automatically — no coordinates or technical input needed from the user.

"Read the values in the legend."
"What does the small text in the bottom section say?"
"Compare the metrics across all three columns."

Skill Mechanics

See Giving Claude a crop tool for better image analysis for a detailed understanding of the mechanics.

In addition to cropping, this skill enhances the extracted region further:

2x upscale — using LANCZOS resampling for maximum quality
1.4x contrast boost — makes text and edges pop
1.3x sharpness boost — reduces blur introduced by upscaling
How Claude Must Invoke the Tool

IMPORTANT: Always use the skill's crop_tool.py CLI via Bash — do NOT write your own PIL/image-processing code.

python3 /Users/jdl/.claude/skills/crop-tool/crop_tool.py \
  <image_path> <x1> <y1> <x2> <y2> [--output <out_path>]

Coordinates are normalized (0–1), where (0,0) is top-left and (1,1) is bottom-right
The script prints the output file path; read that file with the Read tool to view the cropped region
Iterate across regions as needed until the question is fully answered

Example:

python3 /Users/jdl/.claude/skills/crop-tool/crop_tool.py \
  chart.png 0.5 0.2 1.0 0.65 --output /tmp/legend_crop.png


For full documentation see README.md.

Weekly Installs
26
Repository
jdluther2020/ai…ode-talk
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass