---
rating: ⭐⭐
title: powershell-7-expert
url: https://skills.sh/404kidwiz/claude-supercode-skills/powershell-7-expert
---

# powershell-7-expert

skills/404kidwiz/claude-supercode-skills/powershell-7-expert
powershell-7-expert
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill powershell-7-expert
SKILL.md
PowerShell 7 Expert
Purpose

Provides expertise in modern PowerShell 7+ (PowerShell Core) for cross-platform automation. Specializes in parallel processing, REST API integration, modern scripting patterns, and leveraging new language features.

When to Use
Cross-platform automation (Windows, Linux, macOS)
Parallel processing with ForEach-Object -Parallel
REST API integrations
Modern PowerShell scripting patterns
Pipeline chain operators (&& ||)
Ternary expressions and null coalescing
SSH-based remoting
JSON/YAML data manipulation
Quick Start

Invoke this skill when:

Writing cross-platform PowerShell scripts
Using PowerShell 7+ specific features
Implementing parallel processing
Building REST API integrations
Modernizing scripts from 5.1

Do NOT invoke when:

Legacy Windows-only systems → use /powershell-5.1-expert
GUI development → use /powershell-ui-architect
Security configuration → use /powershell-security-hardening
Module design → use /powershell-module-architect
Decision Framework
PowerShell 7 Feature Selection?
├── Parallel Processing
│   ├── Simple iteration → ForEach-Object -Parallel
│   └── Complex workflows → Start-ThreadJob
├── API Integration
│   └── Invoke-RestMethod with modern options
├── Null Handling
│   ├── Default value → ?? operator
│   └── Conditional access → ?. operator
└── Pipeline Control
    └── && and || chain operators

Core Workflows
1. Parallel Processing
Identify parallelizable workload
Use ForEach-Object -Parallel
Set -ThrottleLimit appropriately
Handle thread-safe data access
Aggregate results
Handle errors from parallel runs
2. REST API Integration
Construct request parameters
Handle authentication (Bearer, OAuth)
Use Invoke-RestMethod
Parse JSON response
Implement pagination
Add retry logic for failures
3. Cross-Platform Script
Avoid Windows-specific paths
Use $PSVersionTable and $IsLinux/$IsWindows
Handle path separators correctly
Test on all target platforms
Use compatible modules
Document platform requirements
Best Practices
Use ternary operator for concise conditionals
Leverage null-coalescing for defaults
Use ForEach-Object -Parallel for CPU-bound tasks
Prefer SSH remoting over WinRM for cross-platform
Use Join-Path for cross-platform paths
Test on all target operating systems
Anti-Patterns
Anti-Pattern	Problem	Correct Approach
Hardcoded backslashes	Breaks on Linux/macOS	Join-Path or /
Windows-only cmdlets	Cross-platform failure	Check availability
Over-parallelization	Thread overhead	Tune ThrottleLimit
Ignoring $Error	Silent failures	Proper error handling
Assuming WinRM	Not cross-platform	SSH remoting
Weekly Installs
203
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn