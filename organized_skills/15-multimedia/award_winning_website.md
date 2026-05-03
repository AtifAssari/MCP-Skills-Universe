---
rating: ⭐⭐
title: award-winning-website
url: https://skills.sh/eng0ai/eng0-template-skills/award-winning-website
---

# award-winning-website

skills/eng0ai/eng0-template-skills/award-winning-website
award-winning-website
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill award-winning-website
SKILL.md
Award-Winning Gaming Website

A visually captivating website with scroll-triggered animations, geometric transitions, 3D hover effects, and video storytelling.

Tech Stack
Framework: React 19
Build Tool: Vite
Animation: GSAP
Styling: Tailwind CSS
Package Manager: npm
Output: dist directory
Dev Port: 5173
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/award-winning-website-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/award-winning-website-template.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
npm install

Build
npm run build


Creates a production build in the dist/ directory.

Deploy

CRITICAL: For Vercel, you MUST use vercel build --prod then vercel deploy --prebuilt --prod. Never use vercel --prod directly.

Vercel (Recommended)
vercel pull --yes -t $VERCEL_TOKEN
vercel build --prod -t $VERCEL_TOKEN
vercel deploy --prebuilt --prod --yes -t $VERCEL_TOKEN

Netlify
netlify deploy --prod --dir=dist

Development
npm run dev


Opens at http://localhost:5173

Notes
Static React site with no backend - no environment variables needed
Never run npm run dev in VM environment
Weekly Installs
209
Repository
eng0ai/eng0-tem…e-skills
GitHub Stars
4
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail