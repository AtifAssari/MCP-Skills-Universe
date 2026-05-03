---
rating: ⭐⭐
title: network-diagnostics
url: https://skills.sh/jackspace/claudeskillz/network-diagnostics
---

# network-diagnostics

skills/jackspace/claudeskillz/network-diagnostics
network-diagnostics
Installation
$ npx skills add https://github.com/jackspace/claudeskillz --skill network-diagnostics
SKILL.md
Network-diagnostics
Instructions

For network troubleshooting:

MTU Issues (common in WSL)
Check current MTU: ip link show
Test different MTU: sudo ip link set dev eth0 mtu 1350
Common WSL MTU: 1300-1400
DNS Resolution
Check /etc/resolv.conf
Test with: dig google.com, nslookup google.com
Try different DNS: 8.8.8.8, 1.1.1.1
Connectivity Tests
Ping gateway: ip route | grep default
Traceroute to destination
Test ports: nc -zv host port, telnet host port
Firewall/Routing
Check iptables: sudo iptables -L
Review routes: ip route show
WSL: Check Windows Firewall
Service Status
Verify service is running
Check listening ports: ss -tlnp, netstat -tlnp
Generate scripts to persist fixes
Include checks for WSL vs native Linux
Add rollback mechanisms
Examples

Add examples of how to use this skill here.

Notes
This skill was auto-generated
Edit this file to customize behavior
Weekly Installs
58
Repository
jackspace/claudeskillz
GitHub Stars
14
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn