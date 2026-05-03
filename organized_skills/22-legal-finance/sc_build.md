---
rating: ⭐⭐⭐
title: sc-build
url: https://skills.sh/tony363/superclaude/sc-build
---

# sc-build

skills/tony363/superclaude/sc-build
sc-build
Installation
$ npx skills add https://github.com/tony363/superclaude --skill sc-build
SKILL.md
Build & Package Skill

Project building and packaging with optimization and error handling.

Quick Start
# Standard build
/sc:build [target]

# Production with optimization
/sc:build --type prod --clean --optimize

# Verbose development build
/sc:build frontend --type dev --verbose

Behavioral Flow
Analyze - Project structure, configs, dependencies
Validate - Build environment, toolchain components
Execute - Build process with real-time monitoring
Optimize - Apply optimizations, minimize bundles
Package - Generate artifacts and build reports
Flags
Flag	Type	Default	Description
--type	string	dev	dev, prod, test
--clean	bool	false	Clean build (remove previous artifacts)
--optimize	bool	false	Enable advanced optimizations
--verbose	bool	false	Detailed build output
--validate	bool	false	Include validation steps
Personas Activated
devops-engineer - Build optimization and deployment preparation
Evidence Requirements

This skill requires evidence. You MUST:

Show build command output and exit codes
Reference generated artifacts
Report timing metrics and optimization results
Build Types
Development (--type dev)
Fast compilation
Source maps enabled
Debug symbols included
No minification
Production (--type prod)
Full optimization
Minification enabled
Tree-shaking applied
Dead code elimination
Test (--type test)
Test coverage instrumentation
Mock configurations
Test-specific environment
Examples
Clean Production Build
/sc:build --type prod --clean --optimize
# Minification, tree-shaking, deployment prep

Component Build
/sc:build frontend --verbose
# Targeted build with detailed output

Validation Build
/sc:build --type dev --validate
# Development build with quality gates

Error Handling

Build failures trigger:

Error log analysis
Dependency verification
Configuration validation
Actionable resolution guidance
Tool Coordination
Bash - Build system execution
Read - Configuration analysis
Grep - Error parsing and log analysis
Glob - Artifact discovery
Write - Build reports
Weekly Installs
25
Repository
tony363/superclaude
GitHub Stars
17
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass