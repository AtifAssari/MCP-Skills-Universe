---
title: fastapi-backend-template
url: https://skills.sh/eng0ai/eng0-template-skills/fastapi-backend-template
---

# fastapi-backend-template

skills/eng0ai/eng0-template-skills/fastapi-backend-template
fastapi-backend-template
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill fastapi-backend-template
SKILL.md
FastAPI Backend Template

FastAPI with PostgreSQL, async SQLAlchemy 2.0, Alembic migrations, and Docker.

Tech Stack
Framework: FastAPI
Language: Python
ORM: SQLAlchemy 2.0 (async)
Migrations: Alembic
Database: PostgreSQL
Prerequisites
Python 3.11+
Docker (recommended)
PostgreSQL
Setup
1. Clone the Template
git clone --depth 1 https://github.com/Aeternalis-Ingenium/FastAPI-Backend-Template.git .


If the directory is not empty:

git clone --depth 1 https://github.com/Aeternalis-Ingenium/FastAPI-Backend-Template.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Setup Virtual Environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

4. Setup Database

Configure PostgreSQL and run Alembic migrations.

Development
uvicorn main:app --reload

Weekly Installs
126
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