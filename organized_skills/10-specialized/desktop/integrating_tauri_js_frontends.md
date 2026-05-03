---
rating: ⭐⭐⭐
title: integrating-tauri-js-frontends
url: https://skills.sh/dchuk/claude-code-tauri-skills/integrating-tauri-js-frontends
---

# integrating-tauri-js-frontends

skills/dchuk/claude-code-tauri-skills/integrating-tauri-js-frontends
integrating-tauri-js-frontends
Installation
$ npx skills add https://github.com/dchuk/claude-code-tauri-skills --skill integrating-tauri-js-frontends
SKILL.md
Tauri v2 JavaScript Frontend Integration

This skill covers integrating JavaScript frontend frameworks with Tauri v2 for desktop application development.

Core Architecture

Tauri functions as a static web host, serving HTML, CSS, JavaScript, and WASM files through a native webview. The framework is frontend-agnostic but requires specific configurations for optimal integration.

Supported Application Types
Static Site Generation (SSG)
Single-Page Applications (SPA)
Multi-Page Applications (MPA)
Not Supported

Server-side rendering (SSR) in its native form. All frameworks must be configured for static output.

General Requirements
Key Principles
Static Output Required: Tauri cannot run a Node.js server - all content must be pre-built static files
Client-Server Architecture: Implement proper client-server relationships between app and APIs (no hybrid SSR solutions)
Mobile Development: Requires a development server hosting the frontend on your internal IP
Common tauri.conf.json Structure
{
  "build": {
    "beforeDevCommand": "<package-manager> dev",
    "beforeBuildCommand": "<package-manager> build",
    "devUrl": "http://localhost:<port>",
    "frontendDist": "../<output-dir>"
  }
}


Replace <package-manager> with npm run, yarn, pnpm, or deno task.

Framework Configurations
Vite (React, Vue, Svelte, Solid)

Vite is the recommended choice for SPA frameworks due to its fast development experience and simple configuration.

package.json
{
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "tauri": "tauri"
  }
}

vite.config.ts
import { defineConfig } from 'vite';

export default defineConfig({
  clearScreen: false,
  server: {
    port: 5173,
    strictPort: true,
    host: process.env.TAURI_DEV_HOST || 'localhost',
    watch: {
      ignored: ['**/src-tauri/**'],
    },
  },
  envPrefix: ['VITE_', 'TAURI_ENV_*'],
  build: {
    target: process.env.TAURI_ENV_PLATFORM === 'windows' ? 'chrome105' : 'safari13',
    minify: process.env.TAURI_ENV_DEBUG ? false : 'esbuild',
    sourcemap: !!process.env.TAURI_ENV_DEBUG,
  },
});

tauri.conf.json
{
  "build": {
    "beforeDevCommand": "npm run dev",
    "beforeBuildCommand": "npm run build",
    "devUrl": "http://localhost:5173",
    "frontendDist": "../dist"
  }
}

Next.js

Next.js requires static export mode since Tauri cannot run Node.js servers.

Critical Requirements
Must use output: 'export' in next.config
Images must be unoptimized for static export
Asset prefix required for development server
next.config.mjs
const isProd = process.env.NODE_ENV === 'production';
const internalHost = process.env.TAURI_DEV_HOST || 'localhost';

/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: {
    unoptimized: true,
  },
  assetPrefix: isProd ? undefined : `http://${internalHost}:3000`,
};

export default nextConfig;

package.json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "tauri": "tauri"
  }
}

tauri.conf.json
{
  "build": {
    "beforeDevCommand": "npm run dev",
    "beforeBuildCommand": "npm run build",
    "devUrl": "http://localhost:3000",
    "frontendDist": "../out"
  }
}

SSG Considerations for Next.js
The out directory contains static exports
Dynamic routes require generateStaticParams()
API routes are not supported - use Tauri commands instead
next/image optimization is disabled; use standard <img> or configure unoptimized
Nuxt

Nuxt must run in SSG mode with ssr: false for Tauri compatibility.

nuxt.config.ts
export default defineNuxtConfig({
  ssr: false,
  telemetry: false,
  devServer: {
    host: '0.0.0.0', // Required for iOS device compatibility
  },
  vite: {
    clearScreen: false,
    envPrefix: ['VITE_', 'TAURI_'],
    server: {
      strictPort: true,
      watch: {
        ignored: ['**/src-tauri/**'],
      },
    },
  },
});

package.json
{
  "scripts": {
    "dev": "nuxt dev",
    "build": "nuxt build",
    "generate": "nuxt generate",
    "tauri": "tauri"
  }
}

tauri.conf.json
{
  "build": {
    "beforeDevCommand": "npm run dev",
    "beforeBuildCommand": "npm run generate",
    "devUrl": "http://localhost:3000",
    "frontendDist": "../dist"
  }
}

SSG Considerations for Nuxt
Use nuxt generate for production builds (creates static files)
Server routes (/server/api) are not available - use Tauri commands
Nitro server functionality is disabled in SSG mode
SvelteKit

SvelteKit requires the static adapter and SSR must be disabled.

Installation
npm install --save-dev @sveltejs/adapter-static

svelte.config.js
import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  preprocess: vitePreprocess(),
  kit: {
    adapter: adapter({
      fallback: 'index.html',
    }),
  },
};

export default config;

src/routes/+layout.ts
export const ssr = false;
export const prerender = true;

vite.config.ts
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [sveltekit()],
  clearScreen: false,
  server: {
    port: 5173,
    strictPort: true,
    host: process.env.TAURI_DEV_HOST || 'localhost',
    watch: {
      ignored: ['**/src-tauri/**'],
    },
  },
  envPrefix: ['VITE_', 'TAURI_ENV_*'],
});

tauri.conf.json
{
  "build": {
    "beforeDevCommand": "npm run dev",
    "beforeBuildCommand": "npm run build",
    "devUrl": "http://localhost:5173",
    "frontendDist": "../build"
  }
}

SSG Considerations for SvelteKit
SPA mode (without prerendering) is recommended for full Tauri API access in load functions
With prerendering, load functions execute at build time without Tauri API access
The fallback: 'index.html' enables SPA routing
Output directory is build/ by default
Qwik

Qwik requires the static adapter for Tauri compatibility.

Setup
# Create project
npm create qwik@latest
cd <project>

# Add static adapter
npm run qwik add static

# Add Tauri CLI
npm install -D @tauri-apps/cli@latest

# Initialize Tauri
npm run tauri init

package.json
{
  "scripts": {
    "dev": "vite",
    "build": "qwik build",
    "tauri": "tauri"
  }
}

tauri.conf.json
{
  "build": {
    "beforeDevCommand": "npm run dev",
    "beforeBuildCommand": "npm run build",
    "devUrl": "http://localhost:5173",
    "frontendDist": "../dist"
  }
}

SSG Considerations for Qwik
The static adapter is mandatory
Qwik City server functions are not available
Use Tauri commands for backend functionality
Quick Reference Table
Framework	Output Dir	Dev Port	Build Command	Key Config
Vite	dist	5173	vite build	Standard Vite config
Next.js	out	3000	next build	output: 'export'
Nuxt	dist	3000	nuxt generate	ssr: false
SvelteKit	build	5173	vite build	adapter-static
Qwik	dist	5173	qwik build	Static adapter
Common Issues and Solutions
Issue: Assets Not Loading in Development

Cause: Asset prefix not configured for development server.

Solution: Configure asset prefix to point to dev server (see Next.js config example).

Issue: Tauri APIs Unavailable

Cause: Code executing during SSG build time instead of runtime.

Solution:

Disable prerendering for pages using Tauri APIs
Use dynamic imports with ssr: false
Check for window.__TAURI__ before API calls
Issue: Hot Reload Not Working

Cause: File watcher including src-tauri directory.

Solution: Add **/src-tauri/** to watch ignore list in Vite config.

Issue: Mobile Development Fails

Cause: Dev server not accessible on network.

Solution: Set host to 0.0.0.0 or use TAURI_DEV_HOST environment variable.

Issue: Build Fails with SSR Errors

Cause: Framework attempting server-side rendering.

Solution: Ensure SSR is disabled:

Next.js: output: 'export'
Nuxt: ssr: false
SvelteKit: export const ssr = false in layout
Qwik: Use static adapter
Environment Variables
Tauri-Provided Variables
Variable	Description
TAURI_DEV_HOST	Host IP for mobile development
TAURI_ENV_PLATFORM	Target platform (windows, macos, linux, ios, android)
TAURI_ENV_DEBUG	Set during debug builds
Recommended envPrefix
envPrefix: ['VITE_', 'TAURI_ENV_*']

Build Targets

Configure build targets based on platform webview capabilities:

build: {
  target: process.env.TAURI_ENV_PLATFORM === 'windows'
    ? 'chrome105'  // WebView2 on Windows
    : 'safari13',  // WebKit on macOS/Linux
}

Mobile Development

For iOS and Android development, the dev server must be accessible on the network:

server: {
  host: process.env.TAURI_DEV_HOST || '0.0.0.0',
  strictPort: true,
}


Run with the appropriate mobile command:

npm run tauri ios dev
npm run tauri android dev

Weekly Installs
197
Repository
dchuk/claude-co…i-skills
GitHub Stars
18
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass