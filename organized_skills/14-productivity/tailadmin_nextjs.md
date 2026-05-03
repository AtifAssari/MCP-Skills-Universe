---
rating: ⭐⭐
title: tailadmin-nextjs
url: https://skills.sh/eng0ai/eng0-template-skills/tailadmin-nextjs
---

# tailadmin-nextjs

skills/eng0ai/eng0-template-skills/tailadmin-nextjs
tailadmin-nextjs
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill tailadmin-nextjs
SKILL.md
TailAdmin Next.js

A free Next.js admin dashboard with 30+ components, dark mode, ApexCharts, calendar, forms, and tables.

Tech Stack
Framework: Next.js 16
React: React 19
Styling: Tailwind CSS 4
Charts: ApexCharts
Package Manager: pnpm
Dev Port: 3000
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/tailadmin-nextjs-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/tailadmin-nextjs-template.git _temp_template
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
netlify deploy --prod

Development
pnpm dev


Opens at http://localhost:3000

Weekly Installs
51
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