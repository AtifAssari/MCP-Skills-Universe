---
rating: ⭐⭐
title: screwfast
url: https://skills.sh/eng0ai/eng0-template-skills/screwfast
---

# screwfast

skills/eng0ai/eng0-template-skills/screwfast
screwfast
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill screwfast
SKILL.md
ScrewFast Landing Page

A versatile landing page, blog, and docs template with Astro 5, Tailwind CSS 4, Preline UI, GSAP animations, and Starlight documentation.

Tech Stack
Framework: Astro 5 with Starlight docs
Styling: Tailwind CSS 4, Preline UI
Animation: GSAP, Lenis smooth scroll
Package Manager: npm
Output: dist directory
Dev Port: 4321
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/screwfast-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/screwfast-template.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
npm install

Build
npm run build


Runs astro check && astro build && node process-html.mjs which type checks, builds, and minifies HTML.

Deploy
Vercel (Recommended)
vercel pull --yes -t $VERCEL_TOKEN
vercel build --prod -t $VERCEL_TOKEN
vercel deploy --prebuilt --prod --yes -t $VERCEL_TOKEN

Netlify
netlify deploy --prod --dir=dist

Development
npm run dev


Opens at http://localhost:4321

Preview production build:

npm run preview

Weekly Installs
30
Repository
eng0ai/eng0-tem…e-skills
GitHub Stars
4
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass