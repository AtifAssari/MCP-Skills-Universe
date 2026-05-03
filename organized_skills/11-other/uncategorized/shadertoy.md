---
rating: ⭐⭐⭐
title: shadertoy
url: https://skills.sh/bfollington/terma/shadertoy
---

# shadertoy

skills/bfollington/terma/shadertoy
shadertoy
Installation
$ npx skills add https://github.com/bfollington/terma --skill shadertoy
Summary

Real-time GLSL fragment shader development for procedural graphics and visual effects.

Provides complete Shadertoy API reference including built-in inputs (iResolution, iTime, iMouse, iChannel0-3) and the mainImage entry point structure
Covers essential patterns: ray marching with distance fields, procedural color palettes, hash functions, 2D/3D rotations, domain repetition, and post-processing techniques
Includes multi-pass rendering workflows for temporal feedback and buffer composition, plus critical GLSL ES rules (no f suffix, no saturate(), protect pow/sqrt operations)
Offers debugging strategies, performance optimization tips, and a reference library of complex number math, noise functions, and blend modes
SKILL.md
Shadertoy Shader Development
Overview

Shadertoy is a platform for creating and sharing GLSL fragment shaders that run in the browser using WebGL. This skill provides comprehensive guidance for writing shaders including GLSL ES syntax, common patterns, mathematical techniques, and best practices specific to real-time procedural graphics.

When to Use This Skill

Activate this skill when:

Writing or editing .glsl shader files
Creating procedural graphics, generative art, or visual effects
Working with Shadertoy.com projects or WebGL fragment shaders
Implementing ray marching, distance fields, or procedural textures
Debugging shader code or optimizing shader performance
Need GLSL ES syntax reference or Shadertoy input variables
Core Concepts
Shader Entry Point

Every Shadertoy shader implements the mainImage function:

void mainImage(out vec4 fragColor, in vec2 fragCoord)
{
    // fragCoord: pixel coordinates (0 to iResolution.xy)
    // fragColor: output color (RGBA, typically alpha = 1.0)

    vec2 uv = fragCoord / iResolution.xy;
    fragColor = vec4(uv, 0.0, 1.0);
}

Shadertoy Built-in Inputs

Always available in shaders:

Type	Name	Description
vec3	iResolution	Viewport resolution (x, y, aspect ratio)
float	iTime	Current time in seconds (primary animation driver)
float	iTimeDelta	Time to render one frame
int	iFrame	Current frame number
vec4	iMouse	Mouse: xy = current position, zw = click position
sampler2D	iChannel0-iChannel3	Input textures/buffers
vec3	iChannelResolution[4]	Resolution of each input channel
vec4	iDate	Year, month, day, time in seconds (.xyzw)
Coordinate System Setup

Standard patterns for normalizing coordinates:

// Aspect-corrected UV centered at origin (-1 to 1, aspect-preserved)
vec2 uv = (fragCoord.xy - 0.5 * iResolution.xy) / min(iResolution.y, iResolution.x);

// Alternative compact form:
vec2 uv = (fragCoord * 2.0 - iResolution.xy) / min(iResolution.x, iResolution.y);

// Simple normalized (0 to 1)
vec2 uv = fragCoord / iResolution.xy;

Common Shader Patterns
1. Procedural Color Palettes

Use Inigo Quilez's cosine palette for smooth color gradients:

vec3 palette(float t, vec3 a, vec3 b, vec3 c, vec3 d) {
    return a + b * cos(6.28318 * (c * t + d));
}

// Example usage:
vec3 col = palette(
    t,
    vec3(0.5, 0.5, 0.5),    // base
    vec3(0.5, 0.5, 0.5),    // amplitude
    vec3(1.0, 1.0, 0.5),    // frequency
    vec3(0.8, 0.90, 0.30)   // phase
);

2. Hash Functions (Pseudo-Random)

Simple 2D hash for noise and randomness:

float hash21(vec2 p) {
    p = fract(p * vec2(234.34, 435.345));
    p += dot(p, p + 34.23);
    return fract(p.x * p.y);
}

3. Ray Marching

Standard pattern for 3D rendering via sphere tracing:

// Distance field function
float map(vec3 p) {
    return length(p) - 1.0;  // Sphere at origin, radius 1
}

// Normal calculation
vec3 calcNormal(vec3 p) {
    vec2 e = vec2(0.001, 0.0);
    return normalize(vec3(
        map(p + e.xyy) - map(p - e.xyy),
        map(p + e.yxy) - map(p - e.yxy),
        map(p + e.yyx) - map(p - e.yyx)
    ));
}

// Ray marching loop
vec3 render(vec3 ro, vec3 rd) {
    float t = 0.0;
    for (int i = 0; i < 100; i++) {
        vec3 p = ro + rd * t;
        float d = map(p);
        if (d < 0.001) {
            // Hit - calculate lighting
            vec3 n = calcNormal(p);
            return n * 0.5 + 0.5;  // Normal visualization
        }
        if (t > 10.0) break;
        t += d * 0.5;  // Step (0.5 factor for safety)
    }
    return vec3(0.0);  // Miss
}

4. Rotations

2D rotation:

mat2 rot2d(float a) {
    float c = cos(a), s = sin(a);
    return mat2(c, -s, s, c);
}
// Usage: p.xy *= rot2d(iTime);


3D axis-angle rotation (modifies in-place):

void rot(inout vec3 p, vec3 axis, float angle) {
    axis = normalize(axis);
    float s = sin(angle), c = cos(angle), oc = 1.0 - c;
    mat3 m = mat3(
        oc * axis.x * axis.x + c,           oc * axis.x * axis.y - axis.z * s,  oc * axis.z * axis.x + axis.y * s,
        oc * axis.x * axis.y + axis.z * s,  oc * axis.y * axis.y + c,           oc * axis.y * axis.z - axis.x * s,
        oc * axis.z * axis.x - axis.y * s,  oc * axis.y * axis.z + axis.x * s,  oc * axis.z * axis.z + c
    );
    p = m * p;
}

5. Domain Repetition and Folding

Create fractal-like structures:

vec3 foldRotate(vec3 p, float timeOffset) {
    for (int i = 0; i < 5; i++) {
        p = abs(p);  // Mirror fold
        rot(p, vec3(0.707, 0.707, 0.0), 0.785);
        p -= 0.5;    // Translate
    }
    return p;
}

6. Post-Processing

Vignette:

float vignette(vec2 uv) {
    uv *= 1.0 - uv.yx;
    return pow(uv.x * uv.y * 15.0, 0.25);
}


Film grain/dithering (reduces banding):

float dither = hash21(fragCoord + iTime) * 0.001;
finalCol += dither;


Gamma correction:

finalCol = pow(finalCol, vec3(0.45));  // ~1/2.2

Multi-Pass Rendering

For complex effects requiring temporal feedback or multiple rendering stages:

Buffer A (Computation):
void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec2 uv = fragCoord / iResolution.xy;
    // Generate or compute values
    fragColor = vec4(computedColor, 1.0);
}

Buffer B (Feedback/Blending):
#define BUFFER_A iChannel0
void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec2 uv = fragCoord / iResolution.xy;
    vec4 current = texture(BUFFER_A, uv);
    vec4 previous = texture(iChannel1, uv);  // Self-reference
    fragColor = mix(previous, current, 0.1);  // Temporal blend
}

Main (Final Output):
#define BUFFER_B iChannel1
void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    vec2 uv = fragCoord / iResolution.xy;
    fragColor = texture(BUFFER_B, uv);
}

Critical GLSL ES Rules

ALWAYS follow these rules to avoid compilation errors:

NO f suffix: Use 1.0 NOT 1.0f
NO saturate(): Use clamp(x, 0.0, 1.0) instead
Protect pow/sqrt: Wrap arguments: pow(max(x, 0.0), p), sqrt(abs(x))
Avoid division by zero: Check denominators or add epsilon
Initialize variables: Don't assume default values
Avoid name conflicts: Don't name functions like variables
NO interactive commands: Avoid find, grep - use Glob/Grep tools instead
Workflow Guide
Creating a New Shader
Set up coordinate system - Choose appropriate UV normalization
Define core effect - Implement main visual algorithm
Add animation - Use iTime for temporal variation
Apply color palette - Use cosine palette or custom scheme
Add post-processing - Vignette, dither, gamma correction
Optimize - Reduce iterations, use early exits, minimize branches
Common Tasks

Visualizing complex numbers:

Use the complex math functions in references/common-patterns.md
Plot with cx_log(), cx_pow(), or polynomial evaluation
Map complex results to color via palette

Ray marching 3D scenes:

Define distance field in map() function
Set up camera (ray origin ro, ray direction rd)
March using standard loop pattern
Calculate normals with tetrahedron method
Apply lighting and material properties

Creating noise/organic effects:

Use hash21() for random values
Implement fbm() (fractional Brownian motion) for natural variation
Combine with sin()/cos() for structured patterns
Apply domain warping for organic distortion

Multi-layer composition:

Render multiple passes with different parameters
Blend layers using mix() or custom blend modes
Add interference patterns by comparing layer differences
Use smoothstep() for soft transitions
Debugging Strategies

Visualize intermediate values:

fragColor = vec4(vec3(distanceField), 1.0);  // Show distance
fragColor = vec4(normal * 0.5 + 0.5, 1.0);   // Show normals
fragColor = vec4(fract(uv), 0.0, 1.0);       // Show UV tiling


Simplify progressively:

Comment out post-processing
Reduce iteration counts
Replace complex functions with simple placeholders
Check coordinate transformations step-by-step

Check for NaN/Inf:

Add guards: if (isnan(value) || isinf(value)) return vec3(1.0, 0.0, 0.0);
Validate divisions and roots
Performance Optimization
Fixed iteration counts - Avoid dynamic loops
Early exit conditions - Break when threshold met
Step multiplier tuning - Balance quality vs speed (0.5 to 1.0)
Minimize texture reads - Cache repeated lookups
Avoid conditionals - Use mix(), step(), smoothstep() instead of if
Reduce precision - Use mediump or lowp where appropriate (mobile)
Naming Conventions

Based on observed patterns in creative work:

Poetic/evocative names - "alien-water", "heavenly-wisp", "comprehension"
Technical descriptors - "complex-plot", "noise-circuits", "ray-marching-demo"
Compound phrases - "coming-apart-at-the-seams", "form-without-form"
Lowercase with hyphens - my-shader-name.glsl
Attribution and Forking

When forking or remixing shaders:

// Fork of "Original Name" by AuthorName. https://shadertoy.com/view/XxXxXx
// Date: YYYY-MM-DD
// License: Creative Commons (CC BY-NC-SA 4.0) [or other]

Resources
references/glsl-reference.md

Complete GLSL ES syntax reference including:

Built-in functions (trig, math, vectors, matrices, textures)
Shadertoy input variables specification
Type conversions and swizzling
Common pitfalls and corrections

Search with: Read /references/glsl-reference.md for complete language reference.

references/common-patterns.md

Comprehensive pattern library including:

Complex number mathematics (cx_mul, cx_div, cx_sin, cx_cos, cx_log, cx_pow)
Color palette functions (cosine palette, multi-layer palettes)
Hash functions (hash21, PCG hash)
Ray marching templates (render loop, normal calculation)
3D transformations (rotations, domain folding)
Distance fields (sphere, box, octahedron)
Noise functions (simplex, FBM)
Post-processing (vignette, blur, film grain, gamma)
Blend modes (soft light, hard light, vivid light)
Multi-pass rendering patterns

Search with: Grep "pattern" references/common-patterns.md for specific techniques.

references/example-compact-shader.glsl

Reference implementation showing:

Compact, algorithmic shader coding style
Efficient ray marching in minimal code
Advanced matrix operations and transformations
Creative Commons licensed example
Quick Reference
#define PI 3.1415926535897932384626433832795

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    // 1. Normalize coordinates
    vec2 uv = (fragCoord * 2.0 - iResolution.xy) / min(iResolution.x, iResolution.y);

    // 2. Compute effect
    float d = length(uv) - 0.5;  // Circle distance field
    vec3 col = vec3(smoothstep(0.01, 0.0, d));  // Sharp edge

    // 3. Animate with time
    col *= 0.5 + 0.5 * sin(iTime + uv.xyx * 3.0);

    // 4. Apply palette
    col = palette(col.x, vec3(0.5), vec3(0.5), vec3(1.0), vec3(0.0));

    // 5. Post-process
    col = pow(col, vec3(0.45));  // Gamma
    col *= vignette(fragCoord / iResolution.xy);

    // 6. Output
    fragColor = vec4(col, 1.0);
}

Common Shader Types in Collection
Mathematical Visualizations - Complex number plots, function graphs
Ray Marched 3D - Distance field rendering, folded geometries
Procedural Textures - Noise-based patterns, organic effects
Multi-Pass Effects - Temporal feedback, buffer composition
Particle Systems - Point-based simulations
2D Patterns - Geometric, kaleidoscopic, interference effects
Tips for Creative Coding
Start simple - Get basic structure working, then iterate
Use time creatively - sin(iTime), mod(iTime, period), smoothstep() transitions
Layer effects - Combine multiple techniques for richness
Embrace accidents - Bugs often lead to interesting visuals
Study references - Learn from existing shaders, understand techniques
Optimize later - Prioritize visual quality first, then performance
Weekly Installs
1.3K
Repository
bfollington/terma
GitHub Stars
44
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass