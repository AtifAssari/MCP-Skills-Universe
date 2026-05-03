---
rating: ⭐⭐
title: content-ops-netlify
url: https://skills.sh/eng0ai/eng0-template-skills/content-ops-netlify
---

# content-ops-netlify

skills/eng0ai/eng0-template-skills/content-ops-netlify
content-ops-netlify
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill content-ops-netlify
SKILL.md
Content Ops Starter (Netlify)

A flexible content model with visual editing.

Tech Stack
Framework: Next.js
Package Manager: npm
Setup
1. Clone the Template
git clone --depth 1 https://github.com/netlify-templates/content-ops-starter.git .


If the directory is not empty:

git clone --depth 1 https://github.com/netlify-templates/content-ops-starter.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
npm install

Build
npm run build

Deploy to Netlify
netlify deploy --prod

Development
npm run dev

Weekly Installs
30
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