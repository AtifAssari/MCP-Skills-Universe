---
rating: ⭐⭐⭐
title: manimgl-best-practices
url: https://skills.sh/adithya-s-k/manim_skill/manimgl-best-practices
---

# manimgl-best-practices

skills/adithya-s-k/manim_skill/manimgl-best-practices
manimgl-best-practices
Installation
$ npx skills add https://github.com/adithya-s-k/manim_skill --skill manimgl-best-practices
Summary

ManimGL best practices and patterns for 3Blue1Brown's OpenGL-based animation engine.

Covers InteractiveScene, Tex with LaTeX rendering, camera frame control, and 3D scene setup with lighting and surfaces
Interactive development workflow with -se flag for checkpoint-based iteration and self.embed() for debugging
Comprehensive rule files for animations, mobjects, text styling, colors, 3D rendering, and CLI configuration
Includes working examples and scene templates for basic 2D, mathematical visualizations, 3D scenes, and graph plotting
Key differences from Manim Community Edition: uses manimgl CLI, ShowCreation instead of Create, self.frame for camera control
SKILL.md
How to use

Read individual rule files for detailed explanations and code examples:

Core Concepts
rules/scenes.md - InteractiveScene, Scene types, and construct method
rules/mobjects.md - Mobject types, VMobject, Groups, and positioning
rules/animations.md - Animation classes, playing animations, and timing
Creation & Transformation
rules/creation-animations.md - ShowCreation, Write, FadeIn, DrawBorderThenFill
rules/transform-animations.md - Transform, ReplacementTransform, TransformMatchingTex
rules/animation-groups.md - LaggedStart, Succession, AnimationGroup
Text & Math
rules/tex.md - Tex class, raw strings R"...", and LaTeX rendering
rules/text.md - Text mobjects, fonts, and styling
rules/t2c.md - tex_to_color_map (t2c) for coloring math expressions
Styling & Appearance
rules/colors.md - Color constants, gradients, RGB, hex, GLSL coloring
rules/styling.md - Fill, stroke, opacity, backstroke, gloss, shadow
3D & Camera
rules/3d.md - 3D objects, surfaces, Sphere, Torus, parametric surfaces, lighting
rules/camera.md - frame.reorient(), Euler angles, fix_in_frame(), camera animations
Interactive Development
rules/interactive.md - Interactive mode with -se flag, checkpoint_paste()
rules/frame.md - self.frame, camera control, reorient, and zooming
rules/embedding.md - self.embed() for IPython debugging, touch() mode
Configuration & CLI
rules/cli.md - manimgl command, flags (-w, -o, -se, -l, -h), rendering options
rules/config.md - custom_config.yml, directories, camera settings, quality presets
Working Examples

Complete, tested example files demonstrating common patterns:

examples/basic_animations.py - Basic shapes, text, and animations
examples/math_visualization.py - LaTeX equations and mathematical content
examples/graph_plotting.py - Axes, functions, and graphing
examples/3d_visualization.py - 3D scenes with camera control and surfaces
examples/updater_patterns.py - Dynamic animations with updaters
Scene Templates

Copy and modify these templates to start new projects:

templates/basic_scene.py - Standard 2D scene template
templates/interactive_scene.py - InteractiveScene with self.embed()
templates/3d_scene.py - 3D scene with frame.reorient()
templates/math_scene.py - Mathematical derivations and equations
Quick Reference
Basic Scene Structure
from manimlib import *

class MyScene(InteractiveScene):
    def construct(self):
        # Create mobjects
        circle = Circle()

        # Add to scene (static)
        self.add(circle)

        # Or animate
        self.play(ShowCreation(circle))  # Note: ShowCreation, not Create

        # Wait
        self.wait(1)

Render Command
# Render and preview
manimgl scene.py MyScene

# Interactive mode - drop into shell at line 15
manimgl scene.py MyScene -se 15

# Write to file
manimgl scene.py MyScene -w

# Low quality for testing
manimgl scene.py MyScene -l

Key Differences from ManimCE
Feature	ManimGL (3b1b)	Manim Community
Import	from manimlib import *	from manim import *
CLI	manimgl	manim
Math text	Tex(R"\pi")	MathTex(r"\pi")
Scene	InteractiveScene	Scene
Create anim	ShowCreation	Create
Camera	self.frame	self.camera.frame
Fix in frame	mob.fix_in_frame()	self.add_fixed_in_frame_mobjects(mob)
Package	manimgl (PyPI)	manim (PyPI)
Interactive Development Workflow

ManimGL's killer feature is interactive development:

# Start at line 20 with state preserved
manimgl scene.py MyScene -se 20


In interactive mode:

# Copy code to clipboard, then run:
checkpoint_paste()           # Run with animations
checkpoint_paste(skip=True)  # Run instantly (no animations)
checkpoint_paste(record=True) # Record while running

Camera Control (self.frame)
# Get the camera frame
frame = self.frame

# Reorient in 3D (phi, theta, gamma, center, height)
frame.reorient(45, -30, 0, ORIGIN, 8)

# Animate camera movement
self.play(frame.animate.reorient(60, -45, 0))

# Fix mobjects to stay in screen space during 3D movement
title.fix_in_frame()

LaTeX with Tex class
# Use raw strings with capital R
formula = Tex(R"\int_0^1 x^2 \, dx = \frac{1}{3}")

# Color mapping with t2c
equation = Tex(
    R"E = mc^2",
    t2c={"E": BLUE, "m": GREEN, "c": YELLOW}
)

# Isolate substrings for animation
formula = Tex(R"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}")
formula.set_color_by_tex("n", BLUE)

Common Patterns
Embedding for debugging
def construct(self):
    circle = Circle()
    self.play(ShowCreation(circle))
    self.embed()  # Drops into IPython shell here

Set floor plane for 3D
self.set_floor_plane("xz")  # Makes xy the viewing plane

Backstroke for text readability
text = Text("Label")
text.set_backstroke(BLACK, 5)  # Black outline behind text

Installation
# Install ManimGL
pip install manimgl

# Check installation
manimgl --version

Common Pitfalls to Avoid
Version confusion - Ensure you're using manimgl, not manim (community version)
ShowCreation vs Create - ManimGL uses ShowCreation, not Create
Tex vs MathTex - ManimGL uses Tex with capital R raw strings
self.frame vs self.camera.frame - ManimGL uses self.frame directly
fix_in_frame() - Call on the mobject, not the scene
Interactive mode - Use -se flag for interactive development
License & Attribution

This skill contains example code adapted from 3Blue1Brown's video repository by Grant Sanderson.

License: CC BY-NC-SA 4.0

Attribution required - Credit both 3Blue1Brown and the adapter
NonCommercial - Not for commercial use
ShareAlike - Derivatives must use the same license

See LICENSE.txt for full details.

Weekly Installs
1.1K
Repository
adithya-s-k/manim_skill
GitHub Stars
825
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn