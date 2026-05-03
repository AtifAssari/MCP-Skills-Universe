---
rating: ⭐⭐
title: 180-java-observability-logging
url: https://skills.sh/jabrena/cursor-rules-java/180-java-observability-logging
---

# 180-java-observability-logging

skills/jabrena/cursor-rules-java/180-java-observability-logging
180-java-observability-logging
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 180-java-observability-logging
SKILL.md
Java Logging Best Practices

Implement effective Java logging following standardized frameworks, meaningful log levels, core practices (parameterized logging, exception handling, no sensitive data), flexible configuration, security-conscious logging, monitoring and alerting, and comprehensive logging validation through testing.

What is covered in this Skill?

Standardized framework selection: SLF4J facade with Logback or Log4j2
Meaningful and consistent log levels: ERROR, WARN, INFO, DEBUG, TRACE
Core practices: parameterized logging, proper exception handling, avoiding sensitive data
Configuration: environment-specific (logback.xml, log4j2.xml), output formats, log rotation
Security: mask sensitive data, control log access, secure transmission, GDPR/HIPAA compliance
Log monitoring and alerting: centralized aggregation (ELK, Splunk, Loki), automated alerts
Logging validation through testing: assert log messages, verify formats, test levels, measure performance impact

Scope: The reference is organized by examples (good/bad code patterns) for each core area. Apply recommendations based on applicable examples.

Constraints

Before applying any logging recommendations, ensure the project compiles. Compilation failure is a blocking condition. After applying improvements, run full verification.

MANDATORY: Run ./mvnw compile or mvn compile before applying any change
SAFETY: If compilation fails, stop immediately — do not proceed until resolved
VERIFY: Run ./mvnw clean verify or mvn clean verify after applying improvements
BEFORE APPLYING: Read the reference for detailed good/bad examples, constraints, and safeguards for each logging pattern
When to use this skill
Improve logging
Apply logging
Refactor logging
Add logging support
Workflow
Compile project before logging changes

Run ./mvnw compile or mvn compile and stop immediately if compilation fails.

Read logging reference and assess current observability

Read references/180-java-observability-logging.md and evaluate framework usage, log levels, sensitive-data handling, and config gaps.

Apply logging and observability improvements

Implement selected framework/configuration/practice changes, including secure logging and monitoring integration where applicable.

Verify with full build

Run ./mvnw clean verify or mvn clean verify after applying improvements.

Reference

For detailed guidance, examples, and constraints, see references/180-java-observability-logging.md.

Weekly Installs
63
Repository
jabrena/cursor-…les-java
GitHub Stars
368
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass