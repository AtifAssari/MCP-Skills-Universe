---
title: bundle-barrel-imports
url: https://skills.sh/theorcdev/8bitcn-ui/bundle-barrel-imports
---

# bundle-barrel-imports

skills/theorcdev/8bitcn-ui/bundle-barrel-imports
bundle-barrel-imports
Installation
$ npx skills add https://github.com/theorcdev/8bitcn-ui --skill bundle-barrel-imports
SKILL.md
Avoid Barrel File Imports

Import directly from source files instead of barrel files to avoid loading thousands of unused modules. Barrel files are entry points that re-export multiple modules (e.g., index.js that does export * from './module').

Popular icon and component libraries can have up to 10,000 re-exports in their entry file. For many React packages, it takes 200-800ms just to import them, affecting both development speed and production cold starts.

Why tree-shaking doesn't help: When a library is marked as external (not bundled), the bundler can't optimize it. If you bundle it to enable tree-shaking, builds become substantially slower analyzing the entire module graph.

Incorrect (imports entire library):

import { Check, X, Menu } from 'lucide-react'
// Loads 1,583 modules, takes ~2.8s extra in dev
// Runtime cost: 200-800ms on every cold start

import { Button, TextField } from '@mui/material'
// Loads 2,225 modules, takes ~4.2s extra in dev


Correct (imports only what you need):

import Check from 'lucide-react/dist/esm/icons/check'
import X from 'lucide-react/dist/esm/icons/x'
import Menu from 'lucide-react/dist/esm/icons/menu'
// Loads only 3 modules (~2KB vs ~1MB)

import Button from '@mui/material/Button'
import TextField from '@mui/material/TextField'
// Loads only what you use


Alternative (Next.js 13.5+):

// next.config.js - use optimizePackageImports
module.exports = {
  experimental: {
    optimizePackageImports: ['lucide-react', '@mui/material']
  }
}

// Then you can keep the ergonomic barrel imports:
import { Check, X, Menu } from 'lucide-react'
// Automatically transformed to direct imports at build time


Direct imports provide 15-70% faster dev boot, 28% faster builds, 40% faster cold starts, and significantly faster HMR.

Libraries commonly affected: lucide-react, @mui/material, @mui/icons-material, @tabler/icons-react, react-icons, @headlessui/react, @radix-ui/react-*, lodash, ramda, date-fns, rxjs, react-use.

Reference: How we optimized package imports in Next.js

Weekly Installs
30
Repository
theorcdev/8bitcn-ui
GitHub Stars
1.8K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass