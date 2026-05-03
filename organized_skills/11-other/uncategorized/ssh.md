---
rating: ⭐⭐⭐
title: ssh
url: https://skills.sh/openhands/skills/ssh
---

# ssh

skills/openhands/skills/ssh
ssh
Installation
$ npx skills add https://github.com/openhands/skills --skill ssh
SKILL.md
SSH Skill

This skill provides capabilities for establishing and managing SSH connections to remote machines.

Capabilities
Establish SSH connections using password or key-based authentication
Generate and manage SSH key pairs
Configure SSH for easier connections
Execute commands on remote machines
Transfer files between local and remote machines
Manage SSH configurations and known hosts
Authentication Methods
Password Authentication
ssh username@hostname


When prompted, you should ask the user for their password or a private key.

Key-Based Authentication

Generate a new SSH key pair:

ssh-keygen -t ed25519 -f ~/.ssh/key_name -C "comment" -N ""


Copy the public key to the remote server:

ssh-copy-id -i ~/.ssh/key_name.pub username@hostname


Connect using the private key:

ssh -i ~/.ssh/key_name username@hostname

SSH Configuration

Create or edit the SSH config file for easier connections:

mkdir -p ~/.ssh
cat > ~/.ssh/config << 'EOF'
Host alias
    HostName hostname_or_ip
    User username
    IdentityFile ~/.ssh/key_name
    Port 22
    ServerAliveInterval 60
EOF
chmod 600 ~/.ssh/config


Then connect using the alias:

ssh alias

Common SSH Options
-p PORT: Connect to a specific port
-X: Enable X11 forwarding
-L local_port:remote_host:remote_port: Set up local port forwarding
-R remote_port:local_host:local_port: Set up remote port forwarding
-N: Do not execute a remote command (useful for port forwarding)
-f: Run in background
-v: Verbose mode (add more v's for increased verbosity)
File Transfer with SCP

Copy a file to the remote server:

scp /path/to/local/file username@hostname:/path/to/remote/directory/


Copy a file from the remote server:

scp username@hostname:/path/to/remote/file /path/to/local/directory/


Copy a directory recursively:

scp -r /path/to/local/directory username@hostname:/path/to/remote/directory/

SSH Agent

Start the SSH agent:

eval "$(ssh-agent -s)"


Add a key to the agent:

ssh-add ~/.ssh/key_name

Troubleshooting
Check SSH service status on remote: systemctl status sshd
Verify SSH port is open: nc -zv hostname 22
Debug connection issues: ssh -vvv username@hostname
Check permissions: SSH private keys should have 600 permissions (chmod 600 ~/.ssh/key_name)
Verify known_hosts: If host key changed, remove the old entry with ssh-keygen -R hostname
Secure SSH Key Management
Local Storage with Proper Permissions

The most basic approach is to ensure proper file permissions:

# Set correct permissions for private keys
chmod 600 ~/.ssh/id_ed25519
# Set correct permissions for public keys
chmod 644 ~/.ssh/id_ed25519.pub
# Set correct permissions for SSH directory
chmod 700 ~/.ssh

Weekly Installs
450
Repository
openhands/skills
GitHub Stars
93
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn