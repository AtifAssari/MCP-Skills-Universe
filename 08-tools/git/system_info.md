---
title: system-info
url: https://skills.sh/ukgovernmentbeis/inspect_ai/system-info
---

# system-info

skills/ukgovernmentbeis/inspect_ai/system-info
system-info
Installation
$ npx skills add https://github.com/ukgovernmentbeis/inspect_ai --skill system-info
SKILL.md
System Information Skill

Gathers comprehensive system information about the Linux host.

Suggested Workflow
Run ./scripts/sysinfo.sh for structured output covering OS, CPU, memory, and uptime.
Use individual commands below for specific details or when the script is unavailable.
Commands Reference
Operating System
cat /etc/os-release - Distribution name and version
uname -a - Kernel version and architecture
hostnamectl - Hostname and OS info (systemd systems)
CPU Information
lscpu - CPU architecture details (cores, threads, model)
cat /proc/cpuinfo | head -30 - Detailed processor info
nproc - Number of available processors
Memory Information
free -h - Memory and swap usage (human-readable)
cat /proc/meminfo | head -10 - Detailed memory statistics
System Uptime
uptime - How long the system has been running
cat /proc/loadavg - Load averages
Tips
The sysinfo.sh script outputs structured text (distribution, kernel, CPU model, cores, memory, uptime) suitable for parsing
Use lscpu for the most readable CPU information
Memory values in /proc/meminfo are in kilobytes
Weekly Installs
56
Repository
ukgovernmentbei…spect_ai
GitHub Stars
2.0K
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass