---
title: langchain-retrieval
url: https://skills.sh/eng0ai/eng0-template-skills/langchain-retrieval
---

# langchain-retrieval

skills/eng0ai/eng0-template-skills/langchain-retrieval
langchain-retrieval
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill langchain-retrieval
SKILL.md
LangChain Retrieval

Document Q&A with RAG (Retrieval Augmented Generation) using Supabase vector store.

Tech Stack
Framework: Next.js
AI: LangChain.js, AI SDK
Vector Store: Supabase pgvector
Package Manager: pnpm
Prerequisites
Supabase project with pgvector extension
OpenAI API key
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Eng0AI/langchain-retrieval.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Eng0AI/langchain-retrieval.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
pnpm install

4. Setup Environment Variables

Create .env with required variables:

SUPABASE_URL - Supabase project URL
SUPABASE_PRIVATE_KEY - Supabase service role key
OPENAI_API_KEY - For embeddings and LLM
SUPABASE_DB_URL - Direct PostgreSQL connection URL
5. Setup Vector Store

Initialize pgvector extension and create documents table in Supabase.

Build
pnpm build

Development
pnpm dev

Weekly Installs
32
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