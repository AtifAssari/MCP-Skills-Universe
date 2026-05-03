---
title: groq-prod-checklist
url: https://skills.sh/jeremylongshore/claude-code-plugins-plus-skills/groq-prod-checklist
---

# groq-prod-checklist

skills/jeremylongshore/claude-code-plugins-plus-skills/groq-prod-checklist
groq-prod-checklist
Installation
$ npx skills add https://github.com/jeremylongshore/claude-code-plugins-plus-skills --skill groq-prod-checklist
SKILL.md
Groq Production Checklist
Overview

Complete checklist for deploying Groq integrations to production.

Prerequisites
Staging environment tested and verified
Production API keys available
Deployment pipeline configured
Monitoring and alerting ready
Instructions
Step 1: Pre-Deployment Configuration
 Production API keys in secure vault
 Environment variables set in deployment platform
 API key scopes are minimal (least privilege)
 Webhook endpoints configured with HTTPS
 Webhook secrets stored securely
Step 2: Code Quality Verification
 All tests passing (npm test)
 No hardcoded credentials
 Error handling covers all Groq error types
 Rate limiting/backoff implemented
 Logging is production-appropriate
Step 3: Infrastructure Setup
 Health check endpoint includes Groq connectivity
 Monitoring/alerting configured
 Circuit breaker pattern implemented
 Graceful degradation configured
Step 4: Documentation Requirements
 Incident runbook created
 Key rotation procedure documented
 Rollback procedure documented
 On-call escalation path defined
Step 5: Deploy with Gradual Rollout
set -euo pipefail
# Pre-flight checks
curl -f https://staging.example.com/health
curl -s https://status.groq.com

# Gradual rollout - start with canary (10%)
kubectl apply -f k8s/production.yaml
kubectl set image deployment/groq-integration app=image:new --record
kubectl rollout pause deployment/groq-integration

# Monitor canary traffic for 10 minutes
sleep 600  # 600: timeout: 10 minutes
# Check error rates and latency before continuing

# If healthy, continue rollout to 50%
kubectl rollout resume deployment/groq-integration
kubectl rollout pause deployment/groq-integration
sleep 300  # 300: timeout: 5 minutes

# Complete rollout to 100%
kubectl rollout resume deployment/groq-integration
kubectl rollout status deployment/groq-integration

Output
Deployed Groq integration
Health checks passing
Monitoring active
Rollback procedure documented
Error Handling
Alert	Condition	Severity
API Down	5xx errors > 10/min	P1
High Latency	p99 > 5000ms	P2
Rate Limited	429 errors > 5/min	P2
Auth Failures	401/403 errors > 0	P1
Examples
Health Check Implementation
async function healthCheck(): Promise<{ status: string; groq: any }> {
  const start = Date.now();
  try {
    await groqClient.ping();
    return { status: 'healthy', groq: { connected: true, latencyMs: Date.now() - start } };
  } catch (error) {
    return { status: 'degraded', groq: { connected: false, latencyMs: Date.now() - start } };
  }
}

Immediate Rollback
set -euo pipefail
kubectl rollout undo deployment/groq-integration
kubectl rollout status deployment/groq-integration

Resources
Groq Status
Groq Support
Next Steps

For version upgrades, see groq-upgrade-migration.

Weekly Installs
26
Repository
jeremylongshore…s-skills
GitHub Stars
2.1K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass