---
rating: ⭐⭐⭐
title: secure-vps-setup
url: https://skills.sh/tibobfd/skills-secure-vps-for-beginners/secure-vps-setup
---

# secure-vps-setup

skills/tibobfd/skills-secure-vps-for-beginners/secure-vps-setup
secure-vps-setup
Installation
$ npx skills add https://github.com/tibobfd/skills-secure-vps-for-beginners --skill secure-vps-setup
SKILL.md
INTERACTION GUIDELINES
Start with the "Why": Never tell the user to run a command without explaining what it does and why it secures them.
Phase-by-Phase: Do NOT output the entire guide at once. Break it down by Phases.
Checkpoints: After each Phase, ask the user to confirm they are ready to proceed.
Verification: Encourage the user to verify success (e.g., "Try logging in now") before moving to the next layer.
ON ACTIVATION (First Turn)
Welcome the user.
Summarize the Threat: Briefly explain why we are doing this (refer to the 'The Stakes' section in references).
Present the Plan: List the 6 Phases we will cover.
Ask: "Are you ready to start Phase 1: OS Hardening?"
Secure VPS Setup Guide (Expert Edition)
Prerequisites
A fresh Linux VPS (Ubuntu LTS - Latest Version preferred).
Root or sudo access.
A domain name (for Traefik).
References

-> Read references/security-concepts.md for detailed concepts.

Phase 1: OS Hardening & Network

Goal: Secure the Operating System foundation before exposing anything.

Update System:
sudo apt update && sudo apt upgrade -y

Install Essential Tools:
sudo apt install ufw unattended-upgrades apt-listchanges -y

Configure Unattended Upgrades: Enable automatic security updates.
sudo dpkg-reconfigure -plow unattended-upgrades
# Select 'Yes'

Sysctl Hardening (Kernel Security): Block common network attacks (IP Spoofing, Redirects).
cat <<EOF | sudo tee /etc/sysctl.d/99-security.conf
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1
net.ipv4.icmp_echo_ignore_broadcasts = 1
net.ipv4.conf.all.accept_redirects = 0
net.ipv6.conf.all.accept_redirects = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.tcp_syncookies = 1
EOF
sudo sysctl --system

Firewall Setup (UFW):
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh  # CRITICAL: Don't lock yourself out!
sudo ufw enable

Phase 2: SSH Hardening (High Priority)

Goal: Replace weak passwords with cryptographic keys.

Generate Key (On your LOCAL machine): If you don't have one yet:
ssh-keygen -t ed25519 -C "your-email@example.com"

Copy Key to VPS (From your LOCAL machine):
ssh-copy-id user@your-vps-ip

Test Login: Open a new terminal and try ssh user@your-vps-ip. It should NOT ask for a password (or only ask for the key passphrase).
Lock Down SSH (On VPS): Edit /etc/ssh/sshd_config:
sudo nano /etc/ssh/sshd_config

Set these values:
PermitRootLogin no
PasswordAuthentication no
ChallengeResponseAuthentication no

Restart SSH:
sudo systemctl restart ssh

Phase 3: Secure Access (Tailscale)

Goal: Hide management ports from the public internet entirely.

Install Tailscale:
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up

Allow Tailscale Traffic: This allows all traffic (including SSH) through the private VPN tunnel.
sudo ufw allow in on tailscale0

TEST YOUR CONNECTION (Critical):
Find your Tailscale IP: tailscale ip -4
Try to SSH into your VPS using this IP from your local machine: ssh user@100.x.y.z
Close the Public Front Door: Once you are SURE you can connect via Tailscale, remove the public SSH rule.

⚠️ SAFETY NET: Ensure you have access to your VPS Provider's "Web Console" or "KVM" (e.g., OVH/Hetzner panel). If Tailscale fails, that is your only way back in!

sudo ufw delete allow ssh

Now, your port 22 is invisible to the public internet but works perfectly via the VPN.
Phase 4: Core Services (Docker & Watchtower)

Goal: Run applications with automated updates.

Install Docker:
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
# Log out and back in

Create Network:
docker network create proxy-net

Deploy Traefik: -> Copy config from references/docker-compose-templates.md Deploy in ~/app-data/traefik. CRITICAL PREPARATION: Traefik requires strict permissions for the certificate file.
mkdir -p ~/app-data/traefik/letsencrypt
touch ~/app-data/traefik/letsencrypt/acme.json
chmod 600 ~/app-data/traefik/letsencrypt/acme.json

Deploy Watchtower: -> Copy config from references/docker-compose-templates.md Create ~/app-data/watchtower/docker-compose.yml and deploy.
Phase 5: Active Defense (Crowdsec)

Goal: Ban malicious IPs automatically.

Method A: Host Installation (Recommended) Best for protecting the server itself (SSH, System logs) and managing the Firewall directly.

Install Crowdsec:

curl -s https://install.crowdsec.net | sudo sh
sudo apt install crowdsec


Install Firewall Bouncer:

sudo apt install crowdsec-firewall-bouncer-iptables


This connects Crowdsec directly to your UFW/IPtables to drop packets.

Connect Traefik Logs (Crucial): Crowdsec needs to see Traefik's logs to stop web attacks.

Install Collection:
sudo cscli collections install crowdsecurity/traefik
# Recommended Extras (Best Practices 2025):
sudo cscli collections install crowdsecurity/whitelist-good-actors crowdsecurity/http-cve

Configure Acquisition: Add this to /etc/crowdsec/acquis.yaml:
filenames:
  - /home/ubuntu/app-data/traefik/logs/access.log
labels:
  type: traefik

Restart: sudo systemctl restart crowdsec

Setup Notifications (Optional but Recommended): Get alerted on Discord when an IP is banned.

Create Config: sudo nano /etc/crowdsec/notifications/discord.yaml
type: http
name: discord_default
log_level: info
url: YOUR_WEBHOOK_URL
method: POST
headers:
  Content-Type: application/json
format: |
  {
    "username": "CrowdSec-VPS",
    "content": "🚨 **CrowdSec Alert**\n{{range . -}}\nIP: **{{.Source.IP}}** ({{.Source.Cn}})\nReason: *{{.Scenario}}*\n{{end}}"
  }

Enable in Profile: Edit /etc/crowdsec/profiles.yaml and add discord_default under notifications:.
Restart: sudo systemctl restart crowdsec

Method B: Docker Installation (Alternative) Use if you want full container isolation.

Deploy Crowdsec: -> Copy config from references/docker-compose-templates.md Deploy in ~/app-data/crowdsec.
Phase 6: Maintenance & Verification

Goal: Ensure resilience and recoverability.

Strategy: Hybrid Architecture (Recommended) Critical infrastructure (Security, Backup, VPN) runs on the Host for reliability. Apps run in Docker.

Vulnerability Scan (Trivy):

trivy fs /


Backups (Duplicati): Method A: Host Installation (Robust) Best for disaster recovery (can restore Docker configs even if Docker is down).

Install Duplicati as a service.
Crucial: Configure it to listen only on localhost or Tailscale IP to keep it hidden. --webservice-interface=100.x.y.z

Method B: Docker Installation -> Copy config from references/docker-compose-templates.md Edit the file and replace 127.0.0.1 with your Tailscale IP. Deploy in ~/app-data/duplicati.

Final Check: -> Run scripts/verify_setup.sh

Weekly Installs
47
Repository
tibobfd/skills-…eginners
GitHub Stars
1
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn