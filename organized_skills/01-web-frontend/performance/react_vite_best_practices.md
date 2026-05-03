---
rating: ⭐⭐
title: react-vite-best-practices
url: https://skills.sh/asyrafhussin/agent-skills/react-vite-best-practices
---

# react-vite-best-practices

skills/asyrafhussin/agent-skills/react-vite-best-practices
react-vite-best-practices
Installation
$ npx skills add https://github.com/asyrafhussin/agent-skills --skill react-vite-best-practices
Summary

23 performance optimization rules for React and Vite across build, code splitting, development, assets, environment, and bundle analysis.

Covers six rule categories prioritized by impact: build optimization and code splitting (critical), development and asset handling (high), environment config and bundle analysis (medium)
Includes route-based lazy loading with React.lazy() and Suspense, manual vendor chunk separation, and strategic prefetching patterns
Provides recommended vite.config.ts setup with modern browser targeting, sourcemap configuration, and dependency prebundling
Addresses asset optimization for images, SVGs as React components, web fonts, and environment variable management with VITE_ prefix convention
SKILL.md
React + Vite Best Practices

Comprehensive performance optimization guide for React applications built with Vite. Contains 23 rules across 6 categories for build optimization, code splitting, development performance, asset handling, environment configuration, and bundle analysis.

Metadata
Version: 2.0.0
Framework: React + Vite
Rule Count: 23 rules across 6 categories
License: MIT
When to Apply

Reference these guidelines when:

Configuring Vite for React projects
Implementing code splitting and lazy loading
Optimizing build output and bundle size
Setting up development environment and HMR
Handling images, fonts, SVGs, and static assets
Managing environment variables across environments
Analyzing bundle size and dependencies
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Build Optimization	CRITICAL	build-
2	Code Splitting	CRITICAL	split-
3	Development	HIGH	dev-
4	Asset Handling	HIGH	asset-
5	Environment Config	MEDIUM	env-
6	Bundle Analysis	MEDIUM	bundle-
Quick Reference
1. Build Optimization (CRITICAL)
build-manual-chunks - Configure manual chunks for vendor separation
build-minification - Minification with OXC (default) or Terser
build-target-modern - Target modern browsers (baseline-widely-available)
build-sourcemaps - Configure sourcemaps per environment
build-tree-shaking - Ensure proper tree shaking with ESM
build-compression - Gzip and Brotli compression
build-asset-hashing - Content-based hashing for cache busting
2. Code Splitting (CRITICAL)
split-route-lazy - Route-based splitting with React.lazy()
split-suspense-boundaries - Strategic Suspense boundary placement
split-dynamic-imports - Dynamic import() for heavy components
split-component-lazy - Lazy load non-critical components
split-prefetch-hints - Prefetch chunks on hover/idle/viewport
3. Development (HIGH)
dev-dependency-prebundling - Configure optimizeDeps for faster starts
dev-fast-refresh - React Fast Refresh patterns
dev-hmr-config - HMR server configuration
4. Asset Handling (HIGH)
asset-image-optimization - Image optimization and lazy loading
asset-svg-components - SVGs as React components with SVGR
asset-fonts - Web font loading strategy
asset-public-dir - Public directory vs JavaScript imports
5. Environment Config (MEDIUM)
env-vite-prefix - VITE_ prefix for client variables
env-modes - Mode-specific environment files
env-sensitive-data - Never expose secrets in client code
6. Bundle Analysis (MEDIUM)
bundle-visualizer - Analyze bundles with rollup-plugin-visualizer
Essential Configurations
Recommended vite.config.ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],

  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },

  build: {
    target: 'baseline-widely-available',
    sourcemap: false,
    chunkSizeWarningLimit: 500,
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
        },
      },
    },
  },

  optimizeDeps: {
    include: ['react', 'react-dom'],
  },

  server: {
    port: 3000,
    hmr: {
      overlay: true,
    },
  },
})

Route-Based Code Splitting
import { lazy, Suspense } from 'react'

const Home = lazy(() => import('./pages/Home'))
const Dashboard = lazy(() => import('./pages/Dashboard'))
const Settings = lazy(() => import('./pages/Settings'))

function App() {
  return (
    <Suspense fallback={<LoadingSpinner />}>
      {/* Routes here */}
    </Suspense>
  )
}

Environment Variables
// src/vite-env.d.ts
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_URL: string
  readonly VITE_APP_TITLE: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}

How to Use

Read individual rule files for detailed explanations and code examples:

rules/build-manual-chunks.md
rules/split-route-lazy.md
rules/env-vite-prefix.md

References
Vite Documentation
React Documentation
Rollup Documentation
Full Compiled Document

For the complete guide with all rules expanded: AGENTS.md

Weekly Installs
1.1K
Repository
asyrafhussin/ag…t-skills
GitHub Stars
34
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass