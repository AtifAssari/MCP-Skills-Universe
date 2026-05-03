---
title: senior-devops
url: https://skills.sh/davila7/claude-code-templates/senior-devops
---

# senior-devops

skills/davila7/claude-code-templates/senior-devops
senior-devops
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill senior-devops
Summary

CI/CD pipelines, infrastructure automation, and deployment management across AWS, GCP, and Azure.

Three core automation scripts: Pipeline Generator for CI/CD scaffolding, Terraform Scaffolder for infrastructure analysis and optimization, and Deployment Manager for production-grade deployments
Supports Docker, Kubernetes, Terraform, GitHub Actions, and CircleCI with built-in best practices and configurable templates
Includes comprehensive reference guides covering CI/CD patterns, infrastructure-as-code workflows, deployment strategies, security considerations, and troubleshooting
Handles multiple tech stacks including Node.js, Python, Go backends and PostgreSQL, Prisma databases with cloud platform integrations
SKILL.md
Senior Devops

Complete toolkit for senior devops with modern tools and best practices.

Quick Start
Main Capabilities

This skill provides three core capabilities through automated scripts:

# Script 1: Pipeline Generator
python scripts/pipeline_generator.py [options]

# Script 2: Terraform Scaffolder
python scripts/terraform_scaffolder.py [options]

# Script 3: Deployment Manager
python scripts/deployment_manager.py [options]

Core Capabilities
1. Pipeline Generator

Automated tool for pipeline generator tasks.

Features:

Automated scaffolding
Best practices built-in
Configurable templates
Quality checks

Usage:

python scripts/pipeline_generator.py <project-path> [options]

2. Terraform Scaffolder

Comprehensive analysis and optimization tool.

Features:

Deep analysis
Performance metrics
Recommendations
Automated fixes

Usage:

python scripts/terraform_scaffolder.py <target-path> [--verbose]

3. Deployment Manager

Advanced tooling for specialized tasks.

Features:

Expert-level automation
Custom configurations
Integration ready
Production-grade output

Usage:

python scripts/deployment_manager.py [arguments] [options]

Reference Documentation
Cicd Pipeline Guide

Comprehensive guide available in references/cicd_pipeline_guide.md:

Detailed patterns and practices
Code examples
Best practices
Anti-patterns to avoid
Real-world scenarios
Infrastructure As Code

Complete workflow documentation in references/infrastructure_as_code.md:

Step-by-step processes
Optimization strategies
Tool integrations
Performance tuning
Troubleshooting guide
Deployment Strategies

Technical reference guide in references/deployment_strategies.md:

Technology stack details
Configuration examples
Integration patterns
Security considerations
Scalability guidelines
Tech Stack

Languages: TypeScript, JavaScript, Python, Go, Swift, Kotlin Frontend: React, Next.js, React Native, Flutter Backend: Node.js, Express, GraphQL, REST APIs Database: PostgreSQL, Prisma, NeonDB, Supabase DevOps: Docker, Kubernetes, Terraform, GitHub Actions, CircleCI Cloud: AWS, GCP, Azure

Development Workflow
1. Setup and Configuration
# Install dependencies
npm install
# or
pip install -r requirements.txt

# Configure environment
cp .env.example .env

2. Run Quality Checks
# Use the analyzer script
python scripts/terraform_scaffolder.py .

# Review recommendations
# Apply fixes

3. Implement Best Practices

Follow the patterns and practices documented in:

references/cicd_pipeline_guide.md
references/infrastructure_as_code.md
references/deployment_strategies.md
Best Practices Summary
Code Quality
Follow established patterns
Write comprehensive tests
Document decisions
Review regularly
Performance
Measure before optimizing
Use appropriate caching
Optimize critical paths
Monitor in production
Security
Validate all inputs
Use parameterized queries
Implement proper authentication
Keep dependencies updated
Maintainability
Write clear code
Use consistent naming
Add helpful comments
Keep it simple
Common Commands
# Development
npm run dev
npm run build
npm run test
npm run lint

# Analysis
python scripts/terraform_scaffolder.py .
python scripts/deployment_manager.py --analyze

# Deployment
docker build -t app:latest .
docker-compose up -d
kubectl apply -f k8s/

Troubleshooting
Common Issues

Check the comprehensive troubleshooting section in references/deployment_strategies.md.

Getting Help
Review reference documentation
Check script output messages
Consult tech stack documentation
Review error logs
Resources
Pattern Reference: references/cicd_pipeline_guide.md
Workflow Guide: references/infrastructure_as_code.md
Technical Guide: references/deployment_strategies.md
Tool Scripts: scripts/ directory
Weekly Installs
921
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass