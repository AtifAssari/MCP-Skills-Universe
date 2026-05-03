---
title: deploy
url: https://skills.sh/felixwayne0318/aitrader/deploy
---

# deploy

skills/felixwayne0318/aitrader/deploy
deploy
Installation
$ npx skills add https://github.com/felixwayne0318/aitrader --skill deploy
SKILL.md
Deploy Trading Bot
Key Information
Item	Value
Entry File	main_live.py (NOT main.py!)
Server	139.180.157.152
User	linuxuser
Path	/home/linuxuser/nautilus_AlgVex
Service	nautilus-trader
Branch	main
Config	~/.env.algvex (permanent storage)
Configuration Management
Location	Description
~/.env.algvex	Permanent storage, survives reinstall
.env	Symlink to ~/.env.algvex
# Edit configuration
nano ~/.env.algvex

# Check symlink
ls -la /home/linuxuser/nautilus_AlgVex/.env

Deployment Commands
Complete Reinstall
curl -fsSL https://raw.githubusercontent.com/FelixWayne0318/AlgVex/main/reinstall.sh | bash

Update and Restart
cd /home/linuxuser/nautilus_AlgVex
git pull origin main
sudo systemctl restart nautilus-trader

Check Status
sudo systemctl status nautilus-trader
sudo journalctl -u nautilus-trader -n 30 --no-hostname

systemd Service Configuration
[Unit]
Description=Nautilus AlgVex Bot
After=network.target

[Service]
Type=simple
User=linuxuser
WorkingDirectory=/home/linuxuser/nautilus_AlgVex
Environment="PATH=/home/linuxuser/nautilus_AlgVex/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
Environment="AUTO_CONFIRM=true"
EnvironmentFile=-/home/linuxuser/nautilus_AlgVex/.env
ExecStart=/home/linuxuser/nautilus_AlgVex/venv/bin/python main_live.py
Restart=on-failure
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target

Common Errors
Error	Cause	Solution
can't open file 'main.py'	Wrong entry file	Use main_live.py
EOFError: EOF when reading a line	Missing AUTO_CONFIRM	Add Environment=AUTO_CONFIRM=true
Service keeps restarting	Config error	Check ExecStart path
.env missing	Broken symlink	ln -sf ~/.env.algvex .env
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
SnykFail