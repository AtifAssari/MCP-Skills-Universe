---
rating: ⭐⭐
title: py-intro
url: https://skills.sh/eng0ai/eng0-template-skills/py-intro
---

# py-intro

skills/eng0ai/eng0-template-skills/py-intro
py-intro
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill py-intro
SKILL.md
Python Zero To Hero Slides

A Slidev presentation for teaching Python fundamentals with interactive code execution.

Tech Stack
Framework: Slidev (Vue-based)
Feature: Python Runner addon for live code demos
Addons: slidev-addon-python-runner, slidev-addon-rabbit
Themes: apple-basic, bricks, penguin
Package Manager: pnpm
Output: dist directory
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/py-intro-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/py-intro-template.git _temp_template
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

Special Features
Interactive Python code execution in slides
Multiple theme options
Weekly Installs
31
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