---
title: 172-java-diagrams
url: https://skills.sh/jabrena/cursor-rules-java/172-java-diagrams
---

# 172-java-diagrams

skills/jabrena/cursor-rules-java/172-java-diagrams
172-java-diagrams
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 172-java-diagrams
SKILL.md
Java Diagrams Generator with modular step-based configuration

Generate comprehensive Java project diagrams through a modular, step-based interactive process that covers UML sequence diagrams, UML class diagrams, C4 model diagrams, and UML state machine diagrams using PlantUML syntax. This is an interactive SKILL.

What is covered in this Skill?

UML sequence diagram generation for application workflows and API interactions
UML class diagram generation for package structure and class relationships
C4 model diagram generation at Context/Container/Component levels only (levels 1–3; Code/Level 4 not generated)
UML state machine diagram generation for entity lifecycles and business workflows
PlantUML syntax for all diagram types
File organization strategies: single-file, separate-files, or integrated with existing documentation
Final diagram validation with PlantUML syntax checking
Constraints

Before applying any diagram generation, ensure the project validates. If validation fails, stop immediately — do not proceed until all validation errors are resolved.

MANDATORY: Run ./mvnw validate or mvn validate before applying any diagram generation
SAFETY: If validation fails, stop immediately — do not proceed until all validation errors are resolved
BEFORE APPLYING: Read the reference for detailed good/bad examples, constraints, and safeguards for each diagram generation pattern
C4 LIMIT: C4 diagrams restricted to levels 1, 2, 3 only (Context, Container, Component); never generate Level 4 (Code) diagrams
Reference

For detailed guidance, examples, and constraints, see references/172-java-diagrams.md.

Weekly Installs
18
Repository
jabrena/cursor-…les-java
GitHub Stars
368
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn