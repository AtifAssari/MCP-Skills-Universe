---
title: webgpu-threejs-tsl
url: https://skills.sh/dgreenheck/webgpu-claude-skill/webgpu-threejs-tsl
---

# webgpu-threejs-tsl

skills/dgreenheck/webgpu-claude-skill/webgpu-threejs-tsl
webgpu-threejs-tsl
Installation
$ npx skills add https://github.com/dgreenheck/webgpu-claude-skill --skill webgpu-threejs-tsl
SKILL.md
WebGPU Three.js with TSL

TSL (Three.js Shading Language) is a node-based shader abstraction that lets you write GPU shaders in JavaScript instead of GLSL/WGSL strings.

Quick Start
import * as THREE from 'three/webgpu';
import { color, time, oscSine } from 'three/tsl';

const renderer = new THREE.WebGPURenderer();
await renderer.init();

const material = new THREE.MeshStandardNodeMaterial();
material.colorNode = color(0xff0000).mul(oscSine(time));

Skill Contents
Documentation
docs/core-concepts.md - Types, operators, uniforms, control flow
docs/materials.md - Node materials and all properties
docs/compute-shaders.md - GPU compute with instanced arrays
docs/post-processing.md - Built-in and custom effects
docs/wgsl-integration.md - Custom WGSL functions
docs/device-loss.md - Handling GPU device loss and recovery
docs/limits-and-features.md - WebGPU device limits and optional features
Examples
examples/basic-setup.js - Minimal WebGPU project
examples/custom-material.js - Custom shader material
examples/particle-system.js - GPU compute particles
examples/post-processing.js - Effect pipeline
examples/earth-shader.js - Complete Earth with atmosphere
Templates
templates/webgpu-project.js - Starter project template
templates/compute-shader.js - Compute shader template
Reference
REFERENCE.md - Quick reference cheatsheet
Key Concepts
Import Pattern
// Always use the WebGPU entry point
import * as THREE from 'three/webgpu';
import { /* TSL functions */ } from 'three/tsl';

Node Materials

Replace standard material properties with TSL nodes:

material.colorNode = texture(map);        // instead of material.map
material.roughnessNode = float(0.5);      // instead of material.roughness
material.positionNode = displaced;         // vertex displacement

Method Chaining

TSL uses method chaining for operations:

// Instead of: sin(time * 2.0 + offset) * 0.5 + 0.5
time.mul(2.0).add(offset).sin().mul(0.5).add(0.5)

Custom Functions

Use Fn() for reusable shader logic:

const fresnel = Fn(([power = 2.0]) => {
  const nDotV = normalWorld.dot(viewDir).saturate();
  return float(1.0).sub(nDotV).pow(power);
});

When to Use This Skill
Setting up Three.js with WebGPU renderer
Creating custom shader materials with TSL
Writing GPU compute shaders
Building post-processing pipelines
Migrating from GLSL to TSL
Implementing visual effects (particles, water, terrain, etc.)
Resources
Three.js TSL Wiki
WebGPU Examples (files prefixed with webgpu_)
Weekly Installs
384
Repository
dgreenheck/webg…de-skill
GitHub Stars
864
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass