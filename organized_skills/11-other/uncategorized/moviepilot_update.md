---
rating: ⭐⭐⭐
title: moviepilot-update
url: https://skills.sh/jxxghp/moviepilot/moviepilot-update
---

# moviepilot-update

skills/jxxghp/moviepilot/moviepilot-update
moviepilot-update
Installation
$ npx skills add https://github.com/jxxghp/moviepilot --skill moviepilot-update
SKILL.md
MoviePilot System Update & Restart

All script paths are relative to this skill file.

This skill provides capabilities to restart MoviePilot service, check for updates, and perform manual upgrades.

Restart MoviePilot
Method 1: Using REST API (Recommended)

Call the restart endpoint with admin authentication:

# Using moviepilot-api skill
python scripts/mp-api.py GET /api/v1/system/restart


Or with curl:

curl -X GET "http://localhost:3000/api/v1/system/restart" \
  -H "X-API-KEY: <YOUR_API_TOKEN>"


Note: This API will restart the Docker container internally. The service will be briefly unavailable during restart.

Method 2: Using execute_command tool

If you have admin privileges, you can execute the restart command directly:

docker restart moviepilot

Check for Updates
Method 1: Using REST API
python scripts/mp-api.py GET /api/v1/system/versions


This returns all available GitHub releases.

Method 2: Check current version
# Check current version
cat /app/version.py

Upgrade MoviePilot
Option 1: Automatic Update (Recommended)

Set the environment variable MOVIEPILOT_AUTO_UPDATE and restart:

For Docker Compose users:

# Edit docker-compose.yml, add environment variable:
environment:
  - MOVIEPILOT_AUTO_UPDATE=release  # or "dev" for dev版本

# Then restart
docker-compose down && docker-compose up -d


For Docker run users:

docker stop moviepilot
docker rm moviepilot
docker run -d ... -e MOVIEPILOT_AUTO_UPDATE=release jxxghp/moviepilot


The update script (/usr/local/bin/mp_update.sh or /app/docker/update.sh) will automatically:

Check GitHub for latest release
Download new backend code
Update dependencies if changed
Download new frontend
Update site resources
Restart the service
Option 2: Manual Upgrade

If you need to manually download and apply updates:

Get latest release version:

curl -s https://api.github.com/repos/jxxghp/MoviePilot/releases | grep '"tag_name"' | grep "v2" | head -1


Download and extract backend:

# Replace v2.x.x with actual version
curl -L -o /tmp/backend.zip https://github.com/jxxghp/MoviePilot/archive/refs/tags/v2.x.x.zip
unzip -d /tmp/backend /tmp/backend.zip


Backup and replace:

# Backup current installation
cp -r /app /app_backup

# Replace files (exclude config and plugins)
cp -r /tmp/backend/MoviePilot-*/* /app/


Restart MoviePilot:

# Use API or docker restart
python scripts/mp-api.py GET /api/v1/system/restart

Important Notes
Backup first: Before upgrading, backup your configuration and database
Dependencies: Check if requirements.in has changes; if so, update virtual environment
Plugins: The update script automatically backs up and restores plugins
Non-Docker: For non-Docker installations, use git pull or pip install -U moviepilot
Troubleshooting
Issue	Solution
Restart fails	Check if Docker daemon is running; verify container has restart policy
Update fails	Check network connectivity to GitHub; ensure sufficient disk space
Version unchanged	Verify MOVIEPILOT_AUTO_UPDATE environment variable is set correctly
Dependency errors	May need to rebuild virtual environment: pip-compile requirements.in && pip install -r requirements.txt
Environment Variables for Auto-Update
Variable	Value	Description
MOVIEPILOT_AUTO_UPDATE	release	Auto-update to latest stable release
MOVIEPILOT_AUTO_UPDATE	dev	Auto-update to latest dev version
MOVIEPILOT_AUTO_UPDATE	false	Disable auto-update (default)
GITHUB_TOKEN	(token)	GitHub token for higher rate limits
GITHUB_PROXY	(url)	GitHub proxy URL for China users
PROXY_HOST	(url)	Global proxy host
Weekly Installs
53
Repository
jxxghp/moviepilot
GitHub Stars
11.0K
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail