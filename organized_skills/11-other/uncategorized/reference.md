---
rating: ⭐⭐⭐
title: reference
url: https://skills.sh/mwguerra/claude-code-plugins/reference
---

# reference

skills/mwguerra/claude-code-plugins/reference
reference
Installation
$ npx skills add https://github.com/mwguerra/claude-code-plugins --skill reference
SKILL.md
docker-local Reference

Quick reference for docker-local Laravel development environment.

When to Use

Use this reference when you need details about:

Service credentials and ports
docker-local CLI commands
File paths and project structure
.env configuration requirements
Service Credentials (Defaults)
Service	Host	Port	User	Password
MySQL	mysql	3306	laravel	secret
PostgreSQL	postgres	5432	laravel	secret
Redis	redis	6379	-	-
Mailpit	mailpit	1025	-	-
MinIO	minio	9000	minio	minio123

Root MySQL password: secret

URLs
Service	URL
Projects	https://{project}.test
Subdomains	https://{sub}.{project}.test
Traefik	https://traefik.localhost:8080
Mailpit	https://mail.localhost
MinIO Console	https://minio.localhost
Key Commands
Status & Health
docker-local status          # Check all services and containers
docker-local doctor          # Full health check with diagnostics
docker-local fix             # Auto-fix common issues

Container Management
docker-local up              # Start all containers
docker-local down            # Stop all containers
docker-local restart         # Restart all containers
docker-local logs [service]  # View logs (nginx, php, mysql, redis, traefik)

Project Management
docker-local link            # Rescan and link all projects
docker-local list            # List all detected projects
docker-local make:laravel X  # Create new Laravel project
docker-local open [project]  # Open project in browser

SSL Certificates
docker-local ssl:status      # Check certificate status
docker-local ssl:regenerate  # Regenerate all certificates

Database
docker-local db:create X     # Create MySQL database
docker-local db:mysql        # Open MySQL CLI
docker-local db:postgres     # Open PostgreSQL CLI
docker-local db:redis        # Open Redis CLI
docker-local db:fresh        # Run migrate:fresh --seed

Environment
docker-local env:check       # Check .env for conflicts
docker-local config          # Show current configuration

File Paths
Path	Purpose
~/projects/	Default projects directory
~/projects/.docker-local-links/	Symlinks for Nginx routing
~/.config/docker-local/	Configuration directory
~/.config/docker-local/config.json	Main config file
~/.config/docker-local/certs/	SSL certificates
Required .env Settings

For Laravel projects to work with docker-local:

APP_URL=https://myproject.test

# Database (MySQL)
DB_CONNECTION=mysql
DB_HOST=mysql
DB_PORT=3306
DB_DATABASE=myproject
DB_USERNAME=laravel
DB_PASSWORD=secret

# Redis
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_PASSWORD=null

# Cache/Session/Queue isolation (unique per project)
CACHE_PREFIX=myproject_
REDIS_CACHE_DB=0
REDIS_SESSION_DB=1
REDIS_QUEUE_DB=2

# Mail
MAIL_MAILER=smtp
MAIL_HOST=mailpit
MAIL_PORT=1025

# S3/MinIO (optional)
AWS_ACCESS_KEY_ID=minio
AWS_SECRET_ACCESS_KEY=minio123
AWS_DEFAULT_REGION=us-east-1
AWS_BUCKET=myproject
AWS_ENDPOINT=http://minio:9000
AWS_USE_PATH_STYLE_ENDPOINT=true

Troubleshooting Quick Reference
Symptom	Likely Cause	Fix
404 error	Missing symlink	docker-local link
"Site can't be reached"	DNS not configured	Check /etc/hosts or dnsmasq
Certificate error	Certs not generated	docker-local ssl:regenerate
Certificate still failing	mkcert not trusted	sudo mkcert -install
Container unhealthy	Service crash	docker-local restart
DB connection refused	Wrong DB_HOST	Use mysql not 127.0.0.1
Multi-Project Isolation

Each project needs unique values to avoid conflicts:

Database name - Unique per project
Redis DBs - 3 DBs per project (0-2, 3-5, 6-8, etc.)
Cache prefix - Unique string per project
MinIO bucket - Unique per project

Use docker-local env:check --all to detect conflicts across projects.

Weekly Installs
14
Repository
mwguerra/claude…-plugins
GitHub Stars
29
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail