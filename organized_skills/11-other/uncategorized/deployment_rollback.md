---
rating: ⭐⭐⭐
title: deployment-rollback
url: https://skills.sh/sgcarstrends/sgcarstrends/deployment-rollback
---

# deployment-rollback

skills/sgcarstrends/sgcarstrends/deployment-rollback
deployment-rollback
Installation
$ npx skills add https://github.com/sgcarstrends/sgcarstrends --skill deployment-rollback
SKILL.md
Deployment Rollback Skill
Quick Rollback via Vercel
Using Vercel Dashboard
Go to Vercel Dashboard → Project → Deployments
Find the previous working deployment
Click the three dots menu → "Promote to Production"
Using Vercel CLI
# List recent deployments
vercel list

# Promote a specific deployment to production
vercel promote <deployment-url>

# Or rollback to previous production deployment
vercel rollback

Database Rollback
# Rollback last migration
pnpm -F @sgcarstrends/database db:rollback

# Rollback to specific migration
pnpm -F @sgcarstrends/database db:rollback --to 20240115_initial

# Restore from backup
pg_dump $DATABASE_URL > backup-pre-deploy.sql  # Before deploy
psql $DATABASE_URL < backup-pre-deploy.sql     # Restore if needed

Git-Based Rollback
# Revert specific commit
git revert <commit-hash>
git push origin main  # Triggers Vercel redeploy

# Create rollback branch
git checkout -b rollback/v1.1.0
git reset --hard v1.1.0
git push origin rollback/v1.1.0
gh pr create --title "Rollback to v1.1.0" --body "Emergency rollback"

Cache Invalidation
# Revalidate Next.js cache
curl -X POST "https://sgcarstrends.com/api/revalidate?tag=all&secret=$REVALIDATE_TOKEN"

# Clear Redis cache
redis-cli -h $REDIS_HOST FLUSHALL

Health Checks During Rollback
curl -f https://sgcarstrends.com || echo "Web unhealthy"
psql $DATABASE_URL -c "SELECT 1" || echo "Database unreachable"

Rollback Checklist

Pre-Rollback:

 Identify issue and severity
 Determine scope (full/partial)
 Check backup availability
 Notify team

During:

 Rollback via Vercel dashboard or CLI
 Rollback database if needed
 Clear caches
 Verify health checks
 Run smoke tests

Post:

 Monitor error rates in Vercel dashboard
 Verify functionality restored
 Document what happened
 Create postmortem
Common Scenarios

Critical Bug:

vercel rollback
curl https://sgcarstrends.com/api/health


Database Migration Failure:

pnpm -F @sgcarstrends/database db:rollback
git revert HEAD
git push origin main

Troubleshooting

Rollback deployment not working:

# Force redeploy from known good commit
git checkout v1.1.0
vercel --prod


Database schema mismatch:

pnpm -F @sgcarstrends/database db:rollback
# Or restore backup: psql $DATABASE_URL < backup-pre-deploy.sql

Best Practices
Always Backup: Create database backups before major deployments
Test Rollback: Practice rollback procedures in preview deployments
Feature Flags: Use for quick feature disabling without rollback
Monitor Closely: Watch Vercel analytics during and after rollback
Document Everything: Record what happened and why
References
Vercel Rollbacks: https://vercel.com/docs/deployments/rollbacks
See monitoring skill for debugging issues
Weekly Installs
57
Repository
sgcarstrends/sg…rstrends
GitHub Stars
20
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass