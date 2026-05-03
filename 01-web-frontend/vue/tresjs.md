---
rating: ⭐⭐⭐
title: tresjs
url: https://skills.sh/onmax/nuxt-skills/tresjs
---

# tresjs

skills/onmax/nuxt-skills/tresjs
tresjs
Installation
$ npx skills add https://github.com/onmax/nuxt-skills --skill tresjs
Summary

Declarative Vue 3 framework for building 3D scenes with Three.js components.

TresCanvas root component wraps WebGL renderer; all Three.js classes available as Vue components with Tres prefix (e.g., TresMesh, TresPerspectiveCamera)
Core packages: @tresjs/core (required), @tresjs/cientos (OrbitControls, model loaders, materials), @tresjs/post-processing (bloom, glitch, depth-of-field effects)
Props are reactive; changes automatically update the 3D scene; use primitive component to inject existing Three.js objects
Composables include useTres (scene access), useLoop (animation frames), useGLTF (model loading), and useGraph (scene traversal)
SKILL.md
TresJS

Vue 3 framework for building 3D scenes with Three.js. Declarative components that wrap Three.js objects.

Packages: @tresjs/core (required), @tresjs/cientos (helpers), @tresjs/post-processing (effects)

Installation
# Core (required)
pnpm add three @tresjs/core

# Helpers - controls, loaders, materials, staging
pnpm add @tresjs/cientos

# Post-processing effects
pnpm add @tresjs/post-processing

Quick Reference
Working on...	Load file
TresCanvas, useTres, useLoop	references/core.md
Controls, loaders, materials	references/cientos.md
Bloom, glitch, DOF effects	references/effects.md
Common patterns, recipes	references/cookbook.md
Loading Files

Load based on your task:

 references/core.md - TresCanvas setup, composables, events, primitives
 references/cientos.md - OrbitControls, useGLTF, Environment, materials
 references/effects.md - EffectComposer, bloom, glitch, DOF
 references/cookbook.md - Load models, camera setup, animations

DO NOT load all files at once. Load only what's relevant.

Core Concepts
TresCanvas

Root component that creates WebGL renderer and scene:

<script setup lang="ts">
import { TresCanvas } from '@tresjs/core'
</script>

<template>
  <TresCanvas shadows alpha>
    <TresPerspectiveCamera :position="[5, 5, 5]" />
    <TresMesh>
      <TresBoxGeometry />
      <TresMeshStandardMaterial color="orange" />
    </TresMesh>
    <TresAmbientLight :intensity="0.5" />
    <TresDirectionalLight :position="[3, 3, 3]" :intensity="1" />
  </TresCanvas>
</template>

Component Naming

All Three.js classes available as Vue components with Tres prefix:

THREE.PerspectiveCamera → <TresPerspectiveCamera />
THREE.Mesh → <TresMesh />
THREE.BoxGeometry → <TresBoxGeometry />
THREE.MeshStandardMaterial → <TresMeshStandardMaterial />

Constructor arguments via :args prop:

<TresPerspectiveCamera :args="[75, 1, 0.1, 1000]" />

Reactivity

Props are reactive - changes update the 3D scene:

<script setup>
const color = ref('orange')
const position = ref([0, 0, 0])
</script>

<template>
  <TresMesh :position="position">
    <TresMeshStandardMaterial :color="color" />
  </TresMesh>
</template>

Primitive Component

Inject existing Three.js objects directly:

<script setup>
import { useGLTF } from '@tresjs/cientos'
const { scene } = await useGLTF('/model.glb')
</script>

<template>
  <primitive :object="scene" />
</template>

Available Guidance

references/core.md - TresCanvas props, useTres, useLoop, useGraph, events, performance

references/cientos.md - OrbitControls, useGLTF, useTexture, Environment, Sky, materials, shapes

references/effects.md - EffectComposer vs EffectComposerPmndrs, bloom, glitch, DOF, effect stacking

references/cookbook.md - Load 3D model, camera with controls, animation loop, post-processing

Weekly Installs
569
Repository
onmax/nuxt-skills
GitHub Stars
649
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass