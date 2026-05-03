---
rating: ⭐⭐
title: ncine-presentation
url: https://skills.sh/eng0ai/eng0-template-skills/ncine-presentation
---

# ncine-presentation

skills/eng0ai/eng0-template-skills/ncine-presentation
ncine-presentation
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill ncine-presentation
SKILL.md
nCine Presentation

A Slidev presentation documenting 14 years of developing nCine, an open-source 2D game framework.

Tech Stack
Framework: Slidev (Vue-based)
Package Manager: pnpm
Output: dist directory
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/ncine-presentation-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/ncine-presentation-template.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
pnpm install

Build
pnpm build

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
28
Repository
eng0ai/eng0-tem…e-skills
GitHub Stars
4
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass