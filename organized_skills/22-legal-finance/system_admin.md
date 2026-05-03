---
rating: ⭐⭐⭐
title: system-admin
url: https://skills.sh/chaterm/terminal-skills/system-admin
---

# system-admin

skills/chaterm/terminal-skills/system-admin
system-admin
Installation
$ npx skills add https://github.com/chaterm/terminal-skills --skill system-admin
SKILL.md
Linux System Administration
Overview

Core commands and best practices for Linux system administration, including system information viewing, resource monitoring, service management, etc.

System Information
Basic Information
# System version
cat /etc/os-release
uname -a

# Hostname
hostnamectl

# Uptime and load
uptime

Hardware Information
# CPU information
lscpu
cat /proc/cpuinfo

# Memory information
free -h
cat /proc/meminfo

# Disk information
lsblk
df -h

Resource Monitoring
Real-time Monitoring
# Comprehensive monitoring
top
htop

# Memory monitoring
vmstat 1

# IO monitoring
iostat -x 1
iotop

# Network monitoring
iftop
nethogs

Historical Data
# System activity report
sar -u 1 10    # CPU
sar -r 1 10    # Memory
sar -d 1 10    # Disk

Service Management
Systemd Services
# Service status
systemctl status service-name
systemctl is-active service-name

# Start/Stop services
systemctl start/stop/restart service-name

# Boot startup
systemctl enable/disable service-name

# View all services
systemctl list-units --type=service

Common Scenarios
Scenario 1: System Health Check
# Quick health check script
echo "=== System Load ===" && uptime
echo "=== Memory Usage ===" && free -h
echo "=== Disk Usage ===" && df -h
echo "=== Failed Services ===" && systemctl --failed

Scenario 2: Troubleshoot High Load
# 1. Check load
uptime

# 2. Find high CPU processes
ps aux --sort=-%cpu | head -10

# 3. Find high memory processes
ps aux --sort=-%mem | head -10

Troubleshooting
Problem	Commands
System lag	top, vmstat 1, iostat -x 1
Disk full	df -h, du -sh /*, ncdu
Memory shortage	free -h, ps aux --sort=-%mem
Service abnormal	systemctl status, journalctl -u
Weekly Installs
262
Repository
chaterm/terminal-skills
GitHub Stars
34
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn