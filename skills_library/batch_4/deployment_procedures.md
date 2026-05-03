---
title: deployment-procedures
url: https://skills.sh/sickn33/antigravity-awesome-skills/deployment-procedures
---

# deployment-procedures

skills/sickn33/antigravity-awesome-skills/deployment-procedures
deployment-procedures
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill deployment-procedures
Summary

Deployment principles and decision-making framework for safe production releases.

Covers five core deployment phases: prepare, backup, deploy, verify, and confirm/rollback, with platform-specific procedures for Vercel, Railway, Docker, Kubernetes, and VPS environments
Includes pre-deployment verification across code quality, build, environment, and safety categories, plus post-deployment health checks and monitoring windows
Provides rollback strategies by platform and decision criteria for when to rollback versus fix forward
Teaches zero-downtime deployment patterns (rolling, blue-green, canary) and emergency response procedures for service outages
Emphasizes principles and reasoning over scripts, encouraging adaptation to your specific platform and risk profile
SKILL.md
Deployment Procedures

Deployment principles and decision-making for safe production releases. Learn to THINK, not memorize scripts.

⚠️ How to Use This Skill

This skill teaches deployment principles, not bash scripts to copy.

Every deployment is unique
Understand the WHY behind each step
Adapt procedures to your platform
1. Platform Selection
Decision Tree
What are you deploying?
│
├── Static site / JAMstack
│   └── Vercel, Netlify, Cloudflare Pages
│
├── Simple web app
│   ├── Managed → Railway, Render, Fly.io
│   └── Control → VPS + PM2/Docker
│
├── Microservices
│   └── Container orchestration
│
└── Serverless
    └── Edge functions, Lambda

Each Platform Has Different Procedures
Platform	Deployment Method
Vercel/Netlify	Git push, auto-deploy
Railway/Render	Git push or CLI
VPS + PM2	SSH + manual steps
Docker	Image push + orchestration
Kubernetes	kubectl apply
2. Pre-Deployment Principles
The 4 Verification Categories
Category	What to Check
Code Quality	Tests passing, linting clean, reviewed
Build	Production build works, no warnings
Environment	Env vars set, secrets current
Safety	Backup done, rollback plan ready
Pre-Deployment Checklist
 All tests passing
 Code reviewed and approved
 Production build successful
 Environment variables verified
 Database migrations ready (if any)
 Rollback plan documented
 Team notified
 Monitoring ready
3. Deployment Workflow Principles
The 5-Phase Process
1. PREPARE
   └── Verify code, build, env vars

2. BACKUP
   └── Save current state before changing

3. DEPLOY
   └── Execute with monitoring open

4. VERIFY
   └── Health check, logs, key flows

5. CONFIRM or ROLLBACK
   └── All good? Confirm. Issues? Rollback.

Phase Principles
Phase	Principle
Prepare	Never deploy untested code
Backup	Can't rollback without backup
Deploy	Watch it happen, don't walk away
Verify	Trust but verify
Confirm	Have rollback trigger ready
4. Post-Deployment Verification
What to Verify
Check	Why
Health endpoint	Service is running
Error logs	No new errors
Key user flows	Critical features work
Performance	Response times acceptable
Verification Window
First 5 minutes: Active monitoring
15 minutes: Confirm stable
1 hour: Final verification
Next day: Review metrics
5. Rollback Principles
When to Rollback
Symptom	Action
Service down	Rollback immediately
Critical errors	Rollback
Performance >50% degraded	Consider rollback
Minor issues	Fix forward if quick
Rollback Strategy by Platform
Platform	Rollback Method
Vercel/Netlify	Redeploy previous commit
Railway/Render	Rollback in dashboard
VPS + PM2	Restore backup, restart
Docker	Previous image tag
K8s	kubectl rollout undo
Rollback Principles
Speed over perfection: Rollback first, debug later
Don't compound errors: One rollback, not multiple changes
Communicate: Tell team what happened
Post-mortem: Understand why after stable
6. Zero-Downtime Deployment
Strategies
Strategy	How It Works
Rolling	Replace instances one by one
Blue-Green	Switch traffic between environments
Canary	Gradual traffic shift
Selection Principles
Scenario	Strategy
Standard release	Rolling
High-risk change	Blue-green (easy rollback)
Need validation	Canary (test with real traffic)
7. Emergency Procedures
Service Down Priority
Assess: What's the symptom?
Quick fix: Restart if unclear
Rollback: If restart doesn't help
Investigate: After stable
Investigation Order
Check	Common Issues
Logs	Errors, exceptions
Resources	Disk full, memory
Network	DNS, firewall
Dependencies	Database, APIs
8. Anti-Patterns
❌ Don't	✅ Do
Deploy on Friday	Deploy early in week
Rush deployment	Follow the process
Skip staging	Always test first
Deploy without backup	Backup before deploy
Walk away after deploy	Monitor for 15+ min
Multiple changes at once	One change at a time
9. Decision Checklist

Before deploying:

 Platform-appropriate procedure?
 Backup strategy ready?
 Rollback plan documented?
 Monitoring configured?
 Team notified?
 Time to monitor after?
10. Best Practices
Small, frequent deploys over big releases
Feature flags for risky changes
Automate repetitive steps
Document every deployment
Review what went wrong after issues
Test rollback before you need it

Remember: Every deployment is a risk. Minimize risk through preparation, not speed.

When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
495
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass