---
title: vite
url: https://skills.sh/mindrally/skills/vite
---

# vite

skills/mindrally/skills/vite
vite
Installation
$ npx skills add https://github.com/mindrally/skills --skill vite
SKILL.md
Vite Development

You are an expert in Vite, modern JavaScript/TypeScript build tooling, and frontend development.

Key Principles
Leverage native ES modules for fast development
Use Vite's opinionated defaults when possible
Configure only what needs customization
Understand the dev/build differences
Optimize for both development speed and production performance
Project Setup
Basic Configuration
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true,
  },
  build: {
    outDir: 'dist',
    sourcemap: true,
  },
});

Path Aliases
import { defineConfig } from 'vite';
import path from 'path';

export default defineConfig({
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@components': path.resolve(__dirname, './src/components'),
      '@utils': path.resolve(__dirname, './src/utils'),
    },
  },
});

Environment Variables
Usage
// .env
VITE_API_URL=https://api.example.com
VITE_APP_TITLE=My App

// In code
const apiUrl = import.meta.env.VITE_API_URL;
const isDev = import.meta.env.DEV;
const isProd = import.meta.env.PROD;
const mode = import.meta.env.MODE;

Type Definitions
// src/vite-env.d.ts
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_URL: string;
  readonly VITE_APP_TITLE: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}

Hot Module Replacement
Manual HMR
// For libraries without HMR support
if (import.meta.hot) {
  import.meta.hot.accept('./module.ts', (newModule) => {
    // Handle the updated module
    console.log('Module updated:', newModule);
  });

  import.meta.hot.dispose(() => {
    // Cleanup before module is replaced
  });
}

Asset Handling
Static Assets
// Import as URL
import imageUrl from './image.png';
// <img src={imageUrl} />

// Import as string (raw)
import shaderCode from './shader.glsl?raw';

// Import as worker
import Worker from './worker.ts?worker';
const worker = new Worker();

Public Directory
public/
├── favicon.ico      # Served at /favicon.ico
├── robots.txt       # Served at /robots.txt
└── images/          # Served at /images/

Framework Integrations
React
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [
    react({
      // Enable Fast Refresh
      fastRefresh: true,
      // Babel plugins
      babel: {
        plugins: ['@emotion/babel-plugin'],
      },
    }),
  ],
});

Vue
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
});

Svelte
import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
  plugins: [svelte()],
});

Build Optimization
Code Splitting
// Dynamic imports create separate chunks
const AdminPanel = lazy(() => import('./AdminPanel'));

// Manual chunks
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          utils: ['lodash', 'date-fns'],
        },
      },
    },
  },
});

Chunk Size Optimization
export default defineConfig({
  build: {
    chunkSizeWarningLimit: 500,
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes('node_modules')) {
            return id.split('node_modules/')[1].split('/')[0];
          }
        },
      },
    },
  },
});

CSS Handling
CSS Modules
// styles.module.css is auto-detected
import styles from './styles.module.css';

// <div className={styles.container}>

PostCSS
// postcss.config.js
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};

Preprocessors
// Automatically handled with package installed
// npm install -D sass
import './styles.scss';

Proxy Configuration
export default defineConfig({
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:4000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
      '/socket.io': {
        target: 'ws://localhost:4000',
        ws: true,
      },
    },
  },
});

Plugin Development
// my-vite-plugin.ts
import type { Plugin } from 'vite';

export function myPlugin(): Plugin {
  return {
    name: 'my-plugin',

    // Hook: modify config
    config(config, { mode }) {
      return {
        define: {
          __BUILD_TIME__: JSON.stringify(new Date().toISOString()),
        },
      };
    },

    // Hook: transform code
    transform(code, id) {
      if (id.endsWith('.md')) {
        return {
          code: `export default ${JSON.stringify(code)}`,
          map: null,
        };
      }
    },

    // Hook: configure dev server
    configureServer(server) {
      server.middlewares.use((req, res, next) => {
        // Custom middleware
        next();
      });
    },
  };
}

Testing with Vitest
// vite.config.ts
import { defineConfig } from 'vite';

export default defineConfig({
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: './src/test/setup.ts',
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
    },
  },
});

SSR Configuration
export default defineConfig({
  build: {
    ssr: true,
    rollupOptions: {
      input: './src/entry-server.ts',
    },
  },
  ssr: {
    external: ['express'],
    noExternal: ['my-ui-library'],
  },
});

Library Mode
export default defineConfig({
  build: {
    lib: {
      entry: './src/index.ts',
      name: 'MyLib',
      fileName: (format) => `my-lib.${format}.js`,
    },
    rollupOptions: {
      external: ['react', 'react-dom'],
      output: {
        globals: {
          react: 'React',
          'react-dom': 'ReactDOM',
        },
      },
    },
  },
});

Best Practices
Use vite preview to test production builds locally
Keep dependencies that support ESM in regular deps
Use optimizeDeps.include for CommonJS dependencies
Enable build.sourcemap for debugging production
Use server.warmup for faster dev server starts
Weekly Installs
274
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