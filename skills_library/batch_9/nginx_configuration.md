---
title: nginx-configuration
url: https://skills.sh/aj-geddes/useful-ai-prompts/nginx-configuration
---

# nginx-configuration

skills/aj-geddes/useful-ai-prompts/nginx-configuration
nginx-configuration
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill nginx-configuration
Summary

Production-grade Nginx configuration for reverse proxying, load balancing, SSL/TLS termination, and API gateway patterns.

Covers eight primary use cases: reverse proxy setup, load balancing, SSL termination, HTTP/2 and gRPC support, caching, rate limiting, URL rewriting, and API gateway functionality
Includes reference guides for production configuration, HTTPS with load balancing, automated setup scripts, and monitoring integration
Best practices section highlights performance tuning (HTTP/2, gzip, connection pooling), security hardening (strong ciphers, security headers), and operational patterns (health checks, least_conn balancing, log separation)
SKILL.md
Nginx Configuration
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Master Nginx configuration for production-grade web servers, reverse proxies, load balancing, SSL termination, caching, and API gateway patterns with advanced performance tuning.

When to Use
Reverse proxy setup
Load balancing between backend services
SSL/TLS termination
HTTP/2 and gRPC support
Caching and compression
Rate limiting and DDoS protection
URL rewriting and routing
API gateway functionality
Quick Start

Minimal working example:

# /etc/nginx/nginx.conf
user nginx;
worker_processes auto;
worker_rlimit_nofile 65535;
error_log /var/log/nginx/error.log warn;
pid /var/run/nginx.pid;

events {
    worker_connections 4096;
    use epoll;
    multi_accept on;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # Logging
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';

    log_format upstream_time '$remote_addr - $remote_user [$time_local] '
                            '"$request" $status $body_bytes_sent '
                            '"$http_referer" "$http_user_agent" '
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Production Nginx Configuration	Production Nginx Configuration
HTTPS Server with Load Balancing	HTTPS Server with Load Balancing
Nginx Configuration Script	Nginx Configuration Script
Nginx Monitoring Configuration	Nginx Monitoring Configuration
Best Practices
✅ DO
Use HTTP/2 for performance
Enable SSL/TLS with strong ciphers
Implement proper caching strategies
Use upstream connection pooling
Monitor with stub_status or prometheus
Rate limit to prevent abuse
Add security headers
Use least_conn load balancing
Keep error logs separate from access logs
❌ DON'T
Disable gzip compression
Use weak SSL ciphers
Cache authenticated responses
Allow direct access to backends
Ignore upstream health checks
Mix HTTP and HTTPS without redirect
Use default error pages in production
Cache sensitive user data
Weekly Installs
733
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn