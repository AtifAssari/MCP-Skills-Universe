---
title: ssh
url: https://skills.sh/dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations/ssh
---

# ssh

skills/dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations/ssh
ssh
Installation
$ npx skills add https://github.com/dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations --skill ssh
SKILL.md
SSH Skill

Use SSH for secure remote access, file transfers, and tunneling.

Basic Connection

Connect to server:

ssh user@hostname


Connect on specific port:

ssh -p 2222 user@hostname


Connect with specific identity:

ssh -i ~/.ssh/my_key user@hostname

SSH Config

Config file location:

~/.ssh/config


Example config entry:

Host myserver
    HostName 192.168.1.100
    User deploy
    Port 22
    IdentityFile ~/.ssh/myserver_key
    ForwardAgent yes


Then connect with just:

ssh myserver

Running Remote Commands

Execute single command:

ssh user@host "ls -la /var/log"


Execute multiple commands:

ssh user@host "cd /app && git pull && pm2 restart all"


Run with pseudo-terminal (for interactive):

ssh -t user@host "htop"

File Transfer with SCP

Copy file to remote:

scp local.txt user@host:/remote/path/


Copy file from remote:

scp user@host:/remote/file.txt ./local/


Copy directory recursively:

scp -r ./local_dir user@host:/remote/path/

File Transfer with rsync (preferred)

Sync directory to remote:

rsync -avz ./local/ user@host:/remote/path/


Sync from remote:

rsync -avz user@host:/remote/path/ ./local/


With progress and compression:

rsync -avzP ./local/ user@host:/remote/path/


Dry run first:

rsync -avzn ./local/ user@host:/remote/path/

Port Forwarding (Tunnels)

Local forward (access remote service locally):

ssh -L 8080:localhost:80 user@host
# Now localhost:8080 connects to host's port 80


Local forward to another host:

ssh -L 5432:db-server:5432 user@jumphost
# Access db-server:5432 via localhost:5432


Remote forward (expose local service to remote):

ssh -R 9000:localhost:3000 user@host
# Remote's port 9000 connects to your local 3000


Dynamic SOCKS proxy:

ssh -D 1080 user@host
# Use localhost:1080 as SOCKS5 proxy

Jump Hosts / Bastion

Connect through jump host:

ssh -J jumphost user@internal-server


Multiple jumps:

ssh -J jump1,jump2 user@internal-server


In config file:

Host internal
    HostName 10.0.0.50
    User deploy
    ProxyJump bastion

Key Management

Generate new key (Ed25519, recommended):

ssh-keygen -t ed25519 -C "your_email@example.com"


Generate RSA key (legacy compatibility):

ssh-keygen -t rsa -b 4096 -C "your_email@example.com"


Copy public key to server:

ssh-copy-id user@host


Copy specific key:

ssh-copy-id -i ~/.ssh/mykey.pub user@host

SSH Agent

Start agent:

eval "$(ssh-agent -s)"


Add key to agent:

ssh-add ~/.ssh/id_ed25519


Add with macOS keychain:

ssh-add --apple-use-keychain ~/.ssh/id_ed25519


List loaded keys:

ssh-add -l

Multiplexing (Connection Sharing)

In ~/.ssh/config:

Host *
    ControlMaster auto
    ControlPath ~/.ssh/sockets/%r@%h-%p
    ControlPersist 600


Create socket directory:

mkdir -p ~/.ssh/sockets

Known Hosts

Remove old host key:

ssh-keygen -R hostname


Scan and add host key:

ssh-keyscan hostname >> ~/.ssh/known_hosts

Debugging

Verbose output:

ssh -v user@host


Very verbose:

ssh -vv user@host


Maximum verbosity:

ssh -vvv user@host

Security Tips
Use Ed25519 keys (faster, more secure than RSA)
Set PasswordAuthentication no on servers
Use fail2ban on servers to block brute force
Keep keys encrypted with passphrases
Use ssh-agent to avoid typing passphrase repeatedly
Restrict key usage with command= in authorized_keys
Weekly Installs
499
Repository
dicklesworthsto…grations
GitHub Stars
63
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass