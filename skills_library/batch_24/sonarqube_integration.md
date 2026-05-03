---
title: sonarqube-integration
url: https://skills.sh/bitsoex/bitso-java/sonarqube-integration
---

# sonarqube-integration

skills/bitsoex/bitso-java/sonarqube-integration
sonarqube-integration
Installation
$ npx skills add https://github.com/bitsoex/bitso-java --skill sonarqube-integration
SKILL.md
SonarQube Integration

SonarQube integration via MCP (Model Context Protocol) for Java code quality analysis.

When to use this skill
Finding and fixing SonarQube issues
Checking quality gate status
Analyzing code for quality issues
Understanding SonarQube rules
Prioritizing issue remediation
When asked to "fix sonarqube issues" or "add sonarqube mcp"
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

📚 references/ - Detailed documentation

common rules
copilot cli setup
intellij setup
mcp tools
Quick Start

The SonarQube MCP server runs remotely at https://sonarqube-mcp.bitso.io/mcp and is automatically configured in all supported IDEs.

No setup required - just use natural language:

"Find HIGH severity issues in my-project"
"Show me details about rule java:S1128"
"What's the quality gate status for my-service?"
"Analyze this code for SonarQube issues"

MCP Tools Available
Tool	Purpose
list_projects	List all SonarQube projects
get_issues	Get issues for a project
get_issue_details	Get details for a specific issue
get_rule	Get rule documentation
get_quality_gate	Check quality gate status
analyze_code	Analyze code snippet
Common Workflows
1. Fix Issues by Severity
"Find all BLOCKER issues in payment-service"
"Get details for issue AYx123..."
"Show me the rule java:S2259"

2. Check Quality Gate
"What's the quality gate status for my-service?"
"List all projects I have access to"

3. Understand Rules
"Explain rule java:S1128 (unused imports)"
"What are the CRITICAL rules for Java?"

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
references/mcp-tools.md	Full MCP tool reference
references/common-rules.md	Common Java rules
Related Rules
.cursor/rules/java-sonarqube-setup.mdc - Setup guide
.cursor/rules/java-sonarqube-mcp.mdc - MCP tool reference
.claude/commands/fix-sonarqube-issues.md - Fix command
Related Skills
Skill	Purpose
java-coverage	JaCoCo coverage for SonarQube
gradle-standards	SonarQube Gradle plugin
Weekly Installs
11
Repository
bitsoex/bitso-java
GitHub Stars
38
First Seen
Jan 24, 2026