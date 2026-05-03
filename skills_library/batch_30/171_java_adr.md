---
title: 171-java-adr
url: https://skills.sh/jabrena/cursor-rules-java/171-java-adr
---

# 171-java-adr

skills/jabrena/cursor-rules-java/171-java-adr
171-java-adr
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 171-java-adr
SKILL.md
Java ADR Generator with interactive conversational approach

Generate Architecture Decision Records (ADRs) for Java projects through an interactive, conversational process that systematically gathers all necessary context to produce well-structured ADR documents. This is an interactive SKILL.

What is covered in this Skill?

ADR file storage configuration
Conversational information gathering: context, stakeholders, decision drivers, options with pros/cons, outcome, consequences
MADR template generation
Validation with ./mvnw validate or mvn validate before proceeding
Constraints

Before applying any ADR generation, ensure the project validates. If validation fails, stop immediately — do not proceed until all validation errors are resolved.

MANDATORY: Run ./mvnw validate or mvn validate before applying any ADR generation
SAFETY: If validation fails, stop immediately — do not proceed until all validation errors are resolved
BEFORE APPLYING: Read the reference for detailed good/bad examples, constraints, and safeguards for each ADR generation pattern
Reference

For detailed guidance, examples, and constraints, see references/171-java-adr.md.

Weekly Installs
17
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