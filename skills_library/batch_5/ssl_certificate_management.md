---
title: ssl-certificate-management
url: https://skills.sh/aj-geddes/useful-ai-prompts/ssl-certificate-management
---

# ssl-certificate-management

skills/aj-geddes/useful-ai-prompts/ssl-certificate-management
ssl-certificate-management
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill ssl-certificate-management
SKILL.md
SSL Certificate Management
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement automated SSL/TLS certificate management across infrastructure, including provisioning, renewal, monitoring, and secure distribution to services.

When to Use
HTTPS/TLS enablement
Certificate renewal automation
Multi-domain certificate management
Wildcard certificate handling
Certificate monitoring and alerts
Zero-downtime certificate rotation
Internal PKI management
Quick Start

Minimal working example:

# cert-manager-setup.yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: admin@myapp.com
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
      # HTTP-01 solver for standard domains
      - http01:
          ingress:
            class: nginx
        selector:
          dnsNames:
            - "myapp.com"
            - "www.myapp.com"

      # DNS-01 solver for wildcard domains
      - dns01:
          route53:
            region: us-east-1
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Let's Encrypt with Cert-Manager	Let's Encrypt with Cert-Manager
AWS ACM Certificate Management	AWS ACM Certificate Management
Certificate Monitoring and Renewal	Certificate Monitoring and Renewal
Automated Certificate Renewal	Automated Certificate Renewal
Certificate Pinning	Certificate Pinning
Best Practices
✅ DO
Automate certificate renewal
Use Let's Encrypt for public certs
Monitor certificate expiration
Use wildcard certs strategically
Implement certificate pinning
Rotate certificates regularly
Store keys securely
Use strong key sizes (2048+ RSA, 256+ ECDSA)
❌ DON'T
Manual certificate management
Self-signed certs in production
Share private keys
Ignore expiration warnings
Use weak key sizes
Mix dev and prod certs
Commit certs to git
Disable certificate validation
Weekly Installs
297
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass