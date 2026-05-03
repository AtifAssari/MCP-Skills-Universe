---
rating: ⭐⭐
title: manim-video
url: https://skills.sh/affaan-m/everything-claude-code/manim-video
---

# manim-video

skills/affaan-m/everything-claude-code/manim-video
manim-video
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill manim-video
SKILL.md
Manim Video

Use Manim for technical explainers where motion, structure, and clarity matter more than photorealism.

When to Activate
the user wants a technical explainer animation
the concept is a graph, workflow, architecture, metric progression, or system diagram
the user wants a short product or launch explainer for X or a landing page
the visual should feel precise instead of generically cinematic
Tool Requirements
manim CLI for scene rendering
ffmpeg for post-processing if needed
video-editing for final assembly or polish
remotion-video-creation when the final package needs composited UI, captions, or additional motion layers
Default Output
short 16:9 MP4
one thumbnail or poster frame
storyboard plus scene plan
Workflow
Define the core visual thesis in one sentence.
Break the concept into 3 to 6 scenes.
Decide what each scene proves.
Write the scene outline before writing Manim code.
Render the smallest working version first.
Tighten typography, spacing, color, and pacing after the render works.
Hand off to the wider video stack only if it adds value.
Scene Planning Rules
each scene should prove one thing
avoid overstuffed diagrams
prefer progressive reveal over full-screen clutter
use motion to explain state change, not just to keep the screen busy
title cards should be short and loaded with meaning
Network Graph Default

For social-graph and network-optimization explainers:

show the current graph before showing the optimized graph
distinguish low-signal follow clutter from high-signal bridges
highlight warm-path nodes and target clusters
if useful, add a final scene showing the self-improvement lineage that informed the skill
Render Conventions
default to 16:9 landscape unless the user asks for vertical
start with a low-quality smoke test render
only push to higher quality after composition and timing are stable
export one clean thumbnail frame that reads at social size
Reusable Starter

Use assets/network_graph_scene.py as a starting point for network-graph explainers.

Example smoke test:

manim -ql assets/network_graph_scene.py NetworkGraphExplainer

Output Format

Return:

core visual thesis
storyboard
scene outline
render plan
any follow-on polish recommendations
Related Skills
video-editing for final polish
remotion-video-creation for motion-heavy post-processing or compositing
content-engine when the animation is part of a broader launch
Weekly Installs
1.5K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass