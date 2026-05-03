---
rating: ⭐⭐
title: convert-to-vite
url: https://skills.sh/puzzmo-com/oss/convert-to-vite
---

# convert-to-vite

skills/puzzmo-com/oss/convert-to-vite
convert-to-vite
Installation
$ npx skills add https://github.com/puzzmo-com/oss --skill convert-to-vite
SKILL.md
Convert to Vite

Convert this HTML game into a Vite-powered project.

Steps

Initialize a new package.json with:

"name" based on the game directory name
"private": true
"type": "module"
"scripts": "dev": "vite", "build": "vite build", "preview": "vite preview"

Install dependencies:

vite as a devDependency

Create vite.config.ts:

import { defineConfig } from "vite"
export default defineConfig({})


Extract inline <script> and <style> from index.html:

Move inline JS to src/main.js (or src/main.ts)
Move inline CSS to src/style.css
Replace inline content with <script type="module" src="/src/main.js"></script> and <link rel="stylesheet" href="/src/style.css">

Move any standalone JS/CSS files into src/

Update all asset references to use relative paths that Vite can resolve

Verify if you need to edit the .gitignore to exclude dist/ and other build artifacts like node_modules etc

Success Criteria
npx vite build completes without errors
The game runs identically with npx vite as it did before
No inline scripts remain in index.html (except small config objects)
All JS is loaded as ES modules
Weekly Installs
9
Repository
puzzmo-com/oss
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass