---
title: deno-monorepo-template
url: https://skills.sh/eng0ai/eng0-template-skills/deno-monorepo-template
---

# deno-monorepo-template

skills/eng0ai/eng0-template-skills/deno-monorepo-template
deno-monorepo-template
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill deno-monorepo-template
SKILL.md
Deno Monorepo

A Deno monorepo with Hono, tRPC, Drizzle, and Supabase.

Tech Stack
Runtime: Deno
Framework: Hono
RPC: tRPC
ORM: Drizzle
Database: Supabase
Prerequisites
Deno installed
Supabase project
Setup
1. Clone the Template
git clone --depth 1 https://github.com/runreal/deno-monorepo-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/runreal/deno-monorepo-template.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
deno install

4. Setup Environment

Configure Supabase credentials.

Development
deno task dev

Weekly Installs
31
Repository
eng0ai/eng0-tem…e-skills
GitHub Stars
4
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass