---
title: langchain-agent
url: https://skills.sh/eng0ai/eng0-template-skills/langchain-agent
---

# langchain-agent

skills/eng0ai/eng0-template-skills/langchain-agent
langchain-agent
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill langchain-agent
SKILL.md
LangChain Agent

An AI agent with tools (search engine and calculator) powered by LangGraph and the Vercel AI SDK.

Tech Stack
Framework: Next.js
AI: LangChain.js, LangGraph, AI SDK
Database: PostgreSQL
Package Manager: pnpm
Prerequisites
PostgreSQL database
OpenAI API key
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/langchain-agent.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/langchain-agent.git _temp_template
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
OPENAI_API_KEY - OpenAI API key for the agent
Build
pnpm build

Development
pnpm dev

Weekly Installs
35
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