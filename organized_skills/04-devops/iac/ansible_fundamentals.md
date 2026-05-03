---
rating: ⭐⭐⭐
title: ansible-fundamentals
url: https://skills.sh/basher83/lunar-claude/ansible-fundamentals
---

# ansible-fundamentals

skills/basher83/lunar-claude/ansible-fundamentals
ansible-fundamentals
Installation
$ npx skills add https://github.com/basher83/lunar-claude --skill ansible-fundamentals
SKILL.md
Ansible Fundamentals

Core principles and golden rules for writing production-quality Ansible automation.

Golden Rules

These rules apply to ALL Ansible code in this repository:

Use uv run prefix - Execute all Ansible commands through uv:

uv run ansible-playbook playbooks/my-playbook.yml
uv run ansible-lint
uv run ansible-galaxy collection install -r requirements.yml


Fully Qualified Collection Names (FQCN) - Avoid short module names:

# CORRECT
- name: Install package
  ansible.builtin.apt:
    name: nginx
    state: present

# WRONG - deprecated short names
- name: Install package
  apt:
    name: nginx


Control command/shell modules - Add changed_when and failed_when:

- name: Check if service exists
  ansible.builtin.command: systemctl status myservice
  register: service_check
  changed_when: false
  failed_when: false


Use set -euo pipefail - In all shell scripts and shell module calls:

- name: Run pipeline command
  ansible.builtin.shell: |
    set -euo pipefail
    cat file.txt | grep pattern | wc -l
  args:
    executable: /bin/bash


Tag sensitive tasks - Use no_log: true for secrets:

- name: Set database password
  ansible.builtin.command: set-password {{ db_password }}
  no_log: true


Idempotency first - Check before create, verify after.

Descriptive task names - Start with action verbs (Ensure, Configure, Install, Create).

Module Selection Guide
Decision Matrix
Need	Use	Why
Install packages	ansible.builtin.apt/yum/dnf	Native modules handle state
Manage files	ansible.builtin.copy/template/file	Idempotent by default
Edit config lines	ansible.builtin.lineinfile	Surgical edits, not full replace
Run commands	ansible.builtin.command	When no native module exists
Need shell features	ansible.builtin.shell	Pipes, redirects, globs
Manage services	ansible.builtin.systemd/service	State management built-in
Manage users	ansible.builtin.user	Cross-platform, idempotent
Prefer Native Modules

Native modules provide:

Built-in idempotency (no need for changed_when)
Better error handling
Cross-platform compatibility
Clear documentation
# PREFER native module
- name: Create user
  ansible.builtin.user:
    name: deploy
    groups: docker
    state: present

# AVOID command when module exists
- name: Create user
  ansible.builtin.command: useradd -G docker deploy
  # Requires: changed_when, failed_when, idempotency logic

When Command/Shell is Acceptable

Use command or shell modules when:

No native module exists for the operation
Interacting with vendor CLI tools (pvecm, pveceph, kubectl)
Running one-off scripts

Add proper controls:

- name: Create Proxmox API token
  ansible.builtin.command: >
    pveum user token add {{ username }}@pam {{ token_name }}
  register: token_result
  changed_when: "'already exists' not in token_result.stderr"
  failed_when:
    - token_result.rc != 0
    - "'already exists' not in token_result.stderr"
  no_log: true

Collections in Use

This repository uses these Ansible collections:

Collection	Purpose	Example Modules
ansible.builtin	Core functionality	copy, template, command, user
ansible.posix	POSIX systems	authorized_key, synchronize
community.general	General utilities	interfaces_file, ini_file
community.proxmox	Proxmox VE	proxmox_vm, proxmox_kvm
infisical.vault	Secrets management	read_secrets
community.docker	Docker management	docker_container, docker_image
Installing Collections
# Install from requirements
cd ansible && uv run ansible-galaxy collection install -r requirements.yml

# Install specific collection
uv run ansible-galaxy collection install community.proxmox

Common Execution Patterns
Running Playbooks
# Basic execution
uv run ansible-playbook playbooks/my-playbook.yml

# With extra variables
uv run ansible-playbook playbooks/create-vm.yml \
  -e "vm_name=docker-01" \
  -e "vm_memory=4096"

# Limit to specific hosts
uv run ansible-playbook playbooks/update.yml --limit proxmox

# Check mode (dry run)
uv run ansible-playbook playbooks/deploy.yml --check --diff

# With tags
uv run ansible-playbook playbooks/setup.yml --tags "network,storage"

Linting
# Run ansible-lint
mise run ansible-lint

# Or directly
uv run ansible-lint ansible/playbooks/

Task Naming Conventions

Use descriptive names with action verbs:

Verb	Use When
Ensure	Verifying state exists
Configure	Modifying settings
Install	Adding packages
Create	Making new resources
Remove	Deleting resources
Deploy	Releasing applications
Update	Modifying existing resources

Examples:

- name: Ensure Docker is installed
- name: Configure SSH security settings
- name: Create admin user account
- name: Deploy application configuration

Variable Naming

Use snake_case with descriptive names:

# GOOD - clear, descriptive
proxmox_api_user: terraform@pam
docker_compose_version: "2.24.0"
vm_memory_mb: 4096

# BAD - vague, abbreviated
pve_usr: terraform@pam
dc_ver: "2.24.0"
mem: 4096

Quick Reference Commands
# Lint all Ansible files
mise run ansible-lint

# Run playbook with secrets from Infisical
cd ansible && uv run ansible-playbook playbooks/my-playbook.yml

# Check syntax
uv run ansible-playbook --syntax-check playbooks/my-playbook.yml

# List hosts in inventory
uv run ansible-inventory --list

# Test connection
uv run ansible all -m ping

Common Anti-Patterns
Missing FQCN
# BAD
- name: Copy file
  copy:
    src: file.txt
    dest: /tmp/

# GOOD
- name: Copy file
  ansible.builtin.copy:
    src: file.txt
    dest: /tmp/

Uncontrolled Commands
# BAD - always shows changed, no error handling
- name: Check status
  ansible.builtin.command: systemctl status app

# GOOD
- name: Check status
  ansible.builtin.command: systemctl status app
  register: status_check
  changed_when: false
  failed_when: false

Using shell When command Suffices
# BAD - shell not needed
- name: List files
  ansible.builtin.shell: ls -la /tmp

# GOOD - command is sufficient
- name: List files
  ansible.builtin.command: ls -la /tmp
  changed_when: false

Missing no_log on Secrets
# BAD - password in logs
- name: Set password
  ansible.builtin.command: set-password {{ password }}

# GOOD
- name: Set password
  ansible.builtin.command: set-password {{ password }}
  no_log: true

Related Skills
ansible-idempotency - Detailed changed_when/failed_when patterns
ansible-secrets - Infisical integration and security
ansible-proxmox - Proxmox-specific module selection
ansible-error-handling - Block/rescue, retry patterns
Weekly Installs
20
Repository
basher83/lunar-claude
GitHub Stars
18
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn