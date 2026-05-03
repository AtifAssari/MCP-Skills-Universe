---
title: mantis-react-admin
url: https://skills.sh/eng0ai/eng0-template-skills/mantis-react-admin
---

# mantis-react-admin

skills/eng0ai/eng0-template-skills/mantis-react-admin
mantis-react-admin
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill mantis-react-admin
SKILL.md
Mantis React Admin

A free React admin dashboard with Material UI v7, React 19, Vite 7, and MUI X Charts.

Tech Stack
Framework: React 19
Build Tool: Vite 7
UI Library: Material UI v7, MUI X Charts
Styling: Emotion CSS-in-JS
Routing: React Router v7
State: SWR for data fetching
Package Manager: yarn
Output: dist directory
Dev Port: 5173
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/mantis-react-admin-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/mantis-react-admin-template.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
yarn install

Build
yarn build

Deploy
Vercel (Recommended)
vercel pull --yes -t $VERCEL_TOKEN
vercel build --prod -t $VERCEL_TOKEN
vercel deploy --prebuilt --prod --yes -t $VERCEL_TOKEN

Netlify
netlify deploy --prod --dir=dist

Development
yarn start


Opens at http://localhost:5173

Linting
yarn lint        # Check for issues
yarn lint:fix    # Auto-fix issues
yarn prettier    # Format code

Weekly Installs
53
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