---
rating: ⭐⭐⭐
title: load-balancer-setup
url: https://skills.sh/aj-geddes/useful-ai-prompts/load-balancer-setup
---

# load-balancer-setup

skills/aj-geddes/useful-ai-prompts/load-balancer-setup
load-balancer-setup
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill load-balancer-setup
SKILL.md
Load Balancer Setup
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Deploy and configure load balancers to distribute traffic across multiple backend servers, ensuring high availability, fault tolerance, and optimal resource utilization across your infrastructure.

When to Use
Multi-server traffic distribution
High availability and failover
Session persistence and sticky sessions
Health checking and auto-recovery
SSL/TLS termination
Cross-region load balancing
API rate limiting at load balancer
DDoS mitigation
Quick Start

Minimal working example:

# /etc/haproxy/haproxy.cfg
global
    log stdout local0
    log stdout local1 notice
    maxconn 4096
    daemon

    # Security
    tune.ssl.default-dh-param 2048
    ssl-default-bind-ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256
    ssl-default-bind-options ssl-min-ver TLSv1.2

defaults
    log global
    mode http
    option httplog
    option denylogin
    option forwardfor
    option http-server-close

    # Timeouts
    timeout connect 5000
    timeout client 50000
    timeout server 50000

// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
HAProxy Configuration	HAProxy Configuration
AWS Application Load Balancer (CloudFormation)	AWS Application Load Balancer (CloudFormation)
Load Balancer Health Check Script	Load Balancer Health Check Script
Load Balancer Monitoring	Load Balancer Monitoring
Best Practices
✅ DO
Implement health checks
Use connection pooling
Enable session persistence when needed
Monitor load balancer metrics
Implement rate limiting
Use multiple availability zones
Enable SSL/TLS termination
Implement graceful connection draining
❌ DON'T
Allow single point of failure
Skip health check configuration
Mix HTTP and HTTPS without redirect
Ignore backend server limits
Over-provision without monitoring
Cache sensitive responses
Use default security groups
Neglect backup load balancers
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
SocketPass
SnykWarn