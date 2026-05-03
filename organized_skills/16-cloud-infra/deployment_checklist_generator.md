---
rating: ⭐⭐⭐
title: deployment-checklist-generator
url: https://skills.sh/patricio0312rev/skills/deployment-checklist-generator
---

# deployment-checklist-generator

skills/patricio0312rev/skills/deployment-checklist-generator
deployment-checklist-generator
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill deployment-checklist-generator
SKILL.md
Deployment Checklist Generator

Ensure safe, reliable deployments with comprehensive checklists.

Pre-Deployment Checklist
# Pre-Deployment Checklist

## Code Quality

- [ ] All CI checks passing
- [ ] Code review approved (2+ reviewers)
- [ ] No known critical bugs
- [ ] Security scan passed
- [ ] Performance tests passed

## Dependencies

- [ ] All dependencies up to date
- [ ] No high/critical vulnerabilities
- [ ] Bundle size within budget
- [ ] Third-party services operational

## Database

- [ ] Migrations tested in staging
- [ ] Backup completed
- [ ] Rollback plan documented
- [ ] Data migration scripts reviewed

## Infrastructure

- [ ] Servers have capacity
- [ ] CDN cache invalidation plan
- [ ] Load balancer configured
- [ ] SSL certificates valid

## Documentation

- [ ] Changelog updated
- [ ] API docs updated (if changed)
- [ ] Deployment notes prepared
- [ ] Rollback instructions ready

## Communication

- [ ] Stakeholders notified
- [ ] Maintenance window scheduled (if needed)
- [ ] Support team briefed
- [ ] Status page prepared

## Deployment Window

- [ ] Off-peak hours selected
- [ ] Team available for monitoring
- [ ] Emergency contacts confirmed

Deployment Workflow with Checks
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  workflow_dispatch:

jobs:
  pre-deploy-checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check branch
        run: |
          if [ "${{ github.ref }}" != "refs/heads/main" ]; then
            echo "❌ Can only deploy from main branch"
            exit 1
          fi

      - name: Verify CI passed
        uses: actions/github-script@v7
        with:
          script: |
            const checks = await github.rest.checks.listForRef({
              owner: context.repo.owner,
              repo: context.repo.repo,
              ref: context.sha,
            });

            const failed = checks.data.check_runs.filter(
              check => check.conclusion === 'failure'
            );

            if (failed.length > 0) {
              throw new Error(`CI checks failed: ${failed.map(c => c.name).join(', ')}`);
            }

      - name: Check deployment window
        run: |
          HOUR=$(date +%H)
          if [ $HOUR -ge 9 ] && [ $HOUR -le 17 ]; then
            echo "⚠️ Deploying during business hours"
          else
            echo "✅ Deploying outside business hours"
          fi

      - name: Verify staging deployment
        run: |
          if ! curl -f https://staging.myapp.com/health; then
            echo "❌ Staging is not healthy"
            exit 1
          fi

  deploy:
    needs: pre-deploy-checks
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://myapp.com
    steps:
      - uses: actions/checkout@v4

      - name: Backup database
        run: ./scripts/backup-db.sh

      - name: Deploy
        run: ./scripts/deploy.sh production

      - name: Run smoke tests
        run: ./scripts/smoke-tests.sh production

      - name: Update status page
        run: |
          curl -X POST https://statuspage.io/api/v1/incidents \
            -H "Authorization: Bearer ${{ secrets.STATUSPAGE_TOKEN }}" \
            -d '{"name":"Deployment Complete","status":"resolved"}'

      - name: Create deployment record
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.repos.createDeployment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              ref: context.sha,
              environment: 'production',
              description: 'Production deployment',
            });

Smoke Test Script
#!/bin/bash
# scripts/smoke-tests.sh

ENVIRONMENT=$1
BASE_URL="https://${ENVIRONMENT}.myapp.com"

echo "🔍 Running smoke tests for $ENVIRONMENT..."

FAILED=0

# Test 1: Health endpoint
echo "Test 1: Health check"
if curl -f "$BASE_URL/health" | grep -q "ok"; then
  echo "✅ Health check passed"
else
  echo "❌ Health check failed"
  FAILED=1
fi

# Test 2: User authentication
echo "Test 2: User login"
TOKEN=$(curl -s -X POST "$BASE_URL/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123"}' \
  | jq -r '.token')

if [ -n "$TOKEN" ] && [ "$TOKEN" != "null" ]; then
  echo "✅ Login passed"
else
  echo "❌ Login failed"
  FAILED=1
fi

# Test 3: Critical API endpoints
echo "Test 3: API endpoints"
ENDPOINTS=("/api/users" "/api/products" "/api/orders")

for endpoint in "${ENDPOINTS[@]}"; do
  STATUS=$(curl -s -o /dev/null -w "%{http_code}" \
    -H "Authorization: Bearer $TOKEN" \
    "$BASE_URL$endpoint")

  if [ "$STATUS" == "200" ]; then
    echo "✅ $endpoint: $STATUS"
  else
    echo "❌ $endpoint: $STATUS"
    FAILED=1
  fi
done

# Test 4: Database connectivity
echo "Test 4: Database check"
if curl -f "$BASE_URL/api/health/db" | grep -q "connected"; then
  echo "✅ Database connected"
else
  echo "❌ Database connection failed"
  FAILED=1
fi

# Test 5: External services
echo "Test 5: External services"
SERVICES=("stripe" "sendgrid" "aws")

for service in "${SERVICES[@]}"; do
  if curl -f "$BASE_URL/api/health/$service" | grep -q "ok"; then
    echo "✅ $service: connected"
  else
    echo "❌ $service: connection failed"
    FAILED=1
  fi
done

if [ $FAILED -eq 1 ]; then
  echo "❌ Smoke tests failed"
  exit 1
fi

echo "✅ All smoke tests passed"
exit 0

Post-Deployment Verification
# Post-Deployment Verification

## Immediate Checks (0-5 minutes)

- [ ] Deployment completed successfully
- [ ] All smoke tests passed
- [ ] Health checks returning 200
- [ ] No 5xx errors in logs
- [ ] Application responding

## Short-term Monitoring (5-30 minutes)

- [ ] Error rate <1%
- [ ] Response time p95 <500ms
- [ ] CPU usage normal (<70%)
- [ ] Memory usage stable
- [ ] Database queries performing well

## Feature Verification

- [ ] Login/authentication working
- [ ] Checkout flow functional
- [ ] Search returning results
- [ ] Email notifications sending
- [ ] Payment processing working

## Metrics Dashboard

- [ ] Request volume normal
- [ ] Success rate >99%
- [ ] Latency within SLA
- [ ] No spike in errors
- [ ] User engagement stable

## Long-term Monitoring (1-24 hours)

- [ ] No user complaints
- [ ] Support tickets normal
- [ ] Revenue tracking normal
- [ ] All scheduled jobs running
- [ ] No memory leaks detected

Sign-off Template
- name: Request deployment approval
  uses: trstringer/manual-approval@v1
  with:
    secret: ${{ secrets.GITHUB_TOKEN }}
    approvers: tech-lead,ops-manager
    minimum-approvals: 2
    issue-title: "Approve Production Deployment"
    issue-body: |
      ## Deployment Details

      **Version:** ${{ github.ref_name }}
      **Commit:** ${{ github.sha }}
      **Changes:** See [changelog](CHANGELOG.md)

      ## Pre-deployment Checklist
      - ✅ All CI checks passed
      - ✅ Code review completed
      - ✅ Security scan passed
      - ✅ Staging verified

      ## Approval Required
      This deployment requires approval from tech lead and ops manager.

      **Approve:** Comment "approve" or "lgtm"
      **Reject:** Comment "reject" or "block"

Monitoring Dashboard
# Deployment Monitoring Dashboard

## Key Metrics

### Health

- API Health: ✅ UP
- Database: ✅ Connected
- Cache: ✅ Connected

### Performance

- Requests/min: 1,234
- Error rate: 0.2%
- p50 latency: 120ms
- p95 latency: 450ms
- p99 latency: 1,200ms

### Infrastructure

- CPU: 45%
- Memory: 62%
- Disk: 38%

### Business Metrics

- Active users: 523
- Successful checkouts: 89/hour
- Revenue: $15,234/hour

## Alerts

No active alerts

## Recent Deployments

- v1.3.0: Deployed 5 minutes ago ✅
- v1.2.9: Deployed 2 days ago ✅
- v1.2.8: Rolled back 3 days ago ⚠️

Best Practices
Automated checks: Enforce via CI/CD
Manual review: Critical deployments need approval
Smoke tests: Verify key functionality
Gradual rollout: Canary or blue-green
Monitoring: Watch metrics for 30 minutes
Communication: Keep stakeholders informed
Rollback ready: One-click rollback available
Output Checklist
 Pre-deployment checklist
 Deployment workflow with gates
 Smoke test script
 Post-deployment verification
 Sign-off workflow
 Monitoring dashboard
 Communication templates
 Rollback instructions
Weekly Installs
92
Repository
patricio0312rev/skills
GitHub Stars
35
First Seen
2 days ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass