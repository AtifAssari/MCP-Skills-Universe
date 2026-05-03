---
rating: ⭐⭐⭐
title: zitadel-identity
url: https://skills.sh/dimdasci/vps-setup/zitadel-identity
---

# zitadel-identity

skills/dimdasci/vps-setup/zitadel-identity
zitadel-identity
Installation
$ npx skills add https://github.com/dimdasci/vps-setup --skill zitadel-identity
SKILL.md
Zitadel Identity Provider

Zitadel is a modern identity management platform providing OIDC, OAuth2, and SAML authentication. This skill covers Docker deployment with Caddy reverse proxy.

Quick Reference
Task	Command/Location
Console UI	https://auth.example.com/ui/console
OIDC Discovery	https://auth.example.com/.well-known/openid-configuration
Health check	curl https://auth.example.com/healthz
View logs	docker compose logs -f zitadel zitadel-login
Restart	docker compose restart zitadel zitadel-login
Architecture
Internet → Caddy (80/443) → Zitadel API (h2c://zitadel:8080)
                          → Login UI (http://zitadel-login:3000)

PostgreSQL ← zitadel-init (runs once)
           ← zitadel (API server)


Three containers:

zitadel-init - Database initialization (runs once, exits)
zitadel - API server (gRPC/REST on port 8080)
zitadel-login - Login UI (port 3000)
Essential Environment Variables
# Required
ZITADEL_MASTERKEY=<32-char-random-string>
ZITADEL_DATABASE_POSTGRES_HOST=postgres
ZITADEL_DATABASE_POSTGRES_USER_PASSWORD=<password>
ZITADEL_EXTERNALDOMAIN=auth.example.com
ZITADEL_EXTERNALPORT=443
ZITADEL_EXTERNALSECURE=true
ZITADEL_TLS_ENABLED=false  # Caddy handles TLS


Generate masterkey: tr -dc A-Za-z0-9 </dev/urandom | head -c 32

Caddy Configuration

Critical: Use h2c:// for HTTP/2 cleartext (required for gRPC):

auth.example.com {
    handle /ui/v2/login/* {
        reverse_proxy http://zitadel-login:3000
    }
    handle {
        reverse_proxy h2c://zitadel:8080
    }
}

Deployment Steps

Start PostgreSQL:

docker compose up -d postgres


Initialize database:

docker compose run zitadel-init


Start services:

docker compose up -d zitadel zitadel-login caddy


Verify health:

curl https://auth.example.com/healthz


Access console:

https://auth.example.com/ui/console

Creating OIDC Applications
Console → Organization → Projects → Applications → + New
Select application type (Web, Native, API)
Configure redirect URIs
Save and copy Client ID and Client Secret

Common redirect URIs:

Nextcloud: https://files.example.com/apps/user_oidc/code
Windmill: https://windmill.example.com/user/login_callback/zitadel
Service Users (API Access)
Console → Users → Service Users → + New
Create Personal Access Token (PAT)
Assign roles (Org Owner, Project Owner)
Use in API calls:
curl -H "Authorization: Bearer <PAT>" \
  https://auth.example.com/management/v1/orgs/me

Reference Files
File	When to Read
configuration.md	Environment variables, config file options
caddy-integration.md	Reverse proxy setup, h2c configuration
oidc-applications.md	Creating apps, Nextcloud integration
api-reference.md	REST/gRPC endpoints, authentication
troubleshooting.md	Common issues and diagnostics
Official Documentation
Topic	URL
Self-Hosting	https://zitadel.com/docs/self-hosting/deploy/overview
Configuration	https://zitadel.com/docs/self-hosting/manage/configure
Caddy Setup	https://zitadel.com/docs/self-hosting/manage/reverseproxy/caddy
OIDC Integration	https://zitadel.com/docs/guides/integrate/login/oidc
API Reference	https://zitadel.com/docs/apis/introduction
Service Users	https://zitadel.com/docs/guides/integrate/service-users/personal-access-token
Troubleshooting Quick Guide
Issue	Check
Container won't start	docker compose logs zitadel - check masterkey (32 chars)
Login page blank	docker compose ps zitadel-login - check Caddy routes
gRPC errors	Ensure h2c:// in Caddyfile, not http://
OIDC 404	curl https://auth.example.com/healthz - check external domain
Token invalid	Check issuer URL matches, token not expired
Weekly Installs
15
Repository
dimdasci/vps-setup
First Seen
Feb 11, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass