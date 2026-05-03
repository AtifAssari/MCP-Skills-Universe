---
title: natural-language-postgres
url: https://skills.sh/eng0ai/eng0-template-skills/natural-language-postgres
---

# natural-language-postgres

skills/eng0ai/eng0-template-skills/natural-language-postgres
natural-language-postgres
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill natural-language-postgres
SKILL.md
Natural Language Postgres

A demo app that lets you ask questions in plain English and get answers from your database.

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
git clone --depth 1 https://github.com/Eng0AI/natural-language-postgres.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/natural-language-postgres.git _temp_template
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
33
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