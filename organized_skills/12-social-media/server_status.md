---
rating: ⭐⭐⭐
title: server-status
url: https://skills.sh/felixwayne0318/aitrader/server-status
---

# server-status

skills/felixwayne0318/aitrader/server-status
server-status
Installation
$ npx skills add https://github.com/felixwayne0318/aitrader --skill server-status
SKILL.md
Server Status Check
Server Information
Item	Value
IP	139.180.157.152
User	linuxuser
Service	nautilus-trader
Path	/home/linuxuser/nautilus_AlgVex
Check Commands
Service Status
sudo systemctl status nautilus-trader

View Logs
# Last 50 lines
sudo journalctl -u nautilus-trader -n 50 --no-hostname

# Real-time follow
sudo journalctl -u nautilus-trader -f --no-hostname

Check Processes
ps aux | grep main_live.py

Status Indicators
✅ Normal Operation
🚀 *Strategy Started*
📊 *Instrument*: BTCUSDT-PERP
Active: active (running)

❌ Common Errors
Error	Cause	Solution
can't open file 'main.py'	Wrong entry file	Change ExecStart to main_live.py
EOFError: EOF when reading a line	Missing env var	Add Environment=AUTO_CONFIRM=true
telegram.error.Conflict	Telegram conflict	Does not affect trading, can ignore
Quick Diagnosis

If service is abnormal, check in this order:

Service Status: sudo systemctl status nautilus-trader
Recent Logs: sudo journalctl -u nautilus-trader -n 100 --no-hostname
Config File: cat /etc/systemd/system/nautilus-trader.service
Entry File: Confirm it's main_live.py
Weekly Installs
14
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