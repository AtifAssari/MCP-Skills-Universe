---
title: fastapi-fullstack
url: https://skills.sh/eng0ai/eng0-template-skills/fastapi-fullstack
---

# fastapi-fullstack

skills/eng0ai/eng0-template-skills/fastapi-fullstack
fastapi-fullstack
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill fastapi-fullstack
SKILL.md
FastAPI Full Stack

A Python full-stack application with FastAPI backend.

Tech Stack
Backend: FastAPI, Python
Frontend: React
Database: PostgreSQL
ORM: SQLAlchemy
Prerequisites
Python 3.11+
Docker (recommended)
Setup
1. Clone the Template
git clone --depth 1 https://github.com/tiangolo/full-stack-fastapi-template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/tiangolo/full-stack-fastapi-template.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Setup with Docker (Recommended)
docker compose up -d

4. Or Setup Manually
cd backend
pip install -r requirements.txt

Development

With Docker:

docker compose up -d


Manual:

cd backend
uvicorn main:app --reload

Weekly Installs
37
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