---
rating: ⭐⭐⭐
title: parcel-bundler
url: https://skills.sh/mindrally/skills/parcel-bundler
---

# parcel-bundler

skills/mindrally/skills/parcel-bundler
parcel-bundler
Installation
$ npx skills add https://github.com/mindrally/skills --skill parcel-bundler
SKILL.md
Parcel Bundler

You are an expert in Parcel, the zero-configuration build tool for the web. Follow these guidelines when working with Parcel projects.

Core Principles
Zero configuration by default - Parcel works out of the box
Automatic dependency detection and installation
Built-in development server with hot module replacement
Native performance with Rust-based compiler
Automatic code splitting and optimization
Project Structure
project/
├── src/
│   ├── index.html        # HTML entry point
│   ├── index.js          # JavaScript entry
│   ├── styles.css        # Stylesheets
│   └── assets/           # Images, fonts, etc.
├── dist/                 # Build output (auto-generated)
├── .parcelrc             # Optional configuration
└── package.json

Getting Started
Basic Usage
# Development with hot reload
parcel src/index.html

# Production build
parcel build src/index.html

Package.json Scripts
{
  "scripts": {
    "dev": "parcel src/index.html",
    "build": "parcel build src/index.html",
    "clean": "rm -rf dist .parcel-cache"
  },
  "source": "src/index.html"
}

Entry Points
HTML Entry
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="./styles.css">
</head>
<body>
  <div id="app"></div>
  <script type="module" src="./index.js"></script>
</body>
</html>

JavaScript Entry
parcel build src/index.js --dist-dir lib

Multiple Entry Points
parcel build src/index.html src/admin.html

Supported Languages and File Types

Parcel supports out of the box:

JavaScript/TypeScript: .js, .jsx, .ts, .tsx, .mjs
Styles: .css, .scss, .sass, .less, .styl
HTML: .html, .htm
Images: .png, .jpg, .gif, .svg, .webp
Fonts: .woff, .woff2, .ttf, .otf, .eot
Data: .json, .yaml, .toml, .xml
WebAssembly: .wasm
Configuration (When Needed)
.parcelrc
{
  "extends": "@parcel/config-default",
  "transformers": {
    "*.svg": ["@parcel/transformer-svg-react"]
  },
  "reporters": ["...", "parcel-reporter-bundle-analyzer"]
}

package.json Targets
{
  "targets": {
    "main": {
      "source": "src/index.js",
      "distDir": "dist",
      "context": "browser",
      "outputFormat": "esm"
    }
  }
}

TypeScript Support
Automatic Configuration

Parcel handles TypeScript automatically. Just use .ts or .tsx files.

tsconfig.json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "isolatedModules": true
  }
}

React Support
Automatic JSX
// Parcel handles JSX automatically
import { useState } from 'react';

function App() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}

CSS and Styling
CSS Imports
import './styles.css';

CSS Modules
import * as styles from './Button.module.css';

function Button() {
  return <button className={styles.primary}>Click me</button>;
}

Sass/SCSS
import './styles.scss';


Parcel installs sass automatically when you use .scss files.

Asset Handling
Importing Assets
import logo from './logo.png';
import data from './data.json';

// Use in JSX
<img src={logo} alt="Logo" />

URL References
const imageUrl = new URL('./image.png', import.meta.url);

Code Splitting
Dynamic Imports
// Automatic code splitting
const LazyComponent = React.lazy(() => import('./LazyComponent'));

// Or manual
async function loadModule() {
  const module = await import('./heavy-module.js');
  return module.default;
}

Shared Bundles

Parcel automatically creates shared bundles for code used across multiple entry points.

Environment Variables
.env Files
# .env
API_URL=https://api.example.com

# .env.production
API_URL=https://api.production.com

Usage in Code
const apiUrl = process.env.API_URL;

Defining in package.json
{
  "targets": {
    "default": {
      "publicUrl": "/my-app/"
    }
  }
}

Development Server
Default Configuration
parcel src/index.html
# Serves at http://localhost:1234

Custom Port
parcel src/index.html --port 3000

HTTPS
parcel src/index.html --https

Proxy API Requests
{
  "devServer": {
    "proxy": {
      "/api": {
        "target": "http://localhost:8080"
      }
    }
  }
}

Production Build
Basic Build
parcel build src/index.html

Output Configuration
parcel build src/index.html --dist-dir build --public-url /app/

No Source Maps
parcel build src/index.html --no-source-maps

Optimization
Automatic Optimizations

Parcel automatically:

Minifies JavaScript, CSS, HTML, and SVG
Compresses images
Generates content hashes for caching
Tree-shakes unused code
Scope hoists modules
Bundle Analysis
npm install -D parcel-reporter-bundle-analyzer

# Add to .parcelrc
{
  "extends": "@parcel/config-default",
  "reporters": ["...", "parcel-reporter-bundle-analyzer"]
}

Caching

Parcel uses aggressive caching:

# Clear cache
rm -rf .parcel-cache

# Or
parcel build --no-cache

Plugin Development
Plugin Types
Transformers: Transform source files
Resolvers: Custom module resolution
Bundlers: Custom bundling logic
Namers: Custom output naming
Packagers: Package bundles
Optimizers: Optimize bundles
Reporters: Custom build reporting
Plugin Rules
Stateless: Avoid internal state
Pure: Same input produces same output
No side effects: Don't modify external state
Library Development
Package.json Configuration
{
  "name": "my-library",
  "source": "src/index.ts",
  "main": "dist/main.js",
  "module": "dist/module.js",
  "types": "dist/types.d.ts",
  "targets": {
    "main": {
      "outputFormat": "commonjs"
    },
    "module": {
      "outputFormat": "esmodule"
    },
    "types": {
      "source": "src/index.ts"
    }
  }
}

Best Practices
Do
Start with zero configuration
Let Parcel handle asset optimization
Use dynamic imports for code splitting
Leverage automatic dependency installation
Use CSS Modules for component styles
Avoid
Over-configuring when defaults work
Fighting against Parcel's conventions
Manually optimizing what Parcel handles
Ignoring build warnings and errors
Common Patterns
Single Page Application
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>My App</title>
</head>
<body>
  <div id="root"></div>
  <script type="module" src="./index.tsx"></script>
</body>
</html>

Static Site
parcel build src/*.html

Web Worker
const worker = new Worker(new URL('./worker.js', import.meta.url), {
  type: 'module'
});

Troubleshooting
Clear Cache
rm -rf .parcel-cache dist

Verbose Output
parcel build --log-level verbose

Debug Mode
DEBUG=parcel:* parcel build

Migration from Other Bundlers
Remove webpack.config.js or similar
Remove loader/plugin dependencies
Update import statements if needed
Parcel will auto-install required dependencies
Weekly Installs
233
Repository
mindrally/skills
GitHub Stars
88
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass