---
rating: ⭐⭐
title: 112-java-maven-plugins
url: https://skills.sh/jabrena/cursor-rules-java/112-java-maven-plugins
---

# 112-java-maven-plugins

skills/jabrena/cursor-rules-java/112-java-maven-plugins
112-java-maven-plugins
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 112-java-maven-plugins
SKILL.md
Maven Plugins: pom.xml Configuration Best Practices

Configure Maven plugins and profiles in pom.xml using a structured, question-driven process that preserves existing configuration. This is an interactive SKILL.

What is covered in this Skill?

Maven plugins:

Maven Compiler
Maven Enforcer
Maven Surefire
Maven Failsafe
HTML test reports (Surefire Report, JXR)
Maven Spotless
Maven Flatten
Maven Versions
Maven Git Commit ID
Maven Jib

Maven profiles:

JaCoCo (code coverage)
PiTest (mutation testing)
Security (OWASP dependency check)
Static analysis (SpotBugs, PMD)
SonarQube/SonarCloud
JMH (Java Microbenchmark Harness)
Cyclomatic complexity
Constraints

Before applying plugin recommendations, ensure the project is in a valid state. Use a structured, question-driven process that preserves existing configuration and adds only what the user selects.

MANDATORY: Run ./mvnw validate or mvn validate before applying any plugin recommendations
SAFETY: If validation fails, stop and ask the user to fix issues—do not proceed until resolved
SCOPE: Begin with Step 1 (existing configuration analysis) before any changes. Never remove or replace existing plugins; only add new ones that do not conflict
BEFORE APPLYING: Read the reference for detailed plugin configurations, XML templates, and constraints for each step
When to use this skill
Add Maven plugins in pom.xml
Improve Maven plugins in pom.xml
Workflow
Validate project before plugin changes

Run ./mvnw validate or mvn validate and stop if validation fails.

Analyze current plugin and profile configuration

Start with existing configuration analysis to identify what is already declared and avoid conflicts or replacement.

Read plugin reference and collect selections

Read references/112-java-maven-plugins.md, then use a question-driven flow to select only needed plugins/profiles.

Add non-conflicting plugin configuration

Add selected plugins and profiles without removing existing ones, preserving project structure and compatibility.

Summarize applied plugin setup

Report added plugins/profiles, rationale, and recommended follow-up commands or checks.

Reference

For detailed guidance, examples, and constraints, see references/112-java-maven-plugins.md.

Weekly Installs
81
Repository
jabrena/cursor-…les-java
GitHub Stars
368
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass