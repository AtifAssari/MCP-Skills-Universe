---
rating: ⭐⭐
title: happiness-dashboard
url: https://skills.sh/eng0ai/eng0-template-skills/happiness-dashboard
---

# happiness-dashboard

skills/eng0ai/eng0-template-skills/happiness-dashboard
happiness-dashboard
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill happiness-dashboard
SKILL.md
Happiness Dashboard

An interactive data dashboard using Evidence framework - write SQL queries in markdown to create visualizations.

Tech Stack
Framework: Evidence
Database: DuckDB (embedded)
Frontend: Svelte
Package Manager: pnpm
Output: build directory
Dev Port: 3000
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/happiness-dashboard-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/happiness-dashboard-template.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
pnpm install

4. Process Data Sources
pnpm run sources

Build
pnpm run build


Generates static site in build/ directory.

Deploy
Vercel (Recommended)
vercel pull --yes -t $VERCEL_TOKEN
vercel build --prod -t $VERCEL_TOKEN
vercel deploy --prebuilt --prod --yes -t $VERCEL_TOKEN


Important: Deploy from project root, not build/ directory.

Netlify
netlify deploy --prod --dir=build

Data Sources

CSV files in sources/happiness_score/:

hs2024.csv - Current year happiness data
hsArchive.csv - Historical happiness data
Notes
Use pnpm (not npm) - .npmrc has shamefully-hoist=true for Evidence compatibility
Build locally - Vercel/Netlify build can timeout due to DuckDB compilation (40+ min)
Uses CSV files, no database setup needed
Never run pnpm run dev in VM environment
Weekly Installs
27
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