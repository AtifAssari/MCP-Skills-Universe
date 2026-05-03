---
rating: ⭐⭐
title: natural-language-postgres-presentation
url: https://skills.sh/eng0ai/eng0-template-skills/natural-language-postgres-presentation
---

# natural-language-postgres-presentation

skills/eng0ai/eng0-template-skills/natural-language-postgres-presentation
natural-language-postgres-presentation
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill natural-language-postgres-presentation
SKILL.md
Natural Language Postgres Presentation

A presentation-focused Natural Language to SQL app with PPT-style visualizations for showcasing data insights.

Tech Stack
Framework: Next.js
AI: AI SDK
Database: PostgreSQL
Package Manager: pnpm
Prerequisites
PostgreSQL database
OpenAI API key or other LLM provider
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/natural-language-postgres-presentation.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/natural-language-postgres-presentation.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
pnpm install

4. Setup Environment Variables

Create .env with required variables:

POSTGRES_URL - PostgreSQL connection string
OPENAI_API_KEY or other LLM provider key
Build
pnpm build

Development
pnpm dev

Weekly Installs
29
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