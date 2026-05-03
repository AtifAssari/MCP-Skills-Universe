---
title: tanstack-chat-netlify
url: https://skills.sh/eng0ai/eng0-template-skills/tanstack-chat-netlify
---

# tanstack-chat-netlify

skills/eng0ai/eng0-template-skills/tanstack-chat-netlify
tanstack-chat-netlify
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill tanstack-chat-netlify
SKILL.md
TanStack Chat (Netlify)

A modern chat application with TanStack Router and Claude AI.

Tech Stack
Framework: React
Router: TanStack Router
AI: Claude AI integration
Package Manager: npm
Setup
1. Clone the Template
git clone --depth 1 https://github.com/netlify-templates/tanstack-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/netlify-templates/tanstack-template.git _temp_template
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
28
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