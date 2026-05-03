---
title: dns-management
url: https://skills.sh/aj-geddes/useful-ai-prompts/dns-management
---

# dns-management

skills/aj-geddes/useful-ai-prompts/dns-management
dns-management
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill dns-management
SKILL.md
DNS Management
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement DNS management strategies for traffic routing, failover, geo-routing, and high availability using Route53, Azure DNS, or CloudFlare.

When to Use
Domain management and routing
Failover and disaster recovery
Geographic load balancing
Multi-region deployments
DNS-based traffic management
CDN integration
Health check routing
Zero-downtime migrations
Quick Start

Minimal working example:

# route53-setup.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: route53-config
  namespace: operations
data:
  setup-dns.sh: |
    #!/bin/bash
    set -euo pipefail

    DOMAIN="myapp.com"
    HOSTED_ZONE_ID="Z1234567890ABC"
    PRIMARY_ENDPOINT="myapp-primary.example.com"
    SECONDARY_ENDPOINT="myapp-secondary.example.com"

    echo "Setting up Route53 DNS for $DOMAIN"

    # Create health check for primary
    PRIMARY_HEALTH=$(aws route53 create-health-check \
      --health-check-config '{
        "Type": "HTTPS",
        "ResourcePath": "/health",
        "FullyQualifiedDomainName": "'${PRIMARY_ENDPOINT}'",
        "Port": 443,
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
AWS Route53 Configuration	AWS Route53 Configuration
DNS Failover Script	DNS Failover Script
CloudFlare DNS Configuration	CloudFlare DNS Configuration
DNS Monitoring and Validation	DNS Monitoring and Validation
Best Practices
✅ DO
Use health checks with failover
Set appropriate TTL values
Implement geolocation routing
Use weighted routing for canary
Monitor DNS resolution
Document DNS changes
Test failover procedures
Use DNS DNSSEC
❌ DON'T
Use TTL of 0
Point to single endpoint
Forget health checks
Mix DNS and application failover
Change DNS during incidents
Ignore DNS propagation time
Use generic names
Skip DNS monitoring
Weekly Installs
287
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