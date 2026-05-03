---
rating: ⭐⭐
title: langchain-retrieval-agent
url: https://skills.sh/eng0ai/eng0-template-skills/langchain-retrieval-agent
---

# langchain-retrieval-agent

skills/eng0ai/eng0-template-skills/langchain-retrieval-agent
langchain-retrieval-agent
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill langchain-retrieval-agent
SKILL.md
LangChain Retrieval Agent

An AI agent with retrieval tool for document Q&A using RAG, powered by LangGraph.

Tech Stack
Framework: Next.js
AI: LangChain.js, LangGraph, AI SDK
Vector Store: Supabase pgvector
Package Manager: pnpm
Prerequisites
Supabase project with pgvector extension
OpenAI API key
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/langchain-retrieval-agent.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/langchain-retrieval-agent.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
pnpm install

4. Setup Environment Variables
SUPABASE_URL - Supabase project URL
SUPABASE_PRIVATE_KEY - Supabase service role key
OPENAI_API_KEY - For embeddings and LLM
Build
pnpm build

Development
pnpm dev

Weekly Installs
34
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