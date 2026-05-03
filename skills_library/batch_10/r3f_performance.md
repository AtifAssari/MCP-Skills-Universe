---
title: r3f-performance
url: https://skills.sh/bbeierle12/skill-mcp-claude/r3f-performance
---

# r3f-performance

skills/bbeierle12/skill-mcp-claude/r3f-performance
r3f-performance
Installation
$ npx skills add https://github.com/bbeierle12/skill-mcp-claude --skill r3f-performance
SKILL.md
R3F Performance

Optimize render performance through draw call reduction, geometry optimization, smart loading, and profiling.

Quick Start
// Performance-optimized Canvas
<Canvas
  dpr={[1, 2]}                    // Limit pixel ratio
  performance={{ min: 0.5 }}      // Adaptive performance
  frameloop="demand"              // Only render on change
  gl={{ 
    powerPreference: 'high-performance',
    antialias: false              // Disable for mobile
  }}
>
  <Suspense fallback={null}>
    <Scene />
  </Suspense>
</Canvas>

Frame Budget

Target 60fps = 16.67ms per frame. Budget breakdown:

Phase	Target	Notes
JavaScript	< 4ms	useFrame logic, state updates
GPU Render	< 10ms	Draw calls, shaders
Compositing	< 2ms	Post-processing, overlays
Buffer	~1ms	Safety margin
Draw Call Optimization
The Golden Rule

Fewer draw calls > fewer triangles

A scene with 100 meshes of 1000 triangles each is slower than 1 mesh of 100,000 triangles.

Reduction Techniques
Technique	Draw Calls	When to Use
Instancing	1 per unique mesh	100+ identical objects
Merged geometry	1 per merged batch	Static scene parts
Texture atlases	Fewer materials	Many similar textures
LOD	Reduces complexity	Large/distant objects
Instancing (Best for Identical Meshes)
// 10,000 cubes = 1 draw call
<instancedMesh args={[undefined, undefined, 10000]}>
  <boxGeometry />
  <meshStandardMaterial />
</instancedMesh>

Geometry Merging (Static Scenes)
import { useMemo } from 'react';
import { mergeGeometries } from 'three/examples/jsm/utils/BufferGeometryUtils';
import * as THREE from 'three';

function MergedScene() {
  const mergedGeometry = useMemo(() => {
    const geometries: THREE.BufferGeometry[] = [];
    
    // Create many positioned geometries
    for (let i = 0; i < 100; i++) {
      const geo = new THREE.BoxGeometry(1, 1, 1);
      geo.translate(
        (Math.random() - 0.5) * 20,
        (Math.random() - 0.5) * 20,
        (Math.random() - 0.5) * 20
      );
      geometries.push(geo);
    }
    
    return mergeGeometries(geometries);
  }, []);
  
  return (
    <mesh geometry={mergedGeometry}>
      <meshStandardMaterial />
    </mesh>
  );
}

Level of Detail (LOD)

Swap geometry based on camera distance:

import { useMemo } from 'react';
import * as THREE from 'three';

function LODMesh() {
  const lod = useMemo(() => {
    const lodObject = new THREE.LOD();
    
    // High detail (close)
    const highGeo = new THREE.SphereGeometry(1, 64, 64);
    const highMesh = new THREE.Mesh(highGeo, new THREE.MeshStandardMaterial({ color: 'red' }));
    lodObject.addLevel(highMesh, 0);
    
    // Medium detail
    const medGeo = new THREE.SphereGeometry(1, 32, 32);
    const medMesh = new THREE.Mesh(medGeo, new THREE.MeshStandardMaterial({ color: 'orange' }));
    lodObject.addLevel(medMesh, 10);
    
    // Low detail (far)
    const lowGeo = new THREE.SphereGeometry(1, 8, 8);
    const lowMesh = new THREE.Mesh(lowGeo, new THREE.MeshStandardMaterial({ color: 'green' }));
    lodObject.addLevel(lowMesh, 30);
    
    return lodObject;
  }, []);
  
  return <primitive object={lod} />;
}

Drei LOD Helper
import { Detailed } from '@react-three/drei';

function AdaptiveSphere() {
  return (
    <Detailed distances={[0, 10, 30]}>
      {/* Close: high detail */}
      <mesh>
        <sphereGeometry args={[1, 64, 64]} />
        <meshStandardMaterial />
      </mesh>
      
      {/* Medium distance */}
      <mesh>
        <sphereGeometry args={[1, 32, 32]} />
        <meshStandardMaterial />
      </mesh>
      
      {/* Far: low detail */}
      <mesh>
        <sphereGeometry args={[1, 8, 8]} />
        <meshStandardMaterial />
      </mesh>
    </Detailed>
  );
}

Frustum Culling

Objects outside camera view are not rendered. Enabled by default, but:

// Disable for objects that animate into view unpredictably
<mesh frustumCulled={false}>
  <boxGeometry />
  <meshStandardMaterial />
</mesh>

// Force bounding sphere update for dynamic geometry
useEffect(() => {
  geometry.computeBoundingSphere();
}, [geometry]);

Adaptive Performance

R3F's adaptive performance system automatically adjusts DPR:

<Canvas
  performance={{
    min: 0.5,     // Minimum DPR under stress
    max: 1,       // Maximum DPR
    debounce: 200 // Debounce time for changes (ms)
  }}
/>

Manual Performance Control
import { useThree } from '@react-three/fiber';

function PerformanceMonitor() {
  const { performance } = useThree();
  
  useFrame(() => {
    // Check current performance
    if (performance.current < 1) {
      // System is under stress, reduce complexity
    }
  });
  
  // Trigger performance drop
  const triggerRegress = () => {
    performance.regress();  // Temporarily lower DPR
  };
}

Lazy Loading
Code Splitting with Suspense
import { Suspense, lazy } from 'react';

const HeavyModel = lazy(() => import('./HeavyModel'));

function Scene() {
  return (
    <Suspense fallback={<SimpleLoader />}>
      <HeavyModel />
    </Suspense>
  );
}

Progressive Loading
import { useGLTF } from '@react-three/drei';

function Model() {
  // Preload in background
  useGLTF.preload('/model.glb');
  
  const { scene } = useGLTF('/model.glb');
  return <primitive object={scene} />;
}

// Preload before component mounts
useEffect(() => {
  useGLTF.preload('/next-model.glb');
}, []);

View-Based Loading
import { useInView } from 'react-intersection-observer';

function LazySection() {
  const { ref, inView } = useInView({
    triggerOnce: true,
    rootMargin: '200px'  // Start loading 200px before visible
  });
  
  return (
    <group ref={ref}>
      {inView && <HeavyContent />}
    </group>
  );
}

Memory Management
Dispose Unused Resources
// Manual disposal
useEffect(() => {
  return () => {
    geometry.dispose();
    material.dispose();
    texture.dispose();
  };
}, []);

// Drei helper for GLTF
import { useGLTF } from '@react-three/drei';

useEffect(() => {
  return () => {
    useGLTF.clear('/model.glb');
  };
}, []);

Texture Optimization
import { useTexture } from '@react-three/drei';
import * as THREE from 'three';

// Compress and optimize
const texture = useTexture('/texture.jpg', (tex) => {
  tex.minFilter = THREE.LinearMipmapLinearFilter;
  tex.generateMipmaps = true;
  tex.anisotropy = 4;  // Lower = faster, higher = sharper
});

// Use compressed formats (KTX2)
import { useKTX2 } from '@react-three/drei';
const texture = useKTX2('/texture.ktx2');

Profiling
Stats Panel
import { Stats } from '@react-three/drei';

<Canvas>
  <Stats />  {/* FPS, MS, MB counters */}
  <Scene />
</Canvas>

Performance Panel
import { Perf } from 'r3f-perf';

<Canvas>
  <Perf 
    position="top-left"
    showGraph          // Show FPS graph
    minimal={false}    // Full or minimal view
  />
  <Scene />
</Canvas>

Manual Profiling
import { useThree } from '@react-three/fiber';

function ProfileInfo() {
  const { gl } = useThree();
  
  useEffect(() => {
    const info = gl.info;
    console.log({
      drawCalls: info.render.calls,
      triangles: info.render.triangles,
      points: info.render.points,
      lines: info.render.lines,
      textures: info.memory.textures,
      geometries: info.memory.geometries
    });
  });
  
  return null;
}

Frame Time Measurement
function FrameProfiler() {
  const frameTimeRef = useRef<number[]>([]);
  
  useFrame(() => {
    const start = performance.now();
    
    // ... your logic ...
    
    const elapsed = performance.now() - start;
    frameTimeRef.current.push(elapsed);
    
    if (frameTimeRef.current.length > 60) {
      const avg = frameTimeRef.current.reduce((a, b) => a + b) / 60;
      console.log(`Avg frame time: ${avg.toFixed(2)}ms`);
      frameTimeRef.current = [];
    }
  });
  
  return null;
}

Common Bottlenecks
Symptom	Likely Cause	Fix
Low FPS, high draw calls	Too many meshes	Instance, merge, or LOD
Low FPS, few draw calls	Heavy shaders/materials	Simplify shaders, use cheaper materials
Stuttering on load	Large assets	Lazy load, compress, use LOD
Memory growth	No disposal	Dispose on unmount
Mobile issues	High DPR, AA	Limit DPR, disable antialias
Optimization Checklist
[ ] Draw calls < 100 for complex scenes
[ ] Instancing for repeated objects
[ ] LOD for large/distant objects
[ ] Geometry merged where possible
[ ] Textures compressed (KTX2/Basis)
[ ] DPR capped at 2
[ ] Lazy loading for heavy assets
[ ] Proper disposal on unmount
[ ] Frustum culling enabled
[ ] Shadows optimized or disabled

File Structure
r3f-performance/
├── SKILL.md
├── references/
│   ├── profiling-guide.md      # Deep profiling techniques
│   ├── mobile-optimization.md  # Mobile-specific tips
│   └── large-scenes.md         # Handling massive scenes
└── scripts/
    ├── utils/
    │   ├── lod-helper.ts       # LOD setup utilities
    │   ├── merge-helper.ts     # Geometry merging
    │   └── perf-monitor.ts     # Performance monitoring
    └── presets/
        ├── mobile.ts           # Mobile-optimized Canvas config
        └── desktop.ts          # Desktop-optimized Canvas config

Reference
references/profiling-guide.md — Deep profiling with browser DevTools
references/mobile-optimization.md — Mobile-specific optimization
references/large-scenes.md — Handling 100k+ object scenes
Weekly Installs
60
Repository
bbeierle12/skil…p-claude
GitHub Stars
8
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass