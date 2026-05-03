---
title: code-reviewer
url: https://skills.sh/davila7/claude-code-templates/code-reviewer
---

# code-reviewer

skills/davila7/claude-code-templates/code-reviewer
code-reviewer
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill code-reviewer
Summary

Automated code review across TypeScript, JavaScript, Python, Swift, Kotlin, and Go with quality analysis and security scanning.

Three core scripts: PR analyzer for automated scaffolding, code quality checker for deep analysis and performance metrics, and review report generator for structured output
Includes comprehensive reference documentation covering code review checklists, coding standards, and common antipatterns with real-world examples
Supports modern tech stacks including React, Node.js, GraphQL, PostgreSQL, Docker, Kubernetes, and major cloud platforms
Built-in best practices for code quality, performance optimization, security validation, and maintainability with configurable templates
SKILL.md
Code Reviewer

Complete toolkit for code reviewer with modern tools and best practices.

Quick Start
Main Capabilities

This skill provides three core capabilities through automated scripts:

# Script 1: Pr Analyzer
python scripts/pr_analyzer.py [options]

# Script 2: Code Quality Checker
python scripts/code_quality_checker.py [options]

# Script 3: Review Report Generator
python scripts/review_report_generator.py [options]

Core Capabilities
1. Pr Analyzer

Automated tool for pr analyzer tasks.

Features:

Automated scaffolding
Best practices built-in
Configurable templates
Quality checks

Usage:

python scripts/pr_analyzer.py <project-path> [options]

2. Code Quality Checker

Comprehensive analysis and optimization tool.

Features:

Deep analysis
Performance metrics
Recommendations
Automated fixes

Usage:

python scripts/code_quality_checker.py <target-path> [--verbose]

3. Review Report Generator

Advanced tooling for specialized tasks.

Features:

Expert-level automation
Custom configurations
Integration ready
Production-grade output

Usage:

python scripts/review_report_generator.py [arguments] [options]

Reference Documentation
Code Review Checklist

Comprehensive guide available in references/code_review_checklist.md:

Detailed patterns and practices
Code examples
Best practices
Anti-patterns to avoid
Real-world scenarios
Coding Standards

Complete workflow documentation in references/coding_standards.md:

Step-by-step processes
Optimization strategies
Tool integrations
Performance tuning
Troubleshooting guide
Common Antipatterns

Technical reference guide in references/common_antipatterns.md:

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
python scripts/code_quality_checker.py .

# Review recommendations
# Apply fixes

3. Implement Best Practices

Follow the patterns and practices documented in:

references/code_review_checklist.md
references/coding_standards.md
references/common_antipatterns.md
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
python scripts/code_quality_checker.py .
python scripts/review_report_generator.py --analyze

# Deployment
docker build -t app:latest .
docker-compose up -d
kubectl apply -f k8s/

Troubleshooting
Common Issues

Check the comprehensive troubleshooting section in references/common_antipatterns.md.

Getting Help
Review reference documentation
Check script output messages
Consult tech stack documentation
Review error logs
Resources
Pattern Reference: references/code_review_checklist.md
Workflow Guide: references/coding_standards.md
Technical Guide: references/common_antipatterns.md
Tool Scripts: scripts/ directory
Weekly Installs
598
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass