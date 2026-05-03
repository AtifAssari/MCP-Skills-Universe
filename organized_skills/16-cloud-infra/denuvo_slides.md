---
rating: ⭐⭐
title: denuvo-slides
url: https://skills.sh/eng0ai/eng0-template-skills/denuvo-slides
---

# denuvo-slides

skills/eng0ai/eng0-template-skills/denuvo-slides
denuvo-slides
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill denuvo-slides
SKILL.md
Denuvo Slides

A Slidev presentation about reverse engineering Denuvo in Hogwarts Legacy.

Tech Stack
Framework: Slidev (Vue-based)
Package Manager: pnpm
Output: dist directory
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/denuvo-slides-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/denuvo-slides-template.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
pnpm install

Build
pnpm build


Note: The default build command may include a custom base path. Modify package.json build script if needed for your deployment target.

Deploy
Vercel (Recommended)
vercel pull --yes -t $VERCEL_TOKEN
vercel build --prod -t $VERCEL_TOKEN
vercel deploy --prebuilt --prod --yes -t $VERCEL_TOKEN

Netlify
netlify deploy --prod --dir=dist

Development
pnpm dev


Starts the Slidev server and opens the presentation in your browser. Edit slides in slides.md.

Weekly Installs
27
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