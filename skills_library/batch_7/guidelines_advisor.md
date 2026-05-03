---
title: guidelines-advisor
url: https://skills.sh/trailofbits/skills/guidelines-advisor
---

# guidelines-advisor

skills/trailofbits/skills/guidelines-advisor
guidelines-advisor
Installation
$ npx skills add https://github.com/trailofbits/skills --skill guidelines-advisor
Summary

Smart contract development advisor applying Trail of Bits' security and design guidelines to analyze codebases systematically.

Performs five-phase analysis covering documentation generation, architecture review, upgradeability assessment, implementation quality checks, and dependency evaluation
Assesses 11 comprehensive areas including function composition, inheritance patterns, event logging, common pitfalls, proxy security, and testing coverage
Generates plain English system descriptions, architectural diagrams, and NatSpec documentation recommendations tailored to your codebase
Delivers prioritized recommendations (CRITICAL, HIGH, MEDIUM, LOW) with specific file references and actionable next steps for production readiness
SKILL.md
Guidelines Advisor
Purpose

Systematically analyzes the codebase and provides guidance based on Trail of Bits' development guidelines:

Generate documentation and specifications (plain English descriptions, architectural diagrams, code documentation)
Optimize on-chain/off-chain architecture (only if applicable)
Review upgradeability patterns (if your project has upgrades)
Check delegatecall/proxy implementations (if present)
Assess implementation quality (functions, inheritance, events)
Identify common pitfalls
Review dependencies
Evaluate test suite and suggest improvements

Framework: Building Secure Contracts - Development Guidelines

How This Works
Phase 1: Discovery & Context

Explores the codebase to understand:

Project structure and platform
Contract/module files and their purposes
Existing documentation
Architecture patterns (proxies, upgrades, etc.)
Testing setup
Dependencies
Phase 2: Documentation Generation

Helps create:

Plain English system description
Architectural diagrams (using Slither printers for Solidity)
Code documentation recommendations (NatSpec for Solidity)
Phase 3: Architecture Analysis

Analyzes:

On-chain vs off-chain component distribution (if applicable)
Upgradeability approach (if applicable)
Delegatecall proxy patterns (if present)
Phase 4: Implementation Review

Assesses:

Function composition and clarity
Inheritance structure
Event logging practices
Common pitfalls presence
Dependencies quality
Testing coverage and techniques
Phase 5: Recommendations

Provides:

Prioritized improvement suggestions
Best practice guidance
Actionable next steps
Assessment Areas

I analyze 11 comprehensive areas covering all aspects of smart contract development. For detailed criteria, best practices, and specific checks, see ASSESSMENT_AREAS.md.

Quick Reference:

Documentation & Specifications

Plain English system descriptions
Architectural diagrams
NatSpec completeness (Solidity)
Documentation gaps identification

On-Chain vs Off-Chain Computation

Complexity analysis
Gas optimization opportunities
Verification vs computation patterns

Upgradeability

Migration vs upgradeability trade-offs
Data separation patterns
Upgrade procedure documentation

Delegatecall Proxy Pattern

Storage layout consistency
Initialization patterns
Function shadowing risks
Slither upgradeability checks

Function Composition

Function size and clarity
Logical grouping
Modularity assessment

Inheritance

Hierarchy depth/width
Diamond problem risks
Inheritance visualization

Events

Critical operation coverage
Event naming consistency
Indexed parameters

Common Pitfalls

Reentrancy patterns
Integer overflow/underflow
Access control issues
Platform-specific vulnerabilities

Dependencies

Library quality assessment
Version management
Dependency manager usage
Copied code detection

Testing & Verification

Coverage analysis
Fuzzing techniques
Formal verification
CI/CD integration

Platform-Specific Guidance

Solidity version recommendations
Compiler warning checks
Inline assembly warnings
Platform-specific tools

For complete details on each area including what I'll check, analyze, and recommend, see ASSESSMENT_AREAS.md.

Example Output

When the analysis is complete, you'll receive comprehensive guidance covering:

System documentation with plain English descriptions
Architectural diagrams and documentation gaps
Architecture analysis (on-chain/off-chain, upgradeability, proxies)
Implementation review (functions, inheritance, events, pitfalls)
Dependencies and testing evaluation
Prioritized recommendations (CRITICAL, HIGH, MEDIUM, LOW)
Overall assessment and path to production

For a complete example analysis report, see EXAMPLE_REPORT.md.

Deliverables

I provide four comprehensive deliverable categories:

1. System Documentation
Plain English descriptions
Architectural diagrams
Documentation gaps analysis
2. Architecture Analysis
On-chain/off-chain assessment
Upgradeability review
Proxy pattern security review
3. Implementation Review
Function composition analysis
Inheritance assessment
Events coverage
Pitfall identification
Dependencies evaluation
Testing analysis
4. Prioritized Recommendations
CRITICAL (address immediately)
HIGH (address before deployment)
MEDIUM (address for production quality)
LOW (nice to have)

For detailed templates and examples of each deliverable, see DELIVERABLES.md.

Assessment Process

When invoked, I will:

Explore the codebase

Identify all contract/module files
Find existing documentation
Locate test files
Check for proxies/upgrades
Identify dependencies

Generate documentation

Create plain English system description
Generate architectural diagrams (if tools available)
Identify documentation gaps

Analyze architecture

Assess on-chain/off-chain distribution (if applicable)
Review upgradeability approach (if applicable)
Audit proxy patterns (if present)

Review implementation

Analyze functions, inheritance, events
Check for common pitfalls
Assess dependencies
Evaluate testing

Provide recommendations

Present findings with file references
Ask clarifying questions about design decisions
Suggest prioritized improvements
Offer actionable next steps
Rationalizations (Do Not Skip)
Rationalization	Why It's Wrong	Required Action
"System is simple, description covers everything"	Plain English descriptions miss security-critical details	Complete all 5 phases: documentation, architecture, implementation, dependencies, recommendations
"No upgrades detected, skip upgradeability section"	Upgradeability can be implicit (ownable patterns, delegatecall)	Search for proxy patterns, delegatecall, storage collisions before declaring N/A
"Not applicable" without verification	Premature scope reduction misses vulnerabilities	Verify with explicit codebase search before skipping any guideline section
"Architecture is straightforward, no analysis needed"	Obvious architectures have subtle trust boundaries	Analyze on-chain/off-chain distribution, access control flow, external dependencies
"Common pitfalls don't apply to this codebase"	Every codebase has common pitfalls	Systematically check all guideline pitfalls with grep/code search
"Tests exist, testing guideline is satisfied"	Test existence ≠ test quality	Check coverage, property-based tests, integration tests, failure cases
"I can provide generic best practices"	Generic advice isn't actionable	Provide project-specific findings with file:line references
"User knows what to improve from findings"	Findings without prioritization = no action plan	Generate prioritized improvement roadmap with specific next steps
Notes
I'll only analyze relevant sections (won't hallucinate about upgrades if not present)
I'll adapt to your platform (Solidity, Rust, Cairo, etc.)
I'll use available tools (Slither, etc.) but work without them if unavailable
I'll provide file references and line numbers for all findings
I'll ask questions about design decisions I can't infer from code
Ready to Begin

What I'll need:

Access to your codebase
Context about your project goals
Any existing documentation or specifications
Information about deployment plans

Let's analyze your codebase and improve it using Trail of Bits' best practices!

Weekly Installs
2.0K
Repository
trailofbits/skills
GitHub Stars
4.9K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass