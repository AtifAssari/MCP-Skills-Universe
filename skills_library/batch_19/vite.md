---
title: vite
url: https://skills.sh/dralgorhythm/claude-agentic-framework/vite
---

# vite

skills/dralgorhythm/claude-agentic-framework/vite
vite
Installation
$ npx skills add https://github.com/dralgorhythm/claude-agentic-framework --skill vite
SKILL.md
Vite

Platform: Web only. Mobile demos use Expo with Metro bundler. See the expo-sdk skill.

Use Context7 MCP (resolve-library-id then query-docs) for full API reference, plugin ecosystem, and advanced configuration options.

Overview

Build tool and development server for Vite 7.x. Provides instant server start, fast HMR, optimized production builds, and first-class TypeScript support.

Install: pnpm add -D vite

Workflows

Initial setup:

 Create vite.config.ts with TypeScript types
 Install React plugin: pnpm add -D @vitejs/plugin-react
 Configure path aliases for clean imports
 Set up environment variables with .env files
 Test dev server: pnpm vite

Production optimization:

 Configure code splitting and chunk optimization
 Enable build compression (gzip/brotli)
 Run production build: pnpm vite build
 Preview build locally: pnpm vite preview
Basic Configuration
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'node:path';

export default defineConfig({
  plugins: [react()],

  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@components': path.resolve(__dirname, './src/components'),
      '@hooks': path.resolve(__dirname, './src/hooks'),
      '@utils': path.resolve(__dirname, './src/utils'),
    }
  },

  server: {
    port: 5173,
    strictPort: true,
    open: true,
    hmr: { overlay: true },
    proxy: {
      '/api': { target: 'http://localhost:3000', changeOrigin: true }
    }
  },

  build: {
    outDir: 'dist',
    sourcemap: true,
    minify: 'esbuild',
  }
});


Update tsconfig.json paths to match aliases:

{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"],
      "@components/*": ["./src/components/*"]
    }
  }
}


React with SWC (faster alternative): pnpm add -D @vitejs/plugin-react-swc, import from @vitejs/plugin-react-swc.

Fast Refresh is enabled by default — no configuration needed.

Environment Variables
# .env - Base config (committed)
VITE_APP_NAME=MyApp
VITE_API_VERSION=v1

# .env.local - Local overrides (gitignored — put secrets here)
VITE_API_URL=http://localhost:3000

# .env.development / .env.production - mode-specific defaults


CRITICAL: All env vars must start with VITE_ to be exposed to client code.

// Access in code
const apiUrl = import.meta.env.VITE_API_URL;
const isDev = import.meta.env.DEV;
const isProd = import.meta.env.PROD;
const mode = import.meta.env.MODE; // 'development' | 'production'

// Type-safe env vars — add to vite-env.d.ts or src/env.d.ts
interface ImportMetaEnv {
  readonly VITE_APP_NAME: string;
  readonly VITE_API_URL: string;
}

// Runtime validation
if (!import.meta.env.VITE_API_URL) {
  throw new Error('VITE_API_URL is required');
}


Dynamic config with loadEnv:

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '');
  return {
    server: { port: Number(env.PORT) || 5173 }
  };
});

Build Optimization
Code Splitting
export default defineConfig({
  build: {
    chunkSizeWarningLimit: 500, // KB
    rollupOptions: {
      output: {
        manualChunks: {
          'react-vendor': ['react', 'react-dom'],
          'router-vendor': ['react-router-dom'],
          'animation-vendor': ['framer-motion'],
        },
        chunkFileNames: 'js/[name]-[hash].js',
        entryFileNames: 'js/[name]-[hash].js',
        assetFileNames: 'assets/[name]-[hash][extname]',
      }
    }
  }
});


Advanced function-based chunking — use when you need per-view splitting:

manualChunks(id) {
  if (id.includes('node_modules')) {
    if (id.includes('framer-motion')) return 'vendor-animation';
    if (id.includes('react')) return 'vendor-react';
    return 'vendor';
  }
}

Compression
import { compression } from 'vite-plugin-compression2';
// pnpm add -D vite-plugin-compression2

plugins: [
  compression({ algorithm: 'gzip', include: /\.(js|css|html|svg)$/ }),
  compression({ algorithm: 'brotliCompress', include: /\.(js|css|html|svg)$/ }),
]


For production-only minification:

minify: isDev ? false : 'terser',
terserOptions: { compress: { drop_console: true, drop_debugger: true } }

CSS and Assets

PostCSS / Tailwind: Point css.postcss to your postcss.config.js. Enable cssCodeSplit: true (default) for large apps.

Asset handling:

// src/assets — processed by Vite (hashed, optimized)
import logo from '@/assets/logo.svg';

// /public — served as-is, NOT processed
<img src="/images/logo.svg" />
// ❌ Never import from public directory


Inline limit: Assets under 4 KB are inlined as base64 by default (assetsInlineLimit: 4096).

Base path for subdirectory hosting: base: '/my-app/'

Vite 7 Notes
Rolldown — new Rust-based bundler (optional, faster builds)
Improved TypeScript support and tree-shaking
Default config works for most projects; advanced bundler options rarely needed
Best Practices
Use path aliases to avoid ../../../ import hell
Prefix client env vars with VITE_ for automatic exposure
Split large vendors into separate chunks for better caching
Use .env.local for secrets — never commit to git
Configure proxy for API calls to avoid CORS in development
Preview builds before deploying: pnpm vite build && pnpm vite preview
Use esbuild for faster builds, terser for smaller output
Set strictPort: true to avoid silent port conflicts
Anti-Patterns
❌ Forgetting VITE_ prefix on environment variables
❌ Importing from /public directory instead of src/assets
❌ Committing .env.local with API keys
❌ Not configuring path aliases (messy imports)
❌ Using terser in development (unnecessary slowdown)
❌ Not setting strictPort (silent port conflicts)
❌ Ignoring chunk size warnings (impacts load time)
❌ Missing tsconfig.json paths when using aliases
❌ Hardcoding localhost URLs (use env vars)
❌ Placing all vendors in single chunk (defeats caching)
Feedback Loops

Build analysis:

pnpm vite build
# Output shows chunk sizes:
# dist/js/vendor-react-abc123.js  142.34 kB
# dist/js/index-def456.js          87.21 kB


Preview testing:

pnpm vite build && pnpm vite preview
# Verify: all routes work, assets load, no console errors


HMR speed: Should be < 50ms for most updates. Check Chrome DevTools → Network → Filter by "vite".

Weekly Installs
32
Repository
dralgorhythm/cl…ramework
GitHub Stars
76
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass