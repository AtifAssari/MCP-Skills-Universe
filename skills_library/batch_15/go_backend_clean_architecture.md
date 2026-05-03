---
title: go-backend-clean-architecture
url: https://skills.sh/eng0ai/eng0-template-skills/go-backend-clean-architecture
---

# go-backend-clean-architecture

skills/eng0ai/eng0-template-skills/go-backend-clean-architecture
go-backend-clean-architecture
Installation
$ npx skills add https://github.com/eng0ai/eng0-template-skills --skill go-backend-clean-architecture
SKILL.md
Go Clean Architecture

A Go backend with Gin, MongoDB, JWT authentication, and Docker support following Clean Architecture principles.

Tech Stack
Framework: Gin
Language: Go
Database: MongoDB
Auth: JWT
Architecture: Clean Architecture
Prerequisites
Go 1.21+
MongoDB
Docker (optional)
Setup
1. Clone the Template
git clone --depth 1 https://github.com/amitshekhariitbhu/go-backend-clean-architecture.git .


If the directory is not empty:

git clone --depth 1 https://github.com/amitshekhariitbhu/go-backend-clean-architecture.git _temp_template
mv _temp_template/* _temp_template/.* . 2>/dev/null || true
rm -rf _temp_template

2. Remove Git History (Optional)
rm -rf .git
git init

3. Install Dependencies
go mod download

4. Setup Environment

Configure MongoDB connection and JWT secret.

Build
go build -o app ./cmd/main.go

Development
go run ./cmd/main.go

Weekly Installs
67
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