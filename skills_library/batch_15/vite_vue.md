---
title: vite-vue
url: https://skills.sh/eng0ai/eng0-template-skills/vite-vue
---

# vite-vue

skills/eng0ai/eng0-template-skills/vite-vue
vite-vue
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill vite-vue
SKILL.md
Vite Vue Template

A lightning-fast Vue 3.5 development environment with Vite 7 and TypeScript.

Tech Stack
Framework: Vue 3.5
Build Tool: Vite 7
Language: TypeScript
Package Manager: npm
Output: dist directory
Dev Port: 5173
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/vite-vue-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/vite-vue-template.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
npm install

Build
npm run build


Vue TypeScript compilation runs before build (vue-tsc -b && vite build).

Deploy
Vercel (Recommended)
vercel pull --yes -t $VERCEL_TOKEN
vercel build --prod -t $VERCEL_TOKEN
vercel deploy --prebuilt --prod --yes -t $VERCEL_TOKEN

Netlify
netlify deploy --prod --dir=dist

Development
npm run dev


Opens at http://localhost:5173 with HMR enabled. Uses Single File Components (SFC) with <script setup> syntax.

Weekly Installs
37
Repository
eng0ai/eng0-tem…e-skills
GitHub Stars
4
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass