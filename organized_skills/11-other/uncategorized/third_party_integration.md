---
rating: ⭐⭐
title: third-party-integration
url: https://skills.sh/aj-geddes/useful-ai-prompts/third-party-integration
---

# third-party-integration

skills/aj-geddes/useful-ai-prompts/third-party-integration
third-party-integration
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill third-party-integration
SKILL.md
Third-Party Integration
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build robust integrations with external services using standardized patterns for API calls, error handling, authentication, and data transformation.

When to Use
Integrating payment processors (Stripe, PayPal)
Using messaging services (SendGrid, Twilio)
Connecting to analytics platforms (Mixpanel, Segment)
Syncing with storage services (AWS S3, Google Cloud)
Integrating CRM systems (Salesforce, HubSpot)
Building multi-service architectures
Quick Start

Minimal working example:

const axios = require("axios");

class ThirdPartyClient {
  constructor(config) {
    this.apiKey = config.apiKey;
    this.baseUrl = config.baseUrl;
    this.timeout = config.timeout || 30000;
    this.retryAttempts = config.retryAttempts || 3;
    this.retryDelay = config.retryDelay || 1000;
    this.client = axios.create({
      baseURL: this.baseUrl,
      timeout: this.timeout,
      headers: {
        Authorization: `Bearer ${this.apiKey}`,
        "Content-Type": "application/json",
      },
    });
  }

  async request(method, endpoint, data = null, options = {}) {
    let lastError;

    for (let attempt = 0; attempt < this.retryAttempts; attempt++) {
      try {
        const response = await this.client({
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Third-Party Client Wrapper	Third-Party Client Wrapper
Payment Processor Integration (Stripe)	Payment Processor Integration (Stripe)
Email Service Integration (SendGrid)	Email Service Integration (SendGrid)
Python Third-Party Integration	Python Third-Party Integration
Data Transformation	Data Transformation
Best Practices
✅ DO
Implement retry logic with exponential backoff
Validate webhook signatures
Log all API interactions
Use environment variables for secrets
Transform API responses to internal models
Implement circuit breakers for critical services
Monitor API quota and rate limits
Add proper error handling
Use timeouts appropriately
Test with sandbox/test API keys
❌ DON'T
Hardcode API keys
Retry all errors indefinitely
Log sensitive data
Trust unvalidated webhook data
Ignore rate limits
Make synchronous blocking calls
Expose vendor-specific details to clients
Skip error handling
Use production keys in tests
Weekly Installs
264
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