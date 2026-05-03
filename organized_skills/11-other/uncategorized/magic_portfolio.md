---
rating: ⭐⭐
title: magic-portfolio
url: https://skills.sh/eng0ai/eng0-template-skills/magic-portfolio
---

# magic-portfolio

skills/eng0ai/eng0-template-skills/magic-portfolio
magic-portfolio
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill magic-portfolio
SKILL.md
Magic Portfolio

A simple, clean portfolio template with MDX-based blog and projects, automatic SEO, gallery, and endless theming options.

Tech Stack
Framework: Next.js 16
React: React 19
UI: Once UI
Styling: Sass
Content: MDX
Package Manager: npm
Dev Port: 3000
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/magic-portfolio-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/magic-portfolio-template.git _temp_template
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
Vercel (Recommended)
vercel pull --yes -t $VERCEL_TOKEN
vercel build --prod -t $VERCEL_TOKEN
vercel deploy --prebuilt --prod --yes -t $VERCEL_TOKEN

Netlify
netlify deploy --prod --dir=.next

Customization
src/resources/once-ui.config.js - Theme and UI settings
src/resources/content.js - Site content
src/app/blog/posts/ - Blog posts in MDX
src/app/work/projects/ - Project case studies
Development
npm run dev


Opens at http://localhost:3000

Requires Node.js v18.17+

Weekly Installs
46
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