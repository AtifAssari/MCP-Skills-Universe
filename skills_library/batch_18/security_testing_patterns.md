---
title: security-testing-patterns
url: https://skills.sh/nickcrew/claude-ctx-plugin/security-testing-patterns
---

# security-testing-patterns

skills/nickcrew/claude-ctx-plugin/security-testing-patterns
security-testing-patterns
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill security-testing-patterns
SKILL.md
Security Testing Patterns

Expert guidance for implementing comprehensive security testing strategies including static analysis, dynamic testing, penetration testing, and vulnerability assessment.

When to Use This Skill
Implementing security testing pipelines in CI/CD
Conducting security audits and vulnerability assessments
Validating application security controls and defenses
Performing penetration testing and security reviews
Configuring SAST/DAST tools and interpreting results
Testing authentication and authorization mechanisms
Evaluating API security and compliance with OWASP standards
Integrating security scanning into development workflows
Responding to security findings and prioritizing remediation
Training teams on security testing methodologies
Core Concepts
Security Testing Pyramid (Layered Approach)
Unit Security Tests - Test security functions (encryption, validation)
SAST - Static analysis during development
SCA - Dependency and component vulnerability scanning
DAST - Dynamic testing in running applications
IAST - Interactive analysis combining SAST and DAST
Penetration Testing - Manual security testing by experts
Red Team Exercises - Adversarial simulation testing
Testing Categories

Static Testing (SAST)

Analyzes source code without execution
Early detection in development lifecycle
Complete code coverage
High false positive rates

Dynamic Testing (DAST)

Tests running applications
Detects runtime and configuration issues
Language agnostic
Requires deployed environment

Composition Analysis (SCA)

Scans dependencies for vulnerabilities
Tracks license compliance
Automated remediation options

Manual Testing

Penetration testing
Business logic validation
Complex attack scenarios
Quick Reference
Task	Load reference
Static Application Security Testing (SAST)	skills/security-testing-patterns/references/sast.md
Dynamic Application Security Testing (DAST)	skills/security-testing-patterns/references/dast.md
Software Composition Analysis (SCA)	skills/security-testing-patterns/references/sca.md
Penetration Testing Techniques	skills/security-testing-patterns/references/penetration-testing.md
API Security Testing (OWASP Top 10)	skills/security-testing-patterns/references/api-security.md
Fuzzing and Property-Based Testing	skills/security-testing-patterns/references/fuzzing.md
Security Automation Pipeline	skills/security-testing-patterns/references/automation-pipeline.md
Security Testing Workflow
Phase 1: Planning
Define security requirements and threat model
Select appropriate testing tools and techniques
Establish baseline security posture
Set severity thresholds and acceptance criteria
Phase 2: Automated Testing
SAST - Integrate into IDE and CI/CD pipeline
SCA - Configure dependency scanning (npm audit, Snyk, Dependabot)
DAST - Schedule scans against deployed environments
Container Scanning - Scan Docker images (Trivy, Aqua)
Phase 3: Manual Testing
Authentication and authorization testing
Business logic vulnerability assessment
API security testing (OWASP API Top 10)
Penetration testing and exploitation
Phase 4: Analysis and Remediation
Triage findings by severity and exploitability
Eliminate false positives
Prioritize remediation based on risk
Track vulnerabilities to resolution
Verify fixes with regression testing
Phase 5: Continuous Monitoring
Monitor for new vulnerabilities in dependencies
Re-scan after code changes
Conduct periodic penetration tests
Update security baselines and policies
Common Mistakes
Tool Selection
Wrong: Using only SAST or only DAST
Right: Layered approach combining multiple testing types
False Positive Management
Wrong: Ignoring or suppressing findings without review
Right: Systematic triage process with security team validation
Integration Timing
Wrong: Security testing only before release
Right: Continuous security testing throughout development
Scope Definition
Wrong: Testing only main application code
Right: Include dependencies, APIs, infrastructure, and third-party integrations
Remediation Priority
Wrong: Fixing all findings equally
Right: Risk-based prioritization (severity × exploitability × business impact)
Authentication in Testing
Wrong: DAST scans without authentication
Right: Configure authenticated scanning to test protected features
Best Practices
Shift Left: Integrate security testing early in development
Continuous Testing: Automate security scans in CI/CD pipelines
Layered Approach: Combine SAST, DAST, SCA, and manual testing
Risk-Based Testing: Prioritize testing based on threat model
False Positive Management: Establish process for triaging findings
Remediation Tracking: Use SIEM/SOAR for vulnerability management
Regular Updates: Keep security tools and signatures current
Security Champions: Train developers in security testing
Metrics and KPIs: Track security posture over time
Compliance Validation: Map tests to regulatory requirements
Resources
OWASP Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
OWASP API Security: https://owasp.org/www-project-api-security/
NIST SP 800-115: Technical Guide to Information Security Testing
PTES: Penetration Testing Execution Standard
SANS Security Testing: https://www.sans.org/security-resources/
HackerOne Methodology: https://www.hackerone.com/ethical-hacker/hack-learn
PortSwigger Academy: https://portswigger.net/web-security
Weekly Installs
90
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass