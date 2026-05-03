---
rating: ⭐⭐
title: vite-react
url: https://skills.sh/eng0ai/eng0-template-skills/vite-react
---

# vite-react

skills/eng0ai/eng0-template-skills/vite-react
vite-react
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill vite-react
SKILL.md
Vite React Template

A complete Vite + React project with TypeScript, ESLint, and hot module replacement.

Tech Stack
Framework: React 19
Build Tool: Vite 7
Language: TypeScript
Package Manager: npm
Output: dist directory
Dev Port: 5173
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/vite-react-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/vite-react-template.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
npm install

Build
npm run build


TypeScript compilation runs before build (tsc -b && vite build).

Deploy
Vercel (Recommended)
vercel pull --yes -t $VERCEL_TOKEN
vercel build --prod -t $VERCEL_TOKEN
vercel deploy --prebuilt --prod --yes -t $VERCEL_TOKEN

Netlify
netlify deploy --prod --dir=dist

Development
npm run dev


Opens at http://localhost:5173 with HMR enabled.

Weekly Installs
40
Repository
eng0ai/eng0-tem…e-skills
GitHub Stars
4
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass