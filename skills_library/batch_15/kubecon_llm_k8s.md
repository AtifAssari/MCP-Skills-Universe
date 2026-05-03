---
title: kubecon-llm-k8s
url: https://skills.sh/eng0ai/eng0-template-skills/kubecon-llm-k8s
---

# kubecon-llm-k8s

skills/eng0ai/eng0-template-skills/kubecon-llm-k8s
kubecon-llm-k8s
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill kubecon-llm-k8s
SKILL.md
KubeCon LLM K8s Slides

A Slidev presentation about taming dependency chaos for LLM in Kubernetes.

Tech Stack
Framework: Slidev (Vue-based)
Icons: Carbon, Logos, Simple Icons, DevIcon, Fluent, Twemoji
Package Manager: pnpm
Output: dist directory
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/kubecon-llm-k8s-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/kubecon-llm-k8s-template.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
pnpm install

Build
pnpm build


Use npm run build (not build-base) for standard deployment without custom base path.

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
26
Repository
eng0ai/eng0-tem…e-skills
GitHub Stars
4
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass