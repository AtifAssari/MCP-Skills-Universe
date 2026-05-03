---
title: chezmoi-chef
url: https://skills.sh/fonnesbeck/shay-mwa/chezmoi-chef
---

# chezmoi-chef

skills/fonnesbeck/shay-mwa/chezmoi-chef
chezmoi-chef
Installation
$ npx skills add https://github.com/fonnesbeck/shay-mwa --skill chezmoi-chef
SKILL.md
Chezmoi Dotfile Management

Chezmoi manages dotfiles across machines with templating, encryption, and password manager integration.

Quick Reference
chezmoi init                    # Initialize
chezmoi add ~/.bashrc           # Add file
chezmoi add --template ~/.zshrc # Add as template
chezmoi add --encrypt ~/.secret # Add encrypted
chezmoi edit ~/.bashrc          # Edit and apply
chezmoi apply                   # Apply all changes
chezmoi diff                    # Preview changes
chezmoi update                  # Pull and apply
chezmoi cd                      # Shell in source dir

Core Workflows
Initialize on New Machine

From GitHub:

chezmoi init --apply github-username


One-liner install + init:

sh -c "$(curl -fsLS get.chezmoi.io)" -- init --apply github-username

Add Files to Management
chezmoi add ~/.bashrc ~/.zshrc ~/.gitconfig    # Multiple files
chezmoi add -r ~/.config/nvim                  # Directory
chezmoi add --template ~/.bashrc               # As template
chezmoi add --encrypt ~/.ssh/id_rsa            # Encrypted

Edit Managed Files
chezmoi edit ~/.bashrc          # Opens source file
chezmoi edit --apply ~/.bashrc  # Auto-apply after save

Sync Changes
chezmoi cd                      # Enter source directory
git add . && git commit -m "update dotfiles" && git push
exit
chezmoi apply                   # Apply locally


Or use chezmoi's git wrapper:

chezmoi git add .
chezmoi git commit -m "update"
chezmoi git push

Templating

Create machine-specific configs. See templates.md for full guide.

Convert to template:

chezmoi add --template ~/.bashrc
# or
chezmoi chattr +template ~/.bashrc


Common patterns:

# OS-specific
{{ if eq .chezmoi.os "darwin" -}}
export PATH="/opt/homebrew/bin:$PATH"
{{- else if eq .chezmoi.os "linux" -}}
export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"
{{- end }}

# Hostname-specific
{{ if eq .chezmoi.hostname "work-laptop" -}}
export HTTP_PROXY="http://proxy.company.com:8080"
{{- end }}

# Distro-specific (Linux)
{{ if eq .chezmoi.osRelease.id "fedora" -}}
alias update="sudo dnf upgrade"
{{- else if eq .chezmoi.osRelease.id "ubuntu" -}}
alias update="sudo apt update && sudo apt upgrade"
{{- end }}


Custom variables in ~/.config/chezmoi/chezmoi.toml:

[data]
  email = "user@example.com"
  editor = "nvim"


Test templates:

chezmoi execute-template '{{ .chezmoi.os }}'
chezmoi data  # Show all variables
chezmoi cat ~/.bashrc  # Show rendered output

Secrets Management

Integrate password managers to avoid committing secrets. See password-managers.md for all integrations.

1Password Example

Config (~/.config/chezmoi/chezmoi.toml):

[onepassword]
  command = "op"
  prompt = true


Template:

export GITHUB_TOKEN='{{ onepasswordRead "op://Personal/github/token" }}'
export AWS_ACCESS_KEY='{{ onepasswordRead "op://Work/aws/access-key" }}'

Bitwarden Example
export API_KEY='{{ (bitwarden "item" "api-credentials").login.password }}'

pass Example
export SECRET='{{ pass "path/to/secret" }}'

Encryption

Encrypt sensitive files stored in source directory.

Setup with age
chezmoi age keygen -o ~/.config/chezmoi/key.txt


Config:

encryption = "age"
[age]
  identity = "~/.config/chezmoi/key.txt"
  recipient = "age1..." # Public key from keygen output

Add Encrypted Files
chezmoi add --encrypt ~/.ssh/id_rsa
chezmoi add --encrypt ~/.aws/credentials


Files stored with encrypted_ prefix, decrypted on apply.

Run Scripts

Execute scripts during apply for setup tasks.

Create in source directory:

chezmoi cd


Script naming:

run_once_install.sh - Run once ever
run_onchange_setup.sh - Run when script changes
run_always.sh - Run every apply

Example run_once_install-packages.sh:

#!/bin/bash
{{ if eq .chezmoi.os "darwin" -}}
brew install ripgrep fd bat
{{- else if eq .chezmoi.osRelease.id "fedora" -}}
sudo dnf install -y ripgrep fd-find bat
{{- end }}

Command Reference

See commands.md for complete command list.

Troubleshooting
chezmoi doctor    # Check configuration
chezmoi verify    # Verify targets match source
chezmoi diff      # See pending changes
chezmoi status    # File status overview
chezmoi --debug apply  # Verbose output


Reset run_once scripts:

chezmoi state delete-bucket --bucket=scriptState

Weekly Installs
93
Repository
fonnesbeck/shay-mwa
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn