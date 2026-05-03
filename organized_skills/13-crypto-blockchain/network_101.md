---
rating: ⭐⭐⭐
title: network 101
url: https://skills.sh/davila7/claude-code-templates/network-101
---

# network 101

skills/davila7/claude-code-templates/Network 101
Network 101
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill 'Network 101'
SKILL.md
Network 101
Purpose

Configure and test common network services (HTTP, HTTPS, SNMP, SMB) for penetration testing lab environments. Enable hands-on practice with service enumeration, log analysis, and security testing against properly configured target systems.

Inputs/Prerequisites
Windows Server or Linux system for hosting services
Kali Linux or similar for testing
Administrative access to target system
Basic networking knowledge (IP addressing, ports)
Firewall access for port configuration
Outputs/Deliverables
Configured HTTP/HTTPS web server
SNMP service with accessible communities
SMB file shares with various permission levels
Captured logs for analysis
Documented enumeration results
Core Workflow
1. Configure HTTP Server (Port 80)

Set up a basic HTTP web server for testing:

Windows IIS Setup:

Open IIS Manager (Internet Information Services)
Right-click Sites → Add Website
Configure site name and physical path
Bind to IP address and port 80

Linux Apache Setup:

# Install Apache
sudo apt update && sudo apt install apache2

# Start service
sudo systemctl start apache2
sudo systemctl enable apache2

# Create test page
echo "<html><body><h1>Test Page</h1></body></html>" | sudo tee /var/www/html/index.html

# Verify service
curl http://localhost


Configure Firewall for HTTP:

# Linux (UFW)
sudo ufw allow 80/tcp

# Windows PowerShell
New-NetFirewallRule -DisplayName "HTTP" -Direction Inbound -Protocol TCP -LocalPort 80 -Action Allow

2. Configure HTTPS Server (Port 443)

Set up secure HTTPS with SSL/TLS:

Generate Self-Signed Certificate:

# Linux - Generate certificate
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/ssl/private/apache-selfsigned.key \
  -out /etc/ssl/certs/apache-selfsigned.crt

# Enable SSL module
sudo a2enmod ssl
sudo systemctl restart apache2


Configure Apache for HTTPS:

# Edit SSL virtual host
sudo nano /etc/apache2/sites-available/default-ssl.conf

# Enable site
sudo a2ensite default-ssl
sudo systemctl reload apache2


Verify HTTPS Setup:

# Check port 443 is open
nmap -p 443 192.168.1.1

# Test SSL connection
openssl s_client -connect 192.168.1.1:443

# Check certificate
curl -kv https://192.168.1.1

3. Configure SNMP Service (Port 161)

Set up SNMP for enumeration practice:

Linux SNMP Setup:

# Install SNMP daemon
sudo apt install snmpd snmp

# Configure community strings
sudo nano /etc/snmp/snmpd.conf

# Add these lines:
# rocommunity public
# rwcommunity private

# Restart service
sudo systemctl restart snmpd


Windows SNMP Setup:

Open Server Manager → Add Features
Select SNMP Service
Configure community strings in Services → SNMP Service → Properties

SNMP Enumeration Commands:

# Basic SNMP walk
snmpwalk -c public -v1 192.168.1.1

# Enumerate system info
snmpwalk -c public -v1 192.168.1.1 1.3.6.1.2.1.1

# Get running processes
snmpwalk -c public -v1 192.168.1.1 1.3.6.1.2.1.25.4.2.1.2

# SNMP check tool
snmp-check 192.168.1.1 -c public

# Brute force community strings
onesixtyone -c /usr/share/seclists/Discovery/SNMP/common-snmp-community-strings.txt 192.168.1.1

4. Configure SMB Service (Port 445)

Set up SMB file shares for enumeration:

Windows SMB Share:

Create folder to share
Right-click → Properties → Sharing → Advanced Sharing
Enable sharing and set permissions
Configure NTFS permissions

Linux Samba Setup:

# Install Samba
sudo apt install samba

# Create share directory
sudo mkdir -p /srv/samba/share
sudo chmod 777 /srv/samba/share

# Configure Samba
sudo nano /etc/samba/smb.conf

# Add share:
# [public]
#    path = /srv/samba/share
#    browsable = yes
#    guest ok = yes
#    read only = no

# Restart service
sudo systemctl restart smbd


SMB Enumeration Commands:

# List shares anonymously
smbclient -L //192.168.1.1 -N

# Connect to share
smbclient //192.168.1.1/share -N

# Enumerate with smbmap
smbmap -H 192.168.1.1

# Full enumeration
enum4linux -a 192.168.1.1

# Check for vulnerabilities
nmap --script smb-vuln* 192.168.1.1

5. Analyze Service Logs

Review logs for security analysis:

HTTP/HTTPS Logs:

# Apache access log
sudo tail -f /var/log/apache2/access.log

# Apache error log
sudo tail -f /var/log/apache2/error.log

# Windows IIS logs
# Location: C:\inetpub\logs\LogFiles\W3SVC1\


Parse Log for Credentials:

# Search for POST requests
grep "POST" /var/log/apache2/access.log

# Extract user agents
awk '{print $12}' /var/log/apache2/access.log | sort | uniq -c

Quick Reference
Essential Ports
Service	Port	Protocol
HTTP	80	TCP
HTTPS	443	TCP
SNMP	161	UDP
SMB	445	TCP
NetBIOS	137-139	TCP/UDP
Service Verification Commands
# Check HTTP
curl -I http://target

# Check HTTPS
curl -kI https://target

# Check SNMP
snmpwalk -c public -v1 target

# Check SMB
smbclient -L //target -N

Common Enumeration Tools
Tool	Purpose
nmap	Port scanning and scripts
nikto	Web vulnerability scanning
snmpwalk	SNMP enumeration
enum4linux	SMB/NetBIOS enumeration
smbclient	SMB connection
gobuster	Directory brute forcing
Constraints
Self-signed certificates trigger browser warnings
SNMP v1/v2c communities transmit in cleartext
Anonymous SMB access is often disabled by default
Firewall rules must allow inbound connections
Lab environments should be isolated from production
Examples
Example 1: Complete HTTP Lab Setup
# Install and configure
sudo apt install apache2
sudo systemctl start apache2

# Create login page
cat << 'EOF' | sudo tee /var/www/html/login.html
<html>
<body>
<form method="POST" action="login.php">
Username: <input type="text" name="user"><br>
Password: <input type="password" name="pass"><br>
<input type="submit" value="Login">
</form>
</body>
</html>
EOF

# Allow through firewall
sudo ufw allow 80/tcp

Example 2: SNMP Testing Setup
# Quick SNMP configuration
sudo apt install snmpd
echo "rocommunity public" | sudo tee -a /etc/snmp/snmpd.conf
sudo systemctl restart snmpd

# Test enumeration
snmpwalk -c public -v1 localhost

Example 3: SMB Anonymous Access
# Configure anonymous share
sudo apt install samba
sudo mkdir /srv/samba/anonymous
sudo chmod 777 /srv/samba/anonymous

# Test access
smbclient //localhost/anonymous -N

Troubleshooting
Issue	Solution
Port not accessible	Check firewall rules (ufw, iptables, Windows Firewall)
Service not starting	Check logs with journalctl -u service-name
SNMP timeout	Verify UDP 161 is open, check community string
SMB access denied	Verify share permissions and user credentials
HTTPS certificate error	Accept self-signed cert or add to trusted store
Cannot connect remotely	Bind service to 0.0.0.0 instead of localhost
Weekly Installs
–
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykWarn