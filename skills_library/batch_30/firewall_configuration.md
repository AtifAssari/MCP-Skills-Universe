---
title: firewall-configuration
url: https://skills.sh/mikr13/secure-server-setup-skills/firewall-configuration
---

# firewall-configuration

skills/mikr13/secure-server-setup-skills/firewall-configuration
firewall-configuration
Installation
$ npx skills add https://github.com/mikr13/secure-server-setup-skills --skill firewall-configuration
SKILL.md
Firewall Configuration Skill

Configure UFW firewall to control network traffic and minimize attack surface on VPS servers.

What This Skill Does

This skill helps AI agents configure UFW (Uncomplicated Firewall) on Ubuntu/Debian servers. Without a firewall, every port is potentially accessible to the internet. A properly configured firewall creates a security perimeter that only allows necessary traffic.

Key capabilities:

Install and enable UFW firewall
Set secure default policies (deny incoming, allow outgoing)
Open specific ports for required services
Configure application-specific rules
Manage firewall rules and verify configuration
Handle IPv4 and IPv6 traffic
When to Use

Use this skill when you need to:

Set up a new VPS server with network security
Restrict network access to only required services
Implement defense in depth security
Fix security audit findings related to open ports
Comply with security best practices
Protect services from unauthorized access

Critical understanding: Every open port is attack surface. Only open ports for services you're actually running.

Prerequisites
Root or sudo access to the server
Ubuntu or Debian-based Linux distribution
Active SSH session (firewall must allow SSH before enabling!)
Knowledge of which services/ports you need open
Firewall Setup Steps
Step 1: Install UFW

UFW is usually pre-installed on Ubuntu. Install if missing:

sudo apt update
sudo apt install ufw -y

Step 2: Set Default Policies

CRITICAL: Set these BEFORE enabling the firewall!

# Deny all incoming traffic by default
sudo ufw default deny incoming

# Allow all outgoing traffic by default
sudo ufw default allow outgoing


This creates a "whitelist" approach - nothing gets in unless explicitly allowed.

Step 3: Allow SSH (CRITICAL!)

WARNING: You must allow SSH before enabling UFW, or you'll lock yourself out!

sudo ufw allow ssh


Or specify the port number explicitly:

sudo ufw allow 22/tcp


If you changed SSH to a custom port (e.g., 2222):

sudo ufw allow 2222/tcp

Step 4: Allow Required Services

Add rules for services you're actually running:

Web Server (HTTP/HTTPS):

sudo ufw allow 80/tcp   # HTTP
sudo ufw allow 443/tcp  # HTTPS


Or use application profiles:

sudo ufw allow 'Nginx Full'
# or
sudo ufw allow 'Apache Full'


Common services:

# FTP
sudo ufw allow 21/tcp

# MySQL (only if remote access needed)
sudo ufw allow 3306/tcp

# PostgreSQL (only if remote access needed)
sudo ufw allow 5432/tcp

# SMTP
sudo ufw allow 25/tcp

# DNS
sudo ufw allow 53

# Custom application
sudo ufw allow 8080/tcp

Step 5: Enable UFW

After confirming SSH is allowed:

sudo ufw enable


Confirm when prompted. The firewall is now active.

Step 6: Verify Configuration

Check firewall status and rules:

sudo ufw status verbose


Expected output:

Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere
80/tcp                     ALLOW IN    Anywhere
443/tcp                    ALLOW IN    Anywhere

Advanced Firewall Configuration
Allow from Specific IPs

Restrict access to specific IP addresses:

# Allow SSH only from specific IP
sudo ufw allow from 203.0.113.10 to any port 22

# Allow MySQL only from application server
sudo ufw allow from 203.0.113.20 to any port 3306

# Allow entire subnet
sudo ufw allow from 192.168.1.0/24

Deny Specific IPs

Block malicious IPs:

sudo ufw deny from 203.0.113.100

Port Ranges

Open a range of ports:

sudo ufw allow 6000:6007/tcp

Limit Connections (Rate Limiting)

Protect against brute-force attacks:

# Limit SSH connections (max 6 in 30 seconds)
sudo ufw limit 22/tcp


This works well for SSH but fail2ban is better for comprehensive protection.

Delete Rules

Remove a firewall rule:

# By rule number (get number from 'ufw status numbered')
sudo ufw status numbered
sudo ufw delete 3

# By rule specification
sudo ufw delete allow 80/tcp

Application Profiles

List available application profiles:

sudo ufw app list


Show profile details:

sudo ufw app info 'Nginx Full'


Create custom application profile in /etc/ufw/applications.d/myapp:

[MyApp]
title=My Application
description=My custom application
ports=8080,8443/tcp


Then reload and use:

sudo ufw app update MyApp
sudo ufw allow 'MyApp'

UFW Management Commands
Check Status
# Basic status
sudo ufw status

# Detailed status
sudo ufw status verbose

# Numbered rules (for deletion)
sudo ufw status numbered

Enable/Disable
# Enable firewall
sudo ufw enable

# Disable firewall (temporarily)
sudo ufw disable

# Reload rules
sudo ufw reload

Reset UFW

WARNING: This removes ALL rules!

sudo ufw reset

Logging
# Enable logging
sudo ufw logging on

# Set logging level (low, medium, high, full)
sudo ufw logging medium

# Disable logging
sudo ufw logging off


View logs:

sudo tail -f /var/log/ufw.log

Common Firewall Configurations
Basic Web Server
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable

Web + Database Server
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow from 203.0.113.0/24 to any port 3306  # DB from app servers only
sudo ufw enable

Restricted SSH Access
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow from 203.0.113.10 to any port 22  # SSH from office IP only
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable

Security Best Practices
Default deny - Start with deny all, then allow specific services
Minimal ports - Only open what you actually use
IP restrictions - Limit admin access to known IPs when possible
Regular audits - Review rules periodically: sudo ufw status numbered
Combine with fail2ban - Add dynamic blocking for brute-force attempts
Monitor logs - Check /var/log/ufw.log for suspicious activity
Test before enabling - Always allow SSH first!
Document rules - Keep notes on why each port is open
Troubleshooting
Locked Out After Enabling UFW

Prevention:

Always allow SSH before enabling: sudo ufw allow ssh
Test in a new terminal before closing existing sessions

Recovery:

Use hosting provider's console/VNC access
Disable firewall: sudo ufw disable
Add SSH rule: sudo ufw allow ssh
Re-enable: sudo ufw enable
Service Not Accessible
# Check if port is allowed
sudo ufw status | grep <port>

# Check if service is listening
sudo ss -tulpn | grep <port>

# Check logs for blocks
sudo tail -f /var/log/ufw.log

UFW Not Starting
# Check status
sudo systemctl status ufw

# Enable UFW service
sudo systemctl enable ufw
sudo systemctl start ufw

# Check for errors
sudo journalctl -u ufw

IPv6 Issues

Enable IPv6 in /etc/default/ufw:

IPV6=yes


Then reload:

sudo ufw reload

Common Mistakes to Avoid
❌ Enabling UFW before allowing SSH (lockout!)
❌ Opening all ports "temporarily" and forgetting to close them
❌ Not testing rules before going to production
❌ Allowing database ports from anywhere (0.0.0.0/0)
❌ Forgetting to enable UFW after configuration
❌ Not documenting why ports are open
❌ Disabling firewall instead of troubleshooting issues
UFW vs iptables

UFW is a frontend for iptables that simplifies firewall management:

UFW: User-friendly, simple syntax, good for most cases
iptables: Full control, complex syntax, advanced scenarios

UFW rules are translated to iptables rules under the hood. For advanced needs, you can still use iptables directly, but UFW is recommended for most users.

Additional Resources

See references/ufw-rules.md for complete UFW rule reference.

See scripts/setup-firewall.sh for automated setup script.

Related Skills
ssh-hardening - Secure SSH before enabling firewall
fail2ban-setup - Add dynamic IP blocking
auto-updates - Keep firewall software updated
Weekly Installs
34
Repository
mikr13/secure-s…p-skills
GitHub Stars
4
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn