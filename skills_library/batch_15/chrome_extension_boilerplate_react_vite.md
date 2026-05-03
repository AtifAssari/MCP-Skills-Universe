---
title: chrome-extension-boilerplate-react-vite
url: https://skills.sh/eng0ai/eng0-template-skills/chrome-extension-boilerplate-react-vite
---

# chrome-extension-boilerplate-react-vite

skills/eng0ai/eng0-template-skills/chrome-extension-boilerplate-react-vite
chrome-extension-boilerplate-react-vite
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill chrome-extension-boilerplate-react-vite
SKILL.md
Chrome Extension Boilerplate

Chrome Extension Boilerplate with React + Vite + TypeScript.

Tech Stack
Framework: React
Build Tool: Vite
Language: TypeScript
Package Manager: pnpm
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Jonghakseo/chrome-extension-boilerplate-react-vite.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Jonghakseo/chrome-extension-boilerplate-react-vite.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
pnpm install

Build
pnpm build

Development
pnpm dev

Loading Extension
Build the extension
Open Chrome and go to chrome://extensions/
Enable "Developer mode"
Click "Load unpacked" and select the dist folder
Weekly Installs
71
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