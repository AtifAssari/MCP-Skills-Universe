---
rating: ⭐⭐
title: dillion-portfolio
url: https://skills.sh/eng0ai/eng0-template-skills/dillion-portfolio
---

# dillion-portfolio

skills/eng0ai/eng0-template-skills/dillion-portfolio
dillion-portfolio
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill dillion-portfolio
SKILL.md
Dillion Portfolio

A minimalist developer portfolio with blog, work experience timeline, and project showcase.

Tech Stack
Framework: Next.js 14
React: React 18
Animation: Framer Motion
Styling: Tailwind CSS, shadcn/ui
Content: MDX for blog
Package Manager: pnpm
Dev Port: 3000
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/portfolio-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/portfolio-template.git _temp_template
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
netlify deploy --prod --dir=.next

Customization

Edit content in the src/data/ directory:

resume.tsx - Personal info, work experience, education, projects

Portfolio content is stored in content/ directory as MDX files.

Development
pnpm dev


Opens at http://localhost:3000

Weekly Installs
32
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