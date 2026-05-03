---
title: alert-management
url: https://skills.sh/aj-geddes/useful-ai-prompts/alert-management
---

# alert-management

skills/aj-geddes/useful-ai-prompts/alert-management
alert-management
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill alert-management
SKILL.md
Alert Management
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Design and implement sophisticated alert management systems with PagerDuty integration, escalation policies, alert routing, and incident coordination.

When to Use
Setting up alert routing
Managing on-call schedules
Coordinating incident response
Creating escalation policies
Integrating alerting systems
Quick Start

Minimal working example:

// pagerduty-client.js
const axios = require("axios");

class PagerDutyClient {
  constructor(apiToken) {
    this.apiToken = apiToken;
    this.baseUrl = "https://api.pagerduty.com";
    this.eventUrl = "https://events.pagerduty.com/v2/enqueue";

    this.client = axios.create({
      baseURL: this.baseUrl,
      headers: {
        Authorization: `Token token=${apiToken}`,
        Accept: "application/vnd.pagerduty+json;version=2",
      },
    });
  }

  async triggerEvent(config) {
    const event = {
      routing_key: config.routingKey,
      event_action: config.eventAction || "trigger",
      dedup_key: config.dedupKey || `event-${Date.now()}`,
      payload: {
        summary: config.summary,
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
PagerDuty Client Integration	PagerDuty Client Integration
Alertmanager Configuration	Alertmanager Configuration
Alert Handler Middleware	Alert Handler Middleware
Alert Routing Engine	Alert Routing Engine
Docker Compose Alert Stack	Docker Compose Alert Stack
Best Practices
✅ DO
Set appropriate thresholds
Implement alert deduplication
Use clear alert names
Include runbook links
Configure escalation properly
Test alert rules
Monitor alert quality
Set repeat intervals
Track alert metrics
Document alert meanings
❌ DON'T
Alert on every anomaly
Ignore alert fatigue
Set thresholds arbitrarily
Skip runbooks
Alert without action
Disable alerts in production
Use vague alert names
Forget escalation policies
Re-alert too frequently
Weekly Installs
273
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass