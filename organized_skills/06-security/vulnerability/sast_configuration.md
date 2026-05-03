---
rating: ⭐⭐⭐
title: sast-configuration
url: https://skills.sh/wshobson/agents/sast-configuration
---

# sast-configuration

skills/wshobson/agents/sast-configuration
sast-configuration
Installation
$ npx skills add https://github.com/wshobson/agents --skill sast-configuration
Summary

Configure SAST tools for automated vulnerability detection across multiple languages and CI/CD pipelines.

Covers three major SAST platforms: Semgrep (custom pattern-based rules), SonarQube (quality gates and code coverage), and CodeQL (GitHub Advanced Security integration)
Includes CI/CD integration patterns for GitHub Actions, GitLab CI, and Jenkins, plus pre-commit hook setup for early detection
Provides production-ready configuration templates, custom rule examples, and performance optimization strategies for large codebases
Addresses false positive management, compliance scanning (PCI-DSS, SOC 2), and team enablement workflows
SKILL.md
SAST Configuration

Static Application Security Testing (SAST) tool setup, configuration, and custom rule creation for comprehensive security scanning across multiple programming languages.

Overview

This skill provides comprehensive guidance for setting up and configuring SAST tools including Semgrep, SonarQube, and CodeQL. Use this skill when you need to:

Set up SAST scanning in CI/CD pipelines
Create custom security rules for your codebase
Configure quality gates and compliance policies
Optimize scan performance and reduce false positives
Integrate multiple SAST tools for defense-in-depth
Core Capabilities
1. Semgrep Configuration
Custom rule creation with pattern matching
Language-specific security rules (Python, JavaScript, Go, Java, etc.)
CI/CD integration (GitHub Actions, GitLab CI, Jenkins)
False positive tuning and rule optimization
Organizational policy enforcement
2. SonarQube Setup
Quality gate configuration
Security hotspot analysis
Code coverage and technical debt tracking
Custom quality profiles for languages
Enterprise integration with LDAP/SAML
3. CodeQL Analysis
GitHub Advanced Security integration
Custom query development
Vulnerability variant analysis
Security research workflows
SARIF result processing
Quick Start
Initial Assessment
Identify primary programming languages in your codebase
Determine compliance requirements (PCI-DSS, SOC 2, etc.)
Choose SAST tool based on language support and integration needs
Review baseline scan to understand current security posture
Basic Setup
# Semgrep quick start
pip install semgrep
semgrep --config=auto --error

# SonarQube with Docker
docker run -d --name sonarqube -p 9000:9000 sonarqube:10.8-community

# CodeQL CLI setup
gh extension install github/gh-codeql
codeql database create mydb --language=python

Integration Patterns
CI/CD Pipeline Integration
# GitHub Actions example
- name: Run Semgrep
  uses: returntocorp/semgrep-action@v1
  with:
    config: >-
      p/security-audit
      p/owasp-top-ten

Pre-commit Hook
# .pre-commit-config.yaml
- repo: https://github.com/returntocorp/semgrep
  rev: v1.45.0
  hooks:
    - id: semgrep
      args: ['--config=auto', '--error']

Best Practices

Start with Baseline

Run initial scan to establish security baseline
Prioritize critical and high severity findings
Create remediation roadmap

Incremental Adoption

Begin with security-focused rules
Gradually add code quality rules
Implement blocking only for critical issues

False Positive Management

Document legitimate suppressions
Create allow lists for known safe patterns
Regularly review suppressed findings

Performance Optimization

Exclude test files and generated code
Use incremental scanning for large codebases
Cache scan results in CI/CD

Team Enablement

Provide security training for developers
Create internal documentation for common patterns
Establish security champions program
Common Use Cases
New Project Setup
./scripts/run-sast.sh --setup --language python --tools semgrep,sonarqube

Custom Rule Development
# See references/semgrep-rules.md for detailed examples
rules:
  - id: hardcoded-jwt-secret
    pattern: jwt.encode($DATA, "...", ...)
    message: JWT secret should not be hardcoded
    severity: ERROR

Compliance Scanning
# PCI-DSS focused scan
semgrep --config p/pci-dss --json -o pci-scan-results.json

Troubleshooting
High False Positive Rate
Review and tune rule sensitivity
Add path filters to exclude test files
Use nostmt metadata for noisy patterns
Create organization-specific rule exceptions
Performance Issues
Enable incremental scanning
Parallelize scans across modules
Optimize rule patterns for efficiency
Cache dependencies and scan results
Integration Failures
Verify API tokens and credentials
Check network connectivity and proxy settings
Review SARIF output format compatibility
Validate CI/CD runner permissions
Related Skills
OWASP Top 10 Checklist
Container Security
Dependency Scanning
Tool Comparison
Tool	Best For	Language Support	Cost	Integration
Semgrep	Custom rules, fast scans	30+ languages	Free/Enterprise	Excellent
SonarQube	Code quality + security	25+ languages	Free/Commercial	Good
CodeQL	Deep analysis, research	10+ languages	Free (OSS)	GitHub native
Next Steps
Complete initial SAST tool setup
Run baseline security scan
Create custom rules for organization-specific patterns
Integrate into CI/CD pipeline
Establish security gate policies
Train development team on findings and remediation
Weekly Installs
5.5K
Repository
wshobson/agents
GitHub Stars
34.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass