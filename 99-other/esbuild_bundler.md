---
rating: ⭐⭐⭐
title: esbuild-bundler
url: https://skills.sh/mindrally/skills/esbuild-bundler
---

# esbuild-bundler

skills/mindrally/skills/esbuild-bundler
esbuild-bundler
Installation
$ npx skills add https://github.com/mindrally/skills --skill esbuild-bundler
SKILL.md
esbuild Bundler

You are an expert in esbuild, the extremely fast JavaScript and TypeScript bundler written in Go. Follow these guidelines when working with esbuild configurations.

Core Principles
esbuild is 10-100x faster than traditional bundlers
Zero configuration needed for most use cases
Native TypeScript and JSX support without additional setup
Focus on speed while maintaining code quality
Written in Go for native performance
Project Structure
project/
├── src/
│   ├── index.ts          # Main entry point
│   ├── components/       # UI components
│   └── utils/            # Utility functions
├── dist/                 # Build output
├── esbuild.config.mjs    # Build script (optional)
├── tsconfig.json         # TypeScript config
└── package.json

Basic Usage
Command Line
# Basic bundle
esbuild src/index.ts --bundle --outfile=dist/bundle.js

# Production build
esbuild src/index.ts --bundle --minify --sourcemap --outfile=dist/bundle.js

# Watch mode
esbuild src/index.ts --bundle --watch --outfile=dist/bundle.js

JavaScript API
import * as esbuild from 'esbuild';

await esbuild.build({
  entryPoints: ['src/index.ts'],
  bundle: true,
  minify: true,
  sourcemap: true,
  outfile: 'dist/bundle.js'
});

TypeScript Configuration
tsconfig.json Best Practices
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "esModuleInterop": true,
    "isolatedModules": true,
    "strict": true,
    "skipLibCheck": true,
    "noEmit": true,
    "verbatimModuleSyntax": true,
    "noUncheckedIndexedAccess": true
  },
  "include": ["src/**/*"]
}

Important TypeScript Settings
isolatedModules: true - Required for esbuild compatibility
esModuleInterop: true - Better ESM compatibility
noEmit: true - Let esbuild handle output, use tsc for type checking only
Build Configuration
Browser Build
await esbuild.build({
  entryPoints: ['src/index.ts'],
  bundle: true,
  minify: true,
  sourcemap: true,
  target: ['chrome90', 'firefox88', 'safari14', 'edge90'],
  outfile: 'dist/bundle.js'
});

Node.js Build
await esbuild.build({
  entryPoints: ['src/index.ts'],
  bundle: true,
  platform: 'node',
  target: 'node18',
  format: 'esm',
  outfile: 'dist/index.js'
});

Multiple Entry Points
await esbuild.build({
  entryPoints: ['src/index.ts', 'src/worker.ts'],
  bundle: true,
  outdir: 'dist',
  splitting: true,
  format: 'esm'
});

Output Formats
ESM (ES Modules)
await esbuild.build({
  format: 'esm',
  // Outputs: import/export syntax
});

CommonJS
await esbuild.build({
  format: 'cjs',
  // Outputs: require/module.exports
});

IIFE (Browser Scripts)
await esbuild.build({
  format: 'iife',
  globalName: 'MyApp',
  // Outputs: self-executing function
});

Loaders
Built-in Loaders
await esbuild.build({
  loader: {
    '.png': 'file',
    '.svg': 'text',
    '.json': 'json',
    '.woff': 'dataurl'
  }
});

Loader Types
js - JavaScript
ts - TypeScript
jsx - JavaScript with JSX
tsx - TypeScript with JSX
json - JSON data
text - Plain text
file - Copy file, return path
dataurl - Inline as data URL
binary - Inline as Uint8Array
base64 - Inline as base64
copy - Copy file, no reference
External Dependencies
Mark as External
await esbuild.build({
  external: ['react', 'react-dom', 'lodash']
});

External Patterns
await esbuild.build({
  external: ['*.png', '@aws-sdk/*']
});

Code Splitting
await esbuild.build({
  entryPoints: ['src/index.ts'],
  bundle: true,
  splitting: true,
  format: 'esm',
  outdir: 'dist'
});


Note: Code splitting requires format: 'esm' and outdir (not outfile).

Plugins
Plugin Structure
const myPlugin = {
  name: 'my-plugin',
  setup(build) {
    // On resolve - intercept import paths
    build.onResolve({ filter: /^env$/ }, args => ({
      path: args.path,
      namespace: 'env-ns'
    }));

    // On load - provide module contents
    build.onLoad({ filter: /.*/, namespace: 'env-ns' }, () => ({
      contents: JSON.stringify(process.env),
      loader: 'json'
    }));
  }
};

await esbuild.build({
  plugins: [myPlugin]
});

Common Plugins
import esbuildPluginTsc from 'esbuild-plugin-tsc';

await esbuild.build({
  plugins: [
    esbuildPluginTsc({
      force: true
    })
  ]
});

Development Server
Serve API
const ctx = await esbuild.context({
  entryPoints: ['src/index.ts'],
  bundle: true,
  outdir: 'dist'
});

await ctx.serve({
  servedir: 'dist',
  port: 3000
});

Watch Mode
const ctx = await esbuild.context({
  entryPoints: ['src/index.ts'],
  bundle: true,
  outfile: 'dist/bundle.js'
});

await ctx.watch();
console.log('Watching for changes...');

Environment Variables
Define API
await esbuild.build({
  define: {
    'process.env.NODE_ENV': '"production"',
    'process.env.API_URL': JSON.stringify(process.env.API_URL)
  }
});

Optimization
Minification
await esbuild.build({
  minify: true,
  // Or granular control:
  minifyWhitespace: true,
  minifyIdentifiers: true,
  minifySyntax: true
});

Tree Shaking
await esbuild.build({
  treeShaking: true,
  // Mark files as side-effect free
  ignoreAnnotations: false
});

Drop Console and Debugger
await esbuild.build({
  drop: ['console', 'debugger']
});

Type Checking

esbuild does not perform type checking. Run TypeScript separately:

{
  "scripts": {
    "typecheck": "tsc --noEmit",
    "build": "npm run typecheck && node esbuild.config.mjs",
    "dev": "concurrently \"tsc --noEmit --watch\" \"node esbuild.config.mjs --watch\""
  }
}

Build Script Example
// esbuild.config.mjs
import * as esbuild from 'esbuild';

const isProduction = process.env.NODE_ENV === 'production';
const isWatch = process.argv.includes('--watch');

const config = {
  entryPoints: ['src/index.ts'],
  bundle: true,
  platform: 'browser',
  target: ['es2020'],
  format: 'esm',
  outdir: 'dist',
  sourcemap: !isProduction,
  minify: isProduction,
  splitting: true,
  define: {
    'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV || 'development')
  }
};

if (isWatch) {
  const ctx = await esbuild.context(config);
  await ctx.watch();
  console.log('Watching for changes...');
} else {
  await esbuild.build(config);
  console.log('Build complete!');
}

Best Practices
Do
Use isolatedModules: true in TypeScript config
Run type checking separately with tsc --noEmit
Use the context API for watch mode
Leverage native TypeScript and JSX support
Use external for peer dependencies in libraries
Avoid
Relying on esbuild for type checking
Using features that require type information (decorators with metadata)
Ignoring the isolatedModules requirement
Over-configuring when defaults work
Common Patterns
Library Build
await esbuild.build({
  entryPoints: ['src/index.ts'],
  bundle: true,
  external: ['react', 'react-dom'],
  format: 'esm',
  outfile: 'dist/index.js',
  sourcemap: true
});

Application Build
await esbuild.build({
  entryPoints: ['src/index.tsx'],
  bundle: true,
  splitting: true,
  format: 'esm',
  outdir: 'dist',
  minify: true,
  sourcemap: true,
  target: ['chrome90', 'firefox88', 'safari14']
});

Performance Tips
esbuild parallelizes work automatically
File system caching is built-in
Use incremental builds in development
Avoid unnecessary plugins that slow builds
Weekly Installs
270
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