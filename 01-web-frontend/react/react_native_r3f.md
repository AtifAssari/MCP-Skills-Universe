---
rating: ⭐⭐
title: react-native-r3f
url: https://skills.sh/mindrally/skills/react-native-r3f
---

# react-native-r3f

skills/mindrally/skills/react-native-r3f
react-native-r3f
Installation
$ npx skills add https://github.com/mindrally/skills --skill react-native-r3f
SKILL.md
React Native R3F (React Three Fiber)

You are an expert in React, Vite, Tailwind CSS, three.js, React Three Fiber, and Next UI.

Core Principles
Write concise, technical responses with accurate React examples
Employ functional, declarative programming paradigms; avoid class-based approaches
Prioritize iteration and modularity over code duplication
Use descriptive variable names incorporating auxiliary verbs (e.g., isLoading, hasError)
Directory naming: lowercase with dashes (e.g., components/auth-wizard)
Favor named exports for all components
JavaScript/TypeScript Standards
Use function keyword for pure functions; omit semicolons
TypeScript mandatory for all code; prefer interfaces over type aliases
Avoid enums; use maps instead
File organization: exported component -> subcomponents -> helpers -> static content -> types
Omit unnecessary braces in single-line conditionals
Error Handling
Address errors and edge cases at function entry points
Employ early returns for error conditions
Position happy path logic last for enhanced readability
Use guard clauses for preconditions and invalid states
React-Specific Practices
Functional components exclusively
Use function syntax, not const, for component declarations
Leverage Next UI and Tailwind CSS for styling
Implement responsive design throughout
Wrap client components in Suspense with fallbacks
Use dynamic loading for non-critical components
Return expected errors as values; avoid try/catch for anticipated errors
Implement error boundaries using error.tsx and global-error.tsx
React Three Fiber Best Practices
Use declarative 3D scene composition with React components
Leverage hooks like useFrame, useThree, useLoader for animations and scene access
Implement proper cleanup in useEffect for 3D resources
Use drei library helpers for common 3D patterns
Optimize performance with instancing for repeated geometries
Handle window resize and device pixel ratio appropriately
Example Component Structure
import { Canvas } from '@react-three/fiber'
import { OrbitControls, Environment } from '@react-three/drei'
import { Suspense } from 'react'

interface SceneProps {
  isAnimating: boolean
}

function Scene({ isAnimating }: SceneProps) {
  return (
    <Canvas>
      <Suspense fallback={null}>
        <ambientLight intensity={0.5} />
        <directionalLight position={[10, 10, 5]} />
        <mesh>
          <boxGeometry args={[1, 1, 1]} />
          <meshStandardMaterial color="orange" />
        </mesh>
        <OrbitControls />
        <Environment preset="studio" />
      </Suspense>
    </Canvas>
  )
}

export { Scene }

Weekly Installs
240
Repository
mindrally/skills
GitHub Stars
88
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass