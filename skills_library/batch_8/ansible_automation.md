---
title: ansible-automation
url: https://skills.sh/aj-geddes/useful-ai-prompts/ansible-automation
---

# ansible-automation

skills/aj-geddes/useful-ai-prompts/ansible-automation
ansible-automation
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill ansible-automation
Summary

Infrastructure automation and configuration management across multiple servers using Ansible playbooks and roles.

Supports playbook-driven deployment, configuration management, patching, and multi-server orchestration with rolling update strategies
Includes role-based modularity, dynamic inventory management, handlers for idempotency, and health check verification
Provides template-based configuration, vault integration for sensitive data, and serial deployment modes for controlled rollouts
Built-in error handling, check mode validation, and support for pre-tasks and post-tasks within playbook workflows
SKILL.md
Ansible Automation
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Automate infrastructure provisioning, configuration management, and application deployment across multiple servers using Ansible playbooks, roles, and dynamic inventory management.

When to Use
Configuration management
Application deployment
Infrastructure patching and updates
Multi-server orchestration
Cloud instance provisioning
Container management
Database administration
Security compliance automation
Quick Start

Minimal working example:

# site.yml - Main playbook
---
- name: Deploy application stack
  hosts: all
  gather_facts: yes
  serial: 1  # Rolling deployment

  pre_tasks:
    - name: Display host information
      debug:
        var: inventory_hostname
      tags: [always]

  roles:
    - common
    - docker
    - application

  post_tasks:
    - name: Verify deployment
      uri:
        url: "http://{{ inventory_hostname }}:8080/health"
        status_code: 200
      retries: 3
      delay: 10
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Playbook Structure and Best Practices	Playbook Structure and Best Practices
Inventory and Variables	Inventory and Variables
Ansible Deployment Script	Ansible Deployment Script
Configuration Template	Configuration Template
Best Practices
✅ DO
Use roles for modularity
Implement proper error handling
Use templates for configuration
Leverage handlers for idempotency
Use serial deployment for rolling updates
Implement health checks
Store inventory in version control
Use vault for sensitive data
❌ DON'T
Use command/shell without conditionals
Copy files without templates
Run without check mode first
Mix environments in inventory
Hardcode values
Ignore error handling
Use shell for simple tasks
Weekly Installs
777
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn