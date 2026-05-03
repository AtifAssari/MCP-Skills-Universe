---
title: secrets-management
url: https://skills.sh/aj-geddes/useful-ai-prompts/secrets-management
---

# secrets-management

skills/aj-geddes/useful-ai-prompts/secrets-management
secrets-management
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill secrets-management
SKILL.md
Secrets Management
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Deploy and configure secure secrets management systems to store, rotate, and audit access to sensitive credentials, API keys, and certificates across your infrastructure.

When to Use
Database credentials management
API key and token storage
Certificate management
SSH key distribution
Credential rotation automation
Audit and compliance logging
Multi-environment secrets
Encryption key management
Quick Start

Minimal working example:

# vault-config.hcl
storage "raft" {
  path    = "/vault/data"
  node_id = "node1"
}

listener "tcp" {
  address       = "0.0.0.0:8200"
  tls_cert_file = "/vault/config/vault.crt"
  tls_key_file  = "/vault/config/vault.key"
}

api_addr     = "https://0.0.0.0:8200"
cluster_addr = "https://0.0.0.0:8201"

ui = true

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
HashiCorp Vault Setup	HashiCorp Vault Setup
Vault Kubernetes Integration	Vault Kubernetes Integration
Vault Secret Configuration	Vault Secret Configuration
AWS Secrets Manager Configuration	AWS Secrets Manager Configuration
Kubernetes Secrets	Kubernetes Secrets
Best Practices
✅ DO
Rotate secrets regularly
Use strong encryption
Implement access controls
Audit secret access
Use managed services
Implement secret versioning
Encrypt secrets in transit
Use separate secrets per environment
❌ DON'T
Store secrets in code
Use weak encryption
Share secrets via email/chat
Commit secrets to version control
Use single master password
Log secret values
Hardcode credentials
Disable rotation
Weekly Installs
271
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass