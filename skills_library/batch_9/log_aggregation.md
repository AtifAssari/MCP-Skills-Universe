---
title: log-aggregation
url: https://skills.sh/aj-geddes/useful-ai-prompts/log-aggregation
---

# log-aggregation

skills/aj-geddes/useful-ai-prompts/log-aggregation
log-aggregation
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill log-aggregation
SKILL.md
Log Aggregation
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build comprehensive log aggregation systems to collect, parse, and analyze logs from multiple sources, enabling centralized monitoring, debugging, and compliance auditing.

When to Use
Centralized log collection
Distributed system debugging
Compliance and audit logging
Security event monitoring
Application performance analysis
Error tracking and alerting
Historical log retention
Real-time log searching
Quick Start

Minimal working example:

# docker-compose.yml - ELK Stack setup
version: "3.8"

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.5.0
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ports:
      - "9200:9200"
    volumes:
      - elasticsearch_data:/usr/share/elasticsearch/data
    healthcheck:
      test: curl -s http://localhost:9200 >/dev/null || exit 1
      interval: 10s
      timeout: 5s
      retries: 5

  logstash:
    image: docker.elastic.co/logstash/logstash:8.5.0
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf
    ports:
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
ELK Stack Configuration	ELK Stack Configuration
Logstash Pipeline Configuration	Logstash Pipeline Configuration
Filebeat Configuration	Filebeat Configuration
Kibana Dashboard and Alerts	Kibana Dashboard and Alerts
Loki Configuration (Kubernetes)	Loki Configuration (Kubernetes)
Log Aggregation Deployment Script	Log Aggregation Deployment Script
Best Practices
✅ DO
Parse and structure log data
Use appropriate log levels
Add contextual information
Implement log retention policies
Set up log-based alerting
Index important fields
Use consistent timestamp formats
Implement access controls
❌ DON'T
Store sensitive data in logs
Log at DEBUG level in production
Send raw unstructured logs
Ignore storage costs
Skip log parsing
Lack monitoring of log systems
Store logs forever
Log PII without encryption
Weekly Installs
276
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