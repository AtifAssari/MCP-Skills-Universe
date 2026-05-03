---
title: openscad
url: https://skills.sh/mitsuhiko/agent-stuff/openscad
---

# openscad

skills/mitsuhiko/agent-stuff/openscad
openscad
Installation
$ npx skills add https://github.com/mitsuhiko/agent-stuff --skill openscad
SKILL.md
OpenSCAD Skill

Create, validate, and export OpenSCAD 3D models. Supports parameter customization, visual preview from multiple angles, and STL export for 3D printing platforms like MakerWorld.

Prerequisites

OpenSCAD must be installed. Install via Homebrew:

brew install openscad

Tools

This skill provides several tools in the tools/ directory:

Preview Generation
# Generate a single preview image
./tools/preview.sh model.scad output.png [--camera=x,y,z,tx,ty,tz,dist] [--size=800x600]

# Generate multi-angle preview (front, back, left, right, top, iso)
./tools/multi-preview.sh model.scad output_dir/

STL Export
# Export to STL for 3D printing
./tools/export-stl.sh model.scad output.stl [-D 'param=value']

Parameter Extraction
# Extract customizable parameters from an OpenSCAD file
./tools/extract-params.sh model.scad

Validation
# Check for syntax errors and warnings
./tools/validate.sh model.scad

Visual Validation (Required)

Always validate your OpenSCAD models visually after creating or modifying them.

After writing or editing any OpenSCAD file:

Generate multi-angle previews using multi-preview.sh
View each generated image using the read tool
Check for issues from multiple perspectives:
Front/back: Verify symmetry, features, and proportions
Left/right: Check depth and side profiles
Top: Ensure top features are correct
Isometric: Overall shape validation
Iterate if needed: If something looks wrong, fix the code and re-validate

This catches issues that syntax validation alone cannot detect:

Inverted normals or inside-out geometry
Misaligned features or incorrect boolean operations
Proportions that don't match the intended design
Missing or floating geometry
Z-fighting or overlapping surfaces

Never deliver an OpenSCAD model without visually confirming it looks correct from multiple angles.

Workflow
1. Creating an OpenSCAD Model

Write OpenSCAD code with customizable parameters at the top:

// Customizable parameters
wall_thickness = 2;        // [1:0.5:5] Wall thickness in mm
width = 50;                // [20:100] Width in mm
height = 30;               // [10:80] Height in mm
rounded = true;            // Add rounded corners

// Model code below
module main_shape() {
    if (rounded) {
        minkowski() {
            cube([width - 4, width - 4, height - 2]);
            sphere(r = 2);
        }
    } else {
        cube([width, width, height]);
    }
}

difference() {
    main_shape();
    translate([wall_thickness, wall_thickness, wall_thickness])
        scale([1 - 2*wall_thickness/width, 1 - 2*wall_thickness/width, 1])
        main_shape();
}


Parameter comment format:

// [min:max] - numeric range
// [min:step:max] - numeric range with step
// [opt1, opt2, opt3] - dropdown options
// Description text - plain description
2. Validate the Model
./tools/validate.sh model.scad

3. Generate Previews

Generate preview images to visually validate the model:

./tools/multi-preview.sh model.scad ./previews/


This creates PNG images from multiple angles. Use the read tool to view them.

4. Export to STL
./tools/export-stl.sh model.scad output.stl
# With custom parameters:
./tools/export-stl.sh model.scad output.stl -D 'width=60' -D 'height=40'

Camera Positions

Common camera angles for previews:

Isometric: --camera=0,0,0,45,0,45,200
Front: --camera=0,0,0,90,0,0,200
Top: --camera=0,0,0,0,0,0,200
Right: --camera=0,0,0,90,0,90,200

Format: x,y,z,rotx,roty,rotz,distance

MakerWorld Publishing

For MakerWorld, you typically need:

STL file(s) exported via export-stl.sh
Preview images (at least one good isometric view)
A description of customizable parameters

Consider creating a model.json with metadata:

{
  "name": "Model Name",
  "description": "Description for MakerWorld",
  "parameters": [...],
  "tags": ["functional", "container", "organizer"]
}

Example: Full Workflow
# 1. Create the model (write .scad file)

# 2. Validate syntax
./tools/validate.sh box.scad

# 3. Generate multi-angle previews
./tools/multi-preview.sh box.scad ./previews/

# 4. IMPORTANT: View and validate ALL preview images
#    Use the read tool on each PNG file to visually inspect:
#    - previews/box_front.png
#    - previews/box_back.png
#    - previews/box_left.png
#    - previews/box_right.png
#    - previews/box_top.png
#    - previews/box_iso.png
#    Look for geometry issues, misalignments, or unexpected results.
#    If anything looks wrong, go back to step 1 and fix it!

# 5. Extract and review parameters
./tools/extract-params.sh box.scad

# 6. Export STL with default parameters
./tools/export-stl.sh box.scad box.stl

# 7. Export STL with custom parameters
./tools/export-stl.sh box.scad box_large.stl -D 'width=80' -D 'height=60'


Remember: Never skip the visual validation step. Many issues (wrong dimensions, boolean operation errors, inverted geometry) are only visible when you actually look at the rendered model.

OpenSCAD Quick Reference
Basic Shapes
cube([x, y, z]);
sphere(r = radius);
cylinder(h = height, r = radius);
cylinder(h = height, r1 = bottom_r, r2 = top_r);  // cone

Transformations
translate([x, y, z]) object();
rotate([rx, ry, rz]) object();
scale([sx, sy, sz]) object();
mirror([x, y, z]) object();

Boolean Operations
union() { a(); b(); }        // combine
difference() { a(); b(); }   // subtract b from a
intersection() { a(); b(); } // overlap only

Advanced
linear_extrude(height) 2d_shape();
rotate_extrude() 2d_shape();
hull() { objects(); }        // convex hull
minkowski() { a(); b(); }    // minkowski sum (rounding)

2D Shapes
circle(r = radius);
square([x, y]);
polygon(points = [[x1,y1], [x2,y2], ...]);
text("string", size = 10);

Weekly Installs
302
Repository
mitsuhiko/agent-stuff
GitHub Stars
2.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass