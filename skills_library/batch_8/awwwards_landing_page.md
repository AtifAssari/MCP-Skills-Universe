---
title: awwwards-landing-page
url: https://skills.sh/eng0ai/eng0-template-skills/awwwards-landing-page
---

# awwwards-landing-page

skills/eng0ai/eng0-template-skills/awwwards-landing-page
awwwards-landing-page
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill awwwards-landing-page
Summary

Awwwards-style portfolio landing page with smooth scroll and motion animations.

Built with Next.js, Locomotive Scroll, GSAP, and Framer Motion for fluid scroll-triggered animations and interactive effects
Static site with no environment variables required; runs on port 3000 during development
Deployment requires special handling on Vercel using vercel build --prod followed by vercel deploy --prebuilt --prod; Netlify deployment available as alternative
SKILL.md
Awwwards Landing Page

A stunning portfolio landing page with smooth scroll animations using Locomotive Scroll, GSAP, and Framer Motion.

Tech Stack
Framework: Next.js
Animation: Locomotive Scroll, GSAP, Framer Motion
Package Manager: pnpm or npm
Dev Port: 3000
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/awwwards-landing-page-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/awwwards-landing-page-template.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
npm install

Build
npm run build

Deploy

CRITICAL: For Vercel, you MUST use vercel build --prod then vercel deploy --prebuilt --prod. Never use vercel --prod directly.

Vercel (Recommended)
vercel pull --yes -t $VERCEL_TOKEN
vercel build --prod -t $VERCEL_TOKEN
vercel deploy --prebuilt --prod --yes -t $VERCEL_TOKEN

Netlify
netlify deploy --prod

Development
npm run dev


Opens at http://localhost:3000

Notes
Static Next.js site - no environment variables needed
Never run npm run dev in VM environment
Weekly Installs
563
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