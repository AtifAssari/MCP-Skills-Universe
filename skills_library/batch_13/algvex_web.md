---
title: algvex-web
url: https://skills.sh/felixwayne0318/aitrader/algvex-web
---

# algvex-web

skills/felixwayne0318/aitrader/algvex-web
algvex-web
Installation
$ npx skills add https://github.com/felixwayne0318/aitrader --skill algvex-web
SKILL.md
Algvex Website Management

Web interface for AlgVex trading system at algvex.com.

Architecture
                    Caddy (HTTPS)
                    algvex.com:443
                        │
            ┌───────────┴───────────┐
            │                       │
        Frontend                Backend
        (Next.js)              (FastAPI)
      localhost:3000         localhost:8000

Key Information
Item	Value
Domain	algvex.com
Server	139.180.157.152
Frontend	Next.js 14 + TypeScript
Backend	FastAPI + Python 3.12
Database	SQLite
Auth	Google OAuth
Install Path	/home/linuxuser/algvex
Directory Structure
/home/linuxuser/algvex/
├── backend/           # FastAPI backend
│   ├── main.py
│   ├── .env           # Configuration
│   └── algvex.db      # SQLite database
├── frontend/          # Next.js frontend
│   ├── .next/         # Build output
│   └── pages/         # Page components
└── deploy/            # Deployment configs

Deployment Commands
Full Deployment
cd /home/linuxuser/nautilus_AlgVex/web/deploy
chmod +x setup.sh
./setup.sh

Restart Services
sudo systemctl restart algvex-backend algvex-frontend caddy

Check Status
sudo systemctl status algvex-backend
sudo systemctl status algvex-frontend
sudo systemctl status caddy

View Logs
# Backend logs
sudo journalctl -u algvex-backend -f

# Frontend logs
sudo journalctl -u algvex-frontend -f

# Caddy logs
sudo journalctl -u caddy -f

Configuration
Backend Environment (/home/linuxuser/algvex/backend/.env)
# Required
SECRET_KEY=your-secure-key
GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-client-secret
ADMIN_EMAILS=your-email@gmail.com

# AlgVex Integration
ALGVEX_PATH=/home/linuxuser/nautilus_AlgVex
ALGVEX_CONFIG_PATH=/home/linuxuser/nautilus_AlgVex/configs/base.yaml
ALGVEX_SERVICE_NAME=nautilus-trader

Google OAuth Setup
Go to https://console.cloud.google.com/apis/credentials
Create OAuth 2.0 Client ID
Add redirect URI: https://algvex.com/api/auth/callback/google
Copy credentials to .env
API Endpoints
Public (No Auth)
Endpoint	Description
/api/public/performance	Trading stats
/api/public/social-links	Social links
/api/public/copy-trading	Copy trading links
/api/public/system-status	Bot status
Admin (Auth Required)
Endpoint	Description
/api/admin/config	Strategy config
/api/admin/service/control	Service control
/api/admin/social-links/*	Manage links
Caddy Configuration

Located at /etc/caddy/Caddyfile:

algvex.com {
    handle /api/* {
        reverse_proxy localhost:8000
    }
    handle {
        reverse_proxy localhost:3000
    }
}

Common Issues
Issue	Solution
HTTPS not working	Check DNS, wait for Let's Encrypt
502 Bad Gateway	Restart backend/frontend services
OAuth callback error	Verify redirect URI in Google Console
Config not updating	Restart algvex-backend
Key Files
File	Purpose
web/backend/main.py	Backend entry point
web/frontend/pages/index.tsx	Homepage
web/frontend/pages/admin/index.tsx	Admin panel
web/deploy/Caddyfile	Reverse proxy config
web/deploy/setup.sh	Deployment script
Weekly Installs
11
Repository
felixwayne0318/aitrader
GitHub Stars
1
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn