---
rating: ⭐⭐⭐
title: senior-qa
url: https://skills.sh/davila7/claude-code-templates/senior-qa
---

# senior-qa

skills/davila7/claude-code-templates/senior-qa
senior-qa
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill senior-qa
Summary

Automated test suite generation, coverage analysis, and E2E testing for React, Next.js, and Node.js applications.

Three core Python scripts: test suite generator with configurable templates, coverage analyzer with performance metrics and recommendations, and E2E test scaffolder for production-grade automation
Supports TypeScript, JavaScript, Python across React, Next.js, Node.js, and full modern tech stacks including Docker, Kubernetes, and cloud platforms
Includes reference documentation covering testing strategies, test automation patterns, QA best practices, and troubleshooting guidance
Built-in quality checks, performance tuning, and security considerations for scalable test infrastructure
SKILL.md
Senior Qa

Complete toolkit for senior qa with modern tools and best practices.

Quick Start
Main Capabilities

This skill provides three core capabilities through automated scripts:

# Script 1: Test Suite Generator
python scripts/test_suite_generator.py [options]

# Script 2: Coverage Analyzer
python scripts/coverage_analyzer.py [options]

# Script 3: E2E Test Scaffolder
python scripts/e2e_test_scaffolder.py [options]

Core Capabilities
1. Test Suite Generator

Automated tool for test suite generator tasks.

Features:

Automated scaffolding
Best practices built-in
Configurable templates
Quality checks

Usage:

python scripts/test_suite_generator.py <project-path> [options]

2. Coverage Analyzer

Comprehensive analysis and optimization tool.

Features:

Deep analysis
Performance metrics
Recommendations
Automated fixes

Usage:

python scripts/coverage_analyzer.py <target-path> [--verbose]

3. E2E Test Scaffolder

Advanced tooling for specialized tasks.

Features:

Expert-level automation
Custom configurations
Integration ready
Production-grade output

Usage:

python scripts/e2e_test_scaffolder.py [arguments] [options]

Reference Documentation
Testing Strategies

Comprehensive guide available in references/testing_strategies.md:

Detailed patterns and practices
Code examples
Best practices
Anti-patterns to avoid
Real-world scenarios
Test Automation Patterns

Complete workflow documentation in references/test_automation_patterns.md:

Step-by-step processes
Optimization strategies
Tool integrations
Performance tuning
Troubleshooting guide
Qa Best Practices

Technical reference guide in references/qa_best_practices.md:

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
python scripts/coverage_analyzer.py .

# Review recommendations
# Apply fixes

3. Implement Best Practices

Follow the patterns and practices documented in:

references/testing_strategies.md
references/test_automation_patterns.md
references/qa_best_practices.md
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
python scripts/coverage_analyzer.py .
python scripts/e2e_test_scaffolder.py --analyze

# Deployment
docker build -t app:latest .
docker-compose up -d
kubectl apply -f k8s/

Troubleshooting
Common Issues

Check the comprehensive troubleshooting section in references/qa_best_practices.md.

Getting Help
Review reference documentation
Check script output messages
Consult tech stack documentation
Review error logs
Resources
Pattern Reference: references/testing_strategies.md
Workflow Guide: references/test_automation_patterns.md
Technical Guide: references/qa_best_practices.md
Tool Scripts: scripts/ directory
Weekly Installs
790
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass