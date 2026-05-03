---
title: _svg-drawing
url: https://skills.sh/site/smithery.ai/_svg-drawing
---

# _svg-drawing

skills/smithery.ai/_svg-drawing
_svg-drawing
$ npx skills add https://smithery.ai/skills/possumworx/svg-drawing
SKILL.md
SVG Drawing Skill

Iterative workflow for creating vector artwork with visual feedback.

The Challenge

Creating SVG artwork by writing code is challenging without visual feedback during the design process. Writing coordinates and shapes blindly often requires guessing and hoping.

The Solution: render-svg Tool

Location: ~/claude-autonomy-platform/utils/render-svg

Converts SVG code to viewable PNG images for iterative design.

Usage:

render-svg <svg-file> [output-file]


Examples:

# Render to default filename
render-svg hedgehog.svg

# Specify custom output
render-svg logo.svg ~/creative/logo-preview.png

Iterative Design Workflow
Start Simple
# 1. Create initial SVG with basic shapes
# 2. Render immediately
render-svg design.svg

# 3. View with Read tool
# 4. Identify what needs adjustment

Refinement Loop
# 1. Edit SVG (adjust coordinates, colors, proportions)
# 2. Render again
render-svg design.svg

# 3. Compare with mental model
# 4. Repeat until satisfied

Version Comparison
# Save iterations to track progress
render-svg design.svg design-v1.png
# Make changes
render-svg design.svg design-v2.png
# Compare side by side

Design Tips

Build Progressively:

Start with basic shapes (circles, rectangles, ellipses)
Render after each major addition
Add complexity gradually

Coordinate Reference:

SVG viewBox defines canvas (e.g., "0 0 400 300")
Origin (0,0) is top-left
X increases right, Y increases down

Layer Workflow:

Background elements first
Build up layers progressively
Render frequently to verify positioning
Benefits
Visual Feedback: See what code creates
Faster Iteration: Spot issues immediately
Confidence: Verify appearance before sharing
Learning: Understand coordinate-to-visual mapping
Experimentation: Try ideas with immediate results

Built by Sparkle Orange & Amy, November 2025 Simple tool, iterate based on real use 🎨✨

Weekly Installs
57
Source
smithery.ai/ski…-drawing
First Seen
Mar 13, 2026