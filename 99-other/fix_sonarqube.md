---
rating: ⭐⭐
title: fix-sonarqube
url: https://skills.sh/bitsoex/bitso-java/fix-sonarqube
---

# fix-sonarqube

skills/bitsoex/bitso-java/fix-sonarqube
fix-sonarqube
Installation
$ npx skills add https://github.com/bitsoex/bitso-java --skill fix-sonarqube
SKILL.md
Fix SonarQube

SonarQube integration via MCP (Model Context Protocol) for Java code quality analysis, coverage checking, security hotspot review, and duplication analysis.

When to use this skill
Finding and fixing SonarQube issues
Checking quality gate status
Checking code coverage without running local JaCoCo builds
Reviewing and triaging security hotspots
Analyzing code duplications
Analyzing code for quality issues
Understanding SonarQube rules
Prioritizing issue remediation
When asked to "fix sonarqube issues", "check coverage", or "add sonarqube mcp"
Skill Contents
Sections
When to use this skill
Quick Start
MCP Tools Available
Common Workflows
Supported IDEs
References
Related Rules
Related Skills
Available Resources

references/ - Detailed documentation

common rules
copilot cli setup
coverage via mcp
intellij setup
mcp tools
Quick Start

The SonarQube MCP server runs remotely at https://sonarqube-mcp.bitso.io/mcp and is automatically configured in all supported IDEs.

No setup required - just use natural language:

"Find BLOCKER issues in my-project"
"Show me details about rule java:S1128"
"What's the quality gate status for my-service?"
"What files have the lowest coverage in my-project?"
"Search for security hotspots in my-service"
"Find duplicated files in my-project"
"Analyze this code for SonarQube issues"

MCP Tools Available
Issues
Tool	Purpose
search_sonar_issues_in_projects	Search issues by project, severity, quality
change_sonar_issue_status	Accept, mark false positive, or reopen
show_rule	Get rule documentation and fix guidance
Coverage
Tool	Purpose
search_files_by_coverage	Find files with lowest test coverage
get_file_coverage_details	Line-by-line coverage for a file
get_component_measures	Coverage metrics for project/dir/file
Security Hotspots
Tool	Purpose
search_security_hotspots	Search for security hotspots
show_security_hotspot	Get hotspot details
change_security_hotspot_status	Review and resolve hotspots
Duplications
Tool	Purpose
search_duplicated_files	Find files with highest duplication
get_duplications	Line-by-line duplication details
Quality & Projects
Tool	Purpose
get_project_quality_gate_status	Check quality gate status
list_quality_gates	List all quality gates
search_my_sonarqube_projects	Find project keys
list_pull_requests	List PRs for a project
analyze_code_snippet	Analyze code snippet inline
Common Workflows
1. Fix Issues by Severity
"Find all BLOCKER issues in payment-service"
"Show me the rule java:S2259"
"What's the quality gate status for my-service?"

2. Check Coverage
"What files have the lowest coverage in my-service?"
"Show me line-by-line coverage for src/main/java/PaymentService.java"
"What's the coverage for PR #247 in my-service?"

3. Review Security Hotspots
"Search for security hotspots to review in payment-service"
"Show me details about this security hotspot"
"Mark this hotspot as safe with comment: verified input is sanitized"

4. Analyze Duplications
"Find the most duplicated files in my-service"
"Show duplication details for this file"

5. Understand Rules
"Explain rule java:S1128 (unused imports)"
"What are the BLOCKER rules for Java?"

Supported IDEs

The MCP is automatically available in:

IDE	Configuration
Cursor	.cursor/mcp.json
VS Code + Copilot	.vscode/mcp.json
Claude Code	.mcp.json
IntelliJ IDEA	See manual setup
Copilot CLI	See manual setup

For IntelliJ and Copilot CLI, see: java/commands/add-sonarqube-mcp-to-intellij-and-copilot-cli.md

References
Reference	Description
references/mcp-tools.md	Full MCP tool reference (all 25 tools)
references/coverage-via-mcp.md	Coverage checking via SonarQube MCP
references/common-rules.md	Common Java rules
Related Rules
java-sonarqube-setup - Setup guide
java-sonarqube-mcp - MCP tool reference
fix-sonarqube-issues - Fix command
Related Skills
Skill	Purpose
java-coverage	JaCoCo coverage for SonarQube
gradle-standards	SonarQube Gradle plugin
Weekly Installs
10
Repository
bitsoex/bitso-java
GitHub Stars
38
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn