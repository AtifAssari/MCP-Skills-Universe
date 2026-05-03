---
title: fail2ban-setup
url: https://skills.sh/mikr13/secure-server-setup-skills/fail2ban-setup
---

# fail2ban-setup

skills/mikr13/secure-server-setup-skills/fail2ban-setup
fail2ban-setup
Installation
$ npx skills add https://github.com/mikr13/secure-server-setup-skills --skill fail2ban-setup
SKILL.md
Fail2ban Setup Skill

Configure fail2ban to automatically protect servers against brute-force attacks by banning malicious IP addresses.

What This Skill Does

This skill helps AI agents install and configure fail2ban on VPS servers. Even with SSH keys configured, bots will constantly hammer your server with login attempts. Fail2ban monitors log files and automatically bans IP addresses that show malicious behavior, such as too many password failures.

Key capabilities:

Install fail2ban package
Configure SSH brute-force protection
Set ban times and retry thresholds
Create custom jails for different services
Monitor and manage banned IPs
Integrate with UFW/iptables firewall
When to Use

Use this skill when you need to:

Protect SSH from brute-force attacks
Reduce server load from automated login attempts
Automatically block malicious IPs
Complement SSH hardening and firewall configuration
Monitor authentication logs for suspicious activity
Protect web applications from abuse

Critical understanding: Three failed attempts in 10 minutes = banned for an hour. This drastically reduces brute-force attack effectiveness.

Prerequisites
Root or sudo access to the server
Ubuntu, Debian, or RHEL-based Linux distribution
SSH access to the server
Firewall configured (UFW or iptables)
Services to protect (SSH, web server, etc.) running and logging
Fail2ban Installation
Ubuntu/Debian
sudo apt update
sudo apt install fail2ban -y

CentOS/RHEL
sudo yum install epel-release -y
sudo yum install fail2ban -y

Verify Installation
sudo systemctl status fail2ban

Basic Configuration
Step 1: Create Local Configuration

CRITICAL: Never edit jail.conf directly. It gets overwritten on updates!

Create a local configuration file:

sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local


Edit the local configuration:

sudo nano /etc/fail2ban/jail.local

Step 2: Configure Global Settings

Find and update these settings in jail.local:

[DEFAULT]
# Ban time in seconds (1 hour)
bantime = 3600

# Find time window (10 minutes)
findtime = 600

# Number of failures before ban
maxretry = 3

# Destination email for notifications (optional)
destemail = admin@example.com

# Sender email
sendername = Fail2Ban

# Email action
action = %(action_)s
# Or with email: %(action_mwl)s

Step 3: Configure SSH Protection

Find the [sshd] section and configure:

[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600
findtime = 600


For custom SSH port:

[sshd]
enabled = true
port = 2222
filter = sshd
logpath = /var/log/auth.log
maxretry = 3

Step 4: Enable and Start Fail2ban
sudo systemctl enable fail2ban
sudo systemctl start fail2ban


Verify it's running:

sudo systemctl status fail2ban

Advanced Configuration
Multiple Service Protection

Add jails for other services in /etc/fail2ban/jail.local:

Nginx/Apache (HTTP Auth):

[nginx-http-auth]
enabled = true
port = http,https
filter = nginx-http-auth
logpath = /var/log/nginx/error.log
maxretry = 3

[apache-auth]
enabled = true
port = http,https
filter = apache-auth
logpath = /var/log/apache*/*error.log
maxretry = 3


WordPress:

[wordpress-auth]
enabled = true
port = http,https
filter = wordpress-auth
logpath = /var/log/auth.log
maxretry = 3


FTP:

[proftpd]
enabled = true
port = ftp,ftp-data,ftps,ftps-data
filter = proftpd
logpath = /var/log/proftpd/proftpd.log
maxretry = 3

Custom Ban Times

Different ban times for different severity:

[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600      # 1 hour
findtime = 600      # 10 minutes

[sshd-aggressive]
enabled = true
port = ssh
filter = sshd-aggressive
logpath = /var/log/auth.log
maxretry = 1
bantime = 86400     # 24 hours
findtime = 3600     # 1 hour

Permanent Bans

For repeated offenders:

[recidive]
enabled = true
filter = recidive
logpath = /var/log/fail2ban.log
bantime = 604800    # 1 week
findtime = 86400    # 1 day
maxretry = 3

Whitelist IPs

Never ban trusted IPs:

[DEFAULT]
ignoreip = 127.0.0.1/8 ::1 203.0.113.10 192.168.1.0/24

Email Notifications

Enable email alerts:

[DEFAULT]
destemail = admin@example.com
sendername = Fail2Ban
mta = sendmail

# Action with email
action = %(action_mwl)s

Fail2ban Management
Check Status
# Overall status
sudo fail2ban-client status

# Specific jail status
sudo fail2ban-client status sshd

View Banned IPs
# List banned IPs for SSH
sudo fail2ban-client status sshd

# List all banned IPs
sudo fail2ban-client banned

Unban IP Address
# Unban specific IP from specific jail
sudo fail2ban-client set sshd unbanip 203.0.113.100

# Unban from all jails
sudo fail2ban-client unban 203.0.113.100

Manually Ban IP
sudo fail2ban-client set sshd banip 203.0.113.100

Test Filter

Test if a filter matches log lines:

fail2ban-regex /var/log/auth.log /etc/fail2ban/filter.d/sshd.conf

Monitoring and Logs
Fail2ban Logs
# View fail2ban log
sudo tail -f /var/log/fail2ban.log

# View recent bans
sudo grep "Ban" /var/log/fail2ban.log

# View unbans
sudo grep "Unban" /var/log/fail2ban.log

Check Firewall Rules

Fail2ban adds rules to iptables/UFW:

# View iptables rules
sudo iptables -L -n

# View fail2ban chains
sudo iptables -L fail2ban-sshd -n

# View UFW status
sudo ufw status numbered

Statistics
# Count bans by jail
sudo fail2ban-client status | grep "Jail list"

# Count current bans
sudo fail2ban-client status sshd | grep "Currently banned"

# Total bans
sudo fail2ban-client status sshd | grep "Total banned"

Configuration Files
Main Configuration Files
/etc/fail2ban/fail2ban.conf      # Main fail2ban configuration
/etc/fail2ban/fail2ban.local     # Local fail2ban config (create if needed)
/etc/fail2ban/jail.conf          # Default jail configurations (don't edit!)
/etc/fail2ban/jail.local         # Local jail overrides (edit this!)
/etc/fail2ban/jail.d/            # Additional jail configs

Filters and Actions
/etc/fail2ban/filter.d/          # Log file filters
/etc/fail2ban/action.d/          # Ban actions (iptables, ufw, etc.)
/var/log/fail2ban.log            # Fail2ban log file

Creating Custom Filters

Create a custom filter for your application:

Create filter file /etc/fail2ban/filter.d/myapp.conf:
[Definition]
failregex = ^.*Failed login attempt from <HOST>.*$
            ^.*Invalid user .* from <HOST>.*$
ignoreregex =

Create jail in /etc/fail2ban/jail.local:
[myapp]
enabled = true
port = 8080
filter = myapp
logpath = /var/log/myapp/access.log
maxretry = 5
bantime = 3600

Test the filter:
fail2ban-regex /var/log/myapp/access.log /etc/fail2ban/filter.d/myapp.conf

Reload fail2ban:
sudo systemctl reload fail2ban

Restart and Reload
Restart Service
# Restart fail2ban
sudo systemctl restart fail2ban

# Check status
sudo systemctl status fail2ban

Reload Configuration
# Reload without restarting (keeps existing bans)
sudo fail2ban-client reload

# Reload specific jail
sudo fail2ban-client reload sshd

Security Best Practices
Start with conservative settings - Don't ban too aggressively
Whitelist trusted IPs - Add your office/home IP to ignoreip
Monitor logs - Regularly check /var/log/fail2ban.log
Test filters - Use fail2ban-regex to test before deploying
Combine with SSH hardening - Fail2ban is not a replacement for proper SSH config
Set reasonable ban times - Too short is ineffective, too long may ban legitimate users
Enable recidive jail - Catch repeated offenders
Keep fail2ban updated - Update regularly for new attack patterns
Troubleshooting
Fail2ban Not Starting
# Check for syntax errors
sudo fail2ban-client -t

# View error logs
sudo journalctl -u fail2ban -n 50

# Check configuration
sudo fail2ban-client -d

Jails Not Working
# Check jail status
sudo fail2ban-client status

# View jail configuration
sudo fail2ban-client get sshd maxretry
sudo fail2ban-client get sshd bantime

# Test filter against log
fail2ban-regex /var/log/auth.log /etc/fail2ban/filter.d/sshd.conf

Log File Not Found

Check log paths in jail configuration:

# Ubuntu/Debian SSH logs
/var/log/auth.log

# CentOS/RHEL SSH logs
/var/log/secure

# Nginx logs
/var/log/nginx/error.log
/var/log/nginx/access.log

Accidentally Banned
# Unban your IP
sudo fail2ban-client set sshd unbanip YOUR.IP.ADDRESS

# Or stop fail2ban temporarily
sudo systemctl stop fail2ban

Common Mistakes to Avoid
❌ Editing jail.conf instead of creating jail.local
❌ Not whitelisting your own IP address
❌ Setting maxretry too low (banning legitimate users)
❌ Not testing filters before deployment
❌ Forgetting to restart after configuration changes
❌ Using fail2ban as sole security measure (combine with other hardening!)
❌ Not monitoring fail2ban logs
Additional Resources

See references/fail2ban-filters.md for common filter patterns.

See scripts/setup-fail2ban.sh for automated setup script.

Related Skills
ssh-hardening - Harden SSH before adding fail2ban
firewall-configuration - Fail2ban works with UFW/iptables
auto-updates - Keep fail2ban updated
Weekly Installs
32
Repository
mikr13/secure-s…p-skills
GitHub Stars
4
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn